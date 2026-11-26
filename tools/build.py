"""Builds the front page and renders it to entry.png (1024 x 1024).

    python tools/build.py [--land <ne_110m_land.geojson>] [--edge <msedge.exe>]

The world map is drawn from Natural Earth's 1:110m land polygons (public
domain); the file is read from --land, or downloaded once into .cache/.
The page is laid out as HTML/SVG and photographed by a headless Edge or
Chrome, then saved as an optimised PNG under 1 MiB.
"""

import argparse
import html
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.request

from PIL import Image

sys.path.insert(0, os.path.dirname(__file__))
import art  # noqa: E402
import edition as ed  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAND_URL = ("https://raw.githubusercontent.com/nvkelso/natural-earth-vector/"
            "master/geojson/ne_110m_land.geojson")
SIZE = 1024
MAX_BYTES = 1048576

# Map frame: equirectangular, longitudes -170..190 so the Pacific islands stay whole.
LON0, LON1, LAT0, LAT1 = -170.0, 190.0, -45.0, 75.0
MAP_W, MAP_H = 330, 110


def esc(s):
    return html.escape(s, quote=True)


def project(lon, lat):
    if lon < LON0:
        lon += 360
    x = (lon - LON0) / (LON1 - LON0) * MAP_W
    y = (LAT1 - lat) / (LAT1 - LAT0) * MAP_H
    return x, y


def land_path(geojson_path):
    with open(geojson_path, encoding="utf8") as f:
        gj = json.load(f)
    parts = []
    for feat in gj["features"]:
        geom = feat["geometry"]
        polys = geom["coordinates"] if geom["type"] == "MultiPolygon" else [geom["coordinates"]]
        for poly in polys:
            ring = poly[0]
            if len(ring) < 4:
                continue
            # Shift rings that sit wholly west of LON0 (e.g. far-east Russia's tip) by +360.
            xs = [p[0] for p in ring]
            shift = 360 if max(xs) < LON0 else 0
            pts = [project(lon + shift, lat) if lon + shift >= LON0 else project(lon + shift + 360, lat)
                   for lon, lat in ring]
            if max(p[0] for p in pts) - min(p[0] for p in pts) > MAP_W * 0.8 and len(ring) < 40:
                continue  # a tiny ring split across the seam: skip
            d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + "Z"
            parts.append(d)
    return " ".join(parts)


def get_land(path_arg):
    if path_arg and os.path.exists(path_arg):
        return path_arg
    cache = os.path.join(ROOT, ".cache", "ne_110m_land.geojson")
    if not os.path.exists(cache):
        os.makedirs(os.path.dirname(cache), exist_ok=True)
        urllib.request.urlretrieve(LAND_URL, cache)
    return cache


def region_color(key):
    return ed.REGIONS[key][1]


def sure_html(label):
    col = ed.SURE[label][0]
    return f'<span class="sure" style="color:{col};border-color:{col}">{esc(label)}</span>'


def chip_html(s):
    if not s.get("chip"):
        return ""
    return f'<span class="chip">{esc(s["chip"])}</span>'


def timeline_html():
    items = "".join(f'<span class="ev"><b>{esc(t)}</b> {esc(x)}</span>' for t, x in ed.TIMELINE)
    return f'<div class="timeline"><span class="tl">THE DAY IN UTC</span>{items}</div>'


def lead_html(i, s):
    c = region_color(s["region"])
    return f"""
<article class="lead">
  <div class="scene">{art.ART[s['art']]()}<span class="num" style="background:{c}">{i}</span>{chip_html(s)}</div>
  <div class="meta"><span class="tag" style="background:{c}">{esc(s['tag'])}</span>
    <span class="where">{esc(s['place'])} \u00b7 {esc(s['beat'])}</span>{sure_html(s['sure'])}</div>
  <h2>{esc(s['head'])}</h2>
  <p>{esc(s['dek'])}</p>
  <div class="why"><b>WHY IT MATTERS</b> {esc(s['why'])}</div>
  <div class="src">{esc(s['src'])}</div>
</article>"""


def card_html(i, s):
    c = region_color(s["region"])
    return f"""
<article class="card">
  <div class="scene">{art.ART[s['art']]()}<span class="num" style="background:{c}">{i}</span>{chip_html(s)}</div>
  <div class="where"><i style="background:{c}"></i>{esc(s['place'])}{sure_html(s['sure'])}</div>
  <h3>{esc(s['head'])}</h3>
  <p>{esc(s['dek'])}</p>
</article>"""


def map_svg(land_d):
    pins = []
    for pin in ed.PINS:
        n, lon, lat, reg = pin[:4]
        dx, dy = pin[4:6] if len(pin) > 4 else (0, 0)
        x, y = project(lon, lat)
        x, y = x + dx, y + dy
        pins.append(f'<g transform="translate({x:.1f},{y:.1f})"><circle r="6.2" fill="{region_color(reg)}" '
                    f'stroke="#fff" stroke-width="1.2"/><text y="2.6" font-size="7" text-anchor="middle" '
                    f'fill="#fff" font-family="Arial" font-weight="bold">{n}</text></g>')
    return (f'<svg viewBox="0 0 {MAP_W} {MAP_H}" class="map">'
            f'<rect width="{MAP_W}" height="{MAP_H}" fill="#c9dbe7"/>'
            f'<path d="{land_d}" fill="#efe5cc" stroke="#9c8f72" stroke-width="0.5"/>'
            f'{"".join(pins)}</svg>')


def page(land_d):
    counts = {k: 0 for k in ed.REGIONS}
    for s in ed.LEADS + ed.CARDS:
        counts[s["region"]] += 1
    for b in ed.BRIEFS:
        counts[b[3]] += 1
    total = sum(counts.values())
    strip = "".join(
        f'<span style="flex:{max(counts[k], 3)};background:{col}">{esc(name.upper())} {counts[k]}</span>'
        for k, (name, col) in ed.REGIONS.items())
    kpis = "".join(f'<div class="kpi"><b>{esc(a)}</b><span>{esc(b)}</span></div>' for a, b in ed.KPIS)
    leads = "".join(lead_html(i + 1, s) for i, s in enumerate(ed.LEADS))
    cards = "".join(card_html(i + 4, s) for i, s in enumerate(ed.CARDS))
    briefs = "".join(
        f'<li><em style="color:{region_color(r)}">{n}</em><b>{esc(p)}</b> {esc(t)}</li>'
        for n, p, t, r in ed.BRIEFS)
    sure_legend = " ".join(f'<i style="color:{c};border-color:{c}">{esc(k)}</i> {esc(m)}' for k, (c, m) in ed.SURE.items())
    legend = "".join(f'<span><i style="background:{c}"></i>{esc(n)}</span>' for n, c in ed.REGIONS.values())
    subline = " <b>◆</b> ".join(esc(x) for x in ed.SUBLINE)
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
* {{ box-sizing:border-box; margin:0; padding:0; }}
html,body {{ width:{SIZE}px; height:{SIZE}px; overflow:hidden; background:#f8f4ea; color:#141414;
  font-family:Georgia, 'Times New Roman', serif; }}
.top {{ height:22px; background:#141414; color:#f8f4ea; display:flex; justify-content:space-between;
  align-items:center; padding:0 14px; font:bold 10.5px Arial, sans-serif; letter-spacing:1.6px; }}
.top .r {{ color:#ffcf5a; }}
.mast {{ text-align:center; padding:3px 0 0; border-bottom:3px double #141414; margin:0 14px; }}
.mast h1 {{ font-size:58px; line-height:62px; font-weight:bold; letter-spacing:-1px; white-space:nowrap; }}
.mast .sub {{ font:italic 14px Georgia, serif; color:#3a3a3a; padding:0 0 4px; }}
.mast .sub b {{ color:#b3261e; font-style:normal; }}
.strip {{ display:flex; margin:5px 14px 0; height:15px; font:bold 8.5px Arial, sans-serif; color:#fff;
  letter-spacing:.8px; }}
.strip span {{ display:flex; align-items:center; justify-content:center; white-space:nowrap; overflow:hidden; }}
.kpis {{ display:flex; margin:6px 14px 0; border-top:1px solid #141414; border-bottom:1px solid #141414; }}
.kpi {{ flex:1; padding:3px 8px 3px; border-left:1px solid #cfc6b2; }}
.kpi:first-child {{ border-left:none; padding-left:2px; }}
.kpi b {{ display:block; font:bold 30px Georgia, serif; line-height:31px; color:#b3261e; }}
.kpi span {{ display:block; font:10px/12px Arial, sans-serif; color:#333; }}
.leads {{ display:flex; gap:14px; margin:7px 14px 0; }}
.lead {{ flex:1; }}
.scene {{ position:relative; overflow:hidden; border-radius:2px; }}
.lead .scene {{ height:111px; }}
.lead .scene svg {{ height:auto; margin-top:-12px; }}
.scene svg {{ width:100%; height:100%; display:block; }}
.num {{ position:absolute; left:6px; bottom:6px; width:18px; height:18px; border-radius:50%; color:#fff;
  font:bold 10px/18px Arial, sans-serif; text-align:center; border:1.5px solid #fff; }}
.meta {{ display:flex; align-items:center; gap:6px; margin-top:6px; }}
.tag {{ color:#fff; font:bold 9px Arial, sans-serif; letter-spacing:1px; padding:2px 5px; }}
.where {{ font:bold 9px Arial, sans-serif; letter-spacing:.8px; color:#555; white-space:nowrap; overflow:hidden; }}
.lead h2 {{ font-size:25px; line-height:27px; margin-top:4px; letter-spacing:-.3px; }}
.lead p {{ font:12.5px/15.5px Georgia, serif; color:#2a2a2a; margin-top:3px; }}
.why {{ font:bold 10.5px/13px Arial, sans-serif; color:#1a1a1a; margin-top:3px; white-space:nowrap; overflow:hidden; }}
.why b {{ color:#b3261e; font-size:8.5px; letter-spacing:.8px; margin-right:3px; }}
.src {{ font:bold 7.5px Arial, sans-serif; letter-spacing:.8px; color:#8a8170; margin-top:3px; }}
.rule {{ margin:6px 14px 0; border-top:2px solid #141414; display:flex; justify-content:space-between;
  font:bold 9.5px Arial, sans-serif; letter-spacing:1.5px; padding-top:3px; }}
.rule .how {{ color:#555; font:8px Arial, sans-serif; letter-spacing:.3px; }}
.rule .how i {{ font:bold 7.5px Arial, sans-serif; font-style:normal; border:1px solid; padding:0 3px; margin-left:4px; }}
.sure {{ margin-left:auto; font:bold 7.5px Arial, sans-serif; letter-spacing:.6px; border:1px solid; padding:0 3px;
  line-height:11px; flex:none; }}
.card .where .sure {{ font-size:7px; line-height:10px; }}
.timeline {{ display:flex; align-items:center; margin:5px 14px 0; height:16px; border-bottom:1px solid #cfc6b2;
  font:9px Arial, sans-serif; color:#222; }}
.timeline .tl {{ background:#141414; color:#fff; font:bold 8.5px Arial, sans-serif; letter-spacing:1.2px;
  padding:2px 6px; margin-right:6px; }}
.timeline .ev {{ flex:1; white-space:nowrap; border-left:2px solid #b3261e; padding-left:5px; }}
.timeline .ev b {{ color:#b3261e; }}
.cards {{ display:grid; grid-template-columns:repeat(5,1fr); gap:7px 11px; margin:5px 14px 0; }}
.card .scene {{ height:60px; }}
.card .where {{ margin-top:4px; display:flex; align-items:center; gap:4px; font-size:8px; overflow:visible; }}
.card .where i {{ width:7px; height:7px; display:inline-block; }}
.card h3 {{ font-size:14.5px; line-height:16.5px; margin-top:2px; letter-spacing:-.2px; }}
.card p {{ font:10px/12.5px Arial, sans-serif; color:#333; margin-top:2px; }}
.chip {{ position:absolute; right:5px; bottom:5px; background:#b3261e; color:#fff; font:bold 10px Arial, sans-serif;
  letter-spacing:.6px; padding:2px 5px; border:1.5px solid #fff; box-shadow:0 1px 2px rgba(0,0,0,.35); }}
.lead .chip {{ font-size:15px; padding:3px 8px; right:7px; bottom:7px; }}
.bottom {{ display:flex; gap:14px; margin:7px 14px 0; border-top:2px solid #141414; padding-top:5px; }}
.mapbox {{ width:330px; flex:none; }}
.mapbox h4, .briefs h4 {{ font:bold 9.5px Arial, sans-serif; letter-spacing:1.5px; margin-bottom:4px; }}
.map {{ width:330px; height:110px; display:block; }}
.legend {{ display:flex; flex-wrap:nowrap; gap:7px; margin-top:4px; font:8px Arial, sans-serif; color:#333; white-space:nowrap; }}
.legend i {{ width:7px; height:7px; display:inline-block; margin-right:2px; vertical-align:-1px; }}
.briefs {{ flex:1; }}
.briefs ul {{ list-style:none; columns:2; column-gap:14px; }}
.briefs li {{ font:9.6px/11.1px Arial, sans-serif; color:#222; break-inside:avoid; padding-left:16px;
  text-indent:-16px; }}
.briefs li em {{ font-style:normal; font-weight:bold; display:inline-block; width:16px; text-indent:0; }}
.briefs li b {{ font-size:8.4px; letter-spacing:.5px; color:#141414; }}
.check {{ margin:4px 14px 0; border:1.5px solid #b3261e; background:#fbeee8; padding:3px 8px;
  font:9.6px/12.5px Arial, sans-serif; color:#3a2a26; }}
.check b {{ color:#b3261e; letter-spacing:1px; margin-right:6px; }}
.foot {{ position:absolute; left:0; right:0; bottom:0; height:28px; padding:2px 14px 0;
  font:8px/11px Arial, sans-serif; color:#6e675a; }}
.foot .bar {{ margin-top:3px; background:#141414; color:#f8f4ea; font:bold 8.5px Arial, sans-serif;
  letter-spacing:1.4px; padding:2px 0; text-align:center; margin-left:-14px; margin-right:-14px; }}
</style></head><body>
<div class="top"><span>THE WORLD IN ONE DAY</span><span class="r">{total} STORIES \u00b7 {sum(1 for v in counts.values() if v)} REGIONS \u00b7 ALL FROM {esc(ed.DAY.upper())}</span></div>
<header class="mast"><h1>{esc(ed.DAY)}</h1>
<div class="sub">{subline}</div></header>
<div class="strip">{strip}</div>
{timeline_html()}
<div class="kpis">{kpis}</div>
<section class="leads">{leads}</section>
<div class="rule"><span>ALSO ON {esc(ed.DAY_TAG)}</span><span class="how">HOW SURE: {sure_legend}</span></div>
<section class="cards">{cards}</section>
<section class="bottom">
 <div class="mapbox"><h4>WHERE IT HAPPENED \u00b7 PINS = STORY NUMBERS</h4>{map_svg(land_d)}<div class="legend">{legend}</div></div>
 <div class="briefs"><h4>IN BRIEF \u00b7 {len(ed.BRIEFS)} MORE FROM {esc(ed.DAY_TAG_SHORT)}</h4><ul>{briefs}</ul></div>
</section>
<div class="check"><b>DATE CHECK</b>{esc(ed.DATE_CHECK)}</div>
<div class="foot">{esc(ed.SOURCES)}<div class="bar">DRAWN BY AN AI AGENT FOR MAKE.FUN \u00b7 {esc(ed.DAY.upper())} \u00b7 ONE DAY, ONE PAGE</div></div>
</body></html>"""


def find_browser(arg):
    cands = [arg] if arg else []
    cands += [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        shutil.which("chromium") or "", shutil.which("google-chrome") or "",
    ]
    for c in cands:
        if c and os.path.exists(c):
            return c
    raise SystemExit("no Edge or Chrome found; pass --edge")


def render(html_text, browser, out_png):
    with tempfile.TemporaryDirectory() as tmp:
        page_path = os.path.join(tmp, "page.html")
        shot = os.path.join(tmp, "shot.png")
        with open(page_path, "w", encoding="utf8") as f:
            f.write(html_text)
        cmd = [browser, "--headless=new", "--disable-gpu", "--hide-scrollbars",
               "--force-device-scale-factor=2", f"--window-size={SIZE},{SIZE}",
               "--default-background-color=f8f4eaff", f"--user-data-dir={os.path.join(tmp, 'prof')}",
               f"--screenshot={shot}", "file:///" + page_path.replace("\\", "/")]
        subprocess.run(cmd, check=True, capture_output=True, timeout=120)
        im = Image.open(shot).convert("RGB")
    # Rendered at 2x, downsampled for clean anti-aliasing at exactly 1024 x 1024.
    im = im.resize((SIZE, SIZE), Image.LANCZOS)
    save_png(im, out_png)
    return im


def save_png(im, out_png):
    buf = io.BytesIO()
    im.save(buf, "PNG", optimize=True)
    data = buf.getvalue()
    colors = 256
    while len(data) > MAX_BYTES and colors >= 64:
        q = im.quantize(colors=colors, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
        buf = io.BytesIO()
        q.save(buf, "PNG", optimize=True)
        data = buf.getvalue()
        colors //= 2
    if len(data) > MAX_BYTES:
        raise SystemExit(f"PNG still {len(data)} bytes")
    with open(out_png, "wb") as f:
        f.write(data)
    print(f"wrote {out_png}: {len(data)} bytes")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--land")
    ap.add_argument("--edge")
    ap.add_argument("--html", help="also write the page HTML here")
    ap.add_argument("--out", default=os.path.join(ROOT, "entry.png"))
    a = ap.parse_args()
    text = page(land_path(get_land(a.land)))
    if a.html:
        with open(a.html, "w", encoding="utf8") as f:
            f.write(text)
    render(text, find_browser(a.edge), a.out)


if __name__ == "__main__":
    main()

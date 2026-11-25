"""Drawn scenes for the front page, as inline SVG.

Lead scenes use a 320x150 view box, card scenes 240x84. Everything is drawn
from shapes here: no photographs, no logos, no outside images.
"""

import math
import random


def _stars(n, w, h, seed, ymax=None):
    rnd = random.Random(seed)
    ymax = ymax or h
    out = []
    for _ in range(n):
        x, y = rnd.uniform(0, w), rnd.uniform(0, ymax)
        r = rnd.choice([0.5, 0.6, 0.8, 1.0])
        o = rnd.uniform(0.4, 1.0)
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#fff" opacity="{o:.2f}"/>')
    return "".join(out)


def launch():
    """Long March 2F climbing from Jiuquan at night, Tiangong in the corner."""
    plume = []
    rnd = random.Random(24)
    for i in range(26):
        x = 150 + rnd.uniform(-34, 34) * (i / 26 + 0.25)
        y = 112 + rnd.uniform(-4, 18) + i * 0.4
        r = 8 + rnd.uniform(0, 12) * (i / 26 + 0.4)
        g = 205 + int(rnd.uniform(0, 40))
        plume.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="rgb({g},{g},{g - 6})" opacity="0.9"/>')
    return f"""
<svg viewBox="0 0 320 150" preserveAspectRatio="xMidYMid slice">
 <defs>
  <linearGradient id="skyL" x1="0" y1="0" x2="0" y2="1">
   <stop offset="0" stop-color="#0b1633"/><stop offset="0.7" stop-color="#23345e"/><stop offset="1" stop-color="#5a4a6a"/>
  </linearGradient>
  <radialGradient id="glowL" cx="0.5" cy="0.5" r="0.5">
   <stop offset="0" stop-color="#ffe9a8" stop-opacity="0.95"/><stop offset="1" stop-color="#ff9a3c" stop-opacity="0"/>
  </radialGradient>
 </defs>
 <rect width="320" height="150" fill="url(#skyL)"/>
 {_stars(70, 320, 150, 5, 90)}
 <g transform="translate(262,26)">
  <rect x="-22" y="-3" width="16" height="6" fill="#3d6fb6" stroke="#cfe0ff" stroke-width="0.6"/>
  <rect x="6" y="-3" width="16" height="6" fill="#3d6fb6" stroke="#cfe0ff" stroke-width="0.6"/>
  <rect x="-6" y="-4" width="12" height="8" rx="2" fill="#e8e8e8"/>
  <rect x="-2" y="-9" width="4" height="5" fill="#d0d0d0"/>
  <text x="0" y="17" font-size="7" fill="#cfe0ff" text-anchor="middle" font-family="Arial">TIANGONG</text>
 </g>
 <path d="M0 132 L40 120 L78 126 L120 116 L170 124 L215 114 L262 122 L320 116 L320 150 L0 150Z" fill="#2b2236"/>
 <rect x="0" y="134" width="320" height="16" fill="#1d1724"/>
 <ellipse cx="150" cy="120" rx="70" ry="26" fill="url(#glowL)"/>
 {''.join(plume)}
 <g>
  <rect x="104" y="34" width="8" height="100" fill="#8a8f98"/>
  <path d="M104 40 L130 40 M104 60 L130 60 M104 80 L130 80 M104 100 L130 100" stroke="#8a8f98" stroke-width="2"/>
  <path d="M104 34 L112 42 L104 50 L112 58 L104 66 L112 74 L104 82 L112 90 L104 98 L112 106" stroke="#6c717a" stroke-width="1" fill="none"/>
 </g>
 <g transform="translate(150,16)">
  <path d="M-4 12 L0 2 L4 12Z" fill="#d8d8d8"/>
  <rect x="-5" y="12" width="10" height="16" fill="#f4f4f4"/>
  <rect x="-7" y="28" width="14" height="66" fill="#f7f7f7" stroke="#c9c9c9" stroke-width="0.6"/>
  <rect x="-7" y="46" width="14" height="5" fill="#b3261e"/>
  <rect x="-12" y="62" width="5" height="34" rx="2" fill="#ececec" stroke="#c9c9c9" stroke-width="0.5"/>
  <rect x="7" y="62" width="5" height="34" rx="2" fill="#ececec" stroke="#c9c9c9" stroke-width="0.5"/>
  <path d="M-12 62 L-9.5 55 L-7 62Z M7 62 L9.5 55 L12 62Z" fill="#dcdcdc"/>
  <path d="M-6 94 L0 116 L6 94Z M-12 96 L-9.5 110 L-7 96Z M7 96 L9.5 110 L12 96Z" fill="#ffd36a"/>
  <path d="M-3 94 L0 106 L3 94Z" fill="#fff6d0"/>
 </g>
 <text x="12" y="24" font-size="9" fill="#ffffff" font-family="Arial" font-weight="bold">LIFTOFF · WED 25 NOV</text>
 <text x="12" y="35" font-size="7" fill="#c9d6f2" font-family="Arial">LONG MARCH 2F · 3 CREW</text>
</svg>"""


def markets():
    """A trading board in Seoul: falling red index lines and the day's moves."""
    pts = []
    rnd = random.Random(7)
    y = 38.0
    for i in range(0, 41):
        x = 14 + i * 5.2
        drift = 0.4 if i < 8 else 2.2 if i < 26 else 0.6
        y += drift + rnd.uniform(-2.2, 2.0)
        pts.append(f"{x:.1f},{y:.1f}")
    line = " ".join(pts)
    area = f"14,128 {line} {14 + 40 * 5.2:.1f},128"
    rows = [("KOSPI", "−6.2%"), ("TAIEX", "−4.8%"), ("NIKKEI", "−2.8%"),
            ("HSI", "−1.1%"), ("HYNIX", "−11.1%"), ("SAMSUNG", "−9.9%")]
    board = []
    for i, (k, v) in enumerate(rows):
        yy = 30 + i * 17
        board.append(f'<text x="226" y="{yy}" font-size="7.5" fill="#cfd8e3" font-family="Arial" font-weight="bold">{k}</text>'
                     f'<text x="312" y="{yy}" font-size="9" fill="#ff5a4f" font-family="Arial" font-weight="bold" text-anchor="end">▼{v}</text>')
    return f"""
<svg viewBox="0 0 320 150" preserveAspectRatio="xMidYMid slice">
 <rect width="320" height="150" fill="#0f1722"/>
 <g stroke="#1f2b3b" stroke-width="1">
  <path d="M14 38 H222 M14 60 H222 M14 82 H222 M14 104 H222 M14 126 H222"/>
  <path d="M50 20 V128 M92 20 V128 M134 20 V128 M176 20 V128"/>
 </g>
 <polygon points="{area}" fill="#ff3b30" opacity="0.16"/>
 <polyline points="{line}" fill="none" stroke="#ff4d42" stroke-width="2.4" stroke-linejoin="round"/>
 <circle cx="{14 + 40 * 5.2:.1f}" cy="{y:.1f}" r="3.2" fill="#ff4d42"/>
 <rect x="220" y="14" width="96" height="112" rx="3" fill="#162233" stroke="#26384f"/>
 {''.join(board)}
 <g transform="translate(30,86)">
  <rect x="0" y="0" width="34" height="34" rx="3" fill="#2a3442" stroke="#8da2bb" stroke-width="1.2"/>
  <rect x="7" y="7" width="20" height="20" fill="#3c4a5d"/>
  <path d="M-5 6 H0 M-5 13 H0 M-5 20 H0 M-5 27 H0 M34 6 H39 M34 13 H39 M34 20 H39 M34 27 H39 M6 -5 V0 M13 -5 V0 M20 -5 V0 M27 -5 V0 M6 34 V39 M13 34 V39 M20 34 V39 M27 34 V39" stroke="#8da2bb" stroke-width="1.4"/>
  <path d="M10 4 L17 15 L13 19 L22 31" stroke="#ff4d42" stroke-width="2" fill="none"/>
 </g>
 <text x="14" y="24" font-size="8" fill="#8da2bb" font-family="Arial" font-weight="bold">ASIA CLOSE · WED 25 NOV</text>
</svg>"""


def _tanker(x, y, s, flip=False):
    """An oil tanker with its stern ablaze: flames, glow and a smoke column."""
    tr = f"translate({x},{y}) scale({-s if flip else s},{s})"
    return f"""<g transform="{tr}">
 <ellipse cx="44" cy="-24" rx="30" ry="22" fill="#ff9a3c" opacity="0.28"/>
 <path d="M36 -40 C18 -70 62 -78 34 -112 C78 -96 86 -66 60 -40Z" fill="#2c2c30" opacity="0.8"/>
 <path d="M34 -12 C24 -30 40 -36 34 -54 C50 -42 58 -30 54 -12Z" fill="#ff7a1a"/>
 <path d="M40 -12 C36 -24 46 -28 44 -40 C54 -30 54 -20 50 -12Z" fill="#ffd34d"/>
 <path d="M-64 0 L66 0 L56 18 L-58 18Z" fill="#7a2e22"/>
 <rect x="-64" y="-5" width="130" height="6" fill="#2f2f33"/>
 <path d="M-50 -5 V-11 H24 V-5" fill="#55555c"/>
 <rect x="30" y="-24" width="22" height="19" fill="#e7e2d6"/>
 <rect x="33" y="-20" width="16" height="4" fill="#3a4a5c"/>
 <rect x="40" y="-32" width="5" height="8" fill="#2f2f33"/>
 <path d="M-58 18 L56 18" stroke="#ff9a3c" stroke-width="1" opacity="0.5"/>
</g>"""


def hormuz():
    """Dusk in the strait: two burning tankers between Iran and Oman, a mine in the water."""
    waves = "".join(
        f'<path d="M{x} {y} q6 -3 12 0 t12 0" stroke="#6b96b8" stroke-width="0.9" fill="none" opacity="0.6"/>'
        for x, y in [(12, 96), (66, 128), (150, 100), (196, 132), (262, 98), (290, 126), (120, 130), (20, 112)]
    )
    return f"""
<svg viewBox="0 0 320 150" preserveAspectRatio="xMidYMid slice">
 <defs>
  <linearGradient id="skyH" x1="0" y1="0" x2="0" y2="1">
   <stop offset="0" stop-color="#2a3550"/><stop offset="0.65" stop-color="#b8664a"/><stop offset="1" stop-color="#f0a35e"/>
  </linearGradient>
  <linearGradient id="seaH" x1="0" y1="0" x2="0" y2="1">
   <stop offset="0" stop-color="#3a6584"/><stop offset="1" stop-color="#16324a"/>
  </linearGradient>
 </defs>
 <rect width="320" height="84" fill="url(#skyH)"/>
 <path d="M0 70 L40 62 L80 66 L130 56 L170 64 L196 84 L0 84Z" fill="#6b4b3e"/>
 <path d="M214 84 L234 72 L272 68 L320 74 L320 84Z" fill="#5c4237"/>
 <text x="64" y="78" font-size="9" fill="#f6e3cf" font-family="Arial" font-weight="bold" letter-spacing="2">IRAN</text>
 <text x="262" y="81" font-size="8" fill="#f6e3cf" font-family="Arial" font-weight="bold" letter-spacing="2">OMAN</text>
 <rect y="84" width="320" height="66" fill="url(#seaH)"/>
 {waves}
 {_tanker(112, 104, 0.95)}
 {_tanker(250, 112, 0.72, flip=True)}
 <ellipse cx="150" cy="108" rx="30" ry="3.5" fill="#ff8a1f" opacity="0.35"/>
 <g transform="translate(186,121)" fill="#141416" stroke="#141416" stroke-width="1.3">
  <circle r="5"/><path d="M0 -5 v-3 M-5 -2 l-3 -2 M5 -2 l3 -2 M-3.5 -4 l-2 -3 M3.5 -4 l2 -3"/>
 </g>
 <text x="178" y="129" font-size="7" fill="#e3eef6" font-family="Arial" font-weight="bold" text-anchor="end">NAVAL MINE</text>
</svg>"""


# ---------------------------------------------------------------- card scenes

def court():
    cols = "".join(f'<rect x="{62 + i * 22}" y="30" width="9" height="40" fill="#e9e4d8"/>' for i in range(6))
    return f"""
<svg viewBox="0 0 240 84" preserveAspectRatio="xMidYMid slice">
 <rect width="240" height="84" fill="#d9e3ec"/>
 <path d="M52 30 L120 8 L188 30Z" fill="#f2eee4" stroke="#b9b2a2"/>
 <rect x="54" y="28" width="132" height="4" fill="#cfc7b5"/>
 {cols}
 <rect x="50" y="70" width="140" height="6" fill="#cfc7b5"/><rect x="44" y="76" width="152" height="8" fill="#bdb5a3"/>
 <g transform="translate(196,40) rotate(-30)">
  <rect x="-4" y="0" width="8" height="34" rx="2" fill="#7a4b2a"/>
  <rect x="-14" y="-10" width="28" height="12" rx="3" fill="#5e3820"/>
 </g>
 <rect x="8" y="12" width="38" height="20" rx="2" fill="#b3261e"/>
 <text x="27" y="21" font-size="7" fill="#fff" text-anchor="middle" font-family="Arial" font-weight="bold">10/12</text>
 <text x="27" y="29" font-size="5.5" fill="#fff" text-anchor="middle" font-family="Arial">COUNTS</text>
</svg>"""


def drones():
    return """
<svg viewBox="0 0 240 84" preserveAspectRatio="xMidYMid slice">
 <rect width="240" height="84" fill="#1c2540"/>
 <path d="M0 64 H240 V84 H0Z" fill="#2a2a2e"/>
 <g fill="#5c6270">
  <rect x="18" y="48" width="30" height="16" rx="8"/><rect x="56" y="44" width="34" height="20" rx="9"/>
  <rect x="98" y="50" width="26" height="14" rx="7"/><rect x="150" y="38" width="6" height="26"/>
  <rect x="164" y="44" width="5" height="20"/><rect x="176" y="50" width="40" height="14"/>
 </g>
 <path d="M153 38 q-2 -8 3 -12 q0 6 3 8 q-2 2 -6 4Z" fill="#ffb347"/>
 <path d="M70 64 Q100 20 150 12" stroke="#ffe08a" stroke-width="1.4" fill="none" stroke-dasharray="2 2"/>
 <path d="M30 64 Q70 30 108 22" stroke="#ffe08a" stroke-width="1.4" fill="none" stroke-dasharray="2 2"/>
 <circle cx="152" cy="12" r="7" fill="#ffcf5a" opacity="0.9"/><circle cx="152" cy="12" r="3.5" fill="#fff6d0"/>
 <circle cx="110" cy="22" r="6" fill="#ffcf5a" opacity="0.9"/><circle cx="110" cy="22" r="3" fill="#fff6d0"/>
 <g transform="translate(200,20)" fill="#0e0e10">
  <path d="M-10 0 L10 0 L0 -4Z"/><path d="M-3 0 L-12 6 L-8 0Z M3 0 L12 6 L8 0Z"/>
 </g>
 <text x="6" y="22" font-size="7" fill="#c9d6f2" font-family="Arial" font-weight="bold">4 DRONES DOWNED</text>
</svg>"""


def mine():
    return """
<svg viewBox="0 0 240 84" preserveAspectRatio="xMidYMid slice">
 <rect width="240" height="84" fill="#5c7a55"/>
 <path d="M0 0 H240 V18 Q200 26 170 20 Q130 14 100 22 Q60 30 0 20Z" fill="#7aa06c"/>
 <path d="M40 22 L80 70 L170 70 L204 22Z" fill="#8a6a46"/>
 <path d="M58 40 L186 40 L176 54 L70 54Z" fill="#6f5236" opacity="0.6"/>
 <path d="M70 56 L176 56 L170 70 L80 70Z" fill="#6c8ea8"/>
 <path d="M84 62 q6 -2 12 0 t12 0 t12 0 t12 0 t12 0" stroke="#d6e6f2" stroke-width="0.8" fill="none"/>
 <path d="M150 22 L150 58" stroke="#e8d8b0" stroke-width="1"/>
 <g transform="translate(150,22)"><circle r="4" fill="#ffcf3a"/><rect x="-3" y="4" width="6" height="9" fill="#ff7a1a"/></g>
 <g transform="translate(110,18)"><circle r="3.5" fill="#ffcf3a"/><rect x="-3" y="3.5" width="6" height="8" fill="#ff7a1a"/></g>
 <path d="M200 0 Q206 30 196 60" stroke="#6c8ea8" stroke-width="5" fill="none" opacity="0.8"/>
 <text x="30" y="68" font-size="7" fill="#fff" font-family="Arial" font-weight="bold">100 M DEEP</text>
</svg>"""


def garment():
    machines = "".join(
        f'<g transform="translate({28 + i * 52},48)"><rect x="0" y="12" width="40" height="5" fill="#8a6a46"/>'
        f'<path d="M6 12 V2 H30 V6 H12 V12Z" fill="#e9e4d8" stroke="#9c9484" stroke-width="0.6"/>'
        f'<rect x="26" y="6" width="3" height="6" fill="#9c9484"/>'
        f'<circle cx="18" cy="-6" r="5" fill="#3a2a22"/><rect x="12" y="-1" width="12" height="13" rx="3" fill="{c}"/></g>'
        for i, c in enumerate(["#d14b6b", "#2e7d9a", "#e0a43a", "#5a8f4e"])
    )
    return f"""
<svg viewBox="0 0 240 84" preserveAspectRatio="xMidYMid slice">
 <rect width="240" height="84" fill="#efe7da"/>
 <rect y="66" width="240" height="18" fill="#c9bba4"/>
 {machines}
 <g transform="translate(150,12)">
  <path d="M0 8 L10 0 H78 V22 H10Z" fill="#2e7d4f"/><circle cx="10" cy="11" r="2.2" fill="#efe7da"/>
  <text x="44" y="15" font-size="9" fill="#fff" text-anchor="middle" font-family="Arial" font-weight="bold">17,500 TK</text>
 </g>
 <text x="8" y="24" font-size="9" fill="#2e7d4f" font-family="Arial" font-weight="bold">+36%</text>
</svg>"""


def treaty():
    return """
<svg viewBox="0 0 240 84" preserveAspectRatio="xMidYMid slice">
 <rect width="240" height="84" fill="#cfe3ee"/>
 <path d="M0 62 Q120 50 240 62 V84 H0Z" fill="#7fae6a"/>
 <path d="M70 58 Q120 44 170 58Z" fill="#b8c7b0"/>
 <path d="M118 46 V16" stroke="#6b6b6b" stroke-width="1.2"/>
 <path d="M106 46 L120 14 L134 46" stroke="#8a8a8a" stroke-width="1.4" fill="none"/>
 <rect x="119" y="16" width="16" height="10" fill="#1d3b8a"/>
 <g transform="translate(36,12)">
  <rect width="34" height="22" fill="#1f5f8b"/><path d="M0 22 L34 0" stroke="#ffd34d" stroke-width="3"/>
  <path d="M0 21 L34 -1" stroke="#fff" stroke-width="0.6"/><path d="M0 0 L34 22 V0Z" fill="#2e7d4f" opacity="0"/>
  <path d="M34 0 V22 H0Z" fill="#2e7d4f"/><path d="M0 22 L34 0" stroke="#ffd34d" stroke-width="3"/>
  <circle cx="7" cy="5" r="1" fill="#fff"/><circle cx="12" cy="5" r="1" fill="#fff"/><circle cx="9.5" cy="9" r="1" fill="#fff"/>
 </g>
 <g transform="translate(170,12)">
  <rect width="34" height="22" fill="#1d3b8a"/>
  <path d="M0 0 L14 9 M14 0 L0 9" stroke="#fff" stroke-width="2"/><path d="M7 0 V9 M0 4.5 H14" stroke="#fff" stroke-width="2.6"/>
  <path d="M7 0 V9 M0 4.5 H14" stroke="#c8102e" stroke-width="1.2"/>
  <circle cx="25" cy="7" r="1.4" fill="#fff"/><circle cx="25" cy="17" r="1.4" fill="#fff"/><circle cx="20" cy="13" r="1.4" fill="#fff"/><circle cx="30" cy="12" r="1.4" fill="#fff"/>
 </g>
 <g transform="translate(120,66)">
  <path d="M-34 0 C-24 -6 -12 -6 -2 0 L-8 6 C-16 3 -26 3 -34 6Z" fill="#e8b48a"/>
  <path d="M34 0 C24 -6 12 -6 2 0 L8 6 C16 3 26 3 34 6Z" fill="#a8744e"/>
  <path d="M-40 -2 H-34 V8 H-40Z M40 -2 H34 V8 H40Z" fill="#2a3a5a"/>
 </g>
</svg>"""


def refinery():
    return """
<svg viewBox="0 0 240 84" preserveAspectRatio="xMidYMid slice">
 <rect width="240" height="84" fill="#141a2b"/>
 <path d="M0 70 H240 V84 H0Z" fill="#23232a"/>
 <g fill="#4a5060">
  <rect x="30" y="30" width="10" height="40"/><rect x="46" y="20" width="8" height="50"/>
  <rect x="60" y="44" width="40" height="26" rx="12"/><rect x="150" y="40" width="44" height="30" rx="13"/>
  <rect x="200" y="26" width="8" height="44"/>
 </g>
 <path d="M44 20 C36 4 64 -4 52 -18 C80 -6 76 14 58 22Z" fill="#2a2a30" opacity="0.8"/>
 <path d="M146 44 C136 30 152 24 148 12 C162 22 166 32 160 44Z" fill="#ff7a1a"/>
 <path d="M150 44 C146 36 154 32 152 26 C160 32 160 38 158 44Z" fill="#ffd34d"/>
 <path d="M196 36 C190 26 202 22 200 12 C210 20 212 28 206 36Z" fill="#ff7a1a"/>
 <path d="M150 14 C136 -4 176 -10 160 -30 C196 -14 186 6 168 16Z" fill="#2a2a30" opacity="0.7"/>
 <g fill="#0b0b0d"><path d="M100 14 L116 14 L108 10Z"/><path d="M104 14 L98 18 L102 14Z M112 14 L118 18 L114 14Z"/></g>
 <text x="6" y="22" font-size="7" fill="#c9d6f2" font-family="Arial" font-weight="bold">SYZRAN · KUIBYSHEV</text>
</svg>"""


def sudan():
    return """
<svg viewBox="0 0 240 84" preserveAspectRatio="xMidYMid slice">
 <rect width="240" height="84" fill="#f1dcb4"/>
 <path d="M0 58 Q60 50 120 58 T240 56 V84 H0Z" fill="#d9b67c"/>
 <path d="M0 66 Q80 58 150 70 T240 66" stroke="#4f86b0" stroke-width="5" fill="none"/>
 <rect x="70" y="20" width="100" height="40" rx="3" fill="#fbf6ea" stroke="#b9a37a"/>
 <rect x="80" y="30" width="80" height="4" fill="#d8c8a6"/><rect x="80" y="38" width="64" height="4" fill="#d8c8a6"/>
 <rect x="80" y="46" width="72" height="4" fill="#d8c8a6"/>
 <path d="M60 14 L180 66 M180 14 L60 66" stroke="#b3261e" stroke-width="5" stroke-linecap="round" opacity="0.85"/>
 <text x="120" y="17" font-size="7.5" fill="#5a4630" text-anchor="middle" font-family="Arial" font-weight="bold">TALKS IN ADDIS? NO</text>
</svg>"""


def cuba():
    return """
<svg viewBox="0 0 240 84" preserveAspectRatio="xMidYMid slice">
 <rect width="240" height="84" fill="#bfe1ef"/>
 <path d="M0 60 H240 V84 H0Z" fill="#e8dcc6"/>
 <g fill="#f2c9a0" stroke="#c99a6a" stroke-width="0.6">
  <rect x="18" y="30" width="40" height="30"/><rect x="62" y="22" width="34" height="38"/><rect x="100" y="34" width="30" height="26"/>
 </g>
 <g fill="#5a86a8"><rect x="24" y="36" width="6" height="8"/><rect x="40" y="36" width="6" height="8"/><rect x="70" y="30" width="6" height="8"/><rect x="84" y="30" width="6" height="8"/><rect x="108" y="40" width="6" height="8"/></g>
 <g transform="translate(170,18)">
  <rect x="0" y="0" width="44" height="40" rx="4" fill="#fff" stroke="#3a7bd5" stroke-width="1.5"/>
  <path d="M22 8 V32 M10 20 H34" stroke="#3a7bd5" stroke-width="6"/>
 </g>
 <g transform="translate(140,58)">
  <rect x="0" y="-16" width="16" height="16" rx="2" fill="#b3261e"/><rect x="5" y="-20" width="6" height="4" fill="#7a1a14"/>
  <path d="M-3 -18 L19 2 M19 -18 L-3 2" stroke="#222" stroke-width="2.4"/>
 </g>
 <text x="6" y="20" font-size="7" fill="#1d3557" font-family="Arial" font-weight="bold">$2M FOR VACCINES</text>
</svg>"""


def femicide():
    """UNODC / UN Women rates of femicide by partners or family, per 100,000 women."""
    rows = [("AFRICA", 2.9), ("AMERICAS", 1.4), ("OCEANIA", 1.1), ("ASIA", 0.6), ("EUROPE", 0.5)]
    bars = []
    for i, (name, v) in enumerate(rows):
        y = 19 + i * 11.5
        w = v / 2.9 * 96
        bars.append(f'<text x="136" y="{y + 8}" font-size="7" fill="#f3e9e4" font-family="Arial" font-weight="bold">{name}</text>'
                    f'<rect x="176" y="{y}" width="{w:.1f}" height="8" fill="#e8743b"/>'
                    f'<text x="{176 + w + 3:.1f}" y="{y + 8}" font-size="7" fill="#f3e9e4" font-family="Arial">{v}</text>')
    flags = "".join(
        f'<path d="M{10 + (i % 6) * 9} {44 + (i // 6) * 13} v-9 l6 2.2 l-6 2.2" fill="#ff8c3a" stroke="#ffd9c0" stroke-width="0.4"/>'
        for i in range(18))
    return f"""
<svg viewBox="0 0 240 84" preserveAspectRatio="xMidYMid slice">
 <rect width="240" height="84" fill="#3b2433"/>
 <text x="10" y="22" font-size="16" fill="#ffb37a" font-family="Georgia" font-weight="bold">47,000</text>
 <text x="10" y="32" font-size="7" fill="#f3e9e4" font-family="Arial">KILLED IN 2025 · 5 AN HOUR</text>
 {flags}
 <text x="136" y="15" font-size="6" fill="#d9c3cc" font-family="Arial">RATE PER 100,000 WOMEN</text>
 {''.join(bars)}
</svg>"""


def signing():
    """Two leaders sign at a table in Canberra, flags behind them."""
    return """
<svg viewBox="0 0 240 84" preserveAspectRatio="xMidYMid slice">
 <rect width="240" height="84" fill="#dfe9f1"/>
 <rect y="58" width="240" height="26" fill="#b99a74"/>
 <g transform="translate(26,10)">
  <path d="M0 0 V46" stroke="#8a8a8a" stroke-width="1.5"/>
  <rect x="1" y="0" width="34" height="20" fill="#1d3b8a"/>
  <path d="M1 0 L15 9 M15 0 L1 9" stroke="#fff" stroke-width="1.8"/><path d="M8 0 V9 M1 4.5 H15" stroke="#fff" stroke-width="2.4"/>
  <path d="M8 0 V9 M1 4.5 H15" stroke="#c8102e" stroke-width="1.1"/>
  <circle cx="26" cy="6" r="1.3" fill="#fff"/><circle cx="26" cy="15" r="1.3" fill="#fff"/><circle cx="21" cy="11" r="1.3" fill="#fff"/><circle cx="31" cy="10" r="1.3" fill="#fff"/><circle cx="8" cy="15" r="1.8" fill="#fff"/>
 </g>
 <g transform="translate(180,10)">
  <path d="M34 0 V46" stroke="#8a8a8a" stroke-width="1.5"/>
  <rect x="0" y="0" width="34" height="20" fill="#1f6fb2"/>
  <path d="M34 0 V20 H0Z" fill="#2e8b3e"/><path d="M0 20 L34 0" stroke="#f2c418" stroke-width="3.2"/>
  <circle cx="5" cy="4" r="0.9" fill="#fff"/><circle cx="10" cy="4" r="0.9" fill="#fff"/><circle cx="7.5" cy="7.5" r="0.9" fill="#fff"/><circle cx="5" cy="11" r="0.9" fill="#fff"/><circle cx="10" cy="11" r="0.9" fill="#fff"/>
 </g>
 <g>
  <circle cx="92" cy="30" r="8" fill="#e8c4a0"/><path d="M84 27 q8 -9 16 0" fill="#9a8a7a"/>
  <path d="M80 58 q0 -18 12 -18 q12 0 12 18Z" fill="#26324a"/>
  <circle cx="148" cy="30" r="8" fill="#8a5a3a"/><path d="M140 27 q8 -9 16 0" fill="#1e1a18"/>
  <path d="M136 58 q0 -18 12 -18 q12 0 12 18Z" fill="#2a3a5a"/>
 </g>
 <rect x="60" y="54" width="120" height="8" fill="#6b4a2a"/>
 <rect x="104" y="50" width="32" height="5" fill="#fff" stroke="#bbb" stroke-width="0.5"/>
 <path d="M100 52 l8 -4 M140 52 l-8 -4" stroke="#1a1a1a" stroke-width="1.6"/>
 <text x="120" y="71" font-size="7" fill="#fff" text-anchor="middle" font-family="Arial" font-weight="bold">SIGNED · 25 NOV</text>
</svg>"""


def ebola():
    """A clinic in Ituri with smoke from fighting behind it; a white aid convoy drives staff out."""
    return """
<svg viewBox="0 0 240 84" preserveAspectRatio="xMidYMid slice">
 <rect width="240" height="84" fill="#c9d9c2"/>
 <path d="M0 40 Q40 30 80 38 T160 34 T240 38 V84 H0Z" fill="#5f8f4e"/>
 <path d="M150 34 C140 18 166 12 156 -2 C182 10 178 26 166 36Z" fill="#555" opacity="0.55"/>
 <path d="M196 36 C190 24 206 20 200 8 C216 18 214 28 206 38Z" fill="#555" opacity="0.45"/>
 <rect y="60" width="240" height="24" fill="#a8835a"/>
 <rect x="22" y="26" width="92" height="34" fill="#f4f1e8" stroke="#b5ab95"/>
 <path d="M18 27 L68 12 L118 27Z" fill="#b3261e"/>
 <rect x="58" y="33" width="20" height="20" fill="#fff" stroke="#ddd"/>
 <path d="M68 36 V50 M61 43 H75" stroke="#d62828" stroke-width="5"/>
 <rect x="30" y="34" width="12" height="10" fill="#7fa3c0"/><rect x="92" y="34" width="12" height="10" fill="#7fa3c0"/>
 <rect x="44" y="48" width="10" height="12" fill="#6b4a2a"/>
 <g transform="translate(150,52)">
  <rect x="0" y="0" width="40" height="14" rx="2" fill="#fbfbfb" stroke="#999"/>
  <rect x="26" y="-6" width="14" height="10" rx="2" fill="#fbfbfb" stroke="#999"/>
  <rect x="29" y="-4" width="9" height="5" fill="#7fa3c0"/>
  <text x="13" y="10" font-size="6" fill="#1f6fb2" text-anchor="middle" font-family="Arial" font-weight="bold">WHO</text>
  <circle cx="9" cy="15" r="3.5" fill="#222"/><circle cx="32" cy="15" r="3.5" fill="#222"/>
 </g>
 <path d="M196 64 h20 M200 69 h24" stroke="#fff" stroke-width="1.2" opacity="0.8"/>
 <text x="8" y="20" font-size="7" fill="#1d3557" font-family="Arial" font-weight="bold">AKWE · 3 DAYS</text>
</svg>"""


def court_lead():
    """A federal courthouse in Brooklyn: columns, a gavel and the 10-of-12 tally."""
    cols = "".join(f'<rect x="{78 + i * 30}" y="52" width="12" height="62" fill="#ece7db"/>' for i in range(6))
    marks = "".join(
        f'<rect x="{18 + (i % 6) * 13}" y="{40 + (i // 6) * 18}" width="10" height="13" rx="1.5" '
        f'fill="{"#b3261e" if i < 10 else "#9aa6b2"}"/>' for i in range(12))
    return f"""
<svg viewBox="0 0 320 150" preserveAspectRatio="xMidYMid slice">
 <defs><linearGradient id="skyC" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#9fb7cc"/><stop offset="1" stop-color="#dfe7ee"/></linearGradient></defs>
 <rect width="320" height="150" fill="url(#skyC)"/>
 <g transform="translate(52,14) scale(0.84)">
 <path d="M66 52 L160 20 L254 52Z" fill="#f4f0e6" stroke="#b9b2a2"/>
 <rect x="68" y="49" width="184" height="5" fill="#cfc7b5"/>
 {cols}
 <rect x="62" y="114" width="196" height="8" fill="#cfc7b5"/><rect x="54" y="122" width="212" height="28" fill="#bdb5a3"/>
 <text x="160" y="45" font-size="8.5" fill="#6b6556" text-anchor="middle" font-family="Georgia" letter-spacing="2">U.S. COURT · BROOKLYN</text>
 </g>
 <rect x="10" y="22" width="92" height="76" rx="3" fill="#1d2633" opacity="0.92"/>
 <text x="56" y="34" font-size="7.5" fill="#f2f2f2" text-anchor="middle" font-family="Arial" font-weight="bold">COUNTS: 10 GUILTY</text>
 {marks}
 <text x="56" y="91" font-size="6.5" fill="#c9d3dd" text-anchor="middle" font-family="Arial">2 ACQUITTED</text>
 <g transform="translate(292,74) rotate(-24) scale(0.85)">
  <rect x="-5" y="0" width="10" height="50" rx="3" fill="#7a4b2a"/>
  <rect x="-20" y="-14" width="40" height="17" rx="4" fill="#5e3820"/>
 </g>
 <rect x="266" y="124" width="48" height="7" rx="2" fill="#5e3820"/>
</svg>"""


def pif_tower():
    """Riyadh at dusk: the PIF tower hit, smoke and broken glass, a drone overhead."""
    city = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{150 - y}" fill="#3a3346"/>'
                   for x, y, w in [(8, 100, 26), (40, 88, 20), (66, 108, 30), (198, 96, 24), (228, 84, 18),
                                   (252, 104, 30), (288, 92, 26)])
    wins = "".join(f'<rect x="{151 + (i % 3) * 7}" y="{44 + (i // 3) * 9}" width="4" height="5" fill="#ffd98a" opacity="0.7"/>'
                   for i in range(30))
    return f"""
<svg viewBox="0 0 320 150" preserveAspectRatio="xMidYMid slice">
 <defs><linearGradient id="skyR" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#2b2f55"/><stop offset="0.7" stop-color="#c46a4a"/><stop offset="1" stop-color="#e9a35c"/></linearGradient></defs>
 <rect width="320" height="150" fill="url(#skyR)"/>
 {city}
 <path d="M140 150 L144 36 L162 18 L180 36 L184 150Z" fill="#4c5a74"/>
 <path d="M162 18 L162 150" stroke="#6d7c98" stroke-width="1"/>
 {wins}
 <path d="M144 62 L184 62 L184 80 L144 80Z" fill="#1c1c22"/>
 <path d="M150 64 C140 50 160 44 152 30 C170 40 172 54 166 64Z" fill="#ff8a1f"/>
 <path d="M172 62 C168 40 196 30 186 6 C214 22 206 46 190 62Z" fill="#2a2a30" opacity="0.8"/>
 <g transform="translate(240,30)" fill="#111">
  <path d="M-12 0 L12 0 L0 -5Z"/><path d="M-4 0 L-14 7 L-9 0Z M4 0 L14 7 L9 0Z"/>
 </g>
 <path d="M228 34 Q206 42 186 60" stroke="#ffe08a" stroke-width="1.2" fill="none" stroke-dasharray="2 2"/>
 <text x="10" y="24" font-size="8.5" fill="#fff" font-family="Arial" font-weight="bold">RIYADH · PIF TOWER</text>
 <text x="10" y="35" font-size="7" fill="#ffe2c4" font-family="Arial">11 HURT · 2ND STRIKE IN A WEEK</text>
</svg>"""


def markets_up():
    """A trading board in Taipei: rising green lines and the day's gains."""
    pts = []
    rnd = random.Random(9)
    y = 118.0
    for i in range(0, 41):
        x = 14 + i * 5.2
        drift = -0.3 if i < 6 else -2.3 if i < 28 else -0.5
        y += drift + rnd.uniform(-2.0, 2.2)
        pts.append(f"{x:.1f},{y:.1f}")
    line = " ".join(pts)
    area = f"14,128 {line} {14 + 40 * 5.2:.1f},128"
    rows = [("TAIEX", "+9.0%"), ("KOSPI", "+7.0%"), ("NIKKEI", "+3.9%"), ("TSMC", "+9.9%"),
            ("HYNIX", "+8.6%"), ("SAMSUNG", "+7.5%")]
    board = []
    for i, (k, v) in enumerate(rows):
        yy = 30 + i * 17
        board.append(f'<text x="226" y="{yy}" font-size="7.5" fill="#cfd8e3" font-family="Arial" font-weight="bold">{k}</text>'
                     f'<text x="312" y="{yy}" font-size="9" fill="#3ddc84" font-family="Arial" font-weight="bold" text-anchor="end">▲{v}</text>')
    return f"""
<svg viewBox="0 0 320 150" preserveAspectRatio="xMidYMid slice">
 <rect width="320" height="150" fill="#0f1722"/>
 <g stroke="#1f2b3b" stroke-width="1">
  <path d="M14 38 H216 M14 60 H216 M14 82 H216 M14 104 H216 M14 126 H216"/>
  <path d="M50 20 V128 M92 20 V128 M134 20 V128 M176 20 V128"/>
 </g>
 <polygon points="{area}" fill="#2ecc71" opacity="0.16"/>
 <polyline points="{line}" fill="none" stroke="#3ddc84" stroke-width="2.4" stroke-linejoin="round"/>
 <circle cx="{14 + 40 * 5.2:.1f}" cy="{y:.1f}" r="3.2" fill="#3ddc84"/>
 <rect x="220" y="14" width="96" height="112" rx="3" fill="#162233" stroke="#26384f"/>
 {''.join(board)}
 <text x="14" y="24" font-size="8" fill="#8da2bb" font-family="Arial" font-weight="bold">ASIA CLOSE · TUE 24 NOV</text>
</svg>"""


def probe():
    """A party headquarters under a magnifying glass: the Politburo probe."""
    return """
<svg viewBox="0 0 240 84" preserveAspectRatio="xMidYMid slice">
 <rect width="240" height="84" fill="#f1e2c6"/>
 <rect y="62" width="240" height="22" fill="#cdb48a"/>
 <path d="M30 34 L120 16 L210 34Z" fill="#b3261e"/>
 <rect x="38" y="34" width="164" height="28" fill="#e9dcc0" stroke="#b9a37a"/>
 <g fill="#b9a37a">""" + "".join(f'<rect x="{46 + i * 20}" y="38" width="7" height="24"/>' for i in range(8)) + """</g>
 <circle cx="120" cy="25" r="5" fill="#f2c418"/>
 <g transform="translate(176,44)">
  <circle r="17" fill="#ffffff" fill-opacity="0.35" stroke="#2a2a2a" stroke-width="4"/>
  <path d="M12 12 L26 26" stroke="#2a2a2a" stroke-width="6" stroke-linecap="round"/>
 </g>
 <text x="10" y="20" font-size="7" fill="#7a1a14" font-family="Arial" font-weight="bold">4TH POLITBURO PROBE</text>
</svg>"""


def trophy():
    """The Africa Cup of Nations trophy handed back to Senegal."""
    return """
<svg viewBox="0 0 240 84" preserveAspectRatio="xMidYMid slice">
 <rect width="240" height="84" fill="#1f7a3f"/>
 <rect x="0" y="0" width="80" height="84" fill="#17703a"/><rect x="160" y="0" width="80" height="84" fill="#17703a"/>
 <rect x="0" y="0" width="240" height="84" fill="none"/>
 <g transform="translate(120,14)">
  <path d="M-18 0 H18 C18 22 8 32 0 34 C-8 32 -18 22 -18 0Z" fill="#f2c418" stroke="#b8860b"/>
  <path d="M-18 4 C-30 4 -30 18 -14 20 M18 4 C30 4 30 18 14 20" stroke="#f2c418" stroke-width="3" fill="none"/>
  <rect x="-4" y="34" width="8" height="10" fill="#d4a017"/><rect x="-14" y="44" width="28" height="8" fill="#6b4a2a"/>
 </g>
 <g transform="translate(18,20)"><rect width="30" height="20" fill="#00853f"/><rect x="10" width="10" height="20" fill="#fdef42"/>
  <rect x="20" width="10" height="20" fill="#e31b23"/><circle cx="15" cy="10" r="2.6" fill="#00853f"/></g>
 <text x="196" y="30" font-size="9" fill="#fff" text-anchor="middle" font-family="Arial" font-weight="bold">CAS</text>
 <text x="196" y="42" font-size="7" fill="#d6f0dd" text-anchor="middle" font-family="Arial">RULING</text>
 <text x="120" y="76" font-size="7" fill="#fff" text-anchor="middle" font-family="Arial" font-weight="bold">AFCON 2025</text>
</svg>"""


def scoreline():
    """A floodlit pitch and the 5-1 scoreboard at the Bernabeu."""
    return """
<svg viewBox="0 0 240 84" preserveAspectRatio="xMidYMid slice">
 <rect width="240" height="84" fill="#10213a"/>
 <path d="M0 50 L240 50 L240 84 L0 84Z" fill="#2e8b3e"/>
 <path d="M0 50 L240 50" stroke="#fff" stroke-width="1"/><path d="M120 50 V84" stroke="#fff" stroke-width="0.8"/>
 <ellipse cx="120" cy="68" rx="18" ry="6" fill="none" stroke="#fff" stroke-width="0.8"/>
 <g fill="#fff8d0"><circle cx="20" cy="14" r="4"/><circle cx="220" cy="14" r="4"/></g>
 <path d="M20 18 L10 50 M220 18 L230 50" stroke="#fff8d0" stroke-width="0.6" opacity="0.4"/>
 <rect x="64" y="16" width="112" height="28" rx="3" fill="#0b0b0f" stroke="#444"/>
 <text x="84" y="35" font-size="8" fill="#fff" text-anchor="middle" font-family="Arial" font-weight="bold">RMA</text>
 <text x="120" y="37" font-size="15" fill="#ffd34d" text-anchor="middle" font-family="Arial" font-weight="bold">5-1</text>
 <text x="156" y="35" font-size="8" fill="#fff" text-anchor="middle" font-family="Arial" font-weight="bold">PSV</text>
 <circle cx="196" cy="70" r="5" fill="#fff" stroke="#222" stroke-width="0.8"/>
</svg>"""


def debt():
    """Venezuela's debt stacked into bars: defaulted bonds, PDVSA and arbitration."""
    parts = [("BONDS", 110, "#b3261e"), ("PDVSA ETC", 67.3, "#d4881c"), ("ARBITRATION", 26, "#7b4a9e")]
    bars, x = [], 70
    for name, v, col in parts:
        w = v / 237.5 * 150
        bars.append(f'<rect x="{x:.1f}" y="40" width="{w:.1f}" height="20" fill="{col}"/>'
                    f'<text x="{x + 3:.1f}" y="70" font-size="6" fill="#3a2a26" font-family="Arial">{name}</text>')
        x += w
    return f"""
<svg viewBox="0 0 240 84" preserveAspectRatio="xMidYMid slice">
 <rect width="240" height="84" fill="#f6efe0"/>
 <g transform="translate(14,30)"><rect width="42" height="28" fill="#f4c400"/><rect y="9" width="42" height="10" fill="#0033a0"/>
  <rect y="19" width="42" height="9" fill="#cf142b"/></g>
 <text x="70" y="30" font-size="13" fill="#141414" font-family="Georgia" font-weight="bold">$237.5bn</text>
 {''.join(bars)}
</svg>"""


def pharma():
    """A capsule and a deal tag: Sanofi agrees to buy Insmed."""
    return """
<svg viewBox="0 0 240 84" preserveAspectRatio="xMidYMid slice">
 <rect width="240" height="84" fill="#ece6f4"/>
 <g transform="translate(70,44) rotate(-30)">
  <rect x="-40" y="-14" width="80" height="28" rx="14" fill="#7b4a9e"/>
  <path d="M0 -14 H26 A14 14 0 0 1 26 14 H0Z" fill="#f4f1f8"/>
  <rect x="-40" y="-14" width="80" height="28" rx="14" fill="none" stroke="#4b2a66" stroke-width="1.5"/>
 </g>
 <path d="M126 40 h22 M140 32 l10 8 -10 8" stroke="#4b2a66" stroke-width="3" fill="none"/>
 <rect x="158" y="26" width="70" height="28" rx="4" fill="#fff" stroke="#7b4a9e"/>
 <text x="193" y="38" font-size="7" fill="#4b2a66" text-anchor="middle" font-family="Arial" font-weight="bold">SANOFI → INSMED</text>
 <text x="193" y="49" font-size="7" fill="#555" text-anchor="middle" font-family="Arial">$175 A SHARE</text>
</svg>"""


def ariane():
    """A heavy launcher on the pad at Kourou with a satellite stack above."""
    return """
<svg viewBox="0 0 240 84" preserveAspectRatio="xMidYMid slice">
 <rect width="240" height="84" fill="#16233f"/>
 <g fill="#fff" opacity="0.7"><circle cx="20" cy="18" r="0.8"/><circle cx="60" cy="12" r="0.7"/><circle cx="200" cy="20" r="0.9"/><circle cx="170" cy="10" r="0.7"/><circle cx="222" cy="40" r="0.6"/></g>
 <path d="M0 70 H240 V84 H0Z" fill="#2c5a3a"/>
 <g transform="translate(120,0)">
  <path d="M-6 16 L0 6 L6 16Z" fill="#e8e8e8"/>
  <rect x="-6" y="16" width="12" height="46" fill="#f4f4f4" stroke="#bbb" stroke-width="0.5"/>
  <rect x="-15" y="34" width="6" height="30" rx="2" fill="#dcdcdc"/><rect x="9" y="34" width="6" height="30" rx="2" fill="#dcdcdc"/>
  <rect x="-21" y="38" width="5" height="26" rx="2" fill="#cfcfcf"/><rect x="16" y="38" width="5" height="26" rx="2" fill="#cfcfcf"/>
  <path d="M-5 62 L0 76 L5 62Z M-14 64 L-12 74 L-10 64Z M10 64 L12 74 L14 64Z" fill="#ffcf5a"/>
 </g>
 <text x="10" y="22" font-size="7" fill="#c9d6f2" font-family="Arial" font-weight="bold">KOUROU · ARIANE 6</text>
</svg>"""


def tube():
    """A London Underground train standing at an empty platform, a closed sign."""
    return """
<svg viewBox="0 0 240 84" preserveAspectRatio="xMidYMid slice">
 <rect width="240" height="84" fill="#e9e4da"/>
 <path d="M0 0 H240 V30 Q120 4 0 30Z" fill="#cfc6b2"/>
 <rect y="58" width="240" height="26" fill="#8a8170"/>
 <rect x="10" y="30" width="170" height="28" rx="8" fill="#e8e8e8" stroke="#555"/>
 <rect x="10" y="44" width="170" height="5" fill="#d62828"/>
 <g fill="#5a86a8">""" + "".join(f'<rect x="{20 + i * 26}" y="34" width="16" height="9" rx="2"/>' for i in range(6)) + """</g>
 <g transform="translate(206,36)">
  <circle r="16" fill="none" stroke="#d62828" stroke-width="5"/><rect x="-20" y="-4" width="40" height="8" fill="#1d3b8a"/>
  <text y="3" font-size="5.5" fill="#fff" text-anchor="middle" font-family="Arial" font-weight="bold">CLOSED</text>
 </g>
 <text x="10" y="22" font-size="7" fill="#3a3a3a" font-family="Arial" font-weight="bold">CIRCLE \u00b7 PICCADILLY</text>
</svg>"""


ART = dict(launch=launch, tube=tube, markets=markets, hormuz=hormuz, court=court, drones=drones,
           court_lead=court_lead, pharma=pharma, ariane=ariane, pif_tower=pif_tower, markets_up=markets_up, probe=probe,
           trophy=trophy, scoreline=scoreline, debt=debt,
           mine=mine, garment=garment, treaty=signing, refinery=refinery, sudan=sudan, cuba=cuba,
           femicide=femicide, ebola=ebola)

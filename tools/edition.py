"""The stories on the front page for Wednesday 25 November 2026.

Every story here happened, or was first reported, on 25 November 2026
(in some time zone), and each carries the outlets that reported it.
Claims that rest on one side's word are attributed ("IRGC says", "reported").
"""

DAY = "Wednesday 25 November 2026"
DAY_SHORT = "WED 25 NOV 2026"

# Region keys and their colours on the map and the region strip.
REGIONS = {
    "asia": ("Asia", "#c0392b"),
    "mideast": ("Middle East", "#d4881c"),
    "europe": ("Europe", "#1f5f8b"),
    "americas": ("Americas", "#2e7d4f"),
    "africa": ("Africa", "#7b4a9e"),
    "oceania": ("Oceania", "#138a8a"),
}

# Big numbers across the top: (figure, caption).
KPIS = [
    ("1st", "foreign astronaut to visit China's Tiangong station"),
    ("−6.2%", "Kospi, as Asia's chip stocks plunge"),
    ("2", "tankers hit mines in Hormuz, Iran's IRGC says"),
    ("26", "miners trapped in a flooded West Java pit"),
    ("+36%", "Bangladesh garment minimum wage"),
    ("10 of 12", "counts: Huawei rejects its US conviction"),
]

# Three lead stories, each with a drawn scene (art key in art.py).
LEADS = [
    dict(
        art="launch", tag="LIFTOFF", region="asia", place="JIUQUAN, CHINA",
        beat="SPACE",
        head="Shenzhou-24 lifts off with Pakistan's first astronaut",
        dek="A Long March 2F rose from Jiuquan on Wednesday morning; Muhammad Zeeshan "
            "Ali is the first foreigner to fly to Tiangong, which the crew reached hours later.",
        src="XINHUA · AA · REUTERS",
    ),
    dict(
        art="markets", tag="SELL-OFF", region="asia", place="SEOUL · TAIPEI · TOKYO",
        beat="MARKETS",
        head="Asia's chip stocks plunge on AI doubts",
        dek="Kospi −6.2%, Taiex −4.8%, Nikkei −2.8%; Samsung −9.9% and SK Hynix "
            "−11.1% as Nvidia CEO Huang's return fails to calm markets.",
        src="AL JAZEERA · AFP",
    ),
    dict(
        art="hormuz", tag="WAR AT SEA", region="mideast", place="STRAIT OF HORMUZ",
        beat="IRAN WAR",
        head="Two oil tankers hit mines and burn, Iran says",
        dek="Iran's IRGC Navy says the ships struck naval mines on an "
            "“unauthorised route” early on Wednesday; no independent confirmation yet.",
        src="IRIB · AA · ARAB NEWS",
    ),
]

# Eight secondary stories with small drawn scenes.
CARDS = [
    dict(art="court", region="americas", place="NEW YORK · BEIJING",
         head="Huawei rejects US guilty verdict",
         dek="Convicted in Brooklyn on 10 of 12 counts; Beijing slams US “suppression”.",
         src="CNBC · TIME"),
    dict(art="drones", region="mideast", place="RAS TANURA, SAUDI ARABIA",
         head="Saudis down Houthi drones over oil port",
         dek="Four destroyed after coalition strikes on Hodeidah; Houthis threaten Jeddah.",
         src="AL JAZEERA · AFP"),
    dict(art="mine", region="asia", place="BOGOR, INDONESIA",
         head="26 trapped in flooded gold mine",
         dek="Rescuers search a 100-metre pit at Pongkor after a river burst its banks.",
         src="AL JAZEERA · REUTERS"),
    dict(art="garment", region="asia", place="DHAKA, BANGLADESH",
         head="Garment workers win 36% pay rise",
         dek="Minimum wage to rise to 17,500 taka ($136) a month after weeks of protest.",
         src="AL JAZEERA · AFP"),
    dict(art="treaty", region="oceania", place="CANBERRA, AUSTRALIA",
         head="Solomons PM in Canberra to sign treaty",
         dek="Matthew Wale meets Albanese as Honiara lets its China security pact lapse.",
         src="AAP · AFR"),
    dict(art="refinery", region="europe", place="SAMARA, RUSSIA",
         head="Ukrainian drones hit two refineries",
         dek="Fires reported at Syzran and Kuibyshev; Putin had called retaliation “inevitable”.",
         src="KYIV INDEPENDENT · WORLD"),
    dict(art="sudan", region="africa", place="KHARTOUM, SUDAN",
         head="Sudan rejects Ethiopia's peace offer",
         dek="Army-backed government says Addis Ababa is not neutral in the war with the RSF.",
         src="RADIO TAMAZUJ · NEWS.AZ"),
    dict(art="cuba", region="americas", place="HAVANA, CUBA",
         head="WHO chief urges end to fuel blockade",
         dek="Tedros pledges $2m for vaccines and hospital equipment on a visit to Cuba.",
         src="AL JAZEERA · REUTERS"),
]

# Map pins: (number, lon, lat, region). Numbers match leads (1-3) and cards (4-11).
PINS = [
    (1, 100.3, 40.96, "asia"), (2, 126.98, 37.57, "asia"), (3, 56.3, 26.6, "mideast"),
    (4, -73.99, 40.69, "americas"), (5, 50.16, 26.64, "mideast"), (6, 106.6, -6.6, "asia"),
    (7, 90.41, 23.81, "asia"), (8, 149.13, -35.28, "oceania"), (9, 48.47, 53.16, "europe"),
    (10, 32.56, 15.5, "africa"), (11, -82.37, 23.11, "americas"),
]

# Briefs: (number, place, text, region). Short and attributed.
BRIEFS = [
    (12, "TOKYO", "Tokyo Electron −12.5%, Advantest −12.9%", "asia"),
    (13, "TAIPEI", "Taiex ends −4.8% after an 8% intraday plunge", "asia"),
    (14, "SANAA", "Houthis tell Saudi Red Sea port workers to flee", "mideast"),
    (15, "TEHRAN", "IRGC chief says forces ready to push “enemy” back", "mideast"),
    (16, "HEBRON", "Israel gates roads used by 70,000 Palestinians", "mideast"),
    (17, "HONIARA", "Solomons won't renew 2022 China security pact", "oceania"),
    (18, "SUVA", "Fiji drought: 92 communities without water supply", "oceania"),
    (19, "MANILA", "ADB sees Asia's inflation at 4.2% this year", "asia"),
    (20, "KUALA LUMPUR", "Malaysia to send 6,803 Rohingya back to Myanmar", "asia"),
    (21, "ODESA", "Russian strike kills two, including a teenager", "europe"),
    (22, "WASHINGTON", "Trump team shelves business offers to Russia: FT", "americas"),
    (23, "WASHINGTON", "Hackers breached a CIA–ODNI unclassified system", "americas"),
    (24, "WASHINGTON", "Tariff rise readied for China, EU and 14 others", "americas"),
    (25, "JUNEAU", "Alaska ends voter-roll deal with Justice Dept", "americas"),
    (26, "CARACAS", "Venezuela puts its debt at $237.5bn, 242% of GDP", "americas"),
    (27, "PARIS", "Sarkozy and Carla Bruni ordered to stand trial", "europe"),
    (28, "BRUSSELS", "Costa pushes EU budget deal before Thursday summit", "europe"),
    (29, "KHARTOUM", "UN says drone attack damaged one of its buildings", "africa"),
    (30, "BUNIA, DRC", "CRP rebels halt advance, pledge to withdraw", "africa"),
    (31, "NEW YORK", "UN day against violence on women: 129 flags", "americas"),
]

DATE_CHECK = (
    "Left out as earlier news: Huang's return to Nvidia and the leaked count of Russia's war dead "
    "(Mon 23 Nov), COP31's collapse (Sun 22 Nov), the first strike on Riyadh's PIF tower (Thu 19 Nov). "
    "Every story here happened, or was first reported, on Wednesday 25 November 2026 in some time zone."
)

SOURCES = (
    "Sources: Al Jazeera · Anadolu · AFP · Reuters · AAP · AFR · CNBC · TIME · "
    "Xinhua · IRIB · Kyiv Independent · WORLD · Radio Tamazuj · PACNEWS · FT · Politico"
)

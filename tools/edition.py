"""The stories on the front page for Wednesday 25 November 2026.

Every story here happened, or was first reported, on 25 November 2026
(in some time zone), and each carries the outlets that reported it.
Claims that rest on one side's word are attributed ("IRGC says", "reported"),
and each drawn story carries how sure the reporting is (SURE below).
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
    "global": ("Global", "#5b5b5b"),
}

# How sure the reporting is: label -> (colour, meaning for the legend).
SURE = {
    "OFFICIAL": ("#1f5f8b", "government, agency or company statement"),
    "CONFIRMED": ("#2e7d4f", "two or more major outlets"),
    "REPORTED": ("#a07a18", "one outlet's reporting"),
    "CLAIM": ("#b3261e", "one side's word, unverified"),
}

# The day in UTC: only times the reports give.
TIMELINE = [
    ("00:21", "Shenzhou-24 lifts off"),
    ("03:56", "Crew docks at Tiangong"),
    ("05:30", "Taiex closes −4.8%"),
    ("06:30", "Kospi closes −6.2%"),
    ("10:00", "London Tube strike starts"),
]

# Big numbers across the top: (figure, caption).
KPIS = [
    ("1st", "foreign astronaut to visit China's Tiangong station"),
    ("−6.2%", "Kospi, as Asia's chip stocks plunge"),
    ("2", "tankers hit mines in Hormuz, Iran's IRGC says"),
    ("47,000", "women killed by partner or kin in 2025, UN says"),
    ("26", "miners trapped in a flooded West Java pit"),
    ("+36%", "Bangladesh garment minimum wage"),
]

# Three lead stories, each with a drawn scene (art key in art.py).
LEADS = [
    dict(
        art="launch", tag="LIFTOFF", region="asia", place="JIUQUAN, CHINA",
        beat="SPACE", sure="CONFIRMED",
        head="Shenzhou-24 flies a Pakistani to Tiangong",
        dek="Zeeshan Ali is the first foreigner to fly to Tiangong; the crew "
            "docked hours after the Long March 2F lifted off.",
        src="XINHUA · AA · REUTERS",
    ),
    dict(
        art="markets", tag="SELL-OFF", region="asia", place="SEOUL · TAIPEI · TOKYO",
        beat="MARKETS", sure="CONFIRMED",
        head="Asia's chip stocks crash on AI doubts",
        dek="Samsung −9.9%, SK Hynix −11.1%: Nvidia CEO Huang's return "
            "fails to calm markets; Taiex −4.8%.",
        src="AL JAZEERA · AFP",
    ),
    dict(
        art="hormuz", tag="WAR AT SEA", region="mideast", place="STRAIT OF HORMUZ",
        beat="IRAN WAR", sure="CLAIM",
        head="Two oil tankers hit mines and burn, Iran says",
        dek="The IRGC Navy says they took an “unauthorised route” early "
            "on Wednesday; not independently confirmed.",
        src="IRIB · AA · ARAB NEWS",
    ),
]

# Eight secondary stories with small drawn scenes.
CARDS = [
    dict(art="treaty", region="oceania", place="CANBERRA, AUSTRALIA", sure="OFFICIAL",
         head="Australia and Solomons sign security treaty",
         dek="No foreign bases allowed; more jobs and easier visas for Solomon Islanders.",
         src="PM.GOV.AU · ABC · NBC"),
    dict(art="femicide", region="global", place="UNITED NATIONS", sure="OFFICIAL",
         head="UN: five women an hour killed by partner or kin",
         dek="47,000 in 2025, says a brief for the day to end violence against women.",
         src="UNODC · UN WOMEN"),
    dict(art="court", region="asia", place="SHENZHEN · BEIJING", sure="OFFICIAL",
         head="Huawei rejects US guilty verdict",
         dek="Convicted in Brooklyn on 10 of 12 counts; Beijing slams US “suppression”.",
         src="CNBC · TIME"),
    dict(art="drones", region="mideast", place="RAS TANURA, SAUDI ARABIA", sure="OFFICIAL",
         head="Saudis down Houthi drones over oil port",
         dek="Four destroyed after coalition strikes on Hodeidah; Houthis threaten Jeddah.",
         src="AL JAZEERA · AFP"),
    dict(art="mine", region="asia", place="BOGOR, INDONESIA", sure="OFFICIAL",
         head="26 trapped in flooded gold mine",
         dek="Rescuers search a 100-metre pit at Pongkor after a river burst its banks.",
         src="AL JAZEERA · REUTERS"),
    dict(art="garment", region="asia", place="DHAKA, BANGLADESH", sure="OFFICIAL",
         head="Garment workers win 36% pay rise",
         dek="Minimum wage to rise to 17,500 taka ($136) a month after weeks of protest.",
         src="AL JAZEERA · AFP"),
    dict(art="refinery", region="europe", place="SAMARA, RUSSIA", sure="REPORTED",
         head="Ukrainian drones hit two refineries",
         dek="Fires reported at Syzran and Kuibyshev; Putin had called retaliation “inevitable”.",
         src="KYIV INDEPENDENT · WORLD"),
    dict(art="ebola", region="africa", place="ITURI, DR CONGO", sure="OFFICIAL",
         head="WHO pulls staff out of Ebola zone hospital",
         dek="Team sheltered 3 days in Akwe amid army–CRP fighting; Mongbwalu team moved.",
         src="WHO · ARAB NEWS · ANI"),
]

# Map pins: (number, lon, lat, region). Numbers match leads (1-3) and cards (4-11).
PINS = [
    (1, 100.3, 40.96, "asia"), (2, 126.98, 37.57, "asia"), (3, 56.3, 26.6, "mideast"),
    (4, 149.13, -35.28, "oceania"), (5, -73.97, 40.75, "global"), (6, 114.06, 22.54, "asia"),
    (7, 50.16, 26.64, "mideast"), (8, 106.6, -6.6, "asia"), (9, 90.41, 23.81, "asia"),
    (10, 48.47, 53.16, "europe"), (11, 30.0, 1.9, "africa"),
]

# Briefs: (number, place, text, region). Short and attributed.
BRIEFS = [
    (12, "TOKYO", "Tokyo Electron −12.5%, Advantest −12.9%", "asia"),
    (13, "TAIPEI", "Taiex ends −4.8% after an 8% intraday plunge", "asia"),
    (14, "HONG KONG", "Hang Seng ends 1.1% lower in a milder slide", "asia"),
    (15, "KUALA LUMPUR", "Malaysia Airlines' parent orders 10 Boeing 787s", "asia"),
    (16, "SANAA", "Houthis tell Saudi Red Sea port workers to flee", "mideast"),
    (17, "TEHRAN", "IRGC chief says forces ready to push “enemy” back", "mideast"),
    (18, "CANBERRA", "Australia apologises to LGBTQ military veterans", "oceania"),
    (19, "PERTH", "Deloitte barred from WA work over AI-flawed report", "oceania"),
    (20, "SUVA", "Fiji drought: 92 communities without water supply", "oceania"),
    (21, "KYIV", "US rules out troops in post-war guarantees: report", "europe"),
    (22, "KYIV REGION", "Russian strike kills one, hits delivery depots", "europe"),
    (23, "ODESA", "Russian strike kills two, including a teenager", "europe"),
    (24, "LONDON", "Tube strike shuts Circle and Piccadilly lines", "europe"),
    (25, "BRUSSELS", "EU weighs €50bn fund for AI and quantum firms", "europe"),
    (26, "BENGHAZI", "Two Libyan soldiers die after Ukraine port attack", "africa"),
    (27, "KHARTOUM", "Sudan rejects Ethiopia's offer to host peace talks", "africa"),
    (28, "HAVANA", "WHO chief urges end to US fuel blockade of Cuba", "americas"),
    (29, "WASHINGTON", "Trump team shelves business offers to Russia: FT", "americas"),
    (30, "WASHINGTON", "Hackers breached a CIA–ODNI unclassified system", "americas"),
    (31, "WASHINGTON", "Tariff rise readied for China, EU and 14 others", "americas"),
    (32, "JUNEAU", "Alaska ends voter-roll deal with Justice Dept", "americas"),
    (33, "CARACAS", "Venezuela puts its debt at $237.5bn, 242% of GDP", "americas"),
]

DATE_CHECK = (
    "Left out as earlier news: Huang's return to Nvidia and the leaked count of Russia's war dead "
    "(Mon 23 Nov), COP31's collapse (Sun 22 Nov), the first strike on Riyadh's PIF tower (Thu 19 Nov). "
    "Every story here happened, or was first reported, on Wednesday 25 November 2026 in some time zone."
)

SOURCES = (
    "Sources: Al Jazeera · Anadolu · AFP · Reuters · AAP · ABC · NBC · CNBC · TIME · "
    "Xinhua · IRIB · UNODC · WHO · Kyiv Independent · AP · Radio Tamazuj · PACNEWS · TfL · FT · Politico"
)

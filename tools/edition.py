"""The stories on the front page for Wednesday 25 November 2026.

Every story here happened, or was first reported, on 25 November 2026
(in some time zone), and each carries the outlets that reported it.
Claims that rest on one side's word are attributed ("IRGC says", "reported"),
and each drawn story carries how sure the reporting is (SURE below).
This edition runs to the close of the US day and Wednesday's Champions League.
"""

DAY = "Wednesday 25 November 2026"
DAY_SHORT = "WED 25 NOV 2026"
DAY_TAG = "WEDNESDAY 25 NOVEMBER"
DAY_TAG_SHORT = "25 NOVEMBER"
SUBLINE = ["Pakistan's first astronaut reaches Tiangong", "AI doubts crash Asia's chip stocks",
           "US proposes tariffs on 14 economies"]

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
    ("03:56", "Docks at Tiangong"),
    ("06:30", "Kospi closes −6.2%"),
    ("10:00", "London Tube strike"),
    ("13:30", "US Q3 growth: 4.3%"),
    ("21:00", "Dow ends at 50,183"),
]

# Big numbers across the top: (figure, caption).
KPIS = [
    ("1st", "foreign astronaut aboard China's Tiangong station"),
    ("−6.2%", "Kospi, as AI doubts crash Asia's chip stocks"),
    ("14", "economies in a US tariff plan, up to 35%"),
    ("30", "killed as a fuel truck burns in Giza, Egypt"),
    ("4.3%", "US Q3 growth, revised up from 3.4%"),
    ("47,000", "women killed by partner or kin in 2025, UN says"),
]

# Three lead stories, each with a drawn scene (art key in art.py).
LEADS = [
    dict(
        art="launch", tag="LIFTOFF", region="asia", place="JIUQUAN, CHINA",
        beat="SPACE", sure="CONFIRMED", chip="1ST FOREIGN VISITOR",
        head="Shenzhou-24 flies a Pakistani to Tiangong",
        dek="Zeeshan Ali is the first foreigner to fly to Tiangong; the crew "
            "docked hours after the Long March 2F lifted off.",
        src="XINHUA · AA · REUTERS",
    ),
    dict(
        art="markets", tag="SELL-OFF", region="asia", place="SEOUL · TAIPEI · TOKYO",
        beat="MARKETS", sure="CONFIRMED", chip="KOSPI −6.2%",
        head="Asia's chip stocks crash on AI doubts",
        dek="Samsung −9.9%, SK Hynix −11.1%; in New York the Nasdaq "
            "fell 4.6% before clawing back to −0.6%.",
        src="AL JAZEERA · AFP · INVESTINGLIVE",
    ),
    dict(
        art="tariffs", tag="TRADE WAR", region="americas", place="WASHINGTON, US",
        beat="TRADE", sure="OFFICIAL", chip="14 ECONOMIES",
        head="US proposes new tariffs on 14 economies",
        dek="USTR's “excess capacity” plan: 20% more on China, up to 35% "
            "on Vietnam; hearings in January.",
        src="USTR · REUTERS · RTÉ · AL JAZEERA",
    ),
]

# Ten secondary stories with small drawn scenes.
CARDS = [
    dict(art="treaty", region="oceania", place="CANBERRA, AUSTRALIA", sure="OFFICIAL", chip="TREATY SIGNED",
         head="Australia and Solomons sign security treaty",
         dek="Honiara must consult Canberra on new security deals; more jobs and visas.",
         src="PM.GOV.AU · ABC · AL JAZEERA"),
    dict(art="femicide", region="global", place="UNITED NATIONS", sure="OFFICIAL",
         head="UN: five women an hour killed by partner or kin",
         dek="47,000 in 2025, says a brief for the day to end violence against women.",
         src="UNODC · UN WOMEN"),
    dict(art="hormuz", region="mideast", place="STRAIT OF HORMUZ", sure="CLAIM", chip="TANKERS ABLAZE",
         head="Iran says tankers hit mines and burn",
         dek="IRGC says two took an “unauthorised route”; later a third caught fire.",
         src="IRIB · AA · AL JAZEERA"),
    dict(art="gizafire", region="africa", place="GIZA, EGYPT", sure="OFFICIAL", chip="30 DEAD",
         head="Fuel truck fire kills at least 30",
         dek="A truck of petroleum flipped in Imbaba; 15 hurt, health ministry says.",
         src="EGYPT HEALTH MINISTRY · AL JAZEERA"),
    dict(art="power", region="europe", place="UKRAINE", sure="OFFICIAL", chip="5 REGIONS DARK",
         head="Russian strikes black out five regions",
         dek="At least five killed; occupied nuclear plant on diesel generators again.",
         src="UKRAINE ENERGY MINISTRY · AL JAZEERA"),
    dict(art="drones", region="mideast", place="RAS TANURA, SAUDI ARABIA", sure="OFFICIAL", chip="4 DRONES DOWN",
         head="Saudis down Houthi drones over oil port",
         dek="Four destroyed after coalition strikes on Hodeidah; Houthis threaten Jeddah.",
         src="AL JAZEERA · AFP"),
    dict(art="mine", region="asia", place="BOGOR, INDONESIA", sure="OFFICIAL", chip="26 TRAPPED",
         head="26 trapped in flooded gold mine",
         dek="Rescuers search a 100-metre pit at Pongkor after a river burst its banks.",
         src="AL JAZEERA · REUTERS"),
    dict(art="garment", region="asia", place="DHAKA, BANGLADESH", sure="OFFICIAL", chip="+36% PAY",
         head="Garment workers win 36% pay rise",
         dek="Minimum wage to rise to 17,500 taka ($136) a month after weeks of protest.",
         src="AL JAZEERA · AFP"),
    dict(art="ucl", region="europe", place="LILLE, FRANCE", sure="CONFIRMED", chip="UPSET",
         head="Lille stun Bayern in Champions League",
         dek="Ueda and an own goal turn it round; Isak scores twice as Liverpool beat Brugge 3-0.",
         src="UEFA · ESPN"),
    dict(art="tube", region="europe", place="LONDON, UK", sure="OFFICIAL", chip="LINES SHUT",
         head="Tube strike shuts two London lines",
         dek="No Circle or Piccadilly service all day from 10:00, TfL says.",
         src="TFL · LONDON MINUTE"),
]

# Map pins: (number, lon, lat, region[, dx, dy]). Numbers match leads (1-3) and cards (4-13).
# dx/dy nudge a pin (in map pixels) where two places sit too close to read.
PINS = [
    (1, 100.3, 40.96, "asia"), (2, 126.98, 37.57, "asia"), (3, -77.04, 38.9, "americas", -4, 3),
    (4, 149.13, -35.28, "oceania"), (5, -73.97, 40.75, "global", 6, -5), (6, 56.3, 26.6, "mideast", 5, 2),
    (7, 31.2, 30.05, "africa"), (8, 35.1, 47.8, "europe"), (9, 50.16, 26.64, "mideast", -3, -5),
    (10, 106.6, -6.6, "asia"), (11, 90.41, 23.81, "asia"), (12, 3.06, 50.63, "europe", 5, 4),
    (13, -0.13, 51.5, "europe", -5, -4),
]

# Briefs: (number, place, text, region). Short and attributed.
BRIEFS = [
    (14, "TOKYO", "Tokyo Electron \u221212.5%, Advantest \u221212.9%", "asia"),
    (15, "TAIPEI", "Taiex ends \u22124.8% after an 8% intraday plunge", "asia"),
    (16, "SHENZHEN", "Huawei rejects its US guilty verdict", "asia"),
    (17, "MALAYSIA", "Airline group orders 10 Boeing 787s", "asia"),
    (18, "GAZA", "Israeli strikes kill 11, including two girls", "mideast"),
    (19, "GAZA", "Strike kills internal security chief and family", "mideast"),
    (20, "JERUSALEM", "Judges urge dropping a Netanyahu case", "mideast"),
    (21, "BAGHDAD", "Top court backs Baghdad on Kurdish oil", "mideast"),
    (22, "KYIV", "US rules out troops in guarantees: report", "europe"),
    (23, "SAMARA", "Ukrainian drones hit refineries; one dead", "europe"),
    (24, "FRANKFURT", "DAX ends \u22121.3%; Madrid's IBEX \u22122.0%", "europe"),
    (25, "LISBON", "Sporting 2-2 Man Utd; Fernandes double", "europe"),
    (26, "UCL", "Inter 2-0 Stuttgart, Bar\xe7a 4-1 Sabah", "europe"),
    (27, "CAPE TOWN", "Court lifts Ramaphosa \u2018farmgate\u2019 threat", "africa"),
    (28, "KHARTOUM", "Sudan rejects Ethiopia's peace offer", "africa"),
    (29, "MAIDUGURI", "Tinubu pledges peace for the northeast", "africa"),
    (30, "WASHINGTON", "Q3 growth revised up to 4.3%", "americas"),
    (31, "WASHINGTON", "Jobless claims fall to 189,000", "americas"),
    (32, "NEW YORK", "Dow erases 1,105-pt drop, ends at 50,183", "americas"),
    (33, "US", "SpaceX cleared for 1m space data centres", "americas"),
    (34, "HAVANA", "WHO chief urges end to US fuel blockade", "americas"),
    (35, "BRAS\xcdLIA", "Lula signs a budget-balancing fiscal law", "americas"),
    (36, "CANBERRA", "Apology to LGBTQ military veterans", "oceania"),
    (37, "SUVA", "Fiji drought: 92 communities without water", "oceania"),
]

DATE_CHECK = (
    "Left out as earlier news: Huang's return to Nvidia (Mon 23), Huawei's conviction, the WHO's Ebola staff move "
    "and the CIA–ODNI breach report (Tue 24). Not yet: US Thanksgiving (Thu 26), tariff hearings (January). "
    "Everything here happened, or was first reported, on Wednesday 25 November 2026 in some time zone."
)

SOURCES = (
    "Sources: Al Jazeera · Anadolu · AFP · Reuters · AAP · ABC · CNBC · USTR · RTÉ · "
    "Xinhua · IRIB · UNODC · Kyiv Independent · investingLive · ESPN · UEFA · Rio Times · "
    "Radio Tamazuj · TfL · FT"
)

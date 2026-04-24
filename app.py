from __future__ import annotations

from dataclasses import dataclass, field
from html import escape
from pathlib import Path

import streamlit as st


APP_TITLE = "WarEra Ireland"
APP_SUBTITLE = (
    "Get started quickly, make smart decisions, and grow effectively in both "
    "economy and war."
)
ASSETS_DIR = Path(__file__).parent / "assets" / "screenshots"


@dataclass(frozen=True)
class Screenshot:
    file_name: str
    caption: str


@dataclass(frozen=True)
class ChecklistItem:
    number: int
    text: str
    screenshots: list[Screenshot] = field(default_factory=list)
    note: str | None = None


@dataclass(frozen=True)
class InfoBlock:
    title: str
    paragraphs: list[str]
    tip: str | None = None
    bars: list[tuple[str, str, str]] | None = None
    tags: list[str] | None = None
    steps: list[str] | None = None
    warning: str | None = None


@dataclass(frozen=True)
class FaqItem:
    question: str
    answer: str


CHECKLIST_ITEMS: list[ChecklistItem] = [
    ChecklistItem(
        number=1,
        text=(
            "Complete your Daily missions and Weekly missions every day; aim for at "
            "least 7 out of 10 for the bonus."
        ),
        screenshots=[
            Screenshot(
                "quick_start_daily_weekly_missions.png",
                "Mission overview — Daily and Weekly missions",
            )
        ],
    ),
    ChecklistItem(
        number=2,
        text="Invest your skill points in economic skills until you reach a much higher level.",
        screenshots=[
            Screenshot("skills_profile_menu.png", "Skills menu from your profile"),
            Screenshot("skills_economic_overview.png", "Economic Skills overview"),
        ],
        note=(
            "Recommended ECO skill point split: use the first placeholder for 0–56 points "
            "and the second for 60–120 points."
        ),
    ),
    ChecklistItem(
        number=3,
        text="Empty your four bars at least once every 10 hours. Only use Hunger for missions.",
        screenshots=[
            Screenshot("four_bars_overview.png", "The four bars in the top-left corner")
        ],
    ),
    ChecklistItem(
        number=4,
        text=(
            "Work for other players with <span style=\"color:#4a9eff;font-weight:600;\">energy</span>, "
            "and work in your own companies with <span style=\"color:#d94fa0;font-weight:600;\">entrepreneurship</span>. "
            "One click costs 10 <span style=\"color:#4a9eff;font-weight:600;\">energy</span> or 10 "
            "<span style=\"color:#d94fa0;font-weight:600;\">entrepreneurship</span>."
        ),
        screenshots=[
            Screenshot(
                "working_energy_entrepreneurship.png",
                "Working with energy and entrepreneurship",
            )
        ],
    ),
    ChecklistItem(
        number=5,
        text=(
            "Sell lootboxes instead of opening them. For new players, the cash is usually "
            "worth more than the contents, except when a mission requires opening one."
        ),
        screenshots=[
            Screenshot(
                "market_sell_lootboxes_equipment.png",
                "Market page for selling lootboxes and equipment",
            )
        ],
    ),
    ChecklistItem(
        number=6,
        text=(
            "Sell all resources and products except Concrete and Steel. You need Concrete "
            "for a new company and Steel for upgrades such as Automated Engine."
        ),
        screenshots=[
            Screenshot(
                "sell_resources_except_concrete_steel.png",
                "Sell everything except Concrete and Steel",
            )
        ],
    ),
    ChecklistItem(
        number=7,
        text="Invest in Automated Engine and production upgrades for the best long-term growth.",
        screenshots=[
            Screenshot("companies_upgrade_overview.png", "Company upgrade overview"),
            Screenshot(
                "automated_engine_storage_upgrades.png",
                "Automated Engine and Storage upgrades",
            ),
        ],
    ),
    ChecklistItem(
        number=8,
        text=(
            "Do not buy expensive weapons or equipment until you have enough skill points "
            "in fighting skills. Until then, selling is usually more profitable."
        ),
        screenshots=[
            Screenshot(
                "equipment_market_do_not_buy_yet.png",
                "Equipment market — avoid early purchases",
            )
        ],
    ),
]


ECO_EXTRA_SCREENSHOTS = [
    Screenshot("eco_skill_distribution_0_to_56.png", "Economic skill split for 0–56 points"),
    Screenshot("eco_skill_distribution_60_to_120.png", "Economic skill split for 60–120 points"),
]


BASICS_BLOCKS: list[InfoBlock] = [
    InfoBlock(
        title="Levels, XP, and Skill Points",
        paragraphs=[
            "You earn XP through Starting, Daily, and Weekly missions. Starting missions are permanent, Daily missions reset every day, and Weekly missions reset every week.",
            "You receive skill points when you level up. Priority: invest in economic skills first. Higher levels cost more points, so distribute them carefully.",
            "You get one free reroll per mission set. Reroll Weekly missions if they are unrealistic. Critical-hit and dodge missions are usually not practical early on.",
        ],
    ),
    InfoBlock(
        title="The Four Bars",
        paragraphs=[
            "Each bar refills by one tenth of its maximum per hour. After 10 hours they are full again, so use them at least once every 10 hours.",
        ],
        bars=[
            ("green", "Health", "used for attacking"),
            ("red", "Hunger", "1 Bread = 10% Health, 1 Steak = 15%, 1 Fish = 20%"),
            ("blue", "Energy", "used for working for other players"),
            ("pink", "Entrepreneurship", "used for working in your own company"),
        ],
    ),
    InfoBlock(
        title="Production Points",
        paragraphs=[
            "Production points determine your work output. By default, 10 energy gives 10 production points.",
            "The Production economic skill increases the amount of production you get per click. Since wages are paid per production point, more production per click means more income.",
        ],
    ),
]


ECONOMY_BLOCKS: list[InfoBlock] = [
    InfoBlock(
        title="Making Money",
        paragraphs=[
            "Working for other players uses energy and pays wages per production point, minus taxes.",
            "Your own companies passively produce raw materials, and working inside your own company uses entrepreneurship.",
            "Reinvest the money you earn into company upgrades, especially Automated Engine, or into founding new companies.",
        ],
        tip="You can calculate your income, including employees, or plan the best company upgrade path at warerastats.io/tools.",
    ),
    InfoBlock(
        title="Company Types and Resources",
        paragraphs=[
            "Basic raw resources such as iron are processed into advanced resources such as steel.",
            "Market prices are entirely player-driven through supply and demand.",
        ],
        tip="Check warerastats.io to find profitable resources.",
    ),
    InfoBlock(
        title="Practical Rules",
        paragraphs=[
            "Sell cases instead of opening them. Selling them almost always gives more value for new players.",
            "Also avoid using the equipment from those cases too early.",
            "Check production bonuses and upgrades that increase output to maximize long-term profit.",
        ],
    ),
]


FIGHT_BLOCKS: list[InfoBlock] = [
    InfoBlock(
        title="Fight Skills",
        paragraphs=[
            "Do not spend skill points on fight skills early on.",
            "Hunger works as a reserve: each Hunger lets you eat once to restore Health.",
            "Every attack has a 5% chance to give a lootbox unless you invest points in Loot Chance.",
        ],
        tags=[
            "Attack",
            "Precision",
            "Crit Chance",
            "Crit Damage",
            "Armor",
            "Dodge",
            "Health",
            "Loot Chance",
            "Hunger",
        ],
    ),
    InfoBlock(
        title="Weapons, Equipment, and Ammo",
        paragraphs=[
            "Weapons and equipment add bonuses on top of your skills. Stats can vary a lot even within the same rarity, so always check the exact values.",
            "Most weapons require ammo, except the Knife. Ammo gives an extra 10%, 20%, or 40% bonus depending on the type.",
        ],
        tip="No war skills yet? Do not use equipment. Sell cases and use the proceeds to strengthen your economy instead.",
    ),
    InfoBlock(
        title="Battles and Orders",
        paragraphs=[
            "Battle categories include Orders, Allies, Enemies, and With contracts.",
            "Follow the orders of your country or Military Unit for extra bonuses and the highest impact.",
            "Countries can place coins into a bounty pool. You earn per 1,000 damage as long as the budget lasts, but you cannot earn from your own country's bounty.",
        ],
    ),
    InfoBlock(
        title="Military Units (MU)",
        paragraphs=[
            "Benefits: up to a 20% damage bonus depending on HQ level, plus up to 15% more from orders, for roughly 35% extra damage in total.",
            "Costs depend on HQ level and member count, and members are expected to contribute.",
            "Every 12 hours you can receive 10 extra Health from MU member assistance, and it costs the helpers nothing.",
        ],
    ),
    InfoBlock(
        title="Damage Calculation",
        paragraphs=[
            "Note: the calculation below does not account for Precision, so attacks can still miss.",
        ],
        steps=[
            "Start with your total Attack from skills and weapon.",
            "Apply bonuses in this fixed order: Military Rank → Ammo (10%, 20%, or 40%) → Pill (+60% for 8 hours, then a −60% debuff for 16 hours). Example: 300 × 1.2 × 1.2 × 1.6 = 691 Attack.",
            "Apply battle bonuses such as Orders, Alliance, and MU. Example: 691 × 1.6 = 1105 Damage.",
            "If you land a critical hit, multiply by (100 + Crit Damage)%. Example: 1105 × 3 = 3315 Damage with 200% crit damage.",
        ],
        tip="The order of bonuses matters. A Pill gives a strong short-term boost, but it also causes a long 16-hour debuff afterward.",
    ),
]


STRATEGY_BLOCKS: list[InfoBlock] = [
    InfoBlock(
        title="Money Management and Investments",
        paragraphs=[
            "Reinvesting into Automated Engine and production upgrades gives the best long-term growth.",
            "Do not buy expensive weapons or equipment until you have enough fighting skill points. Until then, selling is often more profitable.",
        ],
    ),
    InfoBlock(
        title="War Participation",
        paragraphs=[
            "Always follow country or MU orders. This gives bonuses and helps your side.",
            "Use Pills only for focused all-out sessions, and plan around the following 16-hour debuff.",
            "Join a Military Unit as soon as possible for consistent damage bonuses and support mechanics.",
        ],
    ),
    InfoBlock(
        title="Equipment During Wartime",
        paragraphs=[
            "During war, you should have at least two full equipment sets ready.",
            "If you use a Pill, you will probably burn through those sets. For longer wars, prepare more in advance.",
        ],
        tip="A high dodge percentage reduces durability loss on equipment, so boots with very high dodge are especially valuable.",
    ),
]


FYI_ITEMS = [
    "There are elections twice per month: once for President and once for Congress. Players from level 10 onward can run and vote.",
    "Ireland has an active community Discord where questions are answered and useful links and tools are shared: https://discord.com/invite/yeknsvtVn4",
    "In practice, some countries such as Japan and Norway are run by players from another country. They may be mercenaries fighting for money or proxy countries managed by another nation.",
    "Your wage in a job is paid per production point, not per work session. Many players wrongly assume it is a fixed amount per click.",
    "You can only fire employees if they are not already assigned to a percentage of your production. Otherwise you must wait until that share has been used up.",
    "A country's production bonus depends entirely on the strategic resources and regional deposits it controls.",
    "Some daily missions do not count if you sell equipment. Only raw materials and consumables count for those item-sale missions.",
    "In Attack or Defend battles, you always help the side whose flag appears next to the button, even if it feels politically illogical.",
    "Limestone plus Concrete is one of the most stable combinations for your first two companies.",
    "Daily missions reset at 01:00, and Weekly missions reset on Sunday night into Monday at 01:00.(Daylight Savings Time, otherwise it is midniight.)",
    "You can earn 10 coins by entering a referral from an Irish player.",
    "The green percentage shown at companies is the wage tax. As an employer, it does not directly cost you more or less to pay workers in a high-tax country, but workers may avoid those jobs. You do not pay wage tax on the work you do yourself in your own company.",
    "You can offer employees a lower wage. If they refuse, they leave your company. Players also use this to leave a job during cooldown by asking the employer to lower the wage and then declining it.",
]


FAQ_ITEMS = [
    FaqItem(
        "No Irish MU vacancies?",
        "Temporarily join a random MU without an entrance fee. In-game vacancies will appear once they become available.",
    ),
    FaqItem(
        "Which button should I click in a battle?",
        "Follow the flag and the order. Click the button that matches the requested action, such as Attack.",
    ),
    FaqItem("Should I open or sell cases?", "Usually sell them. Keep a few in reserve for missions."),
    FaqItem(
        "When should I use equipment?",
        "Only when you already invested heavily into war-related skills. Otherwise, sell it for coins.",
    ),
    FaqItem(
        "How does referral work and what do I get?",
        "You can enter a username as your referral through your profile. You immediately get 10 coins, and the referrer gets a small bonus once you reach level 15.",
    ),
    FaqItem(
        "What is the difference between Produce and Work?",
        "Produce converts raw materials into finished products and requires resources and production. Work generates production points or labor for an employer and pays per production point.",
    ),
    FaqItem(
        "How do I move a company or change its type?",
        "You can change the location or production type under Companies. Each change costs 5 Concrete, so changing both at once costs 10 Concrete.",
    ),
    FaqItem(
        "What is the difference between country specialization and resource deposits?",
        "Country specialization is a permanent bonus chosen by a country and is based on strategic resources the country owns. Resource deposits are temporary regional bonuses, often +30%, that can run out after a number of days.",
    ),
    FaqItem(
        "How does wage per production point work?",
        "Wages are often paid per production point. For example, a wage of 0.089 means 0.089 per production point you provide.",
    ),
    FaqItem(
        "Is hiring employees profitable?",
        "That depends on the product and market price. You need to compare wage costs against the extra production they create. Helpful tool: https://warerastats.io/tools",
    ),
    FaqItem(
        "Can I fire someone who works in my company?",
        "Yes. Click the X next to the employee. You can also lower the salary; if the employee does not accept it, they must leave the company.",
    ),
    FaqItem(
        "How do orders work in attack and defend battles?",
        "You help the side whose flag is shown next to the relevant action.",
    ),
]


SECTION_OPTIONS = [
    ("checklist", "⚡ Quick Start"),
    ("basics", "📖 Basics"),
    ("economy", "💰 Economy"),
    ("fighting", "⚔️ Fighting & War"),
    ("strategies", "🎯 Strategies"),
    ("fyi", "💡 Did You Know?"),
    ("faq", "❓ FAQ"),
]

SECTION_LABELS = dict(SECTION_OPTIONS)
VALID_SECTION_KEYS = set(SECTION_LABELS)


def get_current_section() -> str:
    raw_value = st.query_params.get("section", "checklist")
    if isinstance(raw_value, list):
        raw_value = raw_value[0] if raw_value else "checklist"

    section = str(raw_value)
    return section if section in VALID_SECTION_KEYS else "checklist"


def set_current_section(section: str) -> None:
    if section in VALID_SECTION_KEYS:
        st.session_state.active_section = section
        st.query_params["section"] = section


def nav_label(section_key: str) -> str:
    return SECTION_LABELS[section_key]


def render_nav_button(section_key: str, *, key_prefix: str) -> None:
    is_active = current_section == section_key
    if st.button(
        nav_label(section_key),
        key=f"{key_prefix}_{section_key}",
        use_container_width=True,
        type="primary" if is_active else "secondary",
    ):
        set_current_section(section_key)
        st.rerun()


def render_top_navigation() -> None:
    rows = [SECTION_OPTIONS[:4], SECTION_OPTIONS[4:]]
    for row in rows:
        columns = st.columns(len(row))
        for column, (section_key, _label) in zip(columns, row):
            with column:
                render_nav_button(section_key, key_prefix="topnav")


st.set_page_config(
    page_title=f"{APP_TITLE} — Manual",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;600;700&family=Exo+2:wght@300;400;500;600;700&display=swap');

        :root {
            --bg-primary: #0d1117;
            --bg-secondary: #161b22;
            --bg-card: #1c2333;
            --border: #2a3548;
            --text-primary: #e6edf3;
            --text-secondary: #8b949e;
            --text-muted: #6e7681;
            --accent-teal: #10b981;
            --accent-gold: #d4a843;
            --accent-blue: #4a9eff;
        }

        html, body, [class*="css"] {
            font-family: 'Exo 2', sans-serif;
        }

        .stApp {
            background: var(--bg-primary);
            color: var(--text-primary);
        }

        .stApp::before {
            content: '';
            position: fixed;
            inset: 0;
            background:
                linear-gradient(rgba(16,185,129,0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(16,185,129,0.03) 1px, transparent 1px);
            background-size: 40px 40px;
            pointer-events: none;
            z-index: 0;
        }

        .block-container {
            max-width: 1100px;
            padding-top: 1.4rem;
            padding-bottom: 4rem;
            position: relative;
            z-index: 1;
        }

        h1, h2, h3 {
            font-family: 'Rajdhani', sans-serif !important;
            letter-spacing: 0.03em;
        }

        [data-testid="stSidebar"] {
            background: #10161e;
            border-right: 1px solid var(--border);
        }

        [data-testid="stSidebar"] * {
            color: var(--text-primary);
        }

        .sidebar-brand {
            margin-bottom: 1rem;
        }

        .sidebar-kicker {
            color: var(--accent-teal);
            text-transform: uppercase;
            letter-spacing: 0.18rem;
            font-size: 0.75rem;
            font-weight: 700;
            margin-bottom: 0.25rem;
        }

        .sidebar-title {
            font-family: 'Rajdhani', sans-serif;
            font-size: 1.7rem;
            font-weight: 700;
            margin: 0;
            color: var(--text-primary);
        }

        .sidebar-nav-shell {
            display: flex;
            flex-direction: column;
            gap: 0.45rem;
            margin-top: 1rem;
        }

        .hero {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            padding: 2.5rem 1rem 2rem;
            margin-bottom: 1.5rem;
            position: relative;
        }

        .hero::after {
            content: '';
            position: absolute;
            left: 10%;
            right: 10%;
            bottom: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, var(--accent-teal), transparent);
        }

        .hero-flag {
            color: var(--accent-teal);
            font-size: 0.88rem;
            letter-spacing: 0.25rem;
            text-transform: uppercase;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }

        .hero-title {
            font-size: clamp(2.2rem, 6vw, 3.5rem);
            margin: 0;
        }

        .hero-title span {
            color: var(--accent-teal);
        }

        .hero-subtitle {
            color: var(--text-secondary);
            font-size: 1rem;
            display: block;
            max-width: 700px;
            width: 100%;
            margin: 0.8rem auto 0;
            text-align: center;
        }

        .section-title {
            color: var(--accent-teal);
            font-size: 1.85rem;
            margin-top: 0.35rem;
            margin-bottom: 1rem;
            padding-bottom: 0.45rem;
            border-bottom: 2px solid var(--border);
        }

        .section-intro {
            color: var(--text-secondary);
            margin-bottom: 1rem;
        }

        .nav-shell {
            margin: 0 0 2rem;
            padding: 0.75rem;
            background: var(--bg-secondary);
            border: 1px solid var(--border);
            border-radius: 8px;
        }

        .top-nav-title {
            color: var(--text-muted);
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.12rem;
            margin: 0 0 0.65rem;
        }

        .card {
            background: #1c2333;
            border: 1px solid var(--border);
            border-radius: 10px;
            padding: 1rem 1.1rem;
            margin-bottom: 1rem;
            transition: background 0.2s ease, border-color 0.2s ease;
        }

        .card:hover {
            background: #222d3f;
            border-color: #1f9d74;
        }

        .check-card {
            border-left: 4px solid var(--accent-gold);
        }

        .check-top {
            display: flex;
            gap: 0.8rem;
            align-items: flex-start;
        }

        .check-num {
            width: 2rem;
            height: 2rem;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 8px;
            background: rgba(212,168,67,0.15);
            color: var(--accent-gold);
            font-weight: 700;
            font-family: 'Rajdhani', sans-serif;
            font-size: 1.15rem;
            flex-shrink: 0;
        }

        .tip-box {
            background: rgba(212,168,67,0.12);
            border: 1px solid rgba(212,168,67,0.32);
            color: #f1cd76;
            border-radius: 8px;
            padding: 0.9rem 1rem;
            margin: 0.8rem 0 1rem;
        }

        .bar-chip {
            background: var(--bg-secondary);
            border-radius: 8px;
            padding: 0.75rem 0.9rem;
            border: 1px solid var(--border);
            margin-bottom: 0.65rem;
        }

        .info-card-title {
            color: var(--accent-gold);
            font-size: 1.35rem;
            margin: 0 0 0.7rem;
        }

        .info-card p {
            color: var(--text-secondary);
            font-size: 0.96rem;
            margin: 0 0 0.65rem;
        }

        .info-card p:last-child {
            margin-bottom: 0;
        }

        .bars-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 0.6rem;
            margin: 0.85rem 0 1rem;
        }

        .bar-item {
            display: flex;
            align-items: center;
            gap: 0.55rem;
            padding: 0.75rem 0.9rem;
            background: var(--bg-secondary);
            border: 1px solid var(--border);
            border-radius: 8px;
            color: var(--text-secondary);
            font-size: 0.88rem;
        }

        .bar-dot {
            width: 10px;
            height: 10px;
            border-radius: 999px;
            flex-shrink: 0;
        }

        .bar-dot.green { background: #3fb950; }
        .bar-dot.red { background: #e05252; }
        .bar-dot.blue { background: #4a9eff; }
        .bar-dot.pink { background: #d94fa0; }

        .skill-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.4rem;
            margin: 0.75rem 0 0.9rem;
        }

        .skill-pill {
            display: inline-block;
            padding: 0.32rem 0.6rem;
            margin: 0 0.35rem 0.45rem 0;
            background: var(--bg-secondary);
            border: 1px solid var(--border);
            border-radius: 999px;
            color: var(--text-secondary);
            font-size: 0.85rem;
        }

        .placeholder {
            border: 2px dashed #607087;
            background: rgba(248,250,252,0.03);
            border-radius: 12px;
            padding: 1.2rem;
            text-align: center;
            color: var(--text-secondary);
            min-height: 220px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
        }

        .small-caption {
            color: var(--text-muted);
            font-size: 0.9rem;
        }

        .step-box {
            background: var(--bg-secondary);
            border-left: 3px solid var(--accent-blue);
            border-radius: 0 8px 8px 0;
            padding: 0.9rem 1rem;
            margin-bottom: 0.55rem;
            color: var(--text-secondary);
        }

        .fyi-box {
            background: #1c2333;
            border: 1px solid var(--border);
            border-left: 4px solid var(--accent-teal);
            border-radius: 8px;
            padding: 0.95rem 1rem;
            margin-bottom: 0.75rem;
            color: var(--text-secondary);
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 0.35rem;
            flex-wrap: wrap;
        }

        .stTabs [data-baseweb="tab"] {
            background: var(--bg-secondary);
            border: 1px solid var(--border);
            border-radius: 8px;
            color: var(--text-secondary);
            padding: 0.5rem 0.8rem;
        }

        .stTabs [aria-selected="true"] {
            background: rgba(16,185,129,0.14) !important;
            color: var(--accent-teal) !important;
            border-color: rgba(16,185,129,0.35) !important;
        }

        .stTextInput input {
            background: #1c2333;
            color: var(--text-primary);
            border: 1px solid var(--border);
        }

        [data-testid="stPopoverButton"] {
            background: var(--accent-teal) !important;
            color: #0d1117 !important;
            border: none !important;
            border-radius: 4px !important;
            font-weight: 700 !important;
            min-height: 1.9rem !important;
            padding: 0.1rem 0.5rem !important;
            box-shadow: none !important;
        }

        [data-testid="stPopoverButton"]:hover {
            background: var(--accent-gold) !important;
        }

        .stButton > button {
            width: 100%;
            border-radius: 12px !important;
            border: 1px solid var(--border) !important;
            background: linear-gradient(180deg, rgba(255,255,255,0.01), rgba(255,255,255,0)) !important;
            color: var(--text-secondary) !important;
            font-weight: 700 !important;
            min-height: 2.8rem !important;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.02) !important;
            transition: all 0.2s ease !important;
        }

        .stButton > button:hover {
            color: var(--text-primary) !important;
            border-color: rgba(16,185,129,0.35) !important;
            background: rgba(16,185,129,0.08) !important;
        }

        .stButton > button[kind="primary"] {
            color: var(--text-primary) !important;
            border-color: rgba(16,185,129,0.45) !important;
            background: linear-gradient(90deg, rgba(16,185,129,0.18), rgba(16,185,129,0.05)) !important;
            box-shadow: 0 0 0 1px rgba(16,185,129,0.12) !important;
        }

        [data-testid="stSidebar"] .stButton > button {
            text-align: left !important;
            justify-content: flex-start !important;
            padding-left: 0.95rem !important;
        }

        .screenshot-note {
            color: var(--text-muted);
            font-size: 0.85rem;
            margin: -0.2rem 0 0.9rem;
        }

        @media (max-width: 640px) {
            .nav-shell {
                justify-content: flex-start;
            }

            .bars-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)


if "active_section" not in st.session_state:
    st.session_state.active_section = get_current_section()

query_section = get_current_section()
if st.session_state.active_section != query_section:
    st.session_state.active_section = query_section

current_section = st.session_state.active_section


def render_placeholder(shot: Screenshot, *, image_width: int = 320) -> None:
    image_path = ASSETS_DIR / shot.file_name
    if image_path.exists():
        st.image(str(image_path), caption=shot.caption, width=image_width)
        return

    st.markdown(
        f"""
        <div class="placeholder">
            <strong>Missing screenshot placeholder</strong>
            <div style="margin-top:0.4rem;">{shot.file_name}</div>
            <div class="small-caption" style="margin-top:0.55rem;">{shot.caption}</div>
            <div class="small-caption" style="margin-top:0.55rem;">Place this file in assets/screenshots/</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_screenshot_gallery(screenshots: list[Screenshot]) -> None:
    if not screenshots:
        return

    columns = st.columns(len(screenshots))
    for column, shot in zip(columns, screenshots):
        with column:
            render_placeholder(shot)


def render_screenshot_badges(screenshots: list[Screenshot]) -> None:
    if not screenshots:
        return

    columns = st.columns(len(screenshots))
    for index, (column, shot) in enumerate(zip(columns, screenshots), start=1):
        badge_label = "📷" if len(screenshots) == 1 else f"📷{index}"
        with column:
            with st.popover(badge_label, use_container_width=True):
                st.caption(shot.caption)
                render_placeholder(shot)


def render_info_block(block: InfoBlock) -> None:
    parts = [f'<div class="card info-card"><h3 class="info-card-title">{escape(block.title)}</h3>']

    if block.tags:
        tags_html = "".join(
            f'<span class="skill-pill">{escape(tag)}</span>' for tag in block.tags
        )
        parts.append(f'<div class="skill-tags">{tags_html}</div>')

    if block.bars:
        bars_html = "".join(
            (
                f'<div class="bar-item">'
                f'<span class="bar-dot {escape(color)}"></span>'
                f'<span><strong>{escape(label)}</strong> — {escape(description)}</span>'
                f'</div>'
            )
            for color, label, description in block.bars
        )
        parts.append(f'<div class="bars-grid">{bars_html}</div>')

    parts.extend(f'<p>{escape(paragraph)}</p>' for paragraph in block.paragraphs)

    if block.steps:
        steps_html = "".join(
            (
                '<div class="step-box">'
                f'<strong style="color:#4a9eff; font-family: Rajdhani, sans-serif;">Step {index}</strong><br>'
                f'{escape(step)}'
                '</div>'
            )
            for index, step in enumerate(block.steps, start=1)
        )
        parts.append(steps_html)

    if block.tip:
        parts.append(f'<div class="tip-box">{escape(block.tip)}</div>')

    if block.warning:
        parts.append(f'<div class="tip-box">{escape(block.warning)}</div>')

    parts.append('</div>')
    st.markdown("".join(parts), unsafe_allow_html=True)


def render_quick_start() -> None:
    st.markdown('<h2 class="section-title">Quick Start Checklist</h2>', unsafe_allow_html=True)
    st.markdown(
        '<p class="section-intro">Click the 📷 badges to view screenshots</p>',
        unsafe_allow_html=True,
    )
    st.write(
        "Note: the rules below are good starting guidelines that help you grow quickly at the beginning. "
        "As you play longer, you will discover exceptions."
    )
    st.markdown(
        '<div class="tip-box">Through your profile, you can enter an Irish user\'s username as your referral. You immediately receive 10 coins, and the referrer gets a small bonus once you reach level 15.</div>',
        unsafe_allow_html=True,
    )

    for item in CHECKLIST_ITEMS:
        st.markdown(
            f"""
            <div class="card check-card">
                <div class="check-top">
                    <div class="check-num">{item.number}</div>
                    <div>{item.text}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        render_screenshot_badges(item.screenshots)
        if item.number == 2:
            st.markdown(f'<div class="screenshot-note">{item.note}</div>', unsafe_allow_html=True)
            render_screenshot_badges(ECO_EXTRA_SCREENSHOTS)
        st.markdown("<div style='height:0.45rem;'></div>", unsafe_allow_html=True)


def render_basics() -> None:
    st.markdown('<h2 class="section-title">Core Systems &amp; Basics</h2>', unsafe_allow_html=True)
    for block in BASICS_BLOCKS:
        render_info_block(block)


def render_economy() -> None:
    st.markdown('<h2 class="section-title">Economy &amp; Companies</h2>', unsafe_allow_html=True)
    for block in ECONOMY_BLOCKS:
        render_info_block(block)
    st.markdown(
        '<div class="tip-box">External tools: <a href="https://warerastats.io/tools" target="_blank">warerastats.io/tools</a></div>',
        unsafe_allow_html=True,
    )


def render_fighting() -> None:
    st.markdown('<h2 class="section-title">Fighting &amp; War</h2>', unsafe_allow_html=True)
    for block in FIGHT_BLOCKS:
        render_info_block(block)


def render_strategies() -> None:
    st.markdown('<h2 class="section-title">Strategies &amp; Tips</h2>', unsafe_allow_html=True)
    for block in STRATEGY_BLOCKS:
        render_info_block(block)


def render_fyi() -> None:
    st.markdown('<h2 class="section-title">Did You Know?</h2>', unsafe_allow_html=True)
    for item in FYI_ITEMS:
        st.markdown(f'<div class="fyi-box">{item}</div>', unsafe_allow_html=True)


def render_faq() -> None:
    st.markdown('<h2 class="section-title">FAQ</h2>', unsafe_allow_html=True)
    query = st.text_input("Search the FAQ", placeholder="Type a keyword...").strip().lower()
    visible_items = [
        item
        for item in FAQ_ITEMS
        if not query or query in item.question.lower() or query in item.answer.lower()
    ]

    if not visible_items:
        st.info("No results found.")

    for item in visible_items:
        with st.expander(item.question):
            st.write(item.answer)


with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-brand">
            <div class="sidebar-kicker">WarEra Guide</div>
            <div class="sidebar-title">Navigation</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    for section_key, _label in SECTION_OPTIONS:
        render_nav_button(section_key, key_prefix="sidebar")

st.markdown(
    f"""
    <div class="hero">
        <div class="hero-flag">🇮🇪 {APP_TITLE} 🇮🇪</div>
        <h1 class="hero-title">Beginner Manual <span>&amp;</span> Strategy</h1>
        <p class="hero-subtitle">{APP_SUBTITLE}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="top-nav-title">Sections</div>', unsafe_allow_html=True)
render_top_navigation()

if current_section == "checklist":
    render_quick_start()
elif current_section == "basics":
    render_basics()
elif current_section == "economy":
    render_economy()
elif current_section == "fighting":
    render_fighting()
elif current_section == "strategies":
    render_strategies()
elif current_section == "fyi":
    render_fyi()
else:
    render_faq()

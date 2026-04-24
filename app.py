from __future__ import annotations

import base64
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
RESOURCE_ICONS_DIR = Path(__file__).parent / "assets" / "resource_icons"
EQUIPMENT_ICONS_DIR = Path(__file__).parent / "assets" / "equipment"


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
class ResourceInfo:
    name: str
    category: str
    description: str
    production_cost: str
    icon_file: str | None = None


@dataclass(frozen=True)
class EquipmentTypeInfo:
    name: str
    effect: str
    icon_file: str


@dataclass(frozen=True)
class EquipmentTierInfo:
    tier: str
    theme: str
    helmet: str
    chest: str
    gloves: str
    pants: str
    boots: str
    weapon_name: str
    weapon_damage: str
    weapon_crit: str
    weapon_icon_file: str


@dataclass(frozen=True)
class AmmoInfo:
    name: str
    bonus: str
    description: str
    icon_file: str


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
        title="Companies",
        paragraphs=[
            "Every player can own companies.",
            "A company can produce different resources that you can either use yourself or sell on the market.",
        ],
    ),
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
            "Manufactured goods also consume an equal amount of base material to their Production Point cost, so efficient input planning matters.",
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


ECONOMY_RESOURCES: list[ResourceInfo] = [
    ResourceInfo(
        name="Iron",
        category="Base Material",
        description="Used to produce Steel.",
        production_cost="1 Production Point (PP)",
        icon_file="iron.png",
    ),
    ResourceInfo(
        name="Steel",
        category="Manufactured Material",
        description="Used to craft equipment and to upgrade companies, Military Units, and provincial buildings.",
        production_cost="10 Production Points (PP) + 10 Iron",
        icon_file="steel.png",
    ),
    ResourceInfo(
        name="Limestone",
        category="Base Material",
        description="Used to produce Concrete.",
        production_cost="1 Production Point (PP)",
        icon_file="limestone.png",
    ),
    ResourceInfo(
        name="Concrete",
        category="Manufactured Material",
        description="Used for building new companies and Military Units.",
        production_cost="10 Production Points (PP) + 10 Limestone",
        icon_file="concrete.png",
    ),
    ResourceInfo(
        name="Lead",
        category="Base Material",
        description="Used in the production of Ammunition.",
        production_cost="1 Production Point (PP)",
        icon_file="lead.png",
    ),
    ResourceInfo(
        name="Grain",
        category="Base Material",
        description="Used in the production of Bread.",
        production_cost="1 Production Point (PP)",
        icon_file="grain.png",
    ),
    ResourceInfo(
        name="Bread",
        category="Food Item",
        description="Regenerates 10% of your maximum health.",
        production_cost="10 Production Points (PP) + 10 Grain",
        icon_file="bread.png",
    ),
    ResourceInfo(
        name="Livestock",
        category="Base Material",
        description="Used in the production of Steak.",
        production_cost="20 Production Points (PP)",
        icon_file="livestock.png",
    ),
    ResourceInfo(
        name="Steak",
        category="Food Item",
        description="Regenerates 15% of your maximum health.",
        production_cost="20 Production Points (PP) + 20 Livestock",
        icon_file="steak.png",
    ),
    ResourceInfo(
        name="Fish",
        category="Base Material",
        description="Used in the production of Cooked Fish.",
        production_cost="40 Production Points (PP)",
        icon_file="fish.png",
    ),
    ResourceInfo(
        name="Cooked Fish",
        category="Food Item",
        description="Regenerates 20% of your maximum health.",
        production_cost="40 Production Points (PP) + 40 Fish",
        icon_file="cookedFish.png",
    ),
    ResourceInfo(
        name="Mysterious Plant",
        category="Base Material",
        description="Used in the production of Pills.",
        production_cost="1 Production Point (PP)",
        icon_file="coca.png",
    ),
    ResourceInfo(
        name="Pill",
        category="Manufactured Material",
        description="Gives a 60% damage bonus for 8 hours, followed by a -60% damage cooldown for 16 hours.",
        production_cost="200 Production Points (PP) + 200 Mysterious Plant",
        icon_file="pill.png",
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


EQUIPMENT_TYPES: list[EquipmentTypeInfo] = [
    EquipmentTypeInfo("Helmet", "Critical hit chance", "helmet.png"),
    EquipmentTypeInfo("Chest Armour", "Protects health when attacking by providing armour", "chest.png"),
    EquipmentTypeInfo("Trousers", "Protects health when attacking by providing armour", "pants.png"),
    EquipmentTypeInfo("Gloves", "Hit chance", "gloves.png"),
    EquipmentTypeInfo("Boots", "Dodge chance", "boots.png"),
    EquipmentTypeInfo("Weapon", "Damage and critical hit chance", "gun.png"),
]


EQUIPMENT_TIERS: list[EquipmentTierInfo] = [
    EquipmentTierInfo("Red", "#ef4444", "121–150%", "56–70", "51–60%", "56–70", "51–60%", "Fighter Jet", "221–300", "41–50%", "jet.png"),
    EquipmentTierInfo("Gold", "#d4a843", "91–110%", "36–50", "31–40%", "36–50", "31–40%", "Tank", "141–170", "26–35%", "tank.png"),
    EquipmentTierInfo("Purple", "#a855f7", "71–90%", "21–30", "21–25%", "21–30", "21–25%", "Sniper", "101–130", "16–20%", "sniper.png"),
    EquipmentTierInfo("Blue", "#3b82f6", "31–50%", "11–15", "11–15%", "11–15", "11–15%", "Rifle", "71–90", "11–15%", "rifle.png"),
    EquipmentTierInfo("Green", "#22c55e", "16–30%", "6–10", "6–10%", "6–10", "6–10%", "Gun", "51–60", "6–10%", "gun.png"),
    EquipmentTierInfo("Grey", "#9ca3af", "1–15%", "1–5", "1–5%", "1–5", "1–5%", "Knife", "21–40", "1–5%", "knife.png"),
]


AMMO_TYPES: list[AmmoInfo] = [
    AmmoInfo("Light Ammunition", "+10% damage", "Provides a 10% bonus to weapon damage while equipped.", "lightAmmo.png"),
    AmmoInfo("Medium Ammunition", "+20% damage", "Provides a 20% bonus to weapon damage while equipped.", "ammo.png"),
    AmmoInfo("Heavy Ammunition", "+40% damage", "Provides a 40% bonus to weapon damage while equipped.", "heavyAmmo.png"),
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

        .armour-calc-marker {
            display: none;
        }

        div[data-testid="stVerticalBlockBorderWrapper"]:has(.armour-calc-marker) {
            background: #1c2333 !important;
            border: 1px solid var(--border) !important;
            border-radius: 10px;
            padding: 1rem 1.1rem;
            margin-bottom: 1rem;
            transition: background 0.2s ease, border-color 0.2s ease;
            box-shadow: none !important;
            overflow: hidden;
        }

        div[data-testid="stVerticalBlockBorderWrapper"]:has(.armour-calc-marker) > div,
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.armour-calc-marker) > div > div,
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.armour-calc-marker) [data-testid="stVerticalBlock"] {
            background: transparent !important;
        }

        div[data-testid="stVerticalBlockBorderWrapper"]:has(.armour-calc-marker):hover {
            background: #222d3f !important;
            border-color: #1f9d74 !important;
        }

        div[data-testid="stVerticalBlockBorderWrapper"]:has(.armour-calc-marker):hover > div,
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.armour-calc-marker):hover > div > div,
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.armour-calc-marker):hover [data-testid="stVerticalBlock"] {
            background: transparent !important;
        }

        div[data-testid="stVerticalBlockBorderWrapper"]:has(.armour-calc-marker) h3 {
            color: var(--accent-gold);
            font-size: 1.35rem;
            margin-bottom: 0.7rem;
        }

        div[data-testid="stVerticalBlockBorderWrapper"]:has(.armour-calc-marker) p,
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.armour-calc-marker) label,
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.armour-calc-marker) [data-testid="stCaptionContainer"] {
            color: var(--text-secondary);
        }

        div[data-testid="stVerticalBlockBorderWrapper"]:has(.armour-calc-marker) [data-testid="stMetric"] {
            background: var(--bg-secondary);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 0.85rem 0.95rem;
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

        .resource-section-intro {
            color: var(--text-secondary);
            margin: 0.15rem 0 1rem;
        }

        .resource-card {
            min-height: 178px;
        }

        .resource-header {
            display: flex;
            align-items: center;
            gap: 0.8rem;
            margin-bottom: 0.55rem;
        }

        .resource-icon-wrap {
            width: 52px;
            height: 52px;
            border-radius: 12px;
            background: var(--bg-secondary);
            border: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            overflow: hidden;
        }

        .resource-icon {
            width: 36px;
            height: 36px;
            object-fit: contain;
            display: block;
        }

        .resource-header-copy {
            min-width: 0;
        }

        .resource-card h4 {
            color: var(--text-primary);
            font-family: 'Rajdhani', sans-serif;
            font-size: 1.3rem;
            margin: 0 0 0.2rem;
        }

        .resource-pill {
            display: inline-block;
            margin-bottom: 0.75rem;
            padding: 0.22rem 0.58rem;
            background: rgba(16,185,129,0.12);
            border: 1px solid rgba(16,185,129,0.28);
            border-radius: 999px;
            color: var(--accent-teal);
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.02rem;
        }

        .resource-copy {
            color: var(--text-secondary);
            font-size: 0.95rem;
            line-height: 1.55;
            margin-bottom: 0.8rem;
        }

        .resource-cost {
            padding: 0.7rem 0.8rem;
            background: var(--bg-secondary);
            border: 1px solid var(--border);
            border-radius: 8px;
            color: var(--text-primary);
            font-size: 0.9rem;
        }

        .resource-cost-label {
            display: block;
            color: var(--text-muted);
            font-size: 0.76rem;
            text-transform: uppercase;
            letter-spacing: 0.04rem;
            margin-bottom: 0.25rem;
        }

        .jump-link-row {
            margin: -0.2rem 0 1rem;
        }

        .jump-link {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            color: var(--accent-teal);
            text-decoration: none;
            font-weight: 700;
            font-size: 0.92rem;
            border-bottom: 1px solid rgba(16,185,129,0.28);
            padding-bottom: 0.1rem;
        }

        .jump-link:hover {
            border-color: rgba(16,185,129,0.8);
        }

        .equipment-intro {
            color: var(--text-secondary);
            margin: 0.15rem 0 1rem;
        }

        .equipment-card {
            min-height: 160px;
        }

        .equipment-card-header,
        .ammo-card-header,
        .tier-weapon-header {
            display: flex;
            align-items: center;
            gap: 0.8rem;
            margin-bottom: 0.7rem;
        }

        .equipment-icon-wrap,
        .ammo-icon-wrap,
        .tier-weapon-icon-wrap {
            width: 52px;
            height: 52px;
            border-radius: 12px;
            background: var(--bg-secondary);
            border: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            flex-shrink: 0;
        }

        .equipment-icon,
        .ammo-icon,
        .tier-weapon-icon {
            width: 36px;
            height: 36px;
            object-fit: contain;
        }

        .equipment-card h4,
        .ammo-card h4,
        .tier-card h4 {
            color: var(--text-primary);
            font-family: 'Rajdhani', sans-serif;
            font-size: 1.3rem;
            margin: 0;
        }

        .equipment-copy,
        .ammo-copy,
        .tier-copy {
            color: var(--text-secondary);
            font-size: 0.95rem;
            line-height: 1.55;
        }

        .equipment-effect {
            padding: 0.7rem 0.8rem;
            background: var(--bg-secondary);
            border: 1px solid var(--border);
            border-radius: 8px;
            color: var(--text-primary);
            font-size: 0.9rem;
            margin-top: 0.8rem;
        }

        .equipment-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 0.85rem;
        }

        .equipment-table th {
            text-align: left;
            color: var(--text-muted);
            font-size: 0.74rem;
            text-transform: uppercase;
            letter-spacing: 0.04rem;
            padding: 0 0.45rem 0.45rem;
        }

        .equipment-table td {
            padding: 0.55rem 0.45rem;
            border-top: 1px solid var(--border);
            color: var(--text-secondary);
            font-size: 0.88rem;
            vertical-align: top;
        }

        .equipment-tier-chip {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-width: 56px;
            padding: 0.2rem 0.5rem;
            border-radius: 999px;
            border: 1px solid rgba(255,255,255,0.14);
            font-size: 0.76rem;
            font-weight: 700;
            line-height: 1;
        }

        .equipment-stat-highlight {
            font-weight: 700;
        }

        .weapon-tier-cell {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .weapon-tier-icon-wrap {
            width: 30px;
            height: 30px;
            border-radius: 8px;
            background: var(--bg-secondary);
            border: 1px solid var(--border);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            flex-shrink: 0;
        }

        .weapon-tier-icon {
            width: 22px;
            height: 22px;
            object-fit: contain;
            display: block;
        }

        .equipment-effect-label,
        .tier-stat-label {
            display: block;
            color: var(--text-muted);
            font-size: 0.76rem;
            text-transform: uppercase;
            letter-spacing: 0.04rem;
            margin-bottom: 0.25rem;
        }

        .tier-card {
            min-height: 100%;
        }

        .tier-badge {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 0.25rem 0.6rem;
            border-radius: 999px;
            font-size: 0.78rem;
            font-weight: 700;
            margin-bottom: 0.8rem;
            border: 1px solid rgba(255,255,255,0.12);
        }

        .tier-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 0.55rem;
            margin-bottom: 0.9rem;
        }

        .tier-stat {
            background: var(--bg-secondary);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 0.65rem 0.75rem;
            color: var(--text-primary);
            font-size: 0.9rem;
        }

        .tier-weapon-box {
            margin-top: 0.25rem;
            padding: 0.8rem;
            background: var(--bg-secondary);
            border: 1px solid var(--border);
            border-radius: 8px;
        }

        .tier-weapon-copy {
            color: var(--text-secondary);
            font-size: 0.9rem;
            line-height: 1.5;
        }

        .ammo-bonus {
            display: inline-block;
            margin-bottom: 0.75rem;
            padding: 0.22rem 0.58rem;
            background: rgba(16,185,129,0.12);
            border: 1px solid rgba(16,185,129,0.28);
            border-radius: 999px;
            color: var(--accent-teal);
            font-size: 0.78rem;
            font-weight: 700;
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

            .tier-grid {
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

    if block.title == "Weapons, Equipment, and Ammo":
        parts.append(
            '<div class="jump-link-row"><a class="jump-link" href="#equipment-reference">Jump to equipment reference ↓</a></div>'
        )

    if block.tip:
        parts.append(f'<div class="tip-box">{escape(block.tip)}</div>')

    if block.warning:
        parts.append(f'<div class="tip-box">{escape(block.warning)}</div>')

    parts.append('</div>')
    st.markdown("".join(parts), unsafe_allow_html=True)


def resource_icon_data_uri(resource: ResourceInfo) -> str | None:
    if not resource.icon_file:
        return None

    icon_path = RESOURCE_ICONS_DIR / resource.icon_file
    if not icon_path.exists():
        return None

    extension = icon_path.suffix.lower().lstrip(".") or "png"
    encoded = base64.b64encode(icon_path.read_bytes()).decode("ascii")
    return f"data:image/{extension};base64,{encoded}"


def icon_file_data_uri(directory: Path, file_name: str | None) -> str | None:
    if not file_name:
        return None

    icon_path = directory / file_name
    if not icon_path.exists():
        return None

    extension = icon_path.suffix.lower().lstrip(".") or "png"
    encoded = base64.b64encode(icon_path.read_bytes()).decode("ascii")
    return f"data:image/{extension};base64,{encoded}"


def render_economy_resources() -> None:
    st.markdown('<h3 class="info-card-title">Resources</h3>', unsafe_allow_html=True)
    st.markdown(
        '<p class="resource-section-intro">There is a wide variety of resources in the game, each with its own use. The cards below give a quick overview of what each resource does and what it costs to produce. Manufactured goods also require matching base materials in addition to their Production Point cost.</p>',
        unsafe_allow_html=True,
    )

    for start in range(0, len(ECONOMY_RESOURCES), 2):
        row = ECONOMY_RESOURCES[start : start + 2]
        columns = st.columns(len(row))
        for column, resource in zip(columns, row):
            with column:
                icon_data_uri = resource_icon_data_uri(resource)
                icon_html = (
                    f'<div class="resource-icon-wrap"><img class="resource-icon" src="{icon_data_uri}" alt="{escape(resource.name)} icon"></div>'
                    if icon_data_uri
                    else '<div class="resource-icon-wrap"></div>'
                )
                st.markdown(
                    f"""
                    <div class="card resource-card">
                        <div class="resource-header">
                            {icon_html}
                            <div class="resource-header-copy">
                                <h4>{escape(resource.name)}</h4>
                                <div class="resource-pill">{escape(resource.category)}</div>
                            </div>
                        </div>
                        <div class="resource-copy">{escape(resource.description)}</div>
                        <div class="resource-cost">
                            <span class="resource-cost-label">Production Cost</span>
                            {escape(resource.production_cost)}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


def build_equipment_table_rows(equipment: EquipmentTypeInfo) -> str:
    stat_lookup = {
        "Helmet": "helmet",
        "Chest Armour": "chest",
        "Trousers": "pants",
        "Gloves": "gloves",
        "Boots": "boots",
    }

    if equipment.name == "Weapon":
        rows = []
        for tier in EQUIPMENT_TIERS:
            weapon_icon = icon_file_data_uri(EQUIPMENT_ICONS_DIR, tier.weapon_icon_file)
            weapon_icon_html = (
                f'<span class="weapon-tier-icon-wrap"><img class="weapon-tier-icon" src="{weapon_icon}" alt="{escape(tier.weapon_name)} icon"></span>'
                if weapon_icon
                else ""
            )
            rows.append(
                "".join(
                    [
                        "<tr>",
                        f'<td><span class="equipment-tier-chip" style="background:{tier.theme}22;color:{tier.theme};border-color:{tier.theme}55;">{escape(tier.tier)}</span></td>',
                        f'<td><div class="weapon-tier-cell">{weapon_icon_html}<span class="equipment-stat-highlight" style="color:{tier.theme};">{escape(tier.weapon_name)}</span></div></td>',
                        f'<td><span class="equipment-stat-highlight" style="color:{tier.theme};">{escape(tier.weapon_damage)}</span></td>',
                        f'<td><span class="equipment-stat-highlight" style="color:{tier.theme};">{escape(tier.weapon_crit)}</span></td>',
                        "</tr>",
                    ]
                )
            )

        return (
            '<table class="equipment-table">'
            '<thead><tr><th>Rarity</th><th>Weapon</th><th>Damage</th><th>Crit</th></tr></thead>'
            f'<tbody>{"".join(rows)}</tbody>'
            '</table>'
        )

    attribute_name = stat_lookup[equipment.name]
    rows = []
    for tier in EQUIPMENT_TIERS:
        value = getattr(tier, attribute_name)
        rows.append(
            "".join(
                [
                    "<tr>",
                    f'<td><span class="equipment-tier-chip" style="background:{tier.theme}22;color:{tier.theme};border-color:{tier.theme}55;">{escape(tier.tier)}</span></td>',
                    f'<td><span class="equipment-stat-highlight" style="color:{tier.theme};">{escape(value)}</span></td>',
                    "</tr>",
                ]
            )
        )

    return (
        '<table class="equipment-table">'
        '<thead><tr><th>Rarity</th><th>Stat Range</th></tr></thead>'
        f'<tbody>{"".join(rows)}</tbody>'
        '</table>'
    )


def render_equipment_reference() -> None:
    st.markdown('<div id="equipment-reference"></div>', unsafe_allow_html=True)
    st.markdown('<h3 class="info-card-title">Equipment Reference</h3>', unsafe_allow_html=True)
    st.markdown(
        '<p class="equipment-intro">Equipment comes in six rarity levels from best to worst: Red, Gold, Purple, Blue, Green, and Grey. You can obtain equipment through crafting with scrap, opening cases, or buying it from the market.</p>',
        unsafe_allow_html=True,
    )

    st.markdown('<h3 class="info-card-title">Equipment Types</h3>', unsafe_allow_html=True)
    for start in range(0, len(EQUIPMENT_TYPES), 2):
        row = EQUIPMENT_TYPES[start : start + 2]
        columns = st.columns(len(row))
        for column, equipment in zip(columns, row):
            with column:
                icon_data_uri = icon_file_data_uri(EQUIPMENT_ICONS_DIR, equipment.icon_file)
                icon_html = (
                    f'<div class="equipment-icon-wrap"><img class="equipment-icon" src="{icon_data_uri}" alt="{escape(equipment.name)} icon"></div>'
                    if icon_data_uri
                    else '<div class="equipment-icon-wrap"></div>'
                )
                st.markdown(
                    f"""
                    <div class="card equipment-card">
                        <div class="equipment-card-header">
                            {icon_html}
                            <h4>{escape(equipment.name)}</h4>
                        </div>
                        <div class="equipment-effect">
                            <span class="equipment-effect-label">Main Effect</span>
                            {escape(equipment.effect)}
                        </div>
                        {build_equipment_table_rows(equipment)}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    st.markdown('<h3 class="info-card-title">Ammunition</h3>', unsafe_allow_html=True)
    st.markdown(
        '<p class="equipment-intro">There are three ammunition types in War Era. Each one increases the damage dealt by weapons while that ammunition is equipped.</p>',
        unsafe_allow_html=True,
    )

    ammo_columns = st.columns(len(AMMO_TYPES))
    for column, ammo in zip(ammo_columns, AMMO_TYPES):
        with column:
            icon_data_uri = icon_file_data_uri(EQUIPMENT_ICONS_DIR, ammo.icon_file)
            icon_html = (
                f'<div class="ammo-icon-wrap"><img class="ammo-icon" src="{icon_data_uri}" alt="{escape(ammo.name)} icon"></div>'
                if icon_data_uri
                else '<div class="ammo-icon-wrap"></div>'
            )
            st.markdown(
                f"""
                <div class="card ammo-card">
                    <div class="ammo-card-header">
                        {icon_html}
                        <h4>{escape(ammo.name)}</h4>
                    </div>
                    <div class="ammo-bonus">{escape(ammo.bonus)}</div>
                    <div class="ammo-copy">{escape(ammo.description)}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


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
        if block.title == "Company Types and Resources":
            render_economy_resources()
    st.markdown(
        '<div class="tip-box">External tools: <a href="https://warerastats.io/tools" target="_blank">warerastats.io/tools</a></div>',
        unsafe_allow_html=True,
    )


def render_fighting() -> None:
    st.markdown('<h2 class="section-title">Fighting &amp; War</h2>', unsafe_allow_html=True)
    for block in FIGHT_BLOCKS:
        render_info_block(block)

    with st.container(border=True):
        st.markdown('<div class="armour-calc-marker"></div>', unsafe_allow_html=True)
        st.markdown('<h3 class="info-card-title">Armour Protection Calculator</h3>', unsafe_allow_html=True)
        st.write(
            "Use this calculator to estimate health loss per hit based on your armour percentage."
        )
        st.caption(
            "Formula: health loss = 10 - (armour percentage as a decimal × 10)"
        )

        armor_percentage = st.number_input(
            "Armour percentage",
            min_value=0.0,
            max_value=100.0,
            value=20.0,
            step=1.0,
            help="Enter your armour value as a percentage, for example 20 for 20%.",
        )
        armor_decimal = armor_percentage / 100
        health_loss = 10 - (armor_decimal * 10)

        result_col, formula_col = st.columns([1, 1])
        with result_col:
            st.metric("Health loss per hit", f"{health_loss:.2f}")
        with formula_col:
            st.write(
                f"Example calculation: 10 - ({armor_decimal:.2f} × 10) = {health_loss:.2f}"
            )

    render_equipment_reference()


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

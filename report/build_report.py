from math import pi
from pathlib import Path

from PIL import Image
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas


HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "SYST52461_Term_Project_Report.pdf"
DASHBOARD_IMAGE = HERE / "assets" / "dashboard_published.jpg"

W, H = letter

PAPER = colors.HexColor("#F5F0E7")
PAPER_LIGHT = colors.HexColor("#FBF8F1")
INK = colors.HexColor("#1D2A27")
FOREST = colors.HexColor("#204D45")
FOREST_DARK = colors.HexColor("#15362F")
RUST = colors.HexColor("#C95E37")
GOLD = colors.HexColor("#C79A35")
BRONZE = colors.HexColor("#A96635")
SILVER = colors.HexColor("#7D8782")
SAGE = colors.HexColor("#AFC3AF")
MUTED = colors.HexColor("#66736F")
HAIRLINE = colors.HexColor("#D3CBBE")
WHITE = colors.white

LEFT = 44
RIGHT = W - 44


def wrap_lines(text, font, size, width):
    lines = []
    for paragraph in text.split("\n"):
        if not paragraph:
            lines.append("")
            continue
        words = paragraph.split()
        current = ""
        for word in words:
            trial = word if not current else current + " " + word
            if stringWidth(trial, font, size) <= width:
                current = trial
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
    return lines


def paragraph(c, text, x, y, width, font="Helvetica", size=9.2, leading=13,
              color=INK, max_lines=None):
    c.setFont(font, size)
    c.setFillColor(color)
    lines = wrap_lines(text, font, size, width)
    if max_lines is not None:
        lines = lines[:max_lines]
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y


def bullet(c, text, x, y, width, color=INK, size=8.8, leading=12.2):
    c.setFillColor(RUST)
    c.circle(x + 2.3, y + 3.0, 1.7, stroke=0, fill=1)
    return paragraph(c, text, x + 11, y, width - 11, size=size, leading=leading, color=color)


def small_caps(c, text, x, y, color=RUST, size=7.2):
    c.setFont("Helvetica-Bold", size)
    c.setFillColor(color)
    c.drawString(x, y, text.upper())


def page_header(c, page_num, section):
    c.setFillColor(PAPER)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    small_caps(c, "SYST52461 | BIG DATA STORAGE AND ANALYSIS", LEFT, H - 27, FOREST, 6.8)
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 6.8)
    c.drawRightString(RIGHT, H - 27, section)
    c.setStrokeColor(HAIRLINE)
    c.setLineWidth(0.5)
    c.line(LEFT, H - 36, RIGHT, H - 36)
    c.line(LEFT, 30, RIGHT, 30)
    c.setFont("Helvetica", 6.6)
    c.setFillColor(MUTED)
    c.drawString(LEFT, 18, "FreshRoute Grocery Delivery Analytics Pipeline")
    c.drawRightString(RIGHT, 18, f"{page_num} / 5")


def heading(c, title, subtitle=None, y=715):
    title_size = 25.0
    while stringWidth(title, "Times-Bold", title_size) > RIGHT - LEFT and title_size > 19:
        title_size -= 0.5
    c.setFont("Times-Bold", title_size)
    c.setFillColor(INK)
    c.drawString(LEFT, y, title)
    y -= 24
    if subtitle:
        y = paragraph(c, subtitle, LEFT, y, RIGHT - LEFT, size=9.2, leading=12.5, color=MUTED)
    return y


def metric(c, x, y, number, label, width, accent=RUST, number_size=22):
    c.setStrokeColor(accent)
    c.setLineWidth(2.5)
    c.line(x, y + 25, x, y - 20)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", number_size)
    c.drawString(x + 10, y + 6, number)
    paragraph(c, label.upper(), x + 10, y - 8, width - 10,
              font="Helvetica-Bold", size=6.6, leading=8.5, color=MUTED)


def thin_label(c, label, value, x, y, value_x, width):
    c.setFont("Helvetica", 7.8)
    c.setFillColor(MUTED)
    c.drawString(x, y, label)
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(INK)
    c.drawString(value_x, y, value)
    c.setStrokeColor(HAIRLINE)
    c.setLineWidth(0.35)
    c.line(x, y - 5, x + width, y - 5)


def bar(c, x, y, width, height, fraction, color, background=HAIRLINE):
    c.setFillColor(background)
    c.roundRect(x, y, width, height, height / 2, stroke=0, fill=1)
    c.setFillColor(color)
    c.roundRect(x, y, max(height, width * fraction), height, height / 2, stroke=0, fill=1)


def link_text(c, label, display, x, y, width, target=None):
    c.setFont("Helvetica-Bold", 7.4)
    c.setFillColor(FOREST)
    c.drawString(x, y, label)
    c.setFont("Helvetica", 7.4)
    c.setFillColor(MUTED)
    c.drawString(x + 55, y, display)
    c.linkURL(target or display, (x + 52, y - 2, x + width, y + 9), relative=0)


def page_one(c):
    c.setFillColor(PAPER)
    c.rect(0, 0, W, H, stroke=0, fill=1)

    # Editorial shapes, not UI cards.
    c.saveState()
    c.setFillAlpha(0.13)
    c.setFillColor(RUST)
    c.circle(W + 6, H - 24, 178, stroke=0, fill=1)
    c.setFillColor(GOLD)
    c.circle(W - 34, H + 20, 110, stroke=0, fill=1)
    c.restoreState()

    small_caps(c, "SYST52461 TERM PROJECT | JULY 2026", LEFT, H - 46, FOREST, 7.4)
    c.setFont("Times-Bold", 39)
    c.setFillColor(INK)
    c.drawString(LEFT, H - 115, "Grocery Delivery")
    c.drawString(LEFT, H - 158, "Analytics Pipeline")

    c.setStrokeColor(RUST)
    c.setLineWidth(5)
    c.line(LEFT, H - 181, 160, H - 181)
    c.setStrokeColor(FOREST)
    c.setLineWidth(1)
    c.line(169, H - 181, RIGHT, H - 181)

    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(FOREST)
    c.drawString(LEFT, H - 218, "FRESHROUTE: FROM MESSY EVENTS TO DEFENSIBLE DECISIONS")
    intro = (
        "FreshRoute is a fictional grocery delivery company operating 25 stores across five Ontario cities. "
        "The team built a deterministic PySpark pipeline that generates six connected tables, preserves realistic "
        "quality defects in Bronze, standardizes and validates them in Silver, and produces analysis-ready Gold "
        "tables for a native Databricks dashboard."
    )
    paragraph(c, intro, LEFT, H - 242, 350, size=10.2, leading=15, color=INK)

    c.setFillColor(FOREST)
    c.rect(425, H - 336, 143, 118, stroke=0, fill=1)
    small_caps(c, "WHY THIS DATA MATTERS", 440, H - 239, GOLD, 6.8)
    paragraph(
        c,
        "Grocery delivery links commercial choices to fulfilment. One dashboard can compare revenue, discounts, "
        "loyalty, distance and delay.",
        440, H - 260, 112, size=8.1, leading=11.4, color=WHITE,
    )

    small_caps(c, "SIX CONNECTED SOURCE TABLES", LEFT, H - 357, RUST, 7.0)
    tables = [
        ("CUSTOMERS", "profiles + loyalty"),
        ("STORES", "locations + formats"),
        ("PRODUCTS", "catalog + categories"),
        ("ORDERS", "events + payments"),
        ("ORDER ITEMS", "quantity + discount"),
        ("DELIVERIES", "distance + delay"),
    ]
    x_positions = [LEFT, 218, 392]
    for i, (name, role) in enumerate(tables):
        col = i % 3
        row = i // 3
        x = x_positions[col]
        y = H - 384 - row * 43
        c.setFont("Helvetica-Bold", 8.0)
        c.setFillColor(FOREST)
        c.drawString(x, y, name)
        c.setFont("Helvetica", 7.7)
        c.setFillColor(MUTED)
        c.drawString(x, y - 12, role)
        c.setStrokeColor(HAIRLINE)
        c.line(x, y - 20, x + 132, y - 20)

    small_caps(c, "TEAM MEMBERS", LEFT, 270, RUST, 7.0)
    names = [
        "Hazim Ali", "Mannan", "Maheshwar",
        "Sweta", "Omar Leopoldo", "Shreyansh Pankaj",
    ]
    for i, name in enumerate(names):
        x = LEFT + (i % 3) * 174
        y = 248 - (i // 3) * 26
        c.setFont("Helvetica-Bold", 9.0)
        c.setFillColor(INK)
        c.drawString(x, y, name)

    # KPI band.
    c.setFillColor(FOREST_DARK)
    c.rect(0, 56, W, 126, stroke=0, fill=1)
    c.setStrokeColor(colors.HexColor("#50766E"))
    c.setLineWidth(0.5)
    for x in [132, 250, 370, 490]:
        c.line(x, 82, x, 157)
    kpis = [
        ("$172,835.74", "NET REVENUE"),
        ("3,636", "COMPLETED ORDERS"),
        ("$47.53", "AVERAGE ORDER VALUE"),
        ("27.14%", "ON-TIME DELIVERY"),
        ("83.32%", "REPEAT CUSTOMERS"),
    ]
    centers = [69, 191, 310, 430, 551]
    for center, (number, label) in zip(centers, kpis):
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 14.5 if len(number) < 10 else 12.5)
        c.drawCentredString(center, 124, number)
        c.setFillColor(SAGE)
        c.setFont("Helvetica-Bold", 5.8)
        c.drawCentredString(center, 102, label)
    c.setFont("Helvetica", 6.7)
    c.setFillColor(colors.HexColor("#D8E1DE"))
    c.drawCentredString(W / 2, 73, "Verified Databricks Gold output | catalog: workspace | schema: analytics | seed: 52461")
    c.showPage()


def page_two(c):
    page_header(c, 2, "DATA FOUNDATION")
    heading(c, "From imperfect records to governed analytics",
            "The medallion architecture separates raw evidence, cleaning rules and business logic so every metric can be traced and reproduced.")

    # Three-stage flow with open layout.
    stage_y = 594
    stages = [
        (80, BRONZE, "01", "BRONZE", "Six raw Delta tables preserve nulls, duplicates, inconsistent labels, text-form numbers and orphan keys."),
        (274, SILVER, "02", "SILVER", "Column-specific rules parse types, normalize values, remove invalid rows and enforce key integrity."),
        (468, GOLD, "03", "GOLD", "Eleven purpose-built tables expose stable KPIs, dimensions and aggregates for EDA and the dashboard."),
    ]
    for cx, color, num, name, body in stages:
        c.setFillColor(color)
        c.circle(cx, stage_y + 37, 31, stroke=0, fill=1)
        c.setFillColor(WHITE)
        c.setFont("Times-Bold", 18)
        c.drawCentredString(cx, stage_y + 30, num)
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(cx, stage_y - 8, name)
        paragraph(c, body, cx - 72, stage_y - 29, 144, size=7.5, leading=10.3, color=MUTED)
    c.setStrokeColor(FOREST)
    c.setLineWidth(1.5)
    for x1, x2 in [(115, 237), (309, 431)]:
        c.line(x1, stage_y + 37, x2, stage_y + 37)
        c.line(x2 - 6, stage_y + 42, x2, stage_y + 37)
        c.line(x2 - 6, stage_y + 32, x2, stage_y + 37)

    small_caps(c, "DATA MODEL AND RELATIONSHIPS", LEFT, 465, RUST, 7.0)
    rows = [
        ("customers", "Customer and loyalty profile", "CustomerID -> orders"),
        ("stores", "Location and store format", "StoreID -> orders, products"),
        ("products", "Store product catalogue", "ProductID -> order_items"),
        ("orders", "Order event and payment", "OrderID -> order_items, deliveries"),
        ("order_items", "Quantity, price and discount", "OrderID + ProductID"),
        ("deliveries", "Driver and fulfilment outcome", "OrderID -> orders"),
    ]
    c.setFont("Helvetica-Bold", 7.0)
    c.setFillColor(MUTED)
    c.drawString(LEFT, 446, "TABLE")
    c.drawString(168, 446, "ONE ROW REPRESENTS")
    c.drawString(374, 446, "KEY RELATIONSHIP")
    y = 428
    for i, (name, role, relation) in enumerate(rows):
        if i % 2 == 0:
            c.setFillColor(PAPER_LIGHT)
            c.rect(LEFT - 4, y - 8, RIGHT - LEFT + 8, 25, stroke=0, fill=1)
        c.setFillColor(FOREST)
        c.setFont("Helvetica-Bold", 8.2)
        c.drawString(LEFT, y, name)
        c.setFillColor(INK)
        c.setFont("Helvetica", 8.0)
        c.drawString(168, y, role)
        c.setFillColor(MUTED)
        c.drawString(374, y, relation)
        y -= 27

    small_caps(c, "SILVER CLEANING DECISIONS", LEFT, 248, RUST, 7.0)
    left_items = [
        "Customers: deduplicate IDs, normalize city, loyalty and email, parse dates, reject ages outside 18-90 and median-impute age.",
        "Stores and products: constrain ratings, remove currency symbols, cast numbers, estimate missing cost at 65% of price and reject nonpositive values.",
        "Orders: normalize status and payment, parse timestamps and remove orphan customer/store references.",
    ]
    right_items = [
        "Order items: standardize 0.15, 15 and 15% discount formats; reject invalid quantities and enforce product-store consistency.",
        "Deliveries: remove units, reject nonpositive distance or promised time, and compute delay/on-time only for delivered orders.",
        "Validation: assert six unique primary keys, zero orphan foreign keys and non-empty Gold outputs before dashboard use.",
    ]
    yl = yr = 226
    for text in left_items:
        yl = bullet(c, text, LEFT, yl, 245, size=7.8, leading=10.8) - 5
    for text in right_items:
        yr = bullet(c, text, 322, yr, 246, size=7.8, leading=10.8) - 5

    c.setFillColor(FOREST)
    c.rect(LEFT, 52, RIGHT - LEFT, 42, stroke=0, fill=1)
    small_caps(c, "CRITICAL GRAIN RULE", LEFT + 13, 79, GOLD, 6.5)
    paragraph(
        c,
        "Revenue is calculated per completed line, then summed to exactly one row per order before average order value is calculated. This prevents a line-item average from being reported as order value.",
        LEFT + 126, 78, 382, size=7.6, leading=10.2, color=WHITE,
    )
    c.showPage()


def page_three(c):
    page_header(c, 3, "COMMERCIAL PERFORMANCE")
    heading(c, "Revenue scale is healthy - context makes it useful",
            "The Gold layer connects executive totals to category and store drivers without losing order-level accuracy.")

    metric(c, LEFT, 632, "$172,835.74", "Total net revenue", 156, RUST, 20)
    metric(c, 224, 632, "3,636", "Completed orders", 135, GOLD, 22)
    metric(c, 390, 632, "$47.53", "True order-level AOV", 175, FOREST, 22)

    c.setStrokeColor(HAIRLINE)
    c.setLineWidth(0.6)
    c.line(LEFT, 577, RIGHT, 577)

    # Category share.
    small_caps(c, "FINDING 1 | CATEGORY MIX", LEFT, 552, RUST, 7.0)
    c.setFont("Times-Bold", 23)
    c.setFillColor(INK)
    c.drawString(LEFT, 519, "Meat & Seafood leads")
    category_share = 50649.02 / 172835.74
    c.setLineWidth(10)
    c.setStrokeColor(HAIRLINE)
    c.circle(124, 433, 55, stroke=1, fill=0)
    c.setStrokeColor(RUST)
    c.arc(69, 378, 179, 488, 90, -360 * category_share)
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(FOREST)
    c.drawCentredString(124, 429, f"{category_share * 100:.1f}%")
    c.setFont("Helvetica-Bold", 6.8)
    c.setFillColor(MUTED)
    c.drawCentredString(124, 413, "OF NET REVENUE")

    thin_label(c, "Net revenue", "$50,649.02", 205, 462, 292, 177)
    thin_label(c, "Units sold", "2,710", 205, 432, 292, 177)
    thin_label(c, "Gross profit", "$15,531.76", 205, 402, 292, 177)
    paragraph(
        c,
        "The category generates almost three in every ten revenue dollars. Management should compare revenue, units and gross profit together before expanding assortment because a high-ticket category can lead revenue without leading volume.",
        205, 371, 176, size=8.0, leading=11.2, color=MUTED,
    )

    # Store context.
    c.setFillColor(FOREST_DARK)
    c.rect(407, 348, 161, 197, stroke=0, fill=1)
    small_caps(c, "FINDING 2 | TOP STORE", 423, 522, GOLD, 6.5)
    c.setFont("Times-Bold", 18)
    c.setFillColor(WHITE)
    c.drawString(423, 493, "Oakville 1")
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(GOLD)
    c.drawString(423, 457, "$9,477.16")
    c.setFont("Helvetica-Bold", 6.5)
    c.setFillColor(SAGE)
    c.drawString(423, 444, "NET REVENUE")
    store_rows = [
        ("Completed orders", "171"),
        ("Unique customers", "154"),
        ("Average order value", "$55.42"),
        ("On-time delivery", "10.59%"),
    ]
    sy = 414
    for label, value in store_rows:
        c.setFont("Helvetica", 7.2)
        c.setFillColor(colors.HexColor("#D9E3E0"))
        c.drawString(423, sy, label)
        c.setFont("Helvetica-Bold", 7.5)
        c.setFillColor(WHITE)
        c.drawRightString(552, sy, value)
        sy -= 20

    small_caps(c, "THE MANAGEMENT READING", LEFT, 313, RUST, 7.0)
    paragraph(
        c,
        "Commercial success and operational quality should be read together. Oakville 1 leads revenue and AOV, yet only 10.59% of its analyzed deliveries are on time. The dashboard therefore pairs store revenue with service measures instead of producing a one-dimensional ranking.",
        LEFT, 291, 522, size=9.0, leading=13, color=INK,
    )

    small_caps(c, "HOW THE NUMBERS WERE DEFENDED", LEFT, 213, FOREST, 7.0)
    notes = [
        "Completed orders are distinct OrderID values after valid line items and completed status filters.",
        "Average order value is mean NetRevenue from orders_gold, not an average of product lines.",
        "Category and store metrics reconcile to the same $172,835.74 executive total.",
        "Every result describes the seeded synthetic FreshRoute scenario, not a real grocery market.",
    ]
    ny = 190
    for text in notes:
        ny = bullet(c, text, LEFT, ny, 522, size=8.2, leading=11.4) - 5

    c.setStrokeColor(RUST)
    c.setLineWidth(2.5)
    c.line(LEFT, 59, LEFT, 116)
    paragraph(
        c,
        "Commercial conclusion",
        LEFT + 13, 104, 105, font="Helvetica-Bold", size=8.2, leading=11, color=FOREST,
    )
    paragraph(
        c,
        "FreshRoute has meaningful demand and repeat behavior, but the best commercial segments still need operational scrutiny. Revenue alone is not the decision.",
        LEFT + 130, 104, 390, size=8.2, leading=11.5, color=INK,
    )
    c.showPage()


def page_four(c):
    page_header(c, 4, "PROMOTION, DELIVERY AND LOYALTY")
    heading(c, "Basket response improves; delivery reliability collapses",
            "Two comparisons expose the main business trade-off: promotions can lift quantity, while longer travel sharply erodes service performance.")

    # Discount section.
    small_caps(c, "FINDING 3 | DISCOUNT RESPONSE", LEFT, 635, RUST, 7.0)
    c.setFont("Times-Bold", 19)
    c.setFillColor(INK)
    c.drawString(LEFT, 606, "Higher discount, larger basket")
    c.setFont("Helvetica", 7.5)
    c.setFillColor(MUTED)
    c.drawString(LEFT, 584, "AVERAGE QUANTITY PER LINE")
    bar(c, LEFT, 554, 218, 16, 1.53 / 2.10, SAGE)
    bar(c, LEFT, 512, 218, 16, 1.98 / 2.10, RUST)
    c.setFont("Helvetica-Bold", 8.2)
    c.setFillColor(FOREST)
    c.drawString(LEFT, 574, "0% discount")
    c.drawRightString(LEFT + 218, 574, "1.53 units")
    c.setFillColor(RUST)
    c.drawString(LEFT, 532, "20%+ discount")
    c.drawRightString(LEFT + 218, 532, "1.98 units")
    c.setFont("Helvetica", 7.6)
    c.setFillColor(MUTED)
    c.drawString(LEFT, 489, "Line items")
    c.setFont("Helvetica-Bold", 8.2)
    c.setFillColor(INK)
    c.drawString(102, 489, "3,989 vs 879")
    c.setFont("Helvetica", 7.6)
    c.setFillColor(MUTED)
    c.drawString(LEFT, 472, "Net revenue")
    c.setFont("Helvetica-Bold", 8.2)
    c.setFillColor(INK)
    c.drawString(102, 472, "$67,574.14 vs $14,864.28")
    paragraph(
        c,
        "The highest discount band raises quantity by about 29%, but it covers far fewer lines and contributes much less revenue. The result supports targeted promotions, not blanket discounting.",
        LEFT, 441, 235, size=8.2, leading=11.5, color=INK,
    )

    # Delivery section.
    x2 = 322
    small_caps(c, "FINDING 4 | DISTANCE RISK", x2, 635, RUST, 7.0)
    c.setFont("Times-Bold", 19)
    c.setFillColor(INK)
    c.drawString(x2, 606, "Promises fail at distance")
    c.setFont("Helvetica", 7.5)
    c.setFillColor(MUTED)
    c.drawString(x2, 584, "ON-TIME DELIVERY RATE")

    base_y = 504
    c.setStrokeColor(HAIRLINE)
    c.setLineWidth(0.5)
    c.line(x2, base_y, 552, base_y)
    max_h = 68
    vals = [("0-5 km", 63.86, RUST, 689), ("20+ km", 3.55, FOREST, 647)]
    for idx, (label, val, color, deliveries) in enumerate(vals):
        bx = x2 + 34 + idx * 112
        bh = max_h * (val / 70)
        c.setFillColor(color)
        c.rect(bx, base_y, 55, bh, stroke=0, fill=1)
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(INK)
        c.drawCentredString(bx + 27.5, base_y + bh + 10, f"{val:.2f}%")
        c.setFont("Helvetica-Bold", 7.5)
        c.setFillColor(MUTED)
        c.drawCentredString(bx + 27.5, base_y - 14, label)
        c.setFont("Helvetica", 6.9)
        c.drawCentredString(bx + 27.5, base_y - 26, f"{deliveries} deliveries")
    c.setFont("Helvetica", 7.6)
    c.setFillColor(MUTED)
    c.drawString(x2, 454, "Average delay")
    c.setFont("Helvetica-Bold", 8.2)
    c.setFillColor(INK)
    c.drawString(x2 + 78, 454, "1.48 vs 11.25 minutes")
    paragraph(
        c,
        "The longest band is almost never on time. Distance-aware promise windows, smaller peak-hour delivery zones and courier-capacity monitoring are the clearest operational actions.",
        x2, 423, 246, size=8.2, leading=11.5, color=INK,
    )

    c.setStrokeColor(HAIRLINE)
    c.line(LEFT, 385, RIGHT, 385)
    small_caps(c, "FINDING 5 | RETENTION VERSUS SERVICE", LEFT, 359, RUST, 7.0)
    c.setFont("Times-Bold", 21)
    c.setFillColor(INK)
    c.drawString(LEFT, 328, "Customers return even while service reliability lags")

    # Two large open circles.
    circle_data = [
        (145, 226, 83.32, "REPEAT-CUSTOMER RATE", FOREST),
        (405, 226, 27.14, "ON-TIME DELIVERY RATE", RUST),
    ]
    for cx, cy, value, label, color in circle_data:
        c.setLineWidth(9)
        c.setStrokeColor(HAIRLINE)
        c.circle(cx, cy, 58, stroke=1, fill=0)
        c.setStrokeColor(color)
        c.arc(cx - 58, cy - 58, cx + 58, cy + 58, 90, -360 * value / 100)
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 19)
        c.drawCentredString(cx, cy - 3, f"{value:.2f}%")
        c.setFillColor(MUTED)
        c.setFont("Helvetica-Bold", 6.5)
        c.drawCentredString(cx, cy - 20, label)
    c.setStrokeColor(FOREST)
    c.setLineWidth(1.4)
    c.line(217, 226, 333, 226)
    c.line(327, 231, 333, 226)
    c.line(327, 221, 333, 226)

    paragraph(
        c,
        "The synthetic model shows strong repurchase behavior, but this should not be treated as proof that poor delivery has no consequence. Real customer data may reveal delayed churn, complaint behavior or geographic bias that the mock data cannot capture.",
        LEFT, 133, 522, size=8.5, leading=12.2, color=INK,
    )
    c.setFillColor(FOREST)
    c.rect(LEFT, 52, RIGHT - LEFT, 42, stroke=0, fill=1)
    small_caps(c, "INTERPRETATION DISCIPLINE", LEFT + 13, 79, GOLD, 6.4)
    paragraph(
        c,
        "These findings validate the analytical pipeline and dashboard story. They describe engineered FreshRoute data and do not establish real-world causal effects.",
        LEFT + 150, 78, 360, size=7.6, leading=10.3, color=WHITE,
    )
    c.showPage()


def page_five(c):
    page_header(c, 5, "DASHBOARD, REFLECTION AND CONCLUSION")
    heading(c, "A dashboard designed to move from signal to action",
            "Executive KPIs establish scale; the next visuals explain commercial drivers, promotional response, delivery risk and customer behavior.")

    # Crop away browser chrome and keep the native dashboard evidence.
    source = Image.open(DASHBOARD_IMAGE).convert("RGB")
    crop = source.crop((155, 125, 1070, 650))
    img = ImageReader(crop)
    c.drawImage(img, LEFT, 404, width=RIGHT - LEFT, height=248, preserveAspectRatio=True, anchor="c", mask="auto")
    c.setStrokeColor(FOREST)
    c.setLineWidth(1.2)
    c.rect(LEFT, 404, RIGHT - LEFT, 248, stroke=1, fill=0)
    c.setFont("Helvetica", 6.6)
    c.setFillColor(MUTED)
    c.drawString(LEFT, 393, "Published native Databricks dashboard: FreshRoute Grocery Delivery Performance | Executive Overview")

    # Lower two-column editorial layout.
    small_caps(c, "DASHBOARD STORY", LEFT, 363, RUST, 7.0)
    y1 = 341
    story_points = [
        "Overview: five cards summarize revenue, completed orders, AOV, on-time delivery and repeat customers.",
        "Commercial: category, store and product views explain where revenue and profit originate.",
        "Action: discount, distance and loyalty visuals expose promotion, service and retention trade-offs.",
        "Exploration: the global Month filter changes the time context without modifying notebook code.",
    ]
    for text in story_points:
        y1 = bullet(c, text, LEFT, y1, 245, size=7.8, leading=10.7) - 5

    small_caps(c, "REFLECTION AND LIMITATIONS", 322, 363, RUST, 7.0)
    reflection = (
        "The hardest engineering problem was preserving realistic foreign-key relationships while Bronze still "
        "contained testable defects. A single dependency order, deterministic seed and layer-level assertions made "
        "failures traceable. A second challenge was metric grain: revenue begins at line level, while AOV must be "
        "calculated after grouping to one order. Team integration also required preserving genuine GitHub history "
        "while harmonizing contributor notebooks into one safe, reproducible run order."
    )
    paragraph(c, reflection, 322, 341, 246, size=7.8, leading=10.7, color=INK)

    small_caps(c, "WHAT WE WOULD ADD WITH REAL DATA", 322, 222, FOREST, 6.8)
    future_points = [
        "Inventory events, substitutions, weather, traffic and courier shifts.",
        "Automated quality expectations and scheduled dashboard refresh monitoring.",
        "Real distribution benchmarks, complaint outcomes and controlled promotion tests.",
    ]
    fy = 202
    for text in future_points:
        fy = bullet(c, text, 322, fy, 246, size=7.5, leading=10.2) - 4

    c.setStrokeColor(HAIRLINE)
    c.line(LEFT, 128, RIGHT, 128)
    small_caps(c, "CONCLUSION", LEFT, 108, RUST, 6.8)
    paragraph(
        c,
        "The project delivers a reproducible Bronze-Silver-Gold pipeline and a coherent dashboard story. Its central lesson is that validated relationships, correct aggregation grain and operational context are necessary before transaction data can support defensible business decisions.",
        LEFT, 88, 522, size=8.2, leading=11.2, color=INK,
    )

    link_text(c, "GITHUB", "https://github.com/HazimAli07/grocery-delivery-analytics-pipeline", LEFT, 48, 330)
    link_text(
        c, "DASHBOARD", "FreshRoute Grocery Delivery Performance (published)", 352, 48, 216,
        target="https://dbc-c58ab985-c7cd.cloud.databricks.com/dashboardsv3/01f187bb678d15ae91676a0d5422a14e?o=7474657090248704",
    )
    c.showPage()


def build():
    c = canvas.Canvas(str(OUTPUT), pagesize=letter)
    c.setTitle("Grocery Delivery Analytics Pipeline")
    c.setAuthor("Hazim Ali, Mannan, Maheshwar, Sweta, Omar Leopoldo, Shreyansh Pankaj")
    c.setSubject("SYST52461 Big Data Storage and Analysis Term Project")
    c.setKeywords("Databricks, PySpark, Bronze, Silver, Gold, grocery delivery, analytics")
    page_one(c)
    page_two(c)
    page_three(c)
    page_four(c)
    page_five(c)
    c.save()
    print(OUTPUT)


if __name__ == "__main__":
    build()

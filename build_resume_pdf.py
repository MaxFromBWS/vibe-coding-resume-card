from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors

IMG = r"d:\Проекты Cursor\Resume and business card for a vibe coding specialist\assets\profile-maxim-new.png"
FONT = r"C:\Windows\Fonts\arial.ttf"
OUT_DARK = r"d:\Проекты Cursor\Resume and business card for a vibe coding specialist\assets\Resume_Maxim_Vibecoding_RU_dark.pdf"
OUT_LIGHT = r"d:\Проекты Cursor\Resume and business card for a vibe coding specialist\assets\Resume_Maxim_Vibecoding_RU_light.pdf"
OUT_DEFAULT = r"d:\Проекты Cursor\Resume and business card for a vibe coding specialist\assets\Resume_Maxim_Vibecoding_RU.pdf"
BLOCK_PAD = 14
BLOCK_GAP = 10
SECTION_TITLE_SIZE = 16
SECTION_BODY_SIZE = 11
SECTION_TEXT_GAP = 12
SECTION_LINE_H = 14
SECTION_TITLE_BLOCK = 22


def wrap_by_width(pdf: canvas.Canvas, text: str, font_name: str, font_size: int, max_width: float) -> list[str]:
    words = text.split()
    if not words:
        return [""]
    result: list[str] = []
    current = words[0]
    for word in words[1:]:
        candidate = f"{current} {word}"
        if pdf.stringWidth(candidate, font_name, font_size) <= max_width:
            current = candidate
        else:
            result.append(current)
            current = word
    result.append(current)
    return result


def draw_section(
    pdf: canvas.Canvas,
    title: str,
    lines: list[str],
    y_top: float,
    page_w: float,
    dark: bool,
) -> float:
    title_size = SECTION_TITLE_SIZE
    text_size = SECTION_BODY_SIZE
    line_h = SECTION_LINE_H
    body: list[str] = []
    max_body_width = page_w - 48 - BLOCK_PAD * 2
    for line in lines:
        body.extend(wrap_by_width(pdf, line, "ArialRU", text_size, max_body_width))

    box_h = BLOCK_PAD + SECTION_TITLE_BLOCK + SECTION_TEXT_GAP + len(body) * line_h + BLOCK_PAD
    if dark:
        pdf.setFillColorRGB(0.12, 0.17, 0.33)
        border_col = colors.Color(0.27, 0.36, 0.58, alpha=0.7)
        title_col = colors.white
        text_col = colors.Color(0.83, 0.89, 1)
    else:
        pdf.setFillColorRGB(0.98, 0.99, 1)
        border_col = colors.Color(0.46, 0.55, 0.77, alpha=0.45)
        title_col = colors.Color(0.14, 0.25, 0.47)
        text_col = colors.Color(0.25, 0.36, 0.56)

    box_x = 24
    box_w = page_w - 48
    box_y = y_top - box_h
    pdf.roundRect(box_x, box_y, box_w, box_h, 10, stroke=0, fill=1)
    pdf.setStrokeColor(border_col)
    pdf.setLineWidth(0.8)
    pdf.roundRect(box_x, box_y, box_w, box_h, 10, stroke=1, fill=0)

    pdf.setFillColor(title_col)
    pdf.setFont("ArialRU", title_size)
    title_x = box_x + BLOCK_PAD
    # Baseline заголовка внутри выделенного блока высоты SECTION_TITLE_BLOCK
    title_y = y_top - BLOCK_PAD - 16
    pdf.drawString(title_x, title_y, title)

    pdf.setFillColor(text_col)
    pdf.setFont("ArialRU", text_size)
    # Baseline первой строки тела: строго после блока заголовка и зазора
    ty = y_top - BLOCK_PAD - SECTION_TITLE_BLOCK - SECTION_TEXT_GAP
    for idx, line in enumerate(body):
        pdf.drawString(title_x, ty - idx * line_h, line)

    return y_top - box_h - BLOCK_GAP


def draw_header(pdf: canvas.Canvas, page_w: float, page_h: float, dark: bool) -> float:
    if dark:
        pdf.setFillColorRGB(0.04, 0.07, 0.15)
        pdf.rect(0, 0, page_w, page_h, stroke=0, fill=1)
        pdf.setFillColorRGB(0.08, 0.13, 0.27)
        border_col = colors.Color(0.30, 0.42, 0.70, alpha=0.75)
        badge_col = colors.Color(0.80, 0.85, 0.98)
        title_col = colors.white
        lead_col = colors.Color(0.84, 0.89, 1)
    else:
        pdf.setFillColorRGB(0.94, 0.96, 1)
        pdf.rect(0, 0, page_w, page_h, stroke=0, fill=1)
        pdf.setFillColorRGB(1, 1, 1)
        border_col = colors.Color(0.49, 0.58, 0.79, alpha=0.45)
        badge_col = colors.Color(0.31, 0.45, 0.73)
        title_col = colors.Color(0.12, 0.22, 0.43)
        lead_col = colors.Color(0.20, 0.31, 0.54)

    card_x = 24
    card_w = page_w - 48
    photo_w = 102
    photo_h = 140
    inter_col_gap = 14
    header_x = card_x + BLOCK_PAD + photo_w + inter_col_gap
    header_w = page_w - header_x - 24 - BLOCK_PAD
    title_font = 18
    title_step = 20
    lead_step = 12.5
    lead_lines = [
        "Выпускник школы Нейросетей и СММ Ксении Барановой.",
        "Создаю сайты, ботов и digital-проекты с помощью ИИ.",
        "Запускаю AI-интеграции и автоматизацию для бизнеса.",
        "Проектирую интерфейсы и логику удобных продуктов.",
        "Открыт к новым проектам.",
    ]
    title_lines_probe = wrap_by_width(pdf, "Я — Максим, специалист по вайбкодингу", "ArialRU", title_font, header_w)
    text_h = 11 + 12 + len(title_lines_probe) * title_step + 8 + len(lead_lines) * lead_step
    content_h = text_h
    card_h = content_h + BLOCK_PAD * 2
    card_y = page_h - 24 - card_h
    card_top = card_y + card_h
    pdf.roundRect(card_x, card_y, card_w, card_h, 14, stroke=0, fill=1)
    pdf.setStrokeColor(border_col)
    pdf.setLineWidth(0.9)
    pdf.roundRect(card_x, card_y, card_w, card_h, 14, stroke=1, fill=0)

    content_top = card_top - BLOCK_PAD
    content_bottom = card_y + BLOCK_PAD

    pdf.setFont("ArialRU", 10.5)
    pdf.setFillColor(badge_col)
    badge_y = content_top - 11
    pdf.drawString(header_x, badge_y, "AI + Web + Bots + Automation")

    pdf.setFillColor(title_col)
    pdf.setFont("ArialRU", title_font)
    title_lines = wrap_by_width(pdf, "Я — Максим, специалист по вайбкодингу", "ArialRU", title_font, header_w)
    title_y = badge_y - 24
    for i, line in enumerate(title_lines):
        pdf.drawString(header_x, title_y - i * title_step, line)

    pdf.setFillColor(lead_col)
    pdf.setFont("ArialRU", 10.5)
    lead_start_y = title_y - len(title_lines) * title_step - 2
    for i, line in enumerate(lead_lines):
        pdf.drawString(header_x, lead_start_y - i * lead_step, line)

    photo_x = card_x + BLOCK_PAD
    photo_h = content_h
    photo_y = content_bottom
    pdf.drawImage(ImageReader(IMG), photo_x, photo_y, photo_w, photo_h, preserveAspectRatio=True, mask="auto", anchor="c")

    return card_y - BLOCK_GAP


def build_pdf(output_path: str, dark: bool) -> None:
    pdf = canvas.Canvas(output_path, pagesize=A4)
    page_w, page_h = A4
    y = draw_header(pdf, page_w, page_h, dark)

    y = draw_section(pdf, "Обо мне в цифрах", ["12+ реализованных проектов", "5 ниш и тематик", "7-14 дней средний срок прототипа", "100% фокус на AI и автоматизации"], y, page_w, dark)
    y = draw_section(
        pdf,
        "Чем я помогаю",
        [
            "Помогаю бизнесу и экспертам запускать сайты, ботов и автоматизации, чтобы быстро выходить на рынок и эффективно принимать заявки от клиентов.",
            "Работаю с логикой интерфейсов, сценариями пользователей и интеграциями AI, чтобы продукт был удобным, современным и готовым к масштабированию.",
        ],
        y,
        page_w,
        dark,
    )
    y = draw_section(
        pdf,
        "Мои навыки",
        [
            "• Создание сайтов",
            "• Разработка ботов (Telegram / VK)",
            "• Интеграция ИИ",
            "• Работа с интерфейсами и логикой проектов",
        ],
        y,
        page_w,
        dark,
    )
    draw_section(
        pdf,
        "Контакты",
        ["Telegram: @ONYX_lab", "Почта: onyx.lab.chat@gmail.com", "Телефон: 8-900-318-15-73"],
        y,
        page_w,
        dark,
    )
    pdf.save()


def main() -> None:
    pdfmetrics.registerFont(TTFont("ArialRU", FONT))
    build_pdf(OUT_DARK, dark=True)
    build_pdf(OUT_LIGHT, dark=False)
    # Keep backward-compatible filename as dark default.
    build_pdf(OUT_DEFAULT, dark=True)


if __name__ == "__main__":
    main()

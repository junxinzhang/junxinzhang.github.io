#!/usr/bin/env python3
"""Generate inline images for the AI Agent Security & Commerce article - English version."""

from PIL import Image, ImageDraw, ImageFont
import os

def get_font(size):
    """Try to get a font, fallback to default if not available."""
    try:
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)
    except:
        return ImageFont.load_default()

def get_font_regular(size):
    """Try to get a regular font."""
    try:
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)
    except:
        return ImageFont.load_default()

def draw_rounded_rect(draw, coords, radius, fill, outline=None, width=1):
    """Draw a rounded rectangle."""
    x1, y1, x2, y2 = coords
    draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=fill)
    draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=fill)
    draw.ellipse([x1, y1, x1 + radius * 2, y1 + radius * 2], fill=fill)
    draw.ellipse([x2 - radius * 2, y1, x2, y1 + radius * 2], fill=fill)
    draw.ellipse([x1, y2 - radius * 2, x1 + radius * 2, y2], fill=fill)
    draw.ellipse([x2 - radius * 2, y2 - radius * 2, x2, y2], fill=fill)

def create_attack_chain_image():
    """Create ServiceNow BodySnatcher attack chain diagram."""
    width, height = 900, 500
    img = Image.new('RGB', (width, height), (15, 23, 42))
    draw = ImageDraw.Draw(img)

    font_title = get_font(22)
    font_text = get_font_regular(14)
    font_small = get_font_regular(12)

    # Title
    draw.text((width // 2 - 180, 20), "BodySnatcher Attack Chain Diagram", font=font_title, fill=(241, 245, 249))

    # Attack steps - boxes
    steps = [
        ("1. Send Request", "Use hardcoded cred:\nservicenowexternalagent", (239, 68, 68)),
        ("2. Bypass Auth", "Claim any user identity\nNo MFA/SSO needed", (249, 115, 22)),
        ("3. Impersonate", "Declare admin\nidentity in request", (234, 179, 8)),
        ("4. Agent Exec", "AI Agent creates\nnew admin account", (168, 85, 247)),
        ("5. Full Control", "Complete access to\nServiceNow instance", (239, 68, 68)),
    ]

    box_width = 140
    box_height = 100
    start_x = 50
    y = 150

    for i, (title, desc, color) in enumerate(steps):
        x = start_x + i * (box_width + 30)
        # Box
        draw_rounded_rect(draw, [x, y, x + box_width, y + box_height], 10, (30, 41, 59))
        draw.rectangle([x, y, x + box_width, y + 5], fill=color)
        # Title
        draw.text((x + 10, y + 15), title, font=font_text, fill=(241, 245, 249))
        # Description
        lines = desc.split('\n')
        for j, line in enumerate(lines):
            draw.text((x + 10, y + 45 + j * 18), line, font=font_small, fill=(148, 163, 184))

        # Arrow
        if i < len(steps) - 1:
            arrow_x = x + box_width + 5
            draw.line([(arrow_x, y + box_height // 2), (arrow_x + 20, y + box_height // 2)], fill=(100, 116, 139), width=2)
            draw.polygon([
                (arrow_x + 20, y + box_height // 2 - 5),
                (arrow_x + 25, y + box_height // 2),
                (arrow_x + 20, y + box_height // 2 + 5)
            ], fill=(100, 116, 139))

    # Warning box at bottom
    warning_y = 320
    draw_rounded_rect(draw, [50, warning_y, width - 50, warning_y + 100], 10, (55, 17, 17))
    draw.text((70, warning_y + 15), "! IMPACT", font=font_title, fill=(239, 68, 68))
    draw.text((70, warning_y + 50), "* 85% of Fortune 500 companies use ServiceNow", font=font_text, fill=(252, 165, 165))
    draw.text((70, warning_y + 75), "* No actual login required - completely bypasses existing security", font=font_text, fill=(252, 165, 165))

    # Footer
    draw.text((width - 250, height - 30), "Source: AppOmni Security Research", font=font_small, fill=(100, 116, 139))

    return img

def create_crowdstrike_acquisition_image():
    """Create CrowdStrike acquisition strategy diagram."""
    width, height = 900, 500
    img = Image.new('RGB', (width, height), (15, 23, 42))
    draw = ImageDraw.Draw(img)

    font_title = get_font(22)
    font_text = get_font_regular(16)
    font_small = get_font_regular(14)

    # Title
    draw.text((width // 2 - 180, 20), "CrowdStrike AI Agent Security Strategy", font=font_title, fill=(241, 245, 249))

    # Center: CrowdStrike
    cx, cy = width // 2, height // 2
    draw.ellipse([cx - 80, cy - 80, cx + 80, cy + 80], fill=(249, 115, 22), outline=(251, 146, 60), width=3)
    draw.text((cx - 65, cy - 15), "CrowdStrike", font=font_text, fill=(255, 255, 255))
    draw.text((cx - 35, cy + 5), "Falcon", font=font_small, fill=(255, 237, 213))

    # SGNL acquisition - left
    sgnl_x, sgnl_y = 150, cy
    draw_rounded_rect(draw, [sgnl_x - 80, sgnl_y - 60, sgnl_x + 80, sgnl_y + 60], 10, (30, 58, 138))
    draw.text((sgnl_x - 30, sgnl_y - 45), "SGNL", font=font_title, fill=(96, 165, 250))
    draw.text((sgnl_x - 40, sgnl_y - 15), "$740M", font=font_text, fill=(191, 219, 254))
    draw.text((sgnl_x - 70, sgnl_y + 10), "Continuous Identity", font=font_small, fill=(148, 163, 184))
    draw.text((sgnl_x - 70, sgnl_y + 30), "Real-time Risk Eval", font=font_small, fill=(148, 163, 184))
    # Arrow
    draw.line([(sgnl_x + 80, sgnl_y), (cx - 80, cy)], fill=(96, 165, 250), width=2)

    # Seraphic acquisition - right
    ser_x, ser_y = width - 150, cy
    draw_rounded_rect(draw, [ser_x - 80, ser_y - 60, ser_x + 80, ser_y + 60], 10, (22, 78, 99))
    draw.text((ser_x - 45, ser_y - 45), "Seraphic", font=font_title, fill=(34, 211, 238))
    draw.text((ser_x - 40, ser_y - 15), "$400M", font=font_text, fill=(165, 243, 252))
    draw.text((ser_x - 70, ser_y + 10), "Browser Runtime Sec", font=font_small, fill=(148, 163, 184))
    draw.text((ser_x - 65, ser_y + 30), "Enterprise Browser", font=font_small, fill=(148, 163, 184))
    # Arrow
    draw.line([(ser_x - 80, ser_y), (cx + 80, cy)], fill=(34, 211, 238), width=2)

    # Total at top
    draw_rounded_rect(draw, [cx - 100, 70, cx + 100, 120], 10, (55, 65, 81))
    draw.text((cx - 80, 80), "Total: $1.14 Billion", font=font_text, fill=(241, 245, 249))
    draw.line([(cx, 120), (cx, cy - 80)], fill=(100, 116, 139), width=2)

    # Strategic goal at bottom
    draw_rounded_rect(draw, [150, height - 120, width - 150, height - 40], 10, (30, 41, 59))
    draw.text((170, height - 105), "Strategic Goal:", font=font_text, fill=(249, 115, 22))
    draw.text((320, height - 105), "Protect Every AI Agent Identity", font=font_text, fill=(241, 245, 249))
    draw.text((170, height - 75), '"AI agents operate at superhuman speed - every agent is a privileged identity"', font=font_small, fill=(148, 163, 184))
    draw.text((570, height - 55), "- George Kurtz, CEO", font=font_small, fill=(100, 116, 139))

    return img

def create_ucp_architecture_image():
    """Create Google UCP architecture diagram."""
    width, height = 900, 550
    img = Image.new('RGB', (width, height), (15, 23, 42))
    draw = ImageDraw.Draw(img)

    font_title = get_font(22)
    font_text = get_font_regular(16)
    font_small = get_font_regular(14)

    # Title
    draw.text((width // 2 - 180, 20), "Google Universal Commerce Protocol", font=font_title, fill=(241, 245, 249))

    # User at top
    user_x, user_y = width // 2, 90
    draw.ellipse([user_x - 25, user_y - 25, user_x + 25, user_y + 25], fill=(34, 197, 94))
    draw.text((user_x - 20, user_y + 30), "User", font=font_small, fill=(134, 239, 172))

    # AI Agent layer
    agent_y = 170
    draw_rounded_rect(draw, [width // 2 - 100, agent_y, width // 2 + 100, agent_y + 50], 10, (88, 28, 135))
    draw.text((width // 2 - 45, agent_y + 12), "AI Agent", font=font_text, fill=(232, 121, 249))
    draw.text((width // 2 - 70, agent_y + 32), "(Gemini / 3rd Party)", font=font_small, fill=(216, 180, 254))

    # Arrow from user to agent
    draw.line([(user_x, user_y + 25), (user_x, agent_y)], fill=(100, 116, 139), width=2)

    # UCP Protocol layer
    ucp_y = 260
    draw_rounded_rect(draw, [100, ucp_y, width - 100, ucp_y + 60], 10, (30, 64, 175))
    draw.text((width // 2 - 180, ucp_y + 8), "Universal Commerce Protocol (UCP)", font=font_title, fill=(96, 165, 250))
    draw.text((width // 2 - 130, ucp_y + 35), "Standardized AI Shopping Interface", font=font_small, fill=(191, 219, 254))

    # Arrow
    draw.line([(width // 2, agent_y + 50), (width // 2, ucp_y)], fill=(100, 116, 139), width=2)

    # Retailers layer
    retailer_y = 380
    retailers = [
        ("Shopify", (96, 165, 250)),
        ("Walmart", (34, 197, 94)),
        ("Target", (239, 68, 68)),
        ("Etsy", (249, 115, 22)),
        ("Wayfair", (168, 85, 247)),
    ]

    box_width = 130
    start_x = 80
    for i, (name, color) in enumerate(retailers):
        x = start_x + i * (box_width + 20)
        draw_rounded_rect(draw, [x, retailer_y, x + box_width, retailer_y + 45], 8, (30, 41, 59))
        draw.rectangle([x, retailer_y, x + box_width, retailer_y + 5], fill=color)
        draw.text((x + box_width // 2 - len(name) * 4, retailer_y + 15), name, font=font_text, fill=(241, 245, 249))

    # Arrows from UCP to retailers
    for i in range(5):
        x = start_x + i * (box_width + 20) + box_width // 2
        draw.line([(x, ucp_y + 60), (x, retailer_y)], fill=(100, 116, 139), width=1)

    # Payment layer
    pay_y = 470
    payments = ["Visa", "Mastercard", "Stripe", "Adyen"]
    pay_start = 200
    for i, name in enumerate(payments):
        x = pay_start + i * 140
        draw_rounded_rect(draw, [x, pay_y, x + 120, pay_y + 35], 6, (55, 65, 81))
        draw.text((x + 60 - len(name) * 4, pay_y + 8), name, font=font_small, fill=(148, 163, 184))

    # AP2 label
    draw.text((120, pay_y + 10), "AP2 ->", font=font_small, fill=(34, 197, 94))

    # Market size note
    draw.text((width - 250, height - 30), "Market Size: $3-5 Trillion (2030)", font=font_small, fill=(34, 197, 94))

    return img

def create_security_vs_commerce_image():
    """Create security vs commerce comparison image."""
    width, height = 900, 450
    img = Image.new('RGB', (width, height), (15, 23, 42))
    draw = ImageDraw.Draw(img)

    font_title = get_font(24)
    font_text = get_font_regular(15)
    font_small = get_font_regular(13)

    # Title
    draw.text((width // 2 - 180, 20), "AI Agent: Security vs Commerce", font=font_title, fill=(241, 245, 249))

    # Dividing line
    draw.line([(width // 2, 70), (width // 2, height - 50)], fill=(55, 65, 81), width=2)

    # Left side - Security (Red)
    left_x = width // 4
    draw.text((left_x - 80, 80), "SECURITY RISKS", font=font_title, fill=(239, 68, 68))

    security_items = [
        "* ServiceNow CVE affects 85% Fortune 500",
        "* Agent permissions bypass IAM controls",
        "* Prompt injection attacks hard to prevent",
        "* Agent identity difficult to audit",
        "* 94% enterprises worry about AI security",
    ]

    for i, item in enumerate(security_items):
        draw.text((50, 140 + i * 40), item, font=font_text, fill=(252, 165, 165))

    # CrowdStrike response
    draw_rounded_rect(draw, [50, 350, width // 2 - 30, 420], 10, (55, 17, 17))
    draw.text((70, 360), "Response:", font=font_text, fill=(239, 68, 68))
    draw.text((70, 385), "CrowdStrike $1.14B Agent Security Push", font=font_small, fill=(252, 165, 165))

    # Right side - Commerce (Blue)
    right_x = 3 * width // 4
    draw.text((right_x - 100, 80), "BUSINESS OPPORTUNITY", font=font_title, fill=(59, 130, 246))

    commerce_items = [
        "* Google UCP open standard launched",
        "* $3-5 Trillion market potential",
        "* Meta acquires Manus for $2B",
        "* Enterprise AI spending doubles",
        "* 90% execs expect Agent ROI",
    ]

    for i, item in enumerate(commerce_items):
        draw.text((width // 2 + 30, 140 + i * 40), item, font=font_text, fill=(191, 219, 254))

    # Opportunity highlight
    draw_rounded_rect(draw, [width // 2 + 30, 350, width - 50, 420], 10, (23, 37, 84))
    draw.text((width // 2 + 50, 360), "Market Signal:", font=font_text, fill=(59, 130, 246))
    draw.text((width // 2 + 50, 385), "2026: AI Agents move from demo to production", font=font_small, fill=(191, 219, 254))

    return img

def main():
    """Generate all article images."""
    output_dir = "/home/user/junxinzhang.github.io/assets/images"

    images = [
        ("screenshot-20260117-bodysnatcher-attack-chain.webp", create_attack_chain_image),
        ("screenshot-20260117-crowdstrike-acquisition.webp", create_crowdstrike_acquisition_image),
        ("screenshot-20260117-google-ucp-architecture.webp", create_ucp_architecture_image),
        ("screenshot-20260117-security-vs-commerce.webp", create_security_vs_commerce_image),
    ]

    for filename, create_func in images:
        img = create_func()
        path = os.path.join(output_dir, filename)
        img.save(path, "WEBP", quality=90)
        print(f"Created: {path}")

if __name__ == "__main__":
    main()

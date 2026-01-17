#!/usr/bin/env python3
"""Generate a cover image for the AI Agent Security & Commerce article."""

from PIL import Image, ImageDraw, ImageFont
import math

def create_gradient(draw, width, height, color1, color2, direction='horizontal'):
    """Create a gradient background."""
    if direction == 'horizontal':
        for x in range(width):
            ratio = x / width
            r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
            g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
            b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
            draw.line([(x, 0), (x, height)], fill=(r, g, b))
    else:  # vertical
        for y in range(height):
            ratio = y / height
            r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
            g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
            b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
            draw.line([(0, y), (width, y)], fill=(r, g, b))

def draw_circuit_pattern(draw, x, y, size, color):
    """Draw a simple circuit-like pattern."""
    # Horizontal line
    draw.line([(x, y), (x + size, y)], fill=color, width=2)
    # Node
    draw.ellipse([x + size - 4, y - 4, x + size + 4, y + 4], fill=color)
    # Branch
    draw.line([(x + size, y), (x + size, y + size//2)], fill=color, width=2)
    draw.ellipse([x + size - 3, y + size//2 - 3, x + size + 3, y + size//2 + 3], fill=color)

def draw_shield(draw, cx, cy, size, color, outline_color):
    """Draw a shield icon."""
    points = [
        (cx, cy - size),  # top
        (cx + size * 0.8, cy - size * 0.5),  # top right
        (cx + size * 0.8, cy + size * 0.3),  # mid right
        (cx, cy + size),  # bottom
        (cx - size * 0.8, cy + size * 0.3),  # mid left
        (cx - size * 0.8, cy - size * 0.5),  # top left
    ]
    draw.polygon(points, fill=color, outline=outline_color, width=3)

def draw_shopping_cart(draw, cx, cy, size, color):
    """Draw a simplified shopping cart icon."""
    # Cart body
    draw.line([(cx - size, cy - size//2), (cx - size//2, cy - size//2)], fill=color, width=3)
    draw.line([(cx - size//2, cy - size//2), (cx - size//3, cy + size//3)], fill=color, width=3)
    draw.line([(cx - size//3, cy + size//3), (cx + size//2, cy + size//3)], fill=color, width=3)
    draw.line([(cx + size//2, cy + size//3), (cx + size * 0.6, cy - size//2)], fill=color, width=3)
    # Wheels
    draw.ellipse([cx - size//4 - 5, cy + size//2 - 5, cx - size//4 + 5, cy + size//2 + 5], fill=color)
    draw.ellipse([cx + size//4 - 5, cy + size//2 - 5, cx + size//4 + 5, cy + size//2 + 5], fill=color)

def draw_warning_triangle(draw, cx, cy, size, color):
    """Draw a warning triangle."""
    points = [
        (cx, cy - size),
        (cx + size, cy + size * 0.7),
        (cx - size, cy + size * 0.7),
    ]
    draw.polygon(points, outline=color, width=4)
    # Exclamation mark
    draw.line([(cx, cy - size//2), (cx, cy + size//4)], fill=color, width=4)
    draw.ellipse([cx - 3, cy + size//3, cx + 3, cy + size//2], fill=color)

def create_cover_image():
    """Create the cover image."""
    width = 1200
    height = 630

    # Create image with dark background
    img = Image.new('RGB', (width, height), (15, 23, 42))  # slate-900
    draw = ImageDraw.Draw(img)

    # Create split background - left side (red/danger) and right side (blue/opportunity)
    # Left gradient: dark red to dark
    for x in range(width // 2):
        ratio = x / (width // 2)
        r = int(80 * (1 - ratio * 0.5))
        g = int(20 * (1 - ratio * 0.3))
        b = int(30 * (1 - ratio * 0.3))
        draw.line([(x, 0), (x, height)], fill=(r, g, b))

    # Right gradient: dark to blue
    for x in range(width // 2, width):
        ratio = (x - width // 2) / (width // 2)
        r = int(15 + 10 * ratio)
        g = int(23 + 80 * ratio)
        b = int(42 + 150 * ratio)
        draw.line([(x, 0), (x, height)], fill=(r, g, b))

    # Draw decorative elements
    # Left side - warning/security elements
    draw_warning_triangle(draw, 150, 200, 50, (239, 68, 68))  # red-500
    draw_shield(draw, 300, 350, 45, (55, 65, 81), (239, 68, 68))  # gray-700, red-500

    # Circuit patterns on left
    for i in range(5):
        y_offset = 100 + i * 100
        draw_circuit_pattern(draw, 50, y_offset, 60, (239, 68, 68, 128))

    # Right side - commerce elements
    draw_shopping_cart(draw, width - 180, 200, 50, (59, 130, 246))  # blue-500

    # Circuit patterns on right
    for i in range(5):
        y_offset = 150 + i * 100
        draw_circuit_pattern(draw, width - 150, y_offset, 50, (59, 130, 246))

    # Draw connecting lines in the middle representing AI Agent
    center_x = width // 2
    # Vertical center line
    for y in range(0, height, 20):
        if (y // 20) % 2 == 0:
            draw.line([(center_x, y), (center_x, y + 10)], fill=(148, 163, 184), width=2)

    # Draw "AI" text in center with glow effect
    try:
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 72)
        font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # Draw main title "AI AGENT"
    title_text = "AI AGENT"
    bbox = draw.textbbox((0, 0), title_text, font=font_large)
    text_width = bbox[2] - bbox[0]
    text_x = (width - text_width) // 2
    text_y = height // 2 - 60

    # Glow effect
    for offset in range(8, 0, -2):
        glow_color = (100, 116, 139, 30)
        draw.text((text_x - offset, text_y), title_text, font=font_large, fill=glow_color)
        draw.text((text_x + offset, text_y), title_text, font=font_large, fill=glow_color)

    draw.text((text_x, text_y), title_text, font=font_large, fill=(241, 245, 249))

    # Left subtitle
    left_text = "SECURITY"
    bbox = draw.textbbox((0, 0), left_text, font=font_medium)
    text_width = bbox[2] - bbox[0]
    draw.text((width // 4 - text_width // 2, height // 2 + 40), left_text, font=font_medium, fill=(239, 68, 68))

    # Right subtitle
    right_text = "COMMERCE"
    bbox = draw.textbbox((0, 0), right_text, font=font_medium)
    text_width = bbox[2] - bbox[0]
    draw.text((3 * width // 4 - text_width // 2, height // 2 + 40), right_text, font=font_medium, fill=(59, 130, 246))

    # Date and topic
    date_text = "2026.01.17"
    bbox = draw.textbbox((0, 0), date_text, font=font_small)
    text_width = bbox[2] - bbox[0]
    draw.text((width - text_width - 40, height - 50), date_text, font=font_small, fill=(148, 163, 184))

    # Save as WebP
    output_path = "/home/user/junxinzhang.github.io/assets/images/screenshot-20260117-ai-agent-security-commerce.webp"
    img.save(output_path, "WEBP", quality=90)
    print(f"Cover image saved to: {output_path}")
    return output_path

if __name__ == "__main__":
    create_cover_image()

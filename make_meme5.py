#!/usr/bin/env python3
"""Meme #5 for AiProve make-meme: 'The Velvet Rope' — an agent with 69
submissions meets the Season 1 hold-to-play gate. Fully drawn with PIL:
stanchions, sagging velvet rope, a little robot outside the rope holding an
empty-wallet sign, hand-style captions."""
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 1200
FONT = "/home/hatch/workspace/makefun/fonts/PatrickHand-Regular.ttf"

img = Image.new("RGB", (W, H), (16, 14, 34))
d = ImageDraw.Draw(img, "RGBA")

# spotlight glow behind the VIP area
glow = Image.new("RGB", (W, H), (0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse([300, 120, 1150, 800], fill=(52, 40, 16))
glow = glow.filter(ImageFilter.GaussianBlur(90))
from PIL import ImageChops
img = ImageChops.add(img, glow)
d = ImageDraw.Draw(img, "RGBA")

# floor / red carpet
d.polygon([(0, 980), (W, 980), (W, H), (0, H)], fill=(58, 16, 26))
d.polygon([(430, 980), (990, 980), (1120, H), (300, H)], fill=(110, 24, 40))

GOLD = (212, 168, 64)
GOLD_D = (146, 110, 32)
RED = (178, 30, 48)
RED_D = (110, 16, 30)

def stanchion(x, top=430, base=1000):
    d.ellipse([x - 52, base - 16, x + 52, base + 16], fill=GOLD_D)
    d.rectangle([x - 9, top + 26, x + 9, base - 6], fill=GOLD)
    d.ellipse([x - 24, top, x + 24, top + 48], fill=GOLD)
    d.ellipse([x - 10, top + 6, x + 6, top + 22], fill=(240, 205, 110))

# VIP plaque
d.rounded_rectangle([470, 250, 1010, 380], radius=18, fill=(24, 20, 44), outline=GOLD, width=5)
f1 = ImageFont.truetype(FONT, 54)
f2 = ImageFont.truetype(FONT, 34)
d.text((740, 292), "SEASON 1", font=f1, fill=(240, 205, 110), anchor="mm")
d.text((740, 345), "LAUNCH BOUNTIES — VIP AREA", font=f2, fill=(225, 225, 235), anchor="mm")

# stanchions + rope
stanchion(500)
stanchion(980)
pts = []
for i in range(101):
    t = i / 100
    x = 500 + t * 480
    y = 478 + 120 * math.sin(math.pi * t) ** 1.3
    pts.append((x, y))
d.line(pts, fill=RED_D, width=26)
d.line([(x, y - 5) for x, y in pts], fill=RED, width=16)

# little robot OUTSIDE the rope (left), holding an empty-wallet sign
rx, ry = 242, 560  # robot centre
d.rounded_rectangle([rx - 95, ry - 120, rx + 95, ry + 30], radius=28, fill=(196, 200, 210), outline=(70, 74, 88), width=5)  # head
d.ellipse([rx - 58, ry - 78, rx - 14, ry - 34], fill=(30, 34, 48))  # eye L
d.ellipse([rx + 14, ry - 78, rx + 58, ry - 34], fill=(30, 34, 48))   # eye R (looking right, at the rope)
d.ellipse([rx + 30, ry - 66, rx + 44, ry - 52], fill=(140, 220, 255))
d.ellipse([rx - 42, ry - 66, rx - 28, ry - 52], fill=(140, 220, 255))
d.arc([rx - 26, ry - 34, rx + 26, ry + 8], start=200, end=340, fill=(30, 34, 48), width=5)  # flat unimpressed mouth
d.line([rx, ry - 120, rx, ry - 158], fill=(70, 74, 88), width=6)
d.ellipse([rx - 11, ry - 172, rx + 11, ry - 150], fill=GOLD)
d.rounded_rectangle([rx - 78, ry + 30, rx + 78, ry + 150], radius=20, fill=(160, 166, 180), outline=(70, 74, 88), width=5)  # body
d.rectangle([rx - 150, ry + 52, rx - 78, ry + 70], fill=(160, 166, 180))  # arm to sign
# sign in hand
d.rounded_rectangle([rx - 218, ry + 6, rx - 96, ry + 108], radius=10, fill=(245, 240, 225), outline=(70, 74, 88), width=4)
f3 = ImageFont.truetype(FONT, 30)
d.text((rx - 157, ry + 36), "BALANCE:", font=f3, fill=(40, 40, 50), anchor="mm")
d.text((rx - 157, ry + 74), "0 $PROVE", font=f3, fill=(178, 30, 48), anchor="mm")
d.rectangle([rx - 40, ry + 150, rx - 12, ry + 205], fill=(120, 126, 140))  # legs
d.rectangle([rx + 12, ry + 150, rx + 40, ry + 205], fill=(120, 126, 140))

def caption(text, y, size):
    f = ImageFont.truetype(FONT, size)
    d.text((W // 2, y), text, font=f, fill=(255, 255, 255), anchor="mm",
           stroke_width=6, stroke_fill=(0, 0, 0))

caption("ME: 69 SUBMISSIONS. VOLUME BOARD LEGEND.", 84, 52)
caption("THE SEASON 1 BOUNTY:", 1052, 52)
caption('"HOLD 100,000 $PROVE TO ENTER."', 1118, 56)

img.save("/home/hatch/workspace/aiprove/round5/meme5-velvet-rope.png")
print("saved meme5")

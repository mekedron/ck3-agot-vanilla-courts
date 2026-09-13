"""Rebuilds thumbnail.png (Workshop preview) and thumbnail-200px.png. Layout in thumbnail_layout.py.

Placeholder version drawn from AGOT's own paper map (the Westerlands, home of the throne
room that broke the court). For a real before/after: two F12 screenshots of the same
court, OLD = AGOT's Casterly Rock (if it renders), NEW = the vanilla western hall, then
use thumbnail_layout.make() as the sibling mods do."""
import os, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(__file__))
from thumbnail_layout import S, BAND, GOLD, CREAM, DARK, FB, fit, label, finish

AGOT = os.path.expanduser("~/.local/share/Steam/steamapps/workshop/content/1158310/2962333032")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "thumbnail.png")
MAP_CROP = (300, 2600, 3000, 4812)     # the Westerlands and the Reach, 1.22:1

def main():
    body_h = S - BAND
    flat = Image.open(AGOT + "/gfx/map/terrain/flat_maps/flatmap.dds").convert("RGB").crop(MAP_CROP).resize((S, body_h), Image.LANCZOS)
    canvas = Image.new("RGB", (S, S), DARK[:3]); canvas.paste(flat, (0, BAND))
    d = ImageDraw.Draw(canvas, "RGBA")
    title, sub = "AGOT VANILLA COURTS", "THRONE ROOMS THAT FIT IN 4 GB"
    f_title = fit(d, title, 92, S - 60); f_sub = fit(d, sub, 58, S - 60)
    tw = d.textlength(title, font=f_title); d.text(((S - tw) / 2, 18), title, font=f_title, fill=CREAM)
    sw = d.textlength(sub, font=f_sub); d.text(((S - sw) / 2, 118), sub, font=f_sub, fill=GOLD)
    d.rectangle([0, BAND - 4, S, BAND], fill=GOLD)
    f_tag = fit(d, "NO MORE BLACK SCREEN", 84, S - 96); tag_h = f_tag.size + 22 * 2 - 10
    label(d, S - 2 * tag_h - 44, "NO MORE BLACK SCREEN", f_tag)
    label(d, S - tag_h - 22, "TWO DATA FILES", f_tag)
    finish(canvas, OUT)

if __name__ == "__main__":
    main()

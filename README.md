# AGOT Vanilla Courts (CK3)

For [A Game of Thrones](https://steamcommunity.com/sharedfiles/filedetails/?id=2962333032)
on a GPU that cannot hold AGOT's throne rooms: sends every ruler to the vanilla throne
rooms instead. Two data files, no shaders, no script, nothing checksummed.

## Why

AGOT's own throne rooms are heavy. Casterly Rock's has 18 shadow casting lights and 18
fire particle systems on top of 75 MB of materials, and on a 4 GB card, where the AGOT
map alone sits at 3.5 GB of video memory, opening it made the NVIDIA driver fail its
memory mappings (`NVRM: dmaAllocMapping_GM107: can't update VA space for mapping` in
the kernel log): a black screen, and on closing it a map rendered out of garbage until a
restart. Lowering Texture Quality helped the lighter rooms (Pyke went from 10 to 48 FPS
on Low) but not that one. The vanilla rooms are a fraction of the size and were never a
problem.

## How

AGOT assigns its rooms in `gfx/court_scene/scene_cultures/agot_default_cultures.txt`
by the ruler's capital (King's Landing, Pyke, Casterly Rock, Dragonstone, Highgarden,
Winterfell, the Eyrie, Riverrun, Storm's End, the Free Cities, the Reach), and locks the
vanilla style rooms in its copy of `00_default_cultures.txt` behind the line
`agot_has_throne_room = no`. This mod ships both files rewritten: every AGOT room gets
`trigger = { always = no }`, and the lock line is dropped, so the ordinary culture
triggers (western, mediterranean, mena, byzantine, steppe...) pick the room the way they
do for everyone else. `tools/make_scene_cultures.py` regenerates both from the installed
AGOT; run it after an AGOT update.

What you lose: the Iron Throne room, Pyke, Winterfell and the rest of AGOT's custom
halls. What you keep: everything else, including the characters, their clothes and the
court mechanics. Rulers whose capital has no AGOT room see no difference.

## Installing

Run `./install.sh`, enable the mod in the launcher playset **below** A Game of
Thrones. Independent of the other AGOT patches. Takes effect the next time a court is
opened; no restart needed beyond the game start.

## Versions

Built against CK3 1.19.0.6 (Scribe) and AGOT 0.5.2.1.

## Multiplayer / achievements

Court scene culture files are not checksummed content, but the launcher still marks
any mod as a mod. Treat it like any other graphics mod.

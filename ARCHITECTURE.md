# Colosseum UI Overhaul architecture

## Separation boundary

- Mod ID: `colosseum_ui_overhaul`
- Donor mod ID: `gen3_battle_ui`
- The two packages conflict because they intercept the same renderer and menu
  methods. They must never be enabled together.
- Options, events, manifests, packaging, and future release versions belong to
  the new standalone namespace.

## Ownership rules

- This mod owns layout, typography, panels, portraits, and visual overlays.
- Gen1Recomp owns battle logic, input, menu indices, callbacks, items, Pokémon
  data, switching, move learning, TM/HM consumption, saving, and progression.
- Visual failure must return to a complete native or mature fallback path.

## Renderer families

1. Colosseum battle presentation.
2. Colosseum Party, Summary, Move Manager, and learning flows.
3. Dialogue and choice presentation.
4. START, Bag, and service screens.
5. PC and Pokédex.
6. Save, Options, Mods, Trainer Card, and Pokégear.
7. Cross-generation flow adapters for evolution, naming, held items, mail,
   services, and progression prompts.
8. Gen 2 normalization and compatibility adapters.
9. External sprite and battle-presentation compatibility.

## Shared material adapter

Every enabled renderer family is routed through `withColosseumSkin`. The adapter
translates legacy neutral panel colors into translucent dark glass, steel/cyan
structure and red focus treatments. Text is translated separately so dark donor
glyphs remain readable without turning structural fills white. Exact white
texture tint is preserved, preventing Pokémon, item, map and mod-provided images
from being recolored. Native world rendering is always invoked outside this
adapter. The adapter rejects exact full-frame donor fills while retaining the
actual menu panels, making hanging presentation a shared rule instead of a
screen-by-screen exception.

## Scene continuity rule

- Party, Summary, Bag, PC, Pokédex, Mart, Pokégear, START, and related child
  states are non-opaque when using their Colosseum presentation.
- The engine-owned battle or overworld is drawn normally underneath them.
- The mod must not capture, cache, or replay a screenshot of that scene.
- Readability comes from rounded translucent individual panels, not a full-screen veil.

## Extraction plan

`main.lua` remains intact in 0.1.0 to minimize closure and hook-order risk. New
work should first extract pure palette/layout helpers, followed by one renderer
family per release build. Hook installation remains centralized until extracted
modules have Gen 1 and Gen 2 regression coverage.

## Regression-sensitive flows

- Party A must open the native submenu without changing its Gen 1 boolean or
  Gen 2 table representation.
- Directional navigation must match the two-column visual grid.
- Summary uses the same direct three-tier navigation in both generations while
  retaining each engine's native close and party-data ownership.
- Gold SELECT opens the native Move Manager from the MOVES tier.
- TM/HM, Bag item targeting, evolution stones, and mid-battle learning retain
  callbacks and consumption rules.
- Party and its child flows retain the live underlying scene throughout.
- Evolution presentation reads the active installed sprite package while each
  generation retains native timing, cancellation, commit, and callback logic.
- PC presentation is one shared renderer family for Gen I and Gen II. Adapters
  may translate state fields and callbacks, but may not fork its visual flow.
- Summary content ownership is fixed: MOVES owns current/natural moves;
  PROFILE owns paginated TM/HM compatibility.
- Turning Colosseum portraits off affects both battle and Pokémon menus.

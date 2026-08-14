# Colosseum Inspired UI Overhaul — 1.0.0

Colosseum Inspired UI Overhaul is a presentation-focused Gen1Recomp mod with unified Gen I and Gen II interfaces inspired by Pokémon Colosseum. Version 1.0.0 includes the finalized cross-generation title presentation, continuous menu-session audio, native gameplay handoffs, and the complete approved UI feature set. The native Red/Blue/Yellow and Gold title screens remain authoritative and untouched.
It does not depend on the Gen 3 Inspired UI Overhaul and intentionally conflicts
with that donor mod because both patch the same Gen1Recomp UI hooks.

## Current experience

- Optional **MENU INTRO** treatment: a one-time vector Poké Ball reveal fades into the native title screen while the finalized Colosseum title audio plays continuously through the title and main-menu flow.
- Colosseum battle HUD, command grid, move grid, battle messages, prompts, and
  user-tunable status-panel width/height/portrait sizing for different displays and sprite packs, and
  level-up presentation for supported Gen 1 and Gen 2 battles.
- Two-column hanging Party screen with natural directional navigation.
- Live battle or overworld presentation behind Party, Summary, item-target,
  TM/HM, and move-learning flows; no screenshot/freeze-frame cache.
- Reference-inspired Pokémon Info/Summary with the same labeled, directly
  navigable STATUS / MOVES / PROFILE tiers in Gen I and Gen II, plus Gold's
  native-logic Move Manager.
- Colosseum Status composition with portrait, six readable stat meters, EXP,
  next-level progress, types, Ability, held item, OT, ID, level, and status.
- Current moves/PP, stats, EXP, next-level progress, types, held item, status,
  OT/ID, height/weight, evolution, TM/HM compatibility, and level-up learnsets.
- Independent Colosseum portrait toggle shared by battle and Pokémon menus.
- Authentic normal and shiny Colosseum menu portraits for every base Gen 1 and
  Gen 2 species, #001 through #251.
- Colosseum-styled Bag, START, PC, storage boxes, Pokédex, Mart, Trainer Card,
  Save, Options, Mods, Pokégear, naming, dialogue, and choice presentation.
- Cross-generation area transitions now surface a brief top-center translucent
  Colosseum location banner for routes, towns, cities, and other loaded maps.
- Native starter confirmation in both generations now uses a hanging Pokémon/PC-style selector and the same resolved front-sprite source as Party/PC; native starter scripts remain authoritative.
- Cross-generation presentation adapters keep engine logic intact while
  replacing evolution, naming, held-item/GIVE, mail, daycare, bank, elevator,
  decoration, prize, contest, trade, photo, Hall of Fame, and setup prompts.
- Evolution and egg-hatch transitions now use one suspended Colosseum stage
  with a luminous circular platform and the player's resolved sprite package;
  native evolution timing, cancellation, species rules, and callbacks remain
  authoritative.
- A Colosseum-style PokéDex replaces the handheld presentation: encountered
  list and selected-species dossier share one screen, with type, Ability,
  height, weight, appearance, caught state, and native memo actions.
- PokéDex and data pages deliberately use the game's resolved/native sprite
  pipeline, including player-installed sprite mods, instead of portrait crops.
- Border-connected ROM mattes are removed without deleting legitimate white
  details, and Gen II's PokéDex exposes an in-theme DATA / LOCATION sidecar.
- Gen II Party and battle EXP use Gold's total-experience field and resolved
  native growth-curve records, so both bars represent progress within the
  current level.
- Pokémon storage uses a four-by-five badge grid with a persistent left-side
  inspector for portrait, HP, moves, PP, and battle stats. Gen 1 and Gen 2 keep
  their native deposit, withdraw, move, release, summary, and cancel callbacks.
- Gen I and Gen II now share the same dark glass PC access selector, root
  dashboard, storage/deposit interface, inspector, action card, and footer.
  Generation-specific code is limited to native state data and callbacks.
- The Gen II PC inspector displays Attack, Defense, Special Attack, Special
  Defense, and Speed in addition to its existing HP presentation.
- Summary MOVES contains current moves and natural level-up moves only. PROFILE
  owns the comprehensive, paginated TM/HM compatibility list.
- Large PC inspector and Pokémon Status/Summary portraits always use the active
  game sprite package. Compact PC badges use the Colosseum icon set when its
  toggle is enabled and display each Pokémon's level directly on the badge.
- Party deposit now uses a compact six-member list with no meaningless empty
  box cells; the four-by-five badge matrix is reserved for actual PC boxes.
- The primary PokéDex dossier surfaces wild location, encounter method, and
  additional-area count while retaining the complete AREA passthrough.
- Left/right follows the horizontal TM/HM and mid-battle move-replacement
  strip, with up/down retained as compatible alternate input.
- Overworld and battle dialogue now invoke one shared renderer: the same
  beveled eight-point console, translucency, metallic highlights, centered
  width, bottom offset, padding, font treatment, and continue marker.
- Options, Mods, and the in-game UI settings screen are purpose-styled rounded
  Colosseum overlays and no longer expose the inherited Gen 3 presentation.
- Player Data is a purpose-built metal-and-green-monitor interface with
  Profile, Records, and Badges screens. Up/Down selects pages, Left/Right are
  aliases, and the real Trainer Card state continues to own closing/input.
- Player Data now uses a correctly oriented page chevron, game-native badge
  artwork for Kanto/Johto, and the Trainer Card portrait resolved through the
  active player sprite package before considering a ROM-native fallback.
- Colosseum portraits use one stable authentic frame. Alternate sheet facings
  no longer create left/right jitter for species such as Gloom.
- Save is a dedicated hanging cobalt Colosseum terminal with Name, Play Time,
  PokéDex, Pokémon Caught, and Badges; native confirmation logic remains in
  control for both generations.
- Records presents save-backed wins, fainted Pokémon, league clears, caught
  Pokémon, badges, and play time. Badges presents eight Kanto medals in Gen 1
  and separate Johto/Kanto medal banks in Gen 2.
- Trainer records use native save data where it exists. Battles won and player
  Pokémon fainted are tracked forward per save from this build's battle events;
  historical totals are not guessed.
- Battle Arts, Dramaless Shape, Dramatic Shape, and resolved sprite support.

## Settings

`BATTLE UI` and `POKÉMON MENU` now directly enable or disable the standalone
Colosseum presentations. There is no second Gen 3 theme selector in this mod.
`COLOSSEUM ICONS` switches between supplied portraits and the normal resolved
sprite source. `MENU INTRO` enables or disables the title reveal and its
continuous title/menu music session. Every other mature screen, accessibility,
text, scaling, border, mobile, and compatibility toggle is retained.

Settings are stored under `colosseum_ui_overhaul`; they do not read or overwrite
the donor mod's `gen3_battle_ui` option bucket.

## Unified presentation system

All enabled UI families now pass through the standalone Colosseum material
adapter. It replaces the donor project's cream paper, brown/gold trim, black
selection rows, and dark text with translucent black-teal hanging panels,
steel/cyan structure, red-orange focus framing, and light text. Full-screen
donor backplates are suppressed so the live scene remains visible around the
panels. Texture draws remain untinted, so portraits, item art, maps, and sprite
mods preserve their colors.

The existing mature state adapters remain the architectural base, but their
presentation is explicitly transitional. Party, PokéDex, Status, PC storage,
and Trainer Card are purpose-built Colosseum surfaces. Every remaining
screen is tracked in `NATIVE_SCREEN_SPEC.md` and must be replaced by a native
Colosseum surface while retaining only its engine-facing functional adapter.

## Design rules

- Presentation belongs to this mod; gameplay and state transitions belong to
  Gen1Recomp.
- Existing features are carried forward before their surfaces are reskinned.
- Unsupported or incomplete states fail softly to a complete native renderer.
- Colosseum artwork is optional; resolved sprite mods remain supported.
- Menus hang over the live underlying scene and must not capture a still frame.
- The original Gen 3 project remains a separate, untouched release line.

## Package contents

- `manifest.json`
- `main.lua`
- `assets/`
- `README.md`
- `ARCHITECTURE.md`
- `GOLD_COMPATIBILITY.md`
- `CHANGELOG.md`
- `NATIVE_SCREEN_SPEC.md`

## Portrait asset provenance

The #001-#251 normal and shiny 44x44 menu portraits are Pokémon Colosseum game
sprites obtained from the Bulbagarden Archives Colosseum menu-sprite catalogs.
They are included for non-commercial fan-mod use under the archive's game-sprite
fair-use notices:

- https://archives.bulbagarden.net/wiki/Category:Colosseum_menu_sprites
- https://archives.bulbagarden.net/wiki/Category:Colosseum_Shiny_menu_sprites

# 1.1.0

Compatibility and full-flow UI release.

- Reworked UI ownership around the current Gen1Recomp API so Colosseum presentation remains authoritative while camera, voxel, model, animation, and effects mods retain control of their own rendering layers.
- Added compatibility-focused ordering and suppression behavior for StadiumBattleFX, Battle Cinematics, Dramatic Shape, Dramaless Shape, Battle Art voxel renderers, potato_voxel, and other renderer stacks without making them hard dependencies.
- Strengthened native battle HUD/text suppression so legacy HP/status chrome and bottom battle UI do not reappear when other mods replace battle draw methods.
- Added the independent **BATTLE PORTRAITS** option, allowing battle portrait pods to be hidden without affecting HP/status boxes or Colosseum portraits elsewhere.
- Restored Colosseum portrait loading under the API-v2 asset sandbox and retained all 530 packaged normal/shiny portrait assets.
- Expanded strict presentation ownership for previously uncovered child flows and uncommon native menus while preserving native callbacks, input, saves, inventory, battle logic, and script progression.
- Completed Gen I PP/item-target presentation work so move-targeting item flows remain inside the custom Party/Move presentation.
- Completed Gen II PokéMart parity: compact hanging BUY, custom Bag-backed SELL, hanging quantity/confirmation surfaces, and dedicated cleaned item-description cards.
- Normalized Gen II cartridge item-description control text so `<NEXT>`, narrow-screen word breaks, and `(HOLD)` metadata no longer leak into the modern UI.
- Fixed Gen II dialogue ownership regression introduced during compatibility-firewall work, preserving the existing themed TextBox/ChoiceBox flow.
- Fixed Gen II PC/menu opacity timing and the new-game NamePick cursor mapping while keeping native state/input ownership intact.
- Retained the Gen I 4x dialogue-strobe/photosensitivity fix from 1.0.8.
- Removed obsolete broad battle draw monkey-patches in favor of narrower API-v2 visibility/ownership hooks and renderer-specific compatibility adapters.
- Performed a final non-functional source cleanup and release metadata normalization without changing approved gameplay/UI behavior.

# 1.0.0

First public release of the standalone Colosseum Inspired UI Overhaul.

## Highlights

- Unified Colosseum-inspired presentation across supported Gen I and Gen II screens while preserving native gameplay, state transitions, saves, callbacks, and input ownership.
- Cross-generation battle HUDs, command and move panels, dialogue, prompts, level-up presentation, Safari support, trainer switches, and mobile battle layouts.
- Purpose-built Party, Pokémon Status/Summary, Pokédex, PC/storage, Bag, Mart, Start, Save, Options, Mods, Trainer Card/Player Data, Pokégear, naming, evolution, and area-banner presentation.
- Authentic normal and shiny Pokémon Colosseum menu portraits for species #001–#251, with an option to use the active resolved sprite package instead.
- Presentation-only compatibility with Battle Arts, Dramatic Shape, Dramaless Shape, external sprite packages, and native Gen1Recomp systems.
- Native starter selection and nickname handoffs in both generations, including the shared hanging naming interface and mobile-safe choice layouts.
- Optional **MENU INTRO** with a one-time Poké Ball reveal and finalized Colosseum title audio. The track begins from the approved one-second-trimmed asset, remains uninterrupted through title/main-menu/options navigation, and stops only when New Game or Continue enters gameplay.
- Cross-generation location banners, evolution and egg-hatch staging, Move Manager integration, TM/HM compatibility views, and expanded presentation adapters for special flows.

## Release cleanup

- Normalized package and manifest versioning to `1.0.0`.
- Removed pre-release and obsolete title-timing labels from the runtime and public documentation.
- Consolidated pre-release notes into this release changelog.
- Verified runtime reference integrity, JSON validity, archive contents, portrait assets, title-audio decoding/duration, and SHA-256 integrity before packaging.

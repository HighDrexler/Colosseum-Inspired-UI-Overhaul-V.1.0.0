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

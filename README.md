# Colosseum Inspired UI Overhaul — 1.0.0

A presentation-focused **Gen1Recomp** mod that gives Gen I and Gen II a unified interface inspired by Pokémon Colosseum while leaving native gameplay logic authoritative.

## Highlights

- Colosseum-style battle HUD, command grid, move grid, prompts, dialogue, and level-up presentation.
- Unified hanging Party, Summary, Bag, START, PC, Pokédex, Mart, Trainer Card, Save, Options, Mods, and Pokégear interfaces.
- Gen I and Gen II support through one standalone mod.
- Optional authentic normal and Shiny Colosseum menu portraits for Pokémon #001–#251.
- Respects the active Battle Arts, Crystal, Dramatic Shape, Dramaless Shape, and resolved sprite source.
- Presentation-only architecture: native state transitions, battle rules, save data, callbacks, and user sprite settings remain in control.
- Optional **MENU INTRO** with a vector Poké Ball reveal and continuous Colosseum title music through the title/main-menu session.

## Installation

1. Download `Colosseum-Inspired-UI-Overhaul-1.0.0.zip` from the repository release.
2. Place the ZIP in the Gen1Recomp mods folder.
3. Enable **Colosseum Inspired UI Overhaul** in the mod manager.
4. Do not enable the separate Gen 3 Inspired UI Overhaul at the same time; both modify the same UI hooks.

## Settings

The in-game UI settings include independent toggles for the battle UI, Pokémon menu, Colosseum icons, menu intro, mobile presentation, text/scaling options, and compatibility behavior. Settings are stored under `colosseum_ui_overhaul` and do not overwrite the Gen 3 UI mod's option bucket.

## Design rules

- Presentation belongs to this mod; gameplay belongs to Gen1Recomp.
- Menus remain floating overlays over the live scene where supported.
- Resolved player and Pokémon sprite sources must be preserved.
- Unsupported states fail softly to the complete native renderer.
- Gen I and Gen II should share presentation while retaining generation-specific data and callbacks.

## Documentation

- [Architecture](ARCHITECTURE.md)
- [Gen II compatibility](GOLD_COMPATIBILITY.md)
- [Native screen specification](NATIVE_SCREEN_SPEC.md)
- [Changelog](CHANGELOG.md)
- [Contributing](CONTRIBUTING.md)
- [Security](SECURITY.md)

## Asset provenance

The included #001–#251 normal and Shiny menu portraits are Pokémon Colosseum game sprites obtained from the Bulbagarden Archives Colosseum menu-sprite catalogs for non-commercial fan-mod use:

- https://archives.bulbagarden.net/wiki/Category:Colosseum_menu_sprites
- https://archives.bulbagarden.net/wiki/Category:Colosseum_Shiny_menu_sprites

Pokémon and Pokémon Colosseum are trademarks of Nintendo, Creatures Inc., and GAME FREAK. This is an unofficial, non-commercial fan project.
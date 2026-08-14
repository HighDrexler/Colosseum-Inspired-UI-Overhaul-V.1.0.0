# Native Colosseum screen contract

## Non-negotiable boundary

The Gen 3 Inspired UI project may be consulted to discover engine state,
callbacks, and edge cases. Its screen layouts, presentation flow, panel
composition, and visual hierarchy are not the target implementation.

Each feature below requires two deliberately separate layers:

1. A thin passthrough adapter that reads and invokes the engine-owned state.
2. A purpose-built Colosseum screen that renders that state without donor UI.

No custom screen may replace gameplay rules, mutate inventory independently,
reimplement battle resolution, or synthesize unavailable save statistics.

## Shared screen grammar

- Hanging over the live battle or overworld; no screenshot cache.
- Near-opaque individual PDA/glass panels; no full-screen donor backplate.
- Steel chassis, dark green/teal display glass, cyan/green information accents,
  and red-orange focus.
- Left navigation/action rail, primary information surface, persistent help
  strip, and stable A/B/Left/Right affordances where relevant.
- Every child flow gets a named screen rather than being painted as an ad-hoc
  popup over an unrelated parent layout.
- Native engine update/input/callback ownership remains intact.

## Screen inventory

| Family | Native Colosseum surface required | Passthrough responsibilities | Status |
|---|---|---|---|
| Battle | HUD, command, move select, target/select, messages, choices, switch prompt, level-up | Commands, targeting, move execution, battle state | Custom surface present; contract review pending |
| Party | Browse, action rail, switch/reorder, item target, evolution target, TM/HM target, move-learning target | Party index, submenu callbacks, item/TM use, switching | Native Party surface; action rail fixed |
| Pokémon Info | Profile, stats, moves, move detail, learn/replace, egg state | Summary paging, party cycling, move callbacks | Native Status page present; remaining pages under review |
| Bag/Pack | Pocket browse, item actions, quantity, toss, give, use, key items, TM/HM | Inventory, counts, callbacks, restrictions | Native surface present for the standalone field Bag (battle item-select and Pokémon-menu item-target included); Mart sell-list and PC item-PC embedded views still use the compatibility PACK panel |
| Mart | Welcome/action, buy list, sell list, quantity, confirmation, insufficient funds/full bag | Shop stock, price, money, inventory mutation | Compatibility surface; native rewrite required |
| PC root | Owner select, deposit/withdraw flows, item PC | PC callbacks and state | Compatibility surface; native rewrite required |
| Storage | Box browse, party/box focus, move, deposit, withdraw, release, stats, box change | Box data and mutation callbacks | Compatibility surface; native rewrite required |
| Pokédex | Encounter list, Strategy Memo dossier, habitat/area, cry, unknown/seen/caught states | Pokédex flags, species data, cry/map callbacks | Native Strategy Memo foundation present |
| Start/PDA | Root menu, UI settings, confirmations | Start actions and state launch | Compatibility surface; native rewrite required |
| Trainer record | Profile, records, Johto/Kanto badges, help strip | Native card pages, exposed save counters, per-save forward counters | Native record foundation present |
| Pokégear | Map, phone, radio, clock, Fly handoff | Native card/page/navigation callbacks | Compatibility surface; native rewrite required |
| Save | Save prompt, saving, success/failure, overwrite confirmation | Native serialization and results | Compatibility surface; native rewrite required |
| Options/Mods | Options, mod list, profiles, errors, confirmations | Native setting/mod callbacks | Compatibility surface; native rewrite required |
| Dialogue | Basic text, choice, yes/no, notifications, battle learning dialogue | Text lifecycle, choice callbacks, advance timing | Compatibility surface; native rewrite required |
| Naming | Player, rival, Pokémon naming, keyboard pages | Native text entry and validation | Native hanging name-entry surface present with mobile-safe layout |
| Link/special | Link battle/trade-safe fallback, Hall of Fame, credits and unsupported states | Engine lifecycle and safe fallback | Inventory/audit required |

## Career-stat policy

The Trainer PDA probes documented/native save fields for Pokémon caught,
battles won, Pokémon fainted, league clears, badges, play time, money, and ID.
It displays `--` when a lifetime value is not exposed. It must never infer a
lifetime count from the current party, current box occupancy, or current battle.

## Completion gate

A family is complete only when every row/child flow has a named Colosseum
surface in both Gen 1 and Gen 2 where the engine exposes that feature, plus a
tested native fallback for unsupported or link-sensitive states.

# Pokémon Gold compatibility

The standalone package targets both `gen1` and `gen2` through manifest API 2.

## Colosseum-native Gold surfaces

- Battle HUD, command/move presentation, messages, and prompts.
- Two-column Party presentation and natural grid navigation.
- Live overworld or battle beneath Party and child flows.
- Pokémon Info/Summary and Move Manager.
- Shared Colosseum portrait setting.
- Shared dialogue and choice presentation.
- Direct STATUS / MOVES / PROFILE Summary navigation.
- Held-item GIVE/TAKE and nested Pack selection.
- PC access, root, boxes, deposit/withdraw, inspector, action, and Item-PC surfaces shared directly with Gen I; the inspector exposes both Gen II Special stats independently.
- Evolution, egg hatch, naming, mail, daycare, bank, elevator, decoration, prizes, contest, move deletion, trade, photo, Hall of Fame, and setup prompts.

## Additional themed Gold surfaces

- START and UI settings.
- Pack/Bag and item targeting.
- Pokémon PC and service prompts.
- Pokédex shell and native-backed special views.
- Mart, Save, Options, Mods, Trainer Card, and Pokégear adapters.

These screens retain their proven state adapters and native actions, but their rendered materials use the same Colosseum glass/steel/green system as battle, Party, and Summary.

## Native ownership and fallbacks

Gold battle state is normalized only for drawing. Gold retains battle logic, message timing, input, Party submenus, switching, item use, move learning, Move Manager actions, Pokégear behavior, and progression. The Pokégear Map/Fly views continue to use their complete native renderer where recreating only the chrome would hide cursor or landmark state.

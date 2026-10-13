<!-- dsfp:unavailable — design_fingerprint times out on this file (~6.3k icon components). Regenerate this kit after any DS change. -->
# Pos — design kit

> MACHINE-GENERATED snapshot of Figma file **Pos**, page **Design system**, taken 2026-10-13 via Reqwise Figma MCP.
> Do not hand-edit — regenerate. Human intent belongs in `design.md`.
> Draw by NAME (tokens, text styles) and by VARIANT ID (components). Ids are stable inside this file but change if a component is deleted and recreated.

## How to draw with this kit (free edition)

```js
// 1. Instance of an exact variant (free edition has no instantiate(props) — pick the variant id from the tables below)
const btn = await figma.create({ type: "INSTANCE", componentId: "1544:12321", parentId: frame.id });
// 2. Change its label: find the TEXT layer by name inside the instance, then setText
const t = (await figma.searchNodes({ query: "Label", nodeId: btn.id, types: ["TEXT"] })).nodes[0];
await figma.setText(t.id, "Lưu");
// 3. Colours / numbers bind to variables by name; text uses text styles
await figma.create({ type: "TEXT", parentId: frame.id, characters: "Tiêu đề", textStyle: "heading/h5", fill: "$text-primary" });
await figma.create({ type: "FRAME", parentId: page, fill: "$bg-surface", tokens: { cornerRadius: "radius-md", padding: "spacing-md" } });
```

Icon: `getChildren(<icon set id>)` → pick the child named `Property 1=linear` (or bold/outline/twotone/bulk/broken) → create an INSTANCE of it.

## Tokens

Four live collections. **Use `Pos Design Tokens` for drawing** — it is the compact, resolved set. `Color 2` is the primitive palette; `Color 1` / `Color 3` are semantic state tokens that alias an external library.

### Pos Design Tokens (preferred)

| Token | Value | | Token | Value |
|---|---|---|---|---|
| `bg-base` | #f7f7f7 | | `bg-surface` | #ffffff |
| `text-primary` | #333333 | | `text-secondary` | #545454 |
| `text-muted` | #8a8a8a | | `border` | #ebebeb |
| `primary` | #0074bd | | `secondary` | #e65100 |
| `success` | #13c05d | | `warning` | #f08d14 |
| `error` | #eb5146 | | `font-primary` | Poppins |
| `radius-sm` | 4 | | `radius-md` | 8 |
| `radius-lg` | 12 | | `radius-pill` | 100 |
| `spacing-xs` | 4 | | `spacing-sm` | 8 |
| `spacing-md` | 16 | | `spacing-lg` | 24 |
| `spacing-xl` | 32 | | `text-h1` | 64 |
| `text-h2` | 48 | | `text-h3` | 40 |
| `text-h4` | 36 | | `text-h5` | 24 |
| `text-h6` | 20 | | `text-title-lg` | 16 |
| `text-title-md` | 14 | | `text-title-sm` | 12 |
| `text-title-xs` | 10 | | `text-body-xl` | 18 |
| `text-body-lg` | 16 | | `text-body-md` | 14 |
| `text-body-sm` | 12 | |  |  |

### Color 2 — primitive palette

Ramps `100…900` (`500-main` is the base): **Brand** (`Brand/500-main` #0074bd, 50 #e6f1f8 … 900 #00314f), **Neutral** (`Neutral/50` #fafafa … `Neutral/950` #0c0d0e, step 50), Blue #3355ff, Purple #7733ff, Violet #bb33ff, Red #e50000, Pink #ff3355, Orange #ff8000, Yellow #ffcc00, Green #009933, Teal #00cccc, Cyan #00aaff; plus `Primary/Black|White` (+50/20 alpha variants).

### Color 1 / Color 3 — semantic state tokens

Pattern: `<Layer>/<Intent>/<Level>/<State>` where
- Layer: `Content (Text + Icon)` · `Border (Strock)` · `Background (Frame +Shape)` · `Effect (Shadow)`
- Intent: `Neutral` · `Brand` · `Info` · `Positive` · `Warning` · `Errow` (sic) / `Errow/Negative` (background)
- Level: `Primary` · `Secondary` · `Tertiary` · `Inverse` · `Base|Raised|Overlay|Sunken|Alternate` (neutral backgrounds) · `Sub_State`
- State: `Enabled|Default` · `Hover` · `Pressed` · `Selected` · `Focus` · `Disabled` · `Loading (Progressing)`

They alias variables of an external library, so values resolve only while that library is enabled. Typos are part of the real names — write them exactly (`Errow`, `Strock`, `Fouced`).

### Not to use
- `Variable collection` (`primary-color` = #000000, `Number…`) — leftover, not part of the system.

## Text styles (Poppins)

| Style | Size / line-height | Weight |
|---|---|---|
| `heading/h1` | 64 / 120% | SemiBold |
| `heading/h2` | 48 / 150% | SemiBold |
| `heading/h3` | 40 / 150% | SemiBold |
| `heading/h4` | 36 / 150% | SemiBold |
| `heading/h5` | 24 / 150% | SemiBold |
| `heading/h6` | 20 / 150% | SemiBold |
| `title/lg` | 16 / 24 | SemiBold |
| `title/md` | 14 / 20 | SemiBold |
| `title/sm` | 12 / 16 | SemiBold |
| `body/xl-bold · body/xl-regular` | 18 / 26 | Bold · Regular |
| `body/lg-bold · body/lg-regular` | 16 / 24 | Bold · Regular |
| `body/md-bold · body/md-semibold · body/md-regular` | 14 / 20 | Bold · SemiBold · Regular |
| `body/sm-bold · body/sm-semibold · body/sm-regular` | 12 / 18 | Bold · SemiBold · Regular |

The Typography board also documents an 18px `Heading 7` and a 10px `Title/xs` that have **no text style** — use `text-title-xs` / `text-body-xl` tokens if needed. No paint styles or effect styles exist; shadows live in `Effect (Shadow)` variables.

## Components

45 component sets read from 19 boards on the Design system page.

### Known problems
- Component text was switched from `San Francisco Display` to **Poppins** (same weight) on 2026-10-13 — 824 text layers, incl. overrides on nested library instances. All 45 sets instantiate on Windows. Component text is NOT bound to the text styles yet (font only), so changing a text style does not update components.
- Sidebar sets `Submenu`, `Menu\`, `Side bar Component (Use This)` still use **Nunito** (7 layers) — installed, works, but off-brand.
- **`Component 1` (Input text field, 1544:58725) is BROKEN**: Figma reports "Component set has existing errors" — the 8 `Type=Trailing dropdown` variants exist twice with identical names. Rename/delete the duplicates and give the set a real name (e.g. `Input`). Until then, use the variant ids listed below directly.
- Generic names: `Component 1`, `Menu\`, `Day1...`, two sets called `File`. Rename before relying on names.
- Board names do not always match content: board "Toggle" (1544:59638) holds `Scroll bar`; the real `Toggle` is on board 1544:60167.

### Button  `1544:12320`

Board: Button A · key `2faf9a68248393cb38cb2f5fc8e4981a49e7280b` · default variant `1544:12321` · radius 5

- Variants: **Type** = CTA / Destructive; **Size** = Large / Medium / Small / XSmall; **Hierarchy** = Primary / Secondary / Tertiary / Alternative Tertiary; **State** = Default / Hover / Press / Disable; **Icon Only** = No / Yes
- Properties: `Swap Leading Icon#136:0` (INSTANCE_SWAP), `Swap Trailing Icon#136:73` (INSTANCE_SWAP), `Show Trailing Icon#136:146` (BOOLEAN, default true), `Show Leading Icon#136:219` (BOOLEAN, default true), `Swap Icon#136:292` (INSTANCE_SWAP), `Button Label#7527:4` (TEXT, default "Button")
- Text layers (default variant): `Label="Button"`

<details><summary>224 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Type=CTA, Size=Large, Hierarchy=Primary, State=Default, Icon Only=No | `1544:12321` | 240×40 |
| Type=CTA, Size=Medium, Hierarchy=Primary, State=Default, Icon Only=No | `1544:12325` | 240×40 |
| Type=CTA, Size=Small, Hierarchy=Primary, State=Default, Icon Only=No | `1544:12329` | 160×32 |
| Type=CTA, Size=XSmall, Hierarchy=Primary, State=Default, Icon Only=No | `1544:12333` | 100×24 |
| Type=CTA, Size=Large, Hierarchy=Primary, State=Default, Icon Only=Yes | `1544:12337` | 44×44 |
| Type=CTA, Size=Medium, Hierarchy=Primary, State=Default, Icon Only=Yes | `1544:12339` | 40×40 |
| Type=CTA, Size=Small, Hierarchy=Primary, State=Default, Icon Only=Yes | `1544:12341` | 32×32 |
| Type=CTA, Size=XSmall, Hierarchy=Primary, State=Default, Icon Only=Yes | `1544:12343` | 24×24 |
| Type=CTA, Size=Large, Hierarchy=Secondary, State=Default, Icon Only=Yes | `1544:12345` | 48×44 |
| Type=CTA, Size=Medium, Hierarchy=Secondary, State=Default, Icon Only=Yes | `1544:12347` | 40×40 |
| Type=CTA, Size=Small, Hierarchy=Secondary, State=Default, Icon Only=Yes | `1544:12349` | 32×32 |
| Type=CTA, Size=XSmall, Hierarchy=Secondary, State=Default, Icon Only=Yes | `1544:12351` | 24×24 |
| Type=CTA, Size=Large, Hierarchy=Tertiary, State=Default, Icon Only=Yes | `1544:12353` | 48×44 |
| Type=CTA, Size=Large, Hierarchy=Alternative Tertiary, State=Default, Icon Only=Yes | `1544:12355` | 44×44 |
| Type=CTA, Size=Medium, Hierarchy=Tertiary, State=Default, Icon Only=Yes | `1544:12357` | 40×40 |
| Type=CTA, Size=Medium, Hierarchy=Alternative Tertiary, State=Default, Icon Only=Yes | `1544:12359` | 40×40 |
| Type=CTA, Size=Small, Hierarchy=Tertiary, State=Default, Icon Only=Yes | `1544:12361` | 32×32 |
| Type=CTA, Size=Small, Hierarchy=Alternative Tertiary, State=Default, Icon Only=Yes | `1544:12363` | 32×32 |
| Type=CTA, Size=XSmall, Hierarchy=Tertiary, State=Default, Icon Only=Yes | `1544:12365` | 24×24 |
| Type=CTA, Size=XSmall, Hierarchy=Alternative Tertiary, State=Default, Icon Only=Yes | `1544:12367` | 24×24 |
| Type=CTA, Size=Large, Hierarchy=Secondary, State=Default, Icon Only=No | `1544:12369` | 240×40 |
| Type=CTA, Size=Medium, Hierarchy=Secondary, State=Default, Icon Only=No | `1544:12373` | 240×40 |
| Type=CTA, Size=Small, Hierarchy=Secondary, State=Default, Icon Only=No | `1544:12377` | 160×32 |
| Type=CTA, Size=XSmall, Hierarchy=Secondary, State=Default, Icon Only=No | `1544:12381` | 100×24 |
| Type=CTA, Size=Large, Hierarchy=Tertiary, State=Default, Icon Only=No | `1544:12385` | 240×40 |
| Type=CTA, Size=Large, Hierarchy=Alternative Tertiary, State=Default, Icon Only=No | `1544:12389` | 240×40 |
| Type=CTA, Size=Medium, Hierarchy=Tertiary, State=Default, Icon Only=No | `1544:12393` | 240×40 |
| Type=CTA, Size=Medium, Hierarchy=Alternative Tertiary, State=Default, Icon Only=No | `1544:12397` | 240×40 |
| Type=CTA, Size=Small, Hierarchy=Tertiary, State=Default, Icon Only=No | `1544:12401` | 160×32 |
| Type=CTA, Size=Small, Hierarchy=Alternative Tertiary, State=Default, Icon Only=No | `1544:12405` | 160×32 |
| Type=CTA, Size=XSmall, Hierarchy=Tertiary, State=Default, Icon Only=No | `1544:12409` | 100×24 |
| Type=CTA, Size=XSmall, Hierarchy=Alternative Tertiary, State=Default, Icon Only=No | `1544:12413` | 100×24 |
| Type=CTA, Size=Large, Hierarchy=Primary, State=Hover, Icon Only=No | `1544:12417` | 240×40 |
| Type=CTA, Size=Medium, Hierarchy=Primary, State=Hover, Icon Only=No | `1544:12421` | 240×40 |
| Type=CTA, Size=Small, Hierarchy=Primary, State=Hover, Icon Only=No | `1544:12425` | 160×32 |
| Type=CTA, Size=XSmall, Hierarchy=Primary, State=Hover, Icon Only=No | `1544:12429` | 100×24 |
| Type=CTA, Size=Large, Hierarchy=Primary, State=Hover, Icon Only=Yes | `1544:12433` | 44×44 |
| Type=CTA, Size=Medium, Hierarchy=Primary, State=Hover, Icon Only=Yes | `1544:12435` | 40×40 |
| Type=CTA, Size=Small, Hierarchy=Primary, State=Hover, Icon Only=Yes | `1544:12437` | 32×32 |
| Type=CTA, Size=XSmall, Hierarchy=Primary, State=Hover, Icon Only=Yes | `1544:12439` | 24×24 |
| Type=CTA, Size=Large, Hierarchy=Secondary, State=Hover, Icon Only=Yes | `1544:12441` | 48×44 |
| Type=CTA, Size=Medium, Hierarchy=Secondary, State=Hover, Icon Only=Yes | `1544:12443` | 40×40 |
| Type=CTA, Size=Small, Hierarchy=Secondary, State=Hover, Icon Only=Yes | `1544:12445` | 32×32 |
| Type=CTA, Size=XSmall, Hierarchy=Secondary, State=Hover, Icon Only=Yes | `1544:12447` | 24×24 |
| Type=CTA, Size=Large, Hierarchy=Tertiary, State=Hover, Icon Only=Yes | `1544:12449` | 48×44 |
| Type=CTA, Size=Large, Hierarchy=Alternative Tertiary, State=Hover, Icon Only=Yes | `1544:12451` | 48×44 |
| Type=CTA, Size=Medium, Hierarchy=Tertiary, State=Hover, Icon Only=Yes | `1544:12453` | 40×40 |
| Type=CTA, Size=Medium, Hierarchy=Alternative Tertiary, State=Hover, Icon Only=Yes | `1544:12455` | 40×40 |
| Type=CTA, Size=Small, Hierarchy=Tertiary, State=Hover, Icon Only=Yes | `1544:12457` | 32×32 |
| Type=CTA, Size=Small, Hierarchy=Alternative Tertiary, State=Hover, Icon Only=Yes | `1544:12459` | 32×32 |
| Type=CTA, Size=XSmall, Hierarchy=Tertiary, State=Hover, Icon Only=Yes | `1544:12461` | 24×24 |
| Type=CTA, Size=XSmall, Hierarchy=Alternative Tertiary, State=Hover, Icon Only=Yes | `1544:12463` | 24×24 |
| Type=CTA, Size=Large, Hierarchy=Secondary, State=Hover, Icon Only=No | `1544:12465` | 240×40 |
| Type=CTA, Size=Medium, Hierarchy=Secondary, State=Hover, Icon Only=No | `1544:12469` | 240×40 |
| Type=CTA, Size=Small, Hierarchy=Secondary, State=Hover, Icon Only=No | `1544:12473` | 160×32 |
| Type=CTA, Size=XSmall, Hierarchy=Secondary, State=Hover, Icon Only=No | `1544:12477` | 100×24 |
| Type=CTA, Size=Large, Hierarchy=Tertiary, State=Hover, Icon Only=No | `1544:12481` | 240×40 |
| Type=CTA, Size=Large, Hierarchy=Alternative Tertiary, State=Hover, Icon Only=No | `1544:12485` | 240×40 |
| Type=CTA, Size=Medium, Hierarchy=Tertiary, State=Hover, Icon Only=No | `1544:12489` | 240×40 |
| Type=CTA, Size=Medium, Hierarchy=Alternative Tertiary, State=Hover, Icon Only=No | `1544:12493` | 240×40 |
| Type=CTA, Size=Small, Hierarchy=Tertiary, State=Hover, Icon Only=No | `1544:12497` | 160×32 |
| Type=CTA, Size=Small, Hierarchy=Alternative Tertiary, State=Hover, Icon Only=No | `1544:12501` | 160×32 |
| Type=CTA, Size=XSmall, Hierarchy=Tertiary, State=Hover, Icon Only=No | `1544:12505` | 100×24 |
| Type=CTA, Size=XSmall, Hierarchy=Alternative Tertiary, State=Hover, Icon Only=No | `1544:12509` | 100×24 |
| Type=CTA, Size=Large, Hierarchy=Primary, State=Press, Icon Only=No | `1544:12513` | 240×40 |
| Type=CTA, Size=Medium, Hierarchy=Primary, State=Press, Icon Only=No | `1544:12517` | 240×40 |
| Type=CTA, Size=Small, Hierarchy=Primary, State=Press, Icon Only=No | `1544:12521` | 160×32 |
| Type=CTA, Size=XSmall, Hierarchy=Primary, State=Press, Icon Only=No | `1544:12525` | 100×24 |
| Type=CTA, Size=Large, Hierarchy=Primary, State=Press, Icon Only=Yes | `1544:12529` | 44×44 |
| Type=CTA, Size=Medium, Hierarchy=Primary, State=Press, Icon Only=Yes | `1544:12531` | 40×40 |
| Type=CTA, Size=Small, Hierarchy=Primary, State=Press, Icon Only=Yes | `1544:12533` | 32×32 |
| Type=CTA, Size=XSmall, Hierarchy=Primary, State=Press, Icon Only=Yes | `1544:12535` | 24×24 |
| Type=CTA, Size=Large, Hierarchy=Secondary, State=Press, Icon Only=Yes | `1544:12537` | 48×44 |
| Type=CTA, Size=Medium, Hierarchy=Secondary, State=Press, Icon Only=Yes | `1544:12539` | 40×40 |
| Type=CTA, Size=Small, Hierarchy=Secondary, State=Press, Icon Only=Yes | `1544:12541` | 32×32 |
| Type=CTA, Size=XSmall, Hierarchy=Secondary, State=Press, Icon Only=Yes | `1544:12543` | 24×24 |
| Type=CTA, Size=Large, Hierarchy=Tertiary, State=Press, Icon Only=Yes | `1544:12545` | 48×44 |
| Type=CTA, Size=Large, Hierarchy=Alternative Tertiary, State=Press, Icon Only=Yes | `1544:12547` | 48×44 |
| Type=CTA, Size=Medium, Hierarchy=Tertiary, State=Press, Icon Only=Yes | `1544:12549` | 40×40 |
| Type=CTA, Size=Medium, Hierarchy=Alternative Tertiary, State=Press, Icon Only=Yes | `1544:12551` | 40×40 |
| Type=CTA, Size=Small, Hierarchy=Tertiary, State=Press, Icon Only=Yes | `1544:12553` | 32×32 |
| Type=CTA, Size=Small, Hierarchy=Alternative Tertiary, State=Press, Icon Only=Yes | `1544:12555` | 32×32 |
| Type=CTA, Size=XSmall, Hierarchy=Tertiary, State=Press, Icon Only=Yes | `1544:12557` | 24×24 |
| Type=CTA, Size=XSmall, Hierarchy=Alternative Tertiary, State=Press, Icon Only=Yes | `1544:12559` | 24×24 |
| Type=CTA, Size=Large, Hierarchy=Secondary, State=Press, Icon Only=No | `1544:12561` | 240×40 |
| Type=CTA, Size=Medium, Hierarchy=Secondary, State=Press, Icon Only=No | `1544:12565` | 240×40 |
| Type=CTA, Size=Small, Hierarchy=Secondary, State=Press, Icon Only=No | `1544:12569` | 160×32 |
| Type=CTA, Size=XSmall, Hierarchy=Secondary, State=Press, Icon Only=No | `1544:12573` | 100×24 |
| Type=CTA, Size=Large, Hierarchy=Tertiary, State=Press, Icon Only=No | `1544:12577` | 240×40 |
| Type=CTA, Size=Large, Hierarchy=Alternative Tertiary, State=Press, Icon Only=No | `1544:12581` | 240×40 |
| Type=CTA, Size=Medium, Hierarchy=Tertiary, State=Press, Icon Only=No | `1544:12585` | 240×40 |
| Type=CTA, Size=Medium, Hierarchy=Alternative Tertiary, State=Press, Icon Only=No | `1544:12589` | 240×40 |
| Type=CTA, Size=Small, Hierarchy=Tertiary, State=Press, Icon Only=No | `1544:12593` | 160×32 |
| Type=CTA, Size=Small, Hierarchy=Alternative Tertiary, State=Press, Icon Only=No | `1544:12597` | 160×32 |
| Type=CTA, Size=XSmall, Hierarchy=Tertiary, State=Press, Icon Only=No | `1544:12601` | 100×24 |
| Type=CTA, Size=XSmall, Hierarchy=Alternative Tertiary, State=Press, Icon Only=No | `1544:12605` | 100×24 |
| Type=CTA, Size=Large, Hierarchy=Primary, State=Disable, Icon Only=No | `1544:12609` | 240×40 |
| Type=CTA, Size=Medium, Hierarchy=Primary, State=Disable, Icon Only=No | `1544:12613` | 240×40 |
| Type=CTA, Size=Small, Hierarchy=Primary, State=Disable, Icon Only=No | `1544:12617` | 160×32 |
| Type=CTA, Size=XSmall, Hierarchy=Primary, State=Disable, Icon Only=No | `1544:12621` | 100×24 |
| Type=CTA, Size=Large, Hierarchy=Primary, State=Disable, Icon Only=Yes | `1544:12625` | 44×44 |
| Type=CTA, Size=Medium, Hierarchy=Primary, State=Disable, Icon Only=Yes | `1544:12627` | 40×40 |
| Type=CTA, Size=Small, Hierarchy=Primary, State=Disable, Icon Only=Yes | `1544:12629` | 32×32 |
| Type=CTA, Size=XSmall, Hierarchy=Primary, State=Disable, Icon Only=Yes | `1544:12631` | 24×24 |
| Type=CTA, Size=Large, Hierarchy=Secondary, State=Disable, Icon Only=Yes | `1544:12633` | 48×44 |
| Type=CTA, Size=Medium, Hierarchy=Secondary, State=Disable, Icon Only=Yes | `1544:12635` | 40×40 |
| Type=CTA, Size=Small, Hierarchy=Secondary, State=Disable, Icon Only=Yes | `1544:12637` | 32×32 |
| Type=CTA, Size=XSmall, Hierarchy=Secondary, State=Disable, Icon Only=Yes | `1544:12639` | 24×24 |
| Type=CTA, Size=Large, Hierarchy=Tertiary, State=Disable, Icon Only=Yes | `1544:12641` | 48×44 |
| Type=CTA, Size=Large, Hierarchy=Alternative Tertiary, State=Disable, Icon Only=Yes | `1544:12643` | 48×44 |
| Type=CTA, Size=Medium, Hierarchy=Tertiary, State=Disable, Icon Only=Yes | `1544:12645` | 40×40 |
| Type=CTA, Size=Medium, Hierarchy=Alternative Tertiary, State=Disable, Icon Only=Yes | `1544:12647` | 40×40 |
| Type=CTA, Size=Small, Hierarchy=Tertiary, State=Disable, Icon Only=Yes | `1544:12649` | 32×32 |
| Type=CTA, Size=Small, Hierarchy=Alternative Tertiary, State=Disable, Icon Only=Yes | `1544:12651` | 32×32 |
| Type=CTA, Size=XSmall, Hierarchy=Tertiary, State=Disable, Icon Only=Yes | `1544:12653` | 24×24 |
| Type=CTA, Size=XSmall, Hierarchy=Alternative Tertiary, State=Disable, Icon Only=Yes | `1544:12655` | 24×24 |
| Type=CTA, Size=Large, Hierarchy=Secondary, State=Disable, Icon Only=No | `1544:12657` | 240×40 |
| Type=CTA, Size=Medium, Hierarchy=Secondary, State=Disable, Icon Only=No | `1544:12661` | 240×40 |
| Type=CTA, Size=Small, Hierarchy=Secondary, State=Disable, Icon Only=No | `1544:12665` | 160×32 |
| Type=CTA, Size=XSmall, Hierarchy=Secondary, State=Disable, Icon Only=No | `1544:12669` | 100×24 |
| Type=CTA, Size=Large, Hierarchy=Tertiary, State=Disable, Icon Only=No | `1544:12673` | 240×40 |
| Type=CTA, Size=Large, Hierarchy=Alternative Tertiary, State=Disable, Icon Only=No | `1544:12677` | 240×40 |
| Type=CTA, Size=Medium, Hierarchy=Tertiary, State=Disable, Icon Only=No | `1544:12681` | 240×40 |
| Type=CTA, Size=Medium, Hierarchy=Alternative Tertiary, State=Disable, Icon Only=No | `1544:12685` | 240×40 |
| Type=CTA, Size=Small, Hierarchy=Tertiary, State=Disable, Icon Only=No | `1544:12689` | 160×32 |
| Type=CTA, Size=Small, Hierarchy=Alternative Tertiary, State=Disable, Icon Only=No | `1544:12693` | 160×32 |
| Type=CTA, Size=XSmall, Hierarchy=Tertiary, State=Disable, Icon Only=No | `1544:12697` | 100×24 |
| Type=CTA, Size=XSmall, Hierarchy=Alternative Tertiary, State=Disable, Icon Only=No | `1544:12701` | 100×24 |
| Type=Destructive, Size=Medium, Hierarchy=Primary, State=Default, Icon Only=No | `1544:12705` | 240×40 |
| Type=Destructive, Size=Medium, Hierarchy=Primary, State=Disable, Icon Only=No | `1544:12709` | 240×40 |
| Type=Destructive, Size=Medium, Hierarchy=Primary, State=Hover, Icon Only=No | `1544:12713` | 240×40 |
| Type=Destructive, Size=Medium, Hierarchy=Primary, State=Press, Icon Only=No | `1544:12717` | 240×40 |
| Type=Destructive, Size=Small, Hierarchy=Primary, State=Default, Icon Only=No | `1544:12721` | 160×32 |
| Type=Destructive, Size=Small, Hierarchy=Primary, State=Disable, Icon Only=No | `1544:12725` | 160×32 |
| Type=Destructive, Size=Small, Hierarchy=Primary, State=Hover, Icon Only=No | `1544:12729` | 160×32 |
| Type=Destructive, Size=Small, Hierarchy=Primary, State=Press, Icon Only=No | `1544:12733` | 160×32 |
| Type=Destructive, Size=XSmall, Hierarchy=Primary, State=Default, Icon Only=No | `1544:12737` | 100×24 |
| Type=Destructive, Size=XSmall, Hierarchy=Primary, State=Disable, Icon Only=No | `1544:12741` | 100×24 |
| Type=Destructive, Size=XSmall, Hierarchy=Primary, State=Hover, Icon Only=No | `1544:12745` | 100×24 |
| Type=Destructive, Size=XSmall, Hierarchy=Primary, State=Press, Icon Only=No | `1544:12749` | 100×24 |
| Type=Destructive, Size=Medium, Hierarchy=Primary, State=Default, Icon Only=Yes | `1544:12753` | 40×40 |
| Type=Destructive, Size=Medium, Hierarchy=Primary, State=Disable, Icon Only=Yes | `1544:12755` | 40×40 |
| Type=Destructive, Size=Medium, Hierarchy=Primary, State=Hover, Icon Only=Yes | `1544:12757` | 40×40 |
| Type=Destructive, Size=Medium, Hierarchy=Primary, State=Press, Icon Only=Yes | `1544:12759` | 40×40 |
| Type=Destructive, Size=Small, Hierarchy=Primary, State=Default, Icon Only=Yes | `1544:12761` | 32×32 |
| Type=Destructive, Size=Small, Hierarchy=Primary, State=Disable, Icon Only=Yes | `1544:12763` | 32×32 |
| Type=Destructive, Size=Small, Hierarchy=Primary, State=Hover, Icon Only=Yes | `1544:12765` | 32×32 |
| Type=Destructive, Size=Small, Hierarchy=Primary, State=Press, Icon Only=Yes | `1544:12767` | 32×32 |
| Type=Destructive, Size=XSmall, Hierarchy=Primary, State=Default, Icon Only=Yes | `1544:12769` | 24×24 |
| Type=Destructive, Size=XSmall, Hierarchy=Primary, State=Disable, Icon Only=Yes | `1544:12771` | 24×24 |
| Type=Destructive, Size=XSmall, Hierarchy=Primary, State=Hover, Icon Only=Yes | `1544:12773` | 24×24 |
| Type=Destructive, Size=XSmall, Hierarchy=Primary, State=Press, Icon Only=Yes | `1544:12775` | 24×24 |
| Type=Destructive, Size=Medium, Hierarchy=Secondary, State=Default, Icon Only=Yes | `1544:12777` | 40×40 |
| Type=Destructive, Size=Medium, Hierarchy=Secondary, State=Disable, Icon Only=Yes | `1544:12779` | 40×40 |
| Type=Destructive, Size=Medium, Hierarchy=Secondary, State=Hover, Icon Only=Yes | `1544:12781` | 40×40 |
| Type=Destructive, Size=Medium, Hierarchy=Secondary, State=Press, Icon Only=Yes | `1544:12783` | 40×40 |
| Type=Destructive, Size=Small, Hierarchy=Secondary, State=Default, Icon Only=Yes | `1544:12785` | 32×32 |
| Type=Destructive, Size=Small, Hierarchy=Secondary, State=Disable, Icon Only=Yes | `1544:12787` | 32×32 |
| Type=Destructive, Size=Small, Hierarchy=Secondary, State=Hover, Icon Only=Yes | `1544:12789` | 32×32 |
| Type=Destructive, Size=Small, Hierarchy=Secondary, State=Press, Icon Only=Yes | `1544:12791` | 32×32 |
| Type=Destructive, Size=XSmall, Hierarchy=Secondary, State=Default, Icon Only=Yes | `1544:12793` | 24×24 |
| Type=Destructive, Size=XSmall, Hierarchy=Secondary, State=Disable, Icon Only=Yes | `1544:12795` | 24×24 |
| Type=Destructive, Size=XSmall, Hierarchy=Secondary, State=Hover, Icon Only=Yes | `1544:12797` | 24×24 |
| Type=Destructive, Size=XSmall, Hierarchy=Secondary, State=Press, Icon Only=Yes | `1544:12799` | 24×24 |
| Type=Destructive, Size=Medium, Hierarchy=Tertiary, State=Default, Icon Only=Yes | `1544:12801` | 40×40 |
| Type=Destructive, Size=Medium, Hierarchy=Tertiary, State=Disable, Icon Only=Yes | `1544:12803` | 40×40 |
| Type=Destructive, Size=Medium, Hierarchy=Tertiary, State=Hover, Icon Only=Yes | `1544:12805` | 40×40 |
| Type=Destructive, Size=Medium, Hierarchy=Tertiary, State=Press, Icon Only=Yes | `1544:12807` | 40×40 |
| Type=Destructive, Size=Small, Hierarchy=Tertiary, State=Default, Icon Only=Yes | `1544:12809` | 32×32 |
| Type=Destructive, Size=Small, Hierarchy=Tertiary, State=Disable, Icon Only=Yes | `1544:12811` | 32×32 |
| Type=Destructive, Size=Small, Hierarchy=Tertiary, State=Hover, Icon Only=Yes | `1544:12813` | 32×32 |
| Type=Destructive, Size=Small, Hierarchy=Tertiary, State=Press, Icon Only=Yes | `1544:12815` | 32×32 |
| Type=Destructive, Size=XSmall, Hierarchy=Tertiary, State=Default, Icon Only=Yes | `1544:12817` | 24×24 |
| Type=Destructive, Size=XSmall, Hierarchy=Tertiary, State=Disable, Icon Only=Yes | `1544:12819` | 24×24 |
| Type=Destructive, Size=XSmall, Hierarchy=Tertiary, State=Hover, Icon Only=Yes | `1544:12821` | 24×24 |
| Type=Destructive, Size=XSmall, Hierarchy=Tertiary, State=Press, Icon Only=Yes | `1544:12823` | 24×24 |
| Type=Destructive, Size=Medium, Hierarchy=Secondary, State=Default, Icon Only=No | `1544:12825` | 240×40 |
| Type=Destructive, Size=Medium, Hierarchy=Secondary, State=Disable, Icon Only=No | `1544:12829` | 240×40 |
| Type=Destructive, Size=Medium, Hierarchy=Secondary, State=Hover, Icon Only=No | `1544:12833` | 240×40 |
| Type=Destructive, Size=Medium, Hierarchy=Secondary, State=Press, Icon Only=No | `1544:12837` | 240×40 |
| Type=Destructive, Size=Small, Hierarchy=Secondary, State=Default, Icon Only=No | `1544:12841` | 160×32 |
| Type=Destructive, Size=Small, Hierarchy=Secondary, State=Disable, Icon Only=No | `1544:12845` | 160×32 |
| Type=Destructive, Size=Small, Hierarchy=Secondary, State=Hover, Icon Only=No | `1544:12849` | 160×32 |
| Type=Destructive, Size=Small, Hierarchy=Secondary, State=Press, Icon Only=No | `1544:12853` | 160×32 |
| Type=Destructive, Size=XSmall, Hierarchy=Secondary, State=Default, Icon Only=No | `1544:12857` | 100×24 |
| Type=Destructive, Size=XSmall, Hierarchy=Secondary, State=Disable, Icon Only=No | `1544:12861` | 100×24 |
| Type=Destructive, Size=XSmall, Hierarchy=Secondary, State=Hover, Icon Only=No | `1544:12865` | 100×24 |
| Type=Destructive, Size=XSmall, Hierarchy=Secondary, State=Press, Icon Only=No | `1544:12869` | 100×24 |
| Type=Destructive, Size=Medium, Hierarchy=Tertiary, State=Default, Icon Only=No | `1544:12873` | 240×40 |
| Type=Destructive, Size=Medium, Hierarchy=Tertiary, State=Disable, Icon Only=No | `1544:12877` | 240×40 |
| Type=Destructive, Size=Medium, Hierarchy=Tertiary, State=Hover, Icon Only=No | `1544:12881` | 240×40 |
| Type=Destructive, Size=Medium, Hierarchy=Tertiary, State=Press, Icon Only=No | `1544:12885` | 240×40 |
| Type=Destructive, Size=Small, Hierarchy=Tertiary, State=Default, Icon Only=No | `1544:12889` | 160×32 |
| Type=Destructive, Size=Small, Hierarchy=Tertiary, State=Disable, Icon Only=No | `1544:12893` | 160×32 |
| Type=Destructive, Size=Small, Hierarchy=Tertiary, State=Hover, Icon Only=No | `1544:12897` | 160×32 |
| Type=Destructive, Size=Small, Hierarchy=Tertiary, State=Press, Icon Only=No | `1544:12901` | 160×32 |
| Type=Destructive, Size=XSmall, Hierarchy=Tertiary, State=Default, Icon Only=No | `1544:12905` | 100×24 |
| Type=Destructive, Size=XSmall, Hierarchy=Tertiary, State=Disable, Icon Only=No | `1544:12909` | 100×24 |
| Type=Destructive, Size=XSmall, Hierarchy=Tertiary, State=Hover, Icon Only=No | `1544:12913` | 100×24 |
| Type=Destructive, Size=XSmall, Hierarchy=Tertiary, State=Press, Icon Only=No | `1544:12917` | 100×24 |
| Type=Destructive, Size=Large, Hierarchy=Primary, State=Default, Icon Only=No | `1544:12921` | 240×40 |
| Type=Destructive, Size=Large, Hierarchy=Primary, State=Disable, Icon Only=No | `1544:12925` | 240×40 |
| Type=Destructive, Size=Large, Hierarchy=Primary, State=Hover, Icon Only=No | `1544:12929` | 240×40 |
| Type=Destructive, Size=Large, Hierarchy=Primary, State=Press, Icon Only=No | `1544:12933` | 240×40 |
| Type=Destructive, Size=Large, Hierarchy=Secondary, State=Default, Icon Only=No | `1544:12937` | 240×40 |
| Type=Destructive, Size=Large, Hierarchy=Secondary, State=Disable, Icon Only=No | `1544:12941` | 240×40 |
| Type=Destructive, Size=Large, Hierarchy=Secondary, State=Hover, Icon Only=No | `1544:12945` | 240×40 |
| Type=Destructive, Size=Large, Hierarchy=Secondary, State=Press, Icon Only=No | `1544:12949` | 240×40 |
| Type=Destructive, Size=Large, Hierarchy=Tertiary, State=Default, Icon Only=No | `1544:12953` | 240×40 |
| Type=Destructive, Size=Large, Hierarchy=Tertiary, State=Disable, Icon Only=No | `1544:12957` | 240×40 |
| Type=Destructive, Size=Large, Hierarchy=Tertiary, State=Hover, Icon Only=No | `1544:12961` | 240×40 |
| Type=Destructive, Size=Large, Hierarchy=Tertiary, State=Press, Icon Only=No | `1544:12965` | 240×40 |
| Type=Destructive, Size=Large, Hierarchy=Primary, State=Default, Icon Only=Yes | `1544:12969` | 48×44 |
| Type=Destructive, Size=Large, Hierarchy=Primary, State=Disable, Icon Only=Yes | `1544:12971` | 48×44 |
| Type=Destructive, Size=Large, Hierarchy=Primary, State=Hover, Icon Only=Yes | `1544:12973` | 48×44 |
| Type=Destructive, Size=Large, Hierarchy=Primary, State=Press, Icon Only=Yes | `1544:12975` | 48×44 |
| Type=Destructive, Size=Large, Hierarchy=Secondary, State=Default, Icon Only=Yes | `1544:12977` | 48×44 |
| Type=Destructive, Size=Large, Hierarchy=Secondary, State=Disable, Icon Only=Yes | `1544:12979` | 48×44 |
| Type=Destructive, Size=Large, Hierarchy=Secondary, State=Hover, Icon Only=Yes | `1544:12981` | 48×44 |
| Type=Destructive, Size=Large, Hierarchy=Secondary, State=Press, Icon Only=Yes | `1544:12983` | 48×44 |
| Type=Destructive, Size=Large, Hierarchy=Tertiary, State=Default, Icon Only=Yes | `1544:12985` | 48×44 |
| Type=Destructive, Size=Large, Hierarchy=Tertiary, State=Disable, Icon Only=Yes | `1544:12987` | 48×44 |
| Type=Destructive, Size=Large, Hierarchy=Tertiary, State=Hover, Icon Only=Yes | `1544:12989` | 48×44 |
| Type=Destructive, Size=Large, Hierarchy=Tertiary, State=Press, Icon Only=Yes | `1544:12991` | 48×44 |

</details>

### Button Bar  `1544:13022`

Board: Button B · key `2c303bb56f8eda6ce3a7cd323e44cf37f7bebd4f` · default variant `1544:13118` · radius 5

- Variants: **Device** = Mobile / Desktop; **Type** = 1 Button / 2 Button / 3 Button / Floating; **Direction** = None / Horizontal / Vertical / Both; **Fill Container** = No / Yes
- Properties: `Contextual Ask#7683:6` (BOOLEAN, default false), `Progress#7921:8` (BOOLEAN, default false), `Additional Text#7931:0` (BOOLEAN, default false), `Text#7931:12` (TEXT, default "Lorem ipsum dolor sit amet consectetur."), `Home Indicator#7972:0` (BOOLEAN, default true)
- Text layers (default variant): `label="Option"`, `Step 1/2="Step 1/2"`, `Text="Lorem ipsum dolor sit amet con"`, `Label="Button"`, `Label="Button"`, `Label="Button"`

<details><summary>15 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Device=Mobile, Type=3 Button, Direction=Vertical, Fill Container=Yes | `1544:13023` | 375×186 |
| Device=Mobile, Type=3 Button, Direction=Horizontal, Fill Container=Yes | `1544:13035` | 375×88 |
| Device=Mobile, Type=3 Button, Direction=Both, Fill Container=Yes | `1544:13047` | 375×130 |
| Device=Desktop, Type=3 Button, Direction=Horizontal, Fill Container=No | `1544:13060` | 800×72 |
| Device=Desktop, Type=3 Button, Direction=Horizontal, Fill Container=Yes | `1544:13069` | 800×72 |
| Device=Desktop, Type=3 Button, Direction=Both, Fill Container=Yes | `1544:13078` | 800×120 |
| Device=Mobile, Type=2 Button, Direction=Horizontal, Fill Container=Yes | `1544:13088` | 375×88 |
| Device=Desktop, Type=2 Button, Direction=Horizontal, Fill Container=No | `1544:13100` | 800×72 |
| Device=Desktop, Type=2 Button, Direction=Horizontal, Fill Container=Yes | `1544:13109` | 800×72 |
| Device=Mobile, Type=1 Button, Direction=None, Fill Container=Yes | `1544:13118` | 375×88 |
| Device=Desktop, Type=1 Button, Direction=None, Fill Container=No | `1544:13130` | 800×72 |
| Device=Desktop, Type=Floating, Direction=None, Fill Container=No | `1544:13139` | 560×88 |
| Device=Mobile, Type=Floating, Direction=None, Fill Container=No | `1544:13144` | 375×152 |
| Device=Desktop, Type=1 Button, Direction=None, Fill Container=Yes | `1544:13146` | 800×72 |
| Device=Mobile, Type=2 Button, Direction=Vertical, Fill Container=Yes | `1544:13155` | 375×140 |

</details>

### Badge  `1544:13170`

Board: Badges · key `a1ee07a7ca5aebe7db568ecbb3e0d01f7b1e7a96` · default variant `1544:13205` · radius 5

- Variants: **Size** = Small / Medium / Large / XSmall; **Color** = Primary / Error / Warning / Success / Cyan / Disabled / Gray; **Outline** = On / Off; **Dot** = False / True
- Properties: `Trailing Icon#1125:0` (INSTANCE_SWAP), `Show Trailing Icon#1125:121` (BOOLEAN, default true), `Badge Label#4512:0` (TEXT, default "Label"), `Show Leading Icon#5042:81` (BOOLEAN, default true)
- Text layers (default variant): `Text="Label"`

<details><summary>98 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Size=Small, Color=Primary, Outline=On, Dot=False | `1544:13171` | 87×24 |
| Size=XSmall, Color=Primary, Outline=On, Dot=False | `1544:13175` | 36×16 |
| Size=Small, Color=Warning, Outline=On, Dot=False | `1544:13177` | 87×24 |
| Size=XSmall, Color=Warning, Outline=On, Dot=False | `1544:13181` | 36×16 |
| Size=Small, Color=Success, Outline=On, Dot=False | `1544:13183` | 87×24 |
| Size=XSmall, Color=Success, Outline=On, Dot=False | `1544:13187` | 36×16 |
| Size=Small, Color=Cyan, Outline=On, Dot=False | `1544:13189` | 87×24 |
| Size=XSmall, Color=Cyan, Outline=On, Dot=False | `1544:13193` | 36×16 |
| Size=Small, Color=Error, Outline=On, Dot=False | `1544:13195` | 87×24 |
| Size=XSmall, Color=Error, Outline=On, Dot=False | `1544:13199` | 36×16 |
| Size=Small, Color=Disabled, Outline=On, Dot=False | `1544:13201` | 87×24 |
| Size=XSmall, Color=Disabled, Outline=On, Dot=False | `1544:13205` | 36×16 |
| Size=Small, Color=Primary, Outline=On, Dot=True | `1544:13207` | 77×24 |
| Size=XSmall, Color=Primary, Outline=On, Dot=True | `1544:13212` | 46×16 |
| Size=Small, Color=Warning, Outline=On, Dot=True | `1544:13216` | 77×24 |
| Size=XSmall, Color=Warning, Outline=On, Dot=True | `1544:13221` | 46×16 |
| Size=Small, Color=Success, Outline=On, Dot=True | `1544:13225` | 77×24 |
| Size=XSmall, Color=Success, Outline=On, Dot=True | `1544:13230` | 46×16 |
| Size=Small, Color=Cyan, Outline=On, Dot=True | `1544:13234` | 77×24 |
| Size=XSmall, Color=Cyan, Outline=On, Dot=True | `1544:13239` | 46×16 |
| Size=Small, Color=Error, Outline=On, Dot=True | `1544:13243` | 77×24 |
| Size=XSmall, Color=Error, Outline=On, Dot=True | `1544:13248` | 46×16 |
| Size=Small, Color=Disabled, Outline=On, Dot=True | `1544:13252` | 77×24 |
| Size=XSmall, Color=Disabled, Outline=On, Dot=True | `1544:13257` | 46×16 |
| Size=Medium, Color=Primary, Outline=On, Dot=False | `1544:13261` | 96×25 |
| Size=Medium, Color=Warning, Outline=On, Dot=False | `1544:13265` | 96×25 |
| Size=Medium, Color=Success, Outline=On, Dot=False | `1544:13269` | 96×25 |
| Size=Medium, Color=Cyan, Outline=On, Dot=False | `1544:13273` | 96×25 |
| Size=Medium, Color=Error, Outline=On, Dot=False | `1544:13277` | 96×25 |
| Size=Medium, Color=Disabled, Outline=On, Dot=False | `1544:13281` | 96×25 |
| Size=Medium, Color=Primary, Outline=On, Dot=True | `1544:13285` | 86×25 |
| Size=Medium, Color=Warning, Outline=On, Dot=True | `1544:13290` | 86×25 |
| Size=Medium, Color=Success, Outline=On, Dot=True | `1544:13295` | 86×25 |
| Size=Medium, Color=Cyan, Outline=On, Dot=True | `1544:13300` | 86×25 |
| Size=Medium, Color=Error, Outline=On, Dot=True | `1544:13305` | 86×25 |
| Size=Medium, Color=Disabled, Outline=On, Dot=True | `1544:13310` | 86×25 |
| Size=Large, Color=Primary, Outline=On, Dot=False | `1544:13315` | 105×32 |
| Size=Large, Color=Warning, Outline=On, Dot=False | `1544:13319` | 105×32 |
| Size=Large, Color=Success, Outline=On, Dot=False | `1544:13323` | 105×32 |
| Size=Large, Color=Cyan, Outline=On, Dot=False | `1544:13327` | 105×32 |
| Size=Large, Color=Error, Outline=On, Dot=False | `1544:13331` | 105×32 |
| Size=Large, Color=Disabled, Outline=On, Dot=False | `1544:13335` | 105×32 |
| Size=Large, Color=Primary, Outline=On, Dot=True | `1544:13339` | 95×32 |
| Size=Large, Color=Warning, Outline=On, Dot=True | `1544:13344` | 95×32 |
| Size=Large, Color=Success, Outline=On, Dot=True | `1544:13349` | 95×32 |
| Size=Large, Color=Cyan, Outline=On, Dot=True | `1544:13354` | 95×32 |
| Size=Large, Color=Error, Outline=On, Dot=True | `1544:13359` | 95×32 |
| Size=Large, Color=Disabled, Outline=On, Dot=True | `1544:13364` | 95×32 |
| Size=Small, Color=Primary, Outline=Off, Dot=False | `1544:13369` | 87×24 |
| Size=XSmall, Color=Primary, Outline=Off, Dot=False | `1544:13373` | 36×16 |
| Size=Small, Color=Warning, Outline=Off, Dot=False | `1544:13375` | 87×24 |
| Size=XSmall, Color=Warning, Outline=Off, Dot=False | `1544:13379` | 36×16 |
| Size=Small, Color=Success, Outline=Off, Dot=False | `1544:13381` | 87×24 |
| Size=XSmall, Color=Success, Outline=Off, Dot=False | `1544:13385` | 36×16 |
| Size=Small, Color=Cyan, Outline=Off, Dot=False | `1544:13387` | 87×24 |
| Size=XSmall, Color=Cyan, Outline=Off, Dot=False | `1544:13391` | 36×16 |
| Size=Small, Color=Error, Outline=Off, Dot=False | `1544:13393` | 87×24 |
| Size=XSmall, Color=Error, Outline=Off, Dot=False | `1544:13397` | 36×16 |
| Size=Small, Color=Disabled, Outline=Off, Dot=False | `1544:13399` | 87×24 |
| Size=XSmall, Color=Disabled, Outline=Off, Dot=False | `1544:13403` | 36×16 |
| Size=Small, Color=Primary, Outline=Off, Dot=True | `1544:13405` | 77×22 |
| Size=XSmall, Color=Primary, Outline=Off, Dot=True | `1544:13410` | 46×16 |
| Size=Small, Color=Warning, Outline=Off, Dot=True | `1544:13414` | 77×22 |
| Size=XSmall, Color=Warning, Outline=Off, Dot=True | `1544:13419` | 46×16 |
| Size=Small, Color=Success, Outline=Off, Dot=True | `1544:13423` | 77×22 |
| Size=XSmall, Color=Success, Outline=Off, Dot=True | `1544:13428` | 46×16 |
| Size=Small, Color=Cyan, Outline=Off, Dot=True | `1544:13432` | 77×22 |
| Size=XSmall, Color=Cyan, Outline=Off, Dot=True | `1544:13437` | 46×16 |
| Size=Small, Color=Error, Outline=Off, Dot=True | `1544:13441` | 77×22 |
| Size=XSmall, Color=Error, Outline=Off, Dot=True | `1544:13446` | 46×16 |
| Size=Small, Color=Disabled, Outline=Off, Dot=True | `1544:13450` | 77×22 |
| Size=XSmall, Color=Disabled, Outline=Off, Dot=True | `1544:13455` | 46×16 |
| Size=Medium, Color=Primary, Outline=Off, Dot=False | `1544:13459` | 96×25 |
| Size=Medium, Color=Gray, Outline=Off, Dot=False | `1544:13463` | 96×25 |
| Size=Medium, Color=Warning, Outline=Off, Dot=False | `1544:13467` | 96×25 |
| Size=Medium, Color=Success, Outline=Off, Dot=False | `1544:13471` | 96×25 |
| Size=Medium, Color=Cyan, Outline=Off, Dot=False | `1544:13475` | 96×25 |
| Size=Medium, Color=Error, Outline=Off, Dot=False | `1544:13479` | 96×25 |
| Size=Medium, Color=Disabled, Outline=Off, Dot=False | `1544:13483` | 96×25 |
| Size=Medium, Color=Primary, Outline=Off, Dot=True | `1544:13487` | 86×25 |
| Size=Medium, Color=Warning, Outline=Off, Dot=True | `1544:13492` | 86×25 |
| Size=Medium, Color=Success, Outline=Off, Dot=True | `1544:13497` | 86×25 |
| Size=Medium, Color=Cyan, Outline=Off, Dot=True | `1544:13502` | 86×25 |
| Size=Medium, Color=Error, Outline=Off, Dot=True | `1544:13507` | 86×25 |
| Size=Medium, Color=Disabled, Outline=Off, Dot=True | `1544:13512` | 86×25 |
| Size=Large, Color=Primary, Outline=Off, Dot=False | `1544:13517` | 105×32 |
| Size=Large, Color=Warning, Outline=Off, Dot=False | `1544:13521` | 105×32 |
| Size=Large, Color=Success, Outline=Off, Dot=False | `1544:13525` | 105×32 |
| Size=Large, Color=Cyan, Outline=Off, Dot=False | `1544:13529` | 105×32 |
| Size=Large, Color=Error, Outline=Off, Dot=False | `1544:13533` | 105×32 |
| Size=Large, Color=Disabled, Outline=Off, Dot=False | `1544:13537` | 105×32 |
| Size=Large, Color=Primary, Outline=Off, Dot=True | `1544:13541` | 95×28 |
| Size=Large, Color=Warning, Outline=Off, Dot=True | `1544:13546` | 95×28 |
| Size=Large, Color=Success, Outline=Off, Dot=True | `1544:13551` | 95×28 |
| Size=Large, Color=Cyan, Outline=Off, Dot=True | `1544:13556` | 95×28 |
| Size=Large, Color=Error, Outline=Off, Dot=True | `1544:13561` | 95×28 |
| Size=Large, Color=Disabled, Outline=Off, Dot=True | `1544:13566` | 95×28 |
| Size=Small, Color=Gray, Outline=Off, Dot=False | `1544:13571` | 87×24 |

</details>

### Tag  `1544:13578`

Board: Tags · key `f1854435b113dff758641427534bd280c467f827` · default variant `1544:13579` · radius 5

- Variants: **Size** = Small / Medium / Large; **Type** = Default / Avatar / Dot; **State** = Active / Disable
- Properties: `Close BT#119:20` (BOOLEAN, default true), `Close CTA#5202:0` (INSTANCE_SWAP), `Badge Label#7527:216` (TEXT, default "Label")
- Text layers (default variant): `Text="Label"`

<details><summary>18 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Size=Small, Type=Default, State=Active | `1544:13579` | 65×24 |
| Size=Small, Type=Default, State=Disable | `1544:13583` | 65×24 |
| Size=Medium, Type=Default, State=Active | `1544:13587` | 70×26 |
| Size=Medium, Type=Default, State=Disable | `1544:13591` | 70×25 |
| Size=Medium, Type=Dot, State=Active | `1544:13595` | 84×26 |
| Size=Medium, Type=Dot, State=Disable | `1544:13601` | 84×25 |
| Size=Small, Type=Dot, State=Active | `1544:13607` | 78×24 |
| Size=Small, Type=Dot, State=Disable | `1544:13613` | 78×24 |
| Size=Medium, Type=Avatar, State=Active | `1544:13619` | 90×26 |
| Size=Medium, Type=Avatar, State=Disable | `1544:13624` | 90×25 |
| Size=Small, Type=Avatar, State=Active | `1544:13629` | 82×24 |
| Size=Small, Type=Avatar, State=Disable | `1544:13634` | 82×24 |
| Size=Large, Type=Default, State=Active | `1544:13639` | 72×32 |
| Size=Large, Type=Default, State=Disable | `1544:13643` | 72×29 |
| Size=Large, Type=Dot, State=Active | `1544:13647` | 86×32 |
| Size=Large, Type=Dot, State=Disable | `1544:13653` | 86×29 |
| Size=Large, Type=Avatar, State=Active | `1544:13659` | 102×32 |
| Size=Large, Type=Avatar, State=Disable | `1544:13664` | 102×32 |

</details>

### Chips  `1544:13669`

Board: Tags · key `f9608eaddeb6c5a0771badeae1d1b3c2f5fba02a` · default variant `1544:13670` · radius 5

- Variants: **Outline** = Yes / No; **State** = Default / Active / Disable; **Size** = Large / Medium / Small
- Properties: `Trailing Icon#2521:4` (BOOLEAN, default true), `Swap Trailing Icon#2521:5` (INSTANCE_SWAP), `Leading Icon#2521:6` (BOOLEAN, default true), `Swap Leading Icon#2521:7` (INSTANCE_SWAP), `Badge Label#7527:197` (TEXT, default "Label")
- Text layers (default variant): `Label="Label"`

<details><summary>18 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Outline=Yes, State=Default, Size=Large | `1544:13670` | 108×32 |
| Outline=Yes, State=Default, Size=Small | `1544:13674` | 91×24 |
| Outline=Yes, State=Default, Size=Medium | `1544:13678` | 104×25 |
| Outline=Yes, State=Active, Size=Large | `1544:13682` | 108×32 |
| Outline=Yes, State=Disable, Size=Large | `1544:13686` | 108×32 |
| Outline=Yes, State=Active, Size=Small | `1544:13690` | 91×24 |
| Outline=Yes, State=Disable, Size=Small | `1544:13694` | 91×24 |
| Outline=Yes, State=Active, Size=Medium | `1544:13698` | 104×25 |
| Outline=Yes, State=Disable, Size=Medium | `1544:13702` | 104×25 |
| Outline=No, State=Default, Size=Large | `1544:13706` | 108×32 |
| Outline=No, State=Default, Size=Small | `1544:13710` | 91×24 |
| Outline=No, State=Default, Size=Medium | `1544:13714` | 104×25 |
| Outline=No, State=Active, Size=Large | `1544:13718` | 108×32 |
| Outline=No, State=Disable, Size=Large | `1544:13722` | 108×32 |
| Outline=No, State=Active, Size=Small | `1544:13726` | 91×24 |
| Outline=No, State=Disable, Size=Small | `1544:13730` | 91×24 |
| Outline=No, State=Active, Size=Medium | `1544:13734` | 104×25 |
| Outline=No, State=Disable, Size=Medium | `1544:13738` | 104×25 |

</details>

### Icon Button with Badge  `1544:13765`

Board: Others · key `eadcc03b34dab1613efeaa37aef8a124e1d80d43` · default variant `1544:13766` · radius 5

- Variants: **State** = Default / Active / Hover / Disable; **Size** = Large / Medium
- Text layers (default variant): `Text="2"`, `Text="2"`

<details><summary>8 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| State=Disable, Size=Large | `1544:13766` | 40×40 |
| State=Default, Size=Large | `1544:13772` | 40×40 |
| State=Hover, Size=Large | `1544:13776` | 40×40 |
| State=Active, Size=Large | `1544:13780` | 40×40 |
| State=Disable, Size=Medium | `1544:13784` | 32×32 |
| State=Default, Size=Medium | `1544:13790` | 32×32 |
| State=Hover, Size=Medium | `1544:13794` | 32×32 |
| State=Active, Size=Medium | `1544:13798` | 32×32 |

</details>

### File  `1544:13802`

Board: Others · key `3c29cba006ca5daecbfb4fb8631633eec817556d` · default variant `1544:13803` · radius 5

- Variants: **State** = Default / Disable; **Size** = Large / Medium; **Shown** = Yes / No
- Properties: `Badge#8188:0` (BOOLEAN, default true)
- Text layers (default variant): `Text="2"`

<details><summary>8 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| State=Default, Size=Large, Shown=Yes | `1544:13803` | 32×32 |
| State=Disable, Size=Large, Shown=Yes | `1544:13807` | 32×32 |
| State=Default, Size=Large, Shown=No | `1544:13812` | 32×32 |
| State=Disable, Size=Large, Shown=No | `1544:13814` | 32×32 |
| State=Default, Size=Medium, Shown=Yes | `1544:13816` | 28×28 |
| State=Disable, Size=Medium, Shown=Yes | `1544:13820` | 28×28 |
| State=Default, Size=Medium, Shown=No | `1544:13825` | 28×28 |
| State=Disable, Size=Medium, Shown=No | `1544:13827` | 28×28 |

</details>

### File  `1544:13829`

Board: Others · key `44cff5387f0a8afbaf6fd2cde3e63be04281bf99` · default variant `1544:13830` · radius 5

- Variants: **State** = Default / Disable; **Size** = Large
- Text layers (default variant): `Text="file.JPEG"`

<details><summary>2 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| State=Default, Size=Large | `1544:13830` | 90×32 |
| State=Disable, Size=Large | `1544:13834` | 90×32 |

</details>

### Avatar  `1544:13842`

Board: Avatar · key `071716119b19cbce9e0150a3c8e33b45c47d314f` · default variant `1544:13958` · radius 5

- Variants: **Size** = Xsmall / Small / Medium / Large / XLarge / 1.5XLarge / 2XLarge / 3XLarge / 4XLarge; **Type** = User / Text / Disabled / Icon / Set avatar
- Properties: `Avatar Name#7527:235` (TEXT, default "OR"), `Additional CTA#9505:0` (BOOLEAN, default true)

<details><summary>45 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Size=Small, Type=User | `1544:13843` | 24×24 |
| Size=Small, Type=Disabled | `1544:13845` | 24×24 |
| Size=Medium, Type=User | `1544:13848` | 32×32 |
| Size=Medium, Type=Disabled | `1544:13850` | 32×32 |
| Size=Large, Type=User | `1544:13853` | 40×40 |
| Size=Large, Type=Disabled | `1544:13855` | 40×40 |
| Size=XLarge, Type=User | `1544:13858` | 48×48 |
| Size=1.5XLarge, Type=User | `1544:13861` | 56×56 |
| Size=2XLarge, Type=User | `1544:13864` | 64×64 |
| Size=3XLarge, Type=User | `1544:13867` | 72×72 |
| Size=4XLarge, Type=User | `1544:13870` | 80×80 |
| Size=XLarge, Type=Disabled | `1544:13873` | 48×48 |
| Size=1.5XLarge, Type=Disabled | `1544:13876` | 56×56 |
| Size=2XLarge, Type=Disabled | `1544:13879` | 64×64 |
| Size=3XLarge, Type=Disabled | `1544:13882` | 72×72 |
| Size=4XLarge, Type=Disabled | `1544:13885` | 80×80 |
| Size=Small, Type=Text | `1544:13888` | 24×24 |
| Size=Small, Type=Icon | `1544:13890` | 24×24 |
| Size=Medium, Type=Text | `1544:13892` | 32×32 |
| Size=Medium, Type=Icon | `1544:13894` | 32×32 |
| Size=Large, Type=Text | `1544:13896` | 40×40 |
| Size=Large, Type=Icon | `1544:13898` | 40×40 |
| Size=XLarge, Type=Text | `1544:13900` | 48×48 |
| Size=XLarge, Type=Icon | `1544:13902` | 48×48 |
| Size=1.5XLarge, Type=Text | `1544:13904` | 56×56 |
| Size=1.5XLarge, Type=Icon | `1544:13906` | 56×56 |
| Size=2XLarge, Type=Text | `1544:13908` | 64×64 |
| Size=2XLarge, Type=Icon | `1544:13910` | 64×64 |
| Size=3XLarge, Type=Text | `1544:13912` | 72×72 |
| Size=3XLarge, Type=Icon | `1544:13914` | 72×72 |
| Size=4XLarge, Type=Text | `1544:13916` | 80×80 |
| Size=4XLarge, Type=Icon | `1544:13918` | 80×80 |
| Size=Xsmall, Type=User | `1544:13920` | 16×16 |
| Size=Xsmall, Type=Disabled | `1544:13922` | 16×16 |
| Size=Xsmall, Type=Text | `1544:13925` | 16×16 |
| Size=Xsmall, Type=Icon | `1544:13927` | 16×16 |
| Size=4XLarge, Type=Set avatar | `1544:13929` | 80×80 |
| Size=3XLarge, Type=Set avatar | `1544:13933` | 72×72 |
| Size=1.5XLarge, Type=Set avatar | `1544:13937` | 56×56 |
| Size=2XLarge, Type=Set avatar | `1544:13941` | 64×64 |
| Size=XLarge, Type=Set avatar | `1544:13945` | 48×48 |
| Size=Large, Type=Set avatar | `1544:13949` | 40×40 |
| Size=Medium, Type=Set avatar | `1544:13952` | 32×32 |
| Size=Small, Type=Set avatar | `1544:13955` | 24×24 |
| Size=Xsmall, Type=Set avatar | `1544:13958` | 16×16 |

</details>

### Avatar Group  `1544:13961`

Board: Avatar · key `3dcd9b864b855d4ee4daa069f6f7e851eaac85d5` · default variant `1544:13962` · radius 5

- Variants: **Size** = Small / Medium / XLarge / Xsmal
- Text layers (default variant): `OR="+5"`

<details><summary>4 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Size=Xsmal | `1544:13962` | 64×16 |
| Size=Small | `1544:13968` | 96×24 |
| Size=Medium | `1544:13974` | 128×32 |
| Size=XLarge | `1544:13980` | 160×40 |

</details>

### Checkbox-Base  `1544:13989`

Board: Checkbox · key `ea146d824be07b81003cb3b2977fce39fedeba26` · default variant `1544:13993` · radius 5

- Variants: **Checked** = Yes / No; **Indeterminate** = Yes / No; **Type** = Checkbox / Radio; **State** = Default / Disable
- Properties: `Show Label#99:0` (BOOLEAN, default true), `Label#7527:251` (TEXT, default "Label")
- Text layers (default variant): `label="Label"`

<details><summary>10 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Checked=No, Indeterminate=No, Type=Checkbox, State=Disable | `1544:13990` | 64×21 |
| Checked=No, Indeterminate=No, Type=Checkbox, State=Default | `1544:13993` | 64×21 |
| Checked=Yes, Indeterminate=No, Type=Checkbox, State=Disable | `1544:13996` | 64×21 |
| Checked=Yes, Indeterminate=No, Type=Checkbox, State=Default | `1544:14001` | 64×21 |
| Checked=No, Indeterminate=No, Type=Radio, State=Disable | `1544:14006` | 64×21 |
| Checked=No, Indeterminate=No, Type=Radio, State=Default | `1544:14011` | 64×21 |
| Checked=Yes, Indeterminate=No, Type=Radio, State=Disable | `1544:14016` | 64×21 |
| Checked=Yes, Indeterminate=No, Type=Radio, State=Default | `1544:14021` | 64×21 |
| Checked=Yes, Indeterminate=Yes, Type=Checkbox, State=Disable | `1544:14026` | 64×21 |
| Checked=Yes, Indeterminate=Yes, Type=Checkbox, State=Default | `1544:14031` | 64×21 |

</details>

### Date Picker  `1544:14059`

Board: Date Picker · key `802742f169325493d2fd2d3260443ce9698cbb31` · default variant `1544:14060` · radius 5

- Variants: **Style** = Date range / Date; **State** = Focus / Placeholder
- Properties: `Hint#34813:0` (BOOLEAN, default true)
- Text layers (default variant): `Label="Date-Picker"`, `Text="11/08/2023"`, `Hint text="This is a hint text to help us"`

<details><summary>4 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Style=Date, State=Placeholder | `1544:14060` | 376×67 |
| Style=Date, State=Focus | `1544:14068` | 376×67 |
| Style=Date range, State=Placeholder | `1544:14076` | 376×67 |
| Style=Date range, State=Focus | `1544:14088` | 376×67 |

</details>

### Date picker menu  `1544:14112`

Board: Date Picker · key `75c349b98479842a9966b1a1058bd1f4e7b5d809` · default variant `1544:14357` · radius 5

- Variants: **Type** = Dual dates / Single date / Single month / Dual month / Single quarter / Dual quarter / Single year / Dual years / Single date-Collapsed
- Properties: `Duo Calendar#521:0` (BOOLEAN, default true)
- Text layers (default variant): `Text="January 2022"`, `Number="Mo"`, `Number="Tu"`, `Number="We"`, `Number="Th"`, `Number="Fr"`, `Number="Sat"`, `Number="Su"`, `Number="1"`, `Number="2"`, `Number="3"`, `Number="4"`, `Number="5"`, `Number="6"`, `Number="7"`, `Number="8"`, `Number="9"`, `Number="10"`, `Number="11"`, `Number="12"`

<details><summary>9 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Type=Dual dates | `1544:14113` | 640×376 |
| Type=Dual month | `1544:14241` | 640×284 |
| Type=Dual quarter | `1544:14287` | 640×116 |
| Type=Dual years | `1544:14311` | 640×284 |
| Type=Single date | `1544:14357` | 320×376 |
| Type=Single date-Collapsed | `1544:14424` | 320×152 |
| Type=Single month | `1544:14482` | 320×284 |
| Type=Single year | `1544:14505` | 320×284 |
| Type=Single quarter | `1544:14528` | 320×116 |

</details>

### _Calendar cell  `1544:14553`

Board: Date Picker · key `538f5025eb618c84e06f3740f7d2fdb0c7ad5518` · default variant `1544:14554` · radius 5

- Variants: **Type** = Default / Range / Today's date; **State** = Default / Hover / In view / Active
- Text layers (default variant): `Number="1"`

<details><summary>11 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Type=Default, State=Default | `1544:14554` | 32×32 |
| Type=Today's date, State=Default | `1544:14556` | 32×32 |
| Type=Default, State=Active | `1544:14558` | 32×32 |
| Type=Range, State=Hover | `1544:14560` | 32×32 |
| Type=Range, State=Active | `1544:14563` | 32×32 |
| Type=Range, State=In view | `1544:14566` | 32×32 |
| Type=Default, State=In view | `1544:14569` | 32×32 |
| Type=Today's date, State=In view | `1544:14571` | 32×32 |
| Type=Default, State=Hover | `1544:14573` | 32×32 |
| Type=Today's date, State=Hover | `1544:14575` | 32×32 |
| Type=Today's date, State=Active | `1544:14577` | 32×32 |

</details>

### Day1...  `1544:14589`

Board: Date Picker · key `2776bcef8afd725ebc65f2646df86047b17f5f32` · default variant `1544:14590` · radius 5

- Variants: **Property 1** = Tue / Wed / Thu / Fri / Sat / Sun / _Mon
- Text layers (default variant): `Number="1"`

<details><summary>7 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Property 1=_Mon | `1544:14590` | 32×32 |
| Property 1=Tue | `1544:14592` | 72×32 |
| Property 1=Wed | `1544:14595` | 112×32 |
| Property 1=Thu | `1544:14599` | 152×32 |
| Property 1=Fri | `1544:14604` | 192×32 |
| Property 1=Sat | `1544:14610` | 232×32 |
| Property 1=Sun | `1544:14617` | 272×32 |

</details>

### Time Picker  `1544:14627`

Board: Time Picker · key `4dcf42db2c53cc325b7fd6c0d9599cc9bd0c09fe` · default variant `1544:14673` · radius 5

- Variants: **Style** = Time / Time range; **State** = Focus (2) / Placeholder / Focus / Focus(1)
- Text layers (default variant): `Label="Time Picker"`, `Red dot="*"`, `Text="8:00 am"`, `Hint text="This is a hint text to help us"`

<details><summary>5 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Style=Time range, State=Focus(1) | `1544:14628` | 320×435 |
| Style=Time range, State=Focus (2) | `1544:14644` | 320×435 |
| Style=Time range, State=Placeholder | `1544:14659` | 320×67 |
| Style=Time, State=Placeholder | `1544:14673` | 320×67 |
| Style=Time, State=Focus | `1544:14682` | 320×435 |

</details>

### Component 1  `1544:58725`

Board: Input text field. ⚠ in get_componentPropertyDefinitions: Component set has existing errors

### Text area  `1544:58907`

Board: Input text field · key `18f35b8eaa04081514c1b200195ec45390f7b167` · default variant `1544:58908` · radius 5

- Variants: **State** = Placeholder / Focus / Filled / Error
- Properties: `Hint#34821:34` (BOOLEAN, default true), `Icon#34821:39` (BOOLEAN, default true)
- Text layers (default variant): `Label="Label"`, `Red dot="*"`, `Text="Describe..."`, `Text="0/1500"`, `Label="Clear"`, `Label="Edit"`, `Hint text="This is a hint text to help us"`

<details><summary>4 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| State=Placeholder | `1544:58908` | 407×151 |
| State=Focus | `1544:58919` | 407×151 |
| State=Filled | `1544:58930` | 407×151 |
| State=Error | `1544:58941` | 407×151 |

</details>

### Text Editor  `1544:58953`

Board: Input text field · key `faeab01e312a34e66e22bc51ec62fa488650974f` · default variant `1544:58954` · radius 5

- Variants: **Property 1** = Default / Filled / Disabled
- Text layers (default variant): `Normal="Normal"`, `Sans Serif="Sans Serif"`, `Label="Label"`, `Red dot="*"`, `Text="12"`, `Hint text="This is a hint text to help us"`, `Text="Description"`

<details><summary>3 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Property 1=Default | `1544:58954` | 921×214 |
| Property 1=Filled | `1544:58998` | 921×214 |
| Property 1=Disabled | `1544:59042` | 921×214 |

</details>

### Input dropdown menu item  `1544:59116`

Board: Input Dropdown · key `a27b0091c5dbdfe4e9f6ed363919a983da960aba` · default variant `1544:59137` · radius 5

- Variants: **Type** = Icon Leading / Default / Avatar Leading; **State** = Default / Hover / Selected / Disable
- Properties: `Show Supporting Text#113:0` (BOOLEAN, default true), `Show Checkbox#155:10` (BOOLEAN, default true), `Show Check Icon#477:0` (BOOLEAN, default true), `Show Badge#2587:19` (BOOLEAN, default false), `Swap Icon#5243:49` (INSTANCE_SWAP), `Show icon right#26156:0` (BOOLEAN, default false)
- Text layers (default variant): `label="Label"`, `Lorem ipsum="Lorem ipsum"`, `Supporting Text="Supporting Text"`, `Text="3"`

<details><summary>12 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Type=Icon Leading, State=Default | `1544:59117` | 280×55 |
| Type=Avatar Leading, State=Default | `1544:59124` | 280×55 |
| Type=Default, State=Default | `1544:59137` | 280×55 |
| Type=Icon Leading, State=Hover | `1544:59144` | 280×55 |
| Type=Avatar Leading, State=Hover | `1544:59152` | 280×55 |
| Type=Default, State=Hover | `1544:59166` | 280×55 |
| Type=Icon Leading, State=Selected | `1544:59174` | 280×55 |
| Type=Icon Leading, State=Disable | `1544:59182` | 280×55 |
| Type=Avatar Leading, State=Selected | `1544:59190` | 280×55 |
| Type=Avatar Leading, State=Disable | `1544:59204` | 280×55 |
| Type=Default, State=Selected | `1544:59218` | 280×55 |
| Type=Default, State=Disable | `1544:59225` | 280×55 |

</details>

### Input item with sub-input  `1544:59234`

Board: Input Dropdown · key `0353221206cf3168198b34df89de9d64d1fcae9a` · default variant `1544:59235` · radius 5

- Variants: **Sub Input** = Yes / No
- Properties: `Sub input#1544:0` (BOOLEAN, default true)
- Text layers (default variant): `label="Label"`, `Lorem ipsum="Lorem ipsum"`, `Supporting Text="Supporting Text"`, `Text="3"`, `label="Label"`, `Lorem ipsum="Lorem ipsum"`, `Supporting Text="Supporting Text"`, `Text="3"`, `label="Label"`, `Lorem ipsum="Lorem ipsum"`, `Supporting Text="Supporting Text"`, `Text="3"`, `label="Label"`, `Lorem ipsum="Lorem ipsum"`, `Supporting Text="Supporting Text"`, `Text="3"`, `label="Label"`, `Lorem ipsum="Lorem ipsum"`, `Supporting Text="Supporting Text"`, `Text="3"`

<details><summary>2 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Sub Input=Yes | `1544:59235` | 284×330 |
| Sub Input=No | `1544:59243` | 284×55 |

</details>

### Menu Dropdown  `1544:59253`

Board: Input Dropdown · key `e74a9ee72d1c18ec46e5a6c757cfb0470b08cb8e` · default variant `1544:59254` · radius 5

- Variants: **Type** = Default / Icon Leading / Avatar Leading; **Checkbox** = Yes / No
- Properties: `Scroll#203:0` (BOOLEAN, default true), `Search#7084:0` (BOOLEAN, default true), `Title#9290:7` (BOOLEAN, default false)
- Text layers (default variant): `Lorem ipsum="Lorem ipsum"`, `label="am"`, `label="pm"`, `Text="Search"`, `label="Label"`, `Lorem ipsum="Lorem ipsum"`, `Supporting Text="Supporting Text"`, `Text="3"`, `label="Label"`, `Lorem ipsum="Lorem ipsum"`, `Supporting Text="Supporting Text"`, `Text="3"`, `label="Label"`, `Lorem ipsum="Lorem ipsum"`, `Supporting Text="Supporting Text"`, `Text="3"`, `label="Label"`, `Lorem ipsum="Lorem ipsum"`, `Supporting Text="Supporting Text"`, `Text="3"`

<details><summary>6 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Type=Default, Checkbox=Yes | `1544:59254` | 296×364 |
| Type=Icon Leading, Checkbox=Yes | `1544:59279` | 296×364 |
| Type=Avatar Leading, Checkbox=Yes | `1544:59304` | 296×355 |
| Type=Default, Checkbox=No | `1544:59329` | 296×355 |
| Type=Icon Leading, Checkbox=No | `1544:59354` | 296×355 |
| Type=Avatar Leading, Checkbox=No | `1544:59379` | 296×355 |

</details>

### Input Dropdown  `1544:59408`

Board: Input Dropdown · key `9e179e84709f27e9fe1cac10e5fdf238551746f8` · default variant `1544:59409` · radius 5

- Variants: **Type** = Frame 1707479033 / Frame 1707479034 / Frame 1707479035 / Frame 1707479036 / Frame 1707479037 / Frame 1707479038 / Dèaul; **State** = Error tag / Placeholder / Focus / Filled / Focus tag / Error
- Properties: `Hint#34823:0` (BOOLEAN, default true), `Label#34993:0` (BOOLEAN, default true)
- Text layers (default variant): `Label="Label"`, `Red dot="*"`, `Text="Select ..."`, `Text="3"`, `Hint text="This is a hint text to help us"`

<details><summary>12 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Type=Dèaul, State=Placeholder | `1544:59409` | 397×65 |
| Type=Frame 1707479033, State=Placeholder | `1544:59418` | 397×65 |
| Type=Dèaul, State=Filled | `1544:59429` | 397×65 |
| Type=Frame 1707479034, State=Filled | `1544:59438` | 397×65 |
| Type=Dèaul, State=Error | `1544:59449` | 397×65 |
| Type=Frame 1707479035, State=Error | `1544:59458` | 397×65 |
| Type=Dèaul, State=Focus tag | `1544:59469` | 397×65 |
| Type=Frame 1707479036, State=Focus tag | `1544:59480` | 397×65 |
| Type=Dèaul, State=Error tag | `1544:59493` | 397×65 |
| Type=Frame 1707479037, State=Error tag | `1544:59504` | 397×65 |
| Type=Dèaul, State=Focus | `1544:59517` | 397×408 |
| Type=Frame 1707479038, State=Focus | `1544:59527` | 397×408 |

</details>

### Filter Dropdown  `1544:59541`

Board: Input Dropdown · key `b0ead09b4f6f26e85aa4726b48895b897ee31ec2` · default variant `1544:59542` · radius 5

- Variants: **State** = Default / Open / Applied Filter
- Properties: `Trailing icon#5667:8` (BOOLEAN, default false), `Leading Icon#5667:12` (BOOLEAN, default true)
- Text layers (default variant): `Text="Filter"`, `Text="3"`

<details><summary>3 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| State=Default | `1544:59542` | 128×40 |
| State=Open | `1544:59548` | 128×40 |
| State=Applied Filter | `1544:59551` | 122×40 |

</details>

### Filter Menu  `1544:59556`

Board: Input Dropdown · key `f299e2f34ca3590cbb4704dae5b75b17c8f01e6f` · default variant `1544:59557` · radius 5

- Variants: **State** = Default / Selected
- Text layers (default variant): `Basic Information="Filter"`, `Label="Clear All"`, `Label="Label"`, `Red dot="*"`, `Text="Select ..."`, `Text="3"`, `Hint text="This is a hint text to help us"`, `Label="Label"`, `Red dot="*"`, `Text="Select ..."`, `Text="3"`, `Hint text="This is a hint text to help us"`, `Label="Label"`, `Red dot="*"`, `Text="Select ..."`, `Text="3"`, `Hint text="This is a hint text to help us"`, `Label="Label"`, `Red dot="*"`, `Text="Select ..."`

<details><summary>2 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| State=Default | `1544:59557` | 360×476 |
| State=Selected | `1544:59575` | 360×476 |

</details>

### _Pagination button group base  `1544:59600`

Board: Pagination · key `f42e08905df30186a09bd2a6e763e54e31c059d9` · default variant `1544:59605` · radius 5

- Variants: **State** = Default / Hover / Disabled / Active; **Icon** = False / Right / Left
- Properties: `Number#5255:11` (TEXT, default "1")

<details><summary>9 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| State=Disabled, Icon=Left | `1544:59601` | 32×32 |
| State=Hover, Icon=Left | `1544:59603` | 32×32 |
| State=Default, Icon=Left | `1544:59605` | 32×32 |
| State=Disabled, Icon=Right | `1544:59607` | 32×32 |
| State=Hover, Icon=Right | `1544:59609` | 32×32 |
| State=Default, Icon=Right | `1544:59611` | 32×32 |
| State=Hover, Icon=False | `1544:59613` | 32×33 |
| State=Active, Icon=False | `1544:59615` | 32×33 |
| State=Default, Icon=False | `1544:59617` | 32×33 |

</details>

### Pagination  `1544:59619`

Board: Pagination · key `8e722e789f9b9f0f203ed7540f4115357188183c` · default variant `1544:59620` · radius 5

- Variants: **Type** = Default
- Text layers (default variant): `10 / page="15 bản ghi"`, `Details="Showing 1-10 of 56"`, `number="1"`, `number="2"`, `number="3"`, `number="4"`, `number="5"`, `ellipsis="•••"`, `number="50"`

<details><summary>1 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Type=Default | `1544:59620` | 1112×81 |

</details>

### Scroll bar  `1544:59643`

Board: Toggle A · key `205ffb35ca50cce8bdf828f1a6fe2cdd6559fef6` · default variant `1544:59644` · radius 5

- Variants: **Type** = Vertical / Horizontal; **Length** = 25% / 50% / 75%

<details><summary>6 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Type=Vertical, Length=25% | `1544:59644` | 14×240 |
| Type=Vertical, Length=50% | `1544:59647` | 14×240 |
| Type=Vertical, Length=75% | `1544:59650` | 14×240 |
| Type=Horizontal, Length=25% | `1544:59653` | 240×14 |
| Type=Horizontal, Length=50% | `1544:59656` | 240×14 |
| Type=Horizontal, Length=75% | `1544:59659` | 240×14 |

</details>

### Submenu  `1544:59667`

Board: Left Navigator Bar · key `4b2bfcd43284af61ac5911a6bcea1dcb1b51f4a6` · default variant `1544:59668` · radius 5

- Variants: **Property 1** = Placholder / Focus / Hover
- Text layers (default variant): `Submenu="Submenu"`

<details><summary>3 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Property 1=Placholder | `1544:59668` | 84×36 |
| Property 1=Hover | `1544:59670` | 84×36 |
| Property 1=Focus | `1544:59672` | 84×36 |

</details>

### Icon sidebar  `1544:59674`

Board: Left Navigator Bar · key `325d112de2a8486c13fcceffebca941981fa3fb8` · default variant `1544:59675` · radius 5

- Variants: **Property 1** = Default / Focus

<details><summary>2 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Property 1=Default | `1544:59675` | 40×40 |
| Property 1=Focus | `1544:59677` | 40×40 |

</details>

### Menu\  `1544:59679`

Board: Left Navigator Bar · key `05a9cac12a373c93b728ce38bfd8d60c3a32aac3` · default variant `1544:59680` · radius 5

- Variants: **Property 1** = Frame 1707481682 / Frame 1707481683 / Frame 1707481685
- Properties: `Icon drop#33942:7` (BOOLEAN, default true)
- Text layers (default variant): `Trang chủ="Trang chủ"`

<details><summary>3 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Property 1=Frame 1707481682 | `1544:59680` | 198×40 |
| Property 1=Frame 1707481683 | `1544:59685` | 198×40 |
| Property 1=Frame 1707481685 | `1544:59690` | 198×396 |

</details>

### Side bar Component (Use This)  `1544:59705`

Board: Left Navigator Bar · key `08de4c1ca146bfa323fd97ce6fdd6bbdfeb8e7b7` · default variant `1544:59706` · radius 5

- Variants: **State** = Mini sidebar / Collapsed sidebar / Mini sidebar 1

<details><summary>3 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| State=Mini sidebar | `1544:59706` | 72×1043 |
| State=Mini sidebar 1 | `1544:59740` | 188×1043 |
| State=Collapsed sidebar | `1544:59783` | 247×1043 |

</details>

### Upload Item  `1544:59825`

Board: File Upload · key `75ddbac997375235e7f6ce0a8b7248ed681c071a` · default variant `1544:59826` · radius 5

- Variants: **State** = Uploaded / Uploading / Submitted; **Size** = Big / Medium / Small; **Thumbnail** = No / Yes
- Properties: `Close Button#2837:0` (BOOLEAN, default true), `More CTA#7702:0` (BOOLEAN, default false), `Date time#7702:11` (BOOLEAN, default false)
- Text layers (default variant): `file_upload_name.csv="file_upload_name.csv"`, `Percentage="40%"`

<details><summary>10 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| State=Uploading, Size=Big, Thumbnail=No | `1544:59826` | 400×74 |
| State=Uploaded, Size=Big, Thumbnail=No | `1544:59834` | 400×73 |
| State=Submitted, Size=Big, Thumbnail=No | `1544:59844` | 400×73 |
| State=Uploading, Size=Medium, Thumbnail=No | `1544:59857` | 320×57 |
| State=Uploading, Size=Small, Thumbnail=No | `1544:59865` | 320×50 |
| State=Uploaded, Size=Medium, Thumbnail=No | `1544:59873` | 320×55 |
| State=Submitted, Size=Medium, Thumbnail=No | `1544:59883` | 320×55 |
| State=Uploaded, Size=Small, Thumbnail=No | `1544:59896` | 320×48 |
| State=Submitted, Size=Small, Thumbnail=No | `1544:59907` | 320×48 |
| State=Uploaded, Size=Big, Thumbnail=Yes | `1544:59920` | 200×240 |

</details>

### Upload Box  `1544:59944`

Board: File Upload · key `f9345a82ce6ffd350907b7092dbd5c7cfcc776ba` · default variant `1544:59945` · radius 5

- Variants: **State** = Default / Disabled / Active / No Files Uploaded; **Mobile** = No / Yes
- Properties: `Description#732:0` (BOOLEAN, default false), `Label#755:0` (BOOLEAN, default true)
- Text layers (default variant): `Label="Label"`, `Text="Drag & drop your file here"`, `Supporting text="or browse to upload a file"`

<details><summary>8 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| State=Default, Mobile=No | `1544:59945` | 568×193 |
| State=No Files Uploaded, Mobile=No | `1544:59978` | 568×96 |
| State=Default, Mobile=Yes | `1544:59983` | 375×148 |
| State=No Files Uploaded, Mobile=Yes | `1544:60019` | 375×96 |
| State=Active, Mobile=No | `1544:60051` | 568×368 |
| State=Active, Mobile=Yes | `1544:60088` | 375×288 |
| State=Disabled, Mobile=No | `1544:60127` | 568×193 |
| State=Disabled, Mobile=Yes | `1544:60160` | 375×148 |

</details>

### Toggle  `1544:60170`

Board: Toggle B · key `b62bffe0af1e30f26512cc0e40b6d7b18866f37d` · default variant `1544:60171` · radius 5

- Variants: **Select** = No / Yes; **State** = Default / Disabled; **Style** = Default / Alternative
- Properties: `Show Right Label#152:10` (BOOLEAN, default false), `Show Left Label#7309:0` (BOOLEAN, default true)
- Text layers (default variant): `label="Label"`, `label="Label"`

<details><summary>6 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Select=No, State=Default, Style=Default | `1544:60171` | 80×21 |
| Select=No, State=Disabled, Style=Default | `1544:60176` | 80×21 |
| Select=Yes, State=Default, Style=Default | `1544:60181` | 80×21 |
| Select=Yes, State=Default, Style=Alternative | `1544:60186` | 80×21 |
| Select=Yes, State=Disabled, Style=Default | `1544:60191` | 80×21 |
| Select=Yes, State=Disabled, Style=Alternative | `1544:60196` | 80×21 |

</details>

### Time Toggle  `1544:60223`

Board: Toggle B · key `69f83b75282ca4f6369e4238065332f78c7b62bb` · default variant `1544:60224` · radius 5

- Variants: **Type** = AM / PM; **State** = Default / Disable
- Text layers (default variant): `label="am"`, `label="pm"`

<details><summary>4 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Type=AM, State=Default | `1544:60224` | 86×28 |
| Type=AM, State=Disable | `1544:60229` | 86×28 |
| Type=PM, State=Default | `1544:60234` | 86×28 |
| Type=PM, State=Disable | `1544:60239` | 86×28 |

</details>

### Tooltip  `1544:60247`

Board: Tooltip · key `8c7465e4260fa2974dedc31389b8771843475813` · default variant `1544:60248` · radius 5

- Variants: **Supporting text** = False / True; **Arrow** = None / Bottom left / Bottom right / Left / Right / Bottom center / Top center / Top right / Bottom. center; **Color** = White / Black
- Properties: `Button(s)#9846:7` (BOOLEAN, default false)
- Text layers (default variant): `Text="This is a tooltip"`

<details><summary>16 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Supporting text=False, Arrow=None, Color=Black | `1544:60248` | 122×41 |
| Supporting text=False, Arrow=Bottom center, Color=Black | `1544:60251` | 122×47 |
| Supporting text=False, Arrow=Bottom left, Color=Black | `1544:60256` | 122×47 |
| Supporting text=False, Arrow=Bottom right, Color=Black | `1544:60261` | 122×47 |
| Supporting text=False, Arrow=Top center, Color=Black | `1544:60266` | 122×47 |
| Supporting text=False, Arrow=Top right, Color=Black | `1544:60271` | 122×47 |
| Supporting text=False, Arrow=Left, Color=Black | `1544:60276` | 128×41 |
| Supporting text=False, Arrow=Right, Color=Black | `1544:60281` | 128×41 |
| Supporting text=True, Arrow=None, Color=Black | `1544:60286` | 320×101 |
| Supporting text=True, Arrow=Bottom center, Color=Black | `1544:60292` | 320×107 |
| Supporting text=True, Arrow=Bottom. center, Color=White | `1544:60300` | 320×107 |
| Supporting text=True, Arrow=Bottom left, Color=Black | `1544:60308` | 320×107 |
| Supporting text=True, Arrow=Bottom right, Color=Black | `1544:60316` | 320×107 |
| Supporting text=True, Arrow=Top center, Color=Black | `1544:60324` | 320×107 |
| Supporting text=True, Arrow=Left, Color=Black | `1544:60332` | 326×101 |
| Supporting text=True, Arrow=Right, Color=Black | `1544:60340` | 326×101 |

</details>

### Help icon  `1544:60348`

Board: Tooltip · key `daa93ebd5951aa14924cefdd817f6aaf8cc29897` · default variant `1544:60349` · radius 5

- Variants: **Open** = False / True; **Supporting text** = False / True; **Tooltip** = Top no arrow / Top arrow / Left / Top left / Bottom / Right / Top right

<details><summary>28 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Open=False, Supporting text=False, Tooltip=Top no arrow | `1544:60349` | 16×16 |
| Open=False, Supporting text=True, Tooltip=Top no arrow | `1544:60351` | 16×16 |
| Open=False, Supporting text=False, Tooltip=Top arrow | `1544:60353` | 16×16 |
| Open=False, Supporting text=True, Tooltip=Top arrow | `1544:60355` | 16×16 |
| Open=False, Supporting text=False, Tooltip=Top right | `1544:60357` | 16×16 |
| Open=False, Supporting text=True, Tooltip=Top right | `1544:60359` | 16×16 |
| Open=False, Supporting text=False, Tooltip=Top left | `1544:60361` | 16×16 |
| Open=False, Supporting text=True, Tooltip=Top left | `1544:60363` | 16×16 |
| Open=False, Supporting text=False, Tooltip=Bottom | `1544:60365` | 16×16 |
| Open=False, Supporting text=True, Tooltip=Bottom | `1544:60367` | 16×16 |
| Open=False, Supporting text=False, Tooltip=Right | `1544:60369` | 16×16 |
| Open=False, Supporting text=True, Tooltip=Right | `1544:60371` | 16×16 |
| Open=False, Supporting text=False, Tooltip=Left | `1544:60373` | 16×16 |
| Open=False, Supporting text=True, Tooltip=Left | `1544:60375` | 16×16 |
| Open=True, Supporting text=False, Tooltip=Top no arrow | `1544:60377` | 16×16 |
| Open=True, Supporting text=True, Tooltip=Top no arrow | `1544:60381` | 16×16 |
| Open=True, Supporting text=False, Tooltip=Top arrow | `1544:60385` | 16×16 |
| Open=True, Supporting text=True, Tooltip=Top arrow | `1544:60389` | 16×16 |
| Open=True, Supporting text=False, Tooltip=Top right | `1544:60393` | 16×16 |
| Open=True, Supporting text=True, Tooltip=Top right | `1544:60397` | 16×16 |
| Open=True, Supporting text=False, Tooltip=Top left | `1544:60401` | 16×16 |
| Open=True, Supporting text=True, Tooltip=Top left | `1544:60405` | 16×16 |
| Open=True, Supporting text=False, Tooltip=Bottom | `1544:60409` | 16×16 |
| Open=True, Supporting text=True, Tooltip=Bottom | `1544:60413` | 16×16 |
| Open=True, Supporting text=False, Tooltip=Right | `1544:60417` | 16×16 |
| Open=True, Supporting text=True, Tooltip=Right | `1544:60421` | 16×16 |
| Open=True, Supporting text=False, Tooltip=Left | `1544:60425` | 16×16 |
| Open=True, Supporting text=True, Tooltip=Left | `1544:60429` | 16×16 |

</details>

### Locked  `1544:60433`

Board: Tooltip · key `9cf3dfa483e381a481670e7ee57074b24004f701` · default variant `1544:60434` · radius 5

- Variants: **Property 1** = Default / Tooltip

<details><summary>2 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Property 1=Default | `1544:60434` | 24×24 |
| Property 1=Tooltip | `1544:60436` | 24×24 |

</details>

### Excluded  `1544:60439`

Board: Tooltip · key `8e395fae64c6f522ae671686dd10449b95cd564f` · default variant `1544:60440` · radius 5

- Variants: **Property 1** = Default / Open

<details><summary>2 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Property 1=Default | `1544:60440` | 24×24 |
| Property 1=Open | `1544:60442` | 24×24 |

</details>

### Featured icon  `1544:60448`

Board: Toast Bar · key `630401fff38b89aebe0521679b31d63270221fd1` · default variant `1544:60453` · radius 5

- Variants: **Property 1** = Success / Error / Warning

<details><summary>3 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Property 1=Error | `1544:60449` | 32×32 |
| Property 1=Warning | `1544:60451` | 32×32 |
| Property 1=Success | `1544:60453` | 32×32 |

</details>

### Toast Bar  `1544:60455`

Board: Toast Bar · key `52232474120a0ef3699f80953ab48c15a66cd943` · default variant `1544:60456` · radius 5

- Variants: **Type** = Successfully / Warning / Error; **Size** = Medium / Small
- Properties: `Show Description#345:0` (BOOLEAN, default true), `Show icon#21813:3` (BOOLEAN, default true)
- Text layers (default variant): `Title="Added new component successful"`, `Description="Urna felis tincidunt pellentes"`

<details><summary>6 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Type=Successfully, Size=Medium | `1544:60456` | 480×70 |
| Type=Successfully, Size=Small | `1544:60462` | 348×67 |
| Type=Warning, Size=Medium | `1544:60468` | 480×70 |
| Type=Warning, Size=Small | `1544:60474` | 393×67 |
| Type=Error, Size=Medium | `1544:60480` | 480×70 |
| Type=Error, Size=Small | `1544:60486` | 347×67 |

</details>

### _Tab Item Base (Horizontal)  `1544:60516`

Board: Frame (misc) · key `03806661213a28be3e8adefdc23954c116518cd6` · default variant `1544:60521` · radius 5

- Variants: **State** = Default / Hover / Active / Disabled; **Level** = Level 1 / Level 2a
- Properties: `Show Badge#152:0` (BOOLEAN, default true)
- Text layers (default variant): `Tab Item="Tab Item"`

<details><summary>8 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| State=Default, Level=Level 2a | `1544:60517` | 57×41 |
| State=Disabled, Level=Level 2a | `1544:60519` | 58×41 |
| State=Default, Level=Level 1 | `1544:60521` | 89×41 |
| State=Disabled, Level=Level 1 | `1544:60523` | 90×41 |
| State=Hover, Level=Level 2a | `1544:60525` | 57×41 |
| State=Hover, Level=Level 1 | `1544:60529` | 89×41 |
| State=Active, Level=Level 2a | `1544:60532` | 58×41 |
| State=Active, Level=Level 1 | `1544:60535` | 90×41 |

</details>

### Tab Item Base (Vertical)  `1544:60537`

Board: Frame (misc) · key `edb4997c7225d42c6d8ac0f671c8dcdfa9672723` · default variant `1544:60538` · radius 5

- Variants: **State** = Default / Hover / Active / Disabled
- Properties: `Active Dot#9103:0` (BOOLEAN, default false)
- Text layers (default variant): `Tab Item="Tab Item"`, `Supporting text="Supporting Text"`, `Supporting text="L-3.2"`, `Supporting text="Academic"`

<details><summary>4 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| State=Default | `1544:60538` | 240×57 |
| State=Hover | `1544:60552` | 240×57 |
| State=Active | `1544:60566` | 240×57 |
| State=Disabled | `1544:60580` | 240×57 |

</details>

### Tab Navigation (Horizontal)  `1544:60600`

Board: Frame (misc) · key `186bff992827cf9b4c4584333a93007216568eea` · default variant `1544:60601` · radius 5

- Variants: **Level** = Level 1 / Level 2a
- Text layers (default variant): `Tab Item="Tab Item"`, `Tab Item="Tab Item"`, `Tab Item="Tab Item"`, `Tab Item="Tab Item"`, `Tab Item="Tab Item"`, `Tab Item="Tab Item"`, `Tab Item="Tab Item"`, `Tab Item="Tab Item"`, `Tab Item="Tab Item"`, `Tab Item="Tab Item"`

<details><summary>2 variant ids</summary>

| Variant | id | w×h |
|---|---|---|
| Level=Level 1 | `1544:60601` | 357×41 |
| Level=Level 2a | `1544:60612` | 349×41 |

</details>

### Component 1 — Input text field  `1544:58725` (broken set, ids still usable)

- Text layers: `Label`, `Red dot`, `Text`, `Dropdown text`, `Hint text`

| Variant | id | w×h |
|---|---|---|
| Type=Trailing dropdown, State=Placeholder | `1544:58726` | 402×65 |
| Type=Trailing dropdown, State=Focus | `1544:58738` | 402×65 |
| Type=Trailing dropdown, State=Filled | `1544:58752` | 402×65 |
| Type=Trailing dropdown, State=Error | `1544:58765` | 402×65 |
| Type=Trailing dropdown, State=Placeholder | `1544:58778` | 402×65 |
| Type=Trailing dropdown, State=Focus | `1544:58791` | 402×65 |
| Type=Trailing dropdown, State=Filled | `1544:58806` | 402×65 |
| Type=Trailing dropdown, State=Error | `1544:58819` | 402×65 |
| Type=Default, State=Placeholder | `1544:58832` | 402×65 |
| Type=Tags, State=Placeholder | `1544:58840` | 402×65 |
| Type=Default, State=Focus | `1544:58848` | 402×65 |
| Type=Tags, State=Focus | `1544:58857` | 402×65 |
| Type=Default, State=Error | `1544:58867` | 402×65 |
| Type=Tags, State=Error | `1544:58876` | 402×65 |
| Type=Default, State=Filled | `1544:58886` | 402×65 |
| Type=Tags, State=Filled | `1544:58894` | 402×65 |

## Icons (Iconsax, board `1544:14693`)

897 icon sets, each with variants `Property 1` = linear / bold / outline / twotone / bulk / broken. Some names repeat (same glyph drawn in two categories) — either id works.

<details><summary>icon name → set id</summary>

`wallet-add` 1544:14697 · `empty-wallet` 1544:14759 · `wallet-check` 1544:14809 · `receipt-item` 1544:14864 · `receipt-discount` 1544:14921 · `empty-wallet-remove` 1544:14974 · `empty-wallet-add` 1544:15044 · `receipt-minus` 1544:15114 · `wallet-search` 1544:15157 · `strongbox-2` 1544:15212 · `empty-wallet-tick` 1544:15265 · `receipt-add` 1544:15328 · `money` 1544:15375 · `empty-wallet-time` 1544:15423 · `transaction-minus` 1544:15486 · `money-2` 1544:15523 · `empty-wallet-change` 1544:15578 · `money-3` 1544:15649 · `percentage-square` 1544:15696 · `money-4` 1544:15743 · `percentage-circle` 1544:15802 · `chart-square` 1544:15850 · `moneys` 1544:15899 · `coin` 1544:15952 · `receipt-edit` 1544:15995 · `money-tick` 1544:16048 · `discount-shape` 1544:16103 · `receipt-search` 1544:16152 · `money-add` 1544:16203 · `convert-card` 1544:16265 · `discount-circle` 1544:16328 · `wallet-2` 1544:16382 · `money-remove` 1544:16424 · `wallet-money` 1544:16486 · `card-remove` 1544:16536 · `cards` 1544:16594 · `money-forbidden` 1544:16649 · `wallet-3` 1544:16703 · `card-tick` 1544:16752 · `receipt-2` 1544:16803 · `receipt` 1544:16846 · `money-change` 1544:16882 · `wallet-remove` 1544:16945 · `money-time` 1544:17007 · `receipt-text` 1544:17061 · `strongbox` 1544:17110 · `wallet` 1544:17154 · `security-card` 1544:17196 · `money-recive` 1544:17250 · `money-send` 1544:17314 · `archive` 1544:17370 · `tag` 1544:17427 · `tag-2` 1544:17463 · `coin` 1544:17504 · `document` 1544:17555 · `wallet` 1544:17596 · `card-add` 1544:17651 · `card-remove` 1544:17708 · `card-tick` 1544:17765 · `card-slash` 1544:17817 · `card-pos` 1544:17880 · `card` 1544:17933 · `card-receive` 1544:17981 · `card-send` 1544:18038 · `card-edit` 1544:18095 · `wallet-minus` 1544:18152 · `wallet-add` 1544:18210 · `dollar-square` 1544:18273 · `dollar-circle` 1544:18316 · `receipt` 1544:18359 · `receipt-2` 1544:18400 · `receipt-disscount` 1544:18451 · `ticket` 1544:18498 · `ticket-star` 1544:18536 · `ticket-expired` 1544:18581 · `ticket-2` 1544:18622 · `ticket-discount` 1544:18666 · `math` 1544:18712 · `textalign-left` 1544:18778 · `textalign-center` 1544:18828 · `textalign-right` 1544:18878 · `textalign-justifyright` 1544:18930 · `textalign-justifycenter` 1544:18981 · `textalign-justifyleft` 1544:19031 · `firstline` 1544:19081 · `paperclip-2` 1544:19137 · `paperclip` 1544:19170 · `link` 1544:19203 · `link` 1544:19247 · `link-2` 1544:19287 · `text-block` 1544:19327 · `text-italic` 1544:19368 · `text` 1544:19409 · `smallcaps` 1544:19450 · `text-bold` 1544:19505 · `text-underline` 1544:19543 · `pharagraphspacing` 1544:19581 · `maximize` 1544:19634 · `eraser` 1544:19691 · `attach-square` 1544:19735 · `attach-circle` 1544:19775 · `quote-up` 1544:19815 · `quote-down` 1544:19869 · `quote-up-square` 1544:19923 · `quote-down-square` 1544:19979 · `quote-down-circle` 1544:20035 · `quote-up-circle` 1544:20091 · `link` 1544:20147 · `link-square` 1544:20187 · `link-circle` 1544:20234 · `translate` 1544:20277 · `language-square` 1544:20361 · `language-circle` 1544:20412 · `received` 1544:20470 · `refresh-circle` 1544:20520 · `repeat-circle` 1544:20573 · `repeat` 1544:20626 · `arrange-circle-2` 1544:20675 · `arrange-circle` 1544:20730 · `refresh` 1544:20785 · `export` 1544:20824 · `import` 1544:20866 · `import` 1544:20908 · `export` 1544:20950 · `logout` 1544:20992 · `login` 1544:21035 · `import` 1544:21078 · `export` 1544:21121 · `export` 1544:21164 · `import` 1544:21208 · `logout` 1544:21252 · `login` 1544:21296 · `receive-square-2` 1544:21340 · `send-sqaure-2` 1544:21389 · `send-square` 1544:21438 · `receive-square` 1544:21487 · `refresh-left-square` 1544:21538 · `refresh-right-square` 1544:21585 · `refresh-square-2` 1544:21632 · `forward-square` 1544:21672 · `back-square` 1544:21715 · `arrange-square-2` 1544:21758 · `arrange-square` 1544:21813 · `convert` 1544:21868 · `arrow-down` 1544:21909 · `arrow-left` 1544:21950 · `arrow-right` 1544:21991 · `arrow-up` 1544:22032 · `arrow-bottom` 1544:22073 · `arrow-up` 1544:22106 · `arrow-right` 1544:22139 · `arrow-left` 1544:22172 · `refresh-2` 1544:22205 · `rotate-right` 1544:22238 · `rotate-left` 1544:22278 · `redo` 1544:22318 · `undo` 1544:22355 · `arrow-swap-horizontal` 1544:22392 · `arrow-swap` 1544:22440 · `arrow-circle-up` 1544:22488 · `arrow-circle-down` 1544:22524 · `arrow-circle-right` 1544:22560 · `arrow-circle-left` 1544:22596 · `arrow-left` 1544:22632 · `arrow-right` 1544:22665 · `arrow-down` 1544:22698 · `arrow-up` 1544:22731 · `arrow-down` 1544:22764 · `arrow-up` 1544:22801 · `arrow-left` 1544:22838 · `arrow-right` 1544:22875 · `arrow-square-left` 1544:22912 · `arrow-square-right` 1544:22948 · `arrow-square-down` 1544:22984 · `arrow-square-up` 1544:23020 · `arrow-3` 1544:23056 · `arrow-2` 1544:23106 · `send` 1544:23157 · `moon` 1544:23212 · `sun` 1544:23244 · `cloud` 1544:23281 · `cloud-plus` 1544:23319 · `cloud-minus` 1544:23370 · `cloud-cross` 1544:23416 · `cloud-sunny` 1544:23467 · `cloud-notif` 1544:23512 · `cloud-drizzle` 1544:23554 · `cloud-snow` 1544:23612 · `cloud-lightning` 1544:23666 · `flash` 1544:23712 · `drop` 1544:23764 · `wind` 1544:23798 · `wind-2` 1544:23845 · `cloud-fog` 1544:23892 · `sun-fog` 1544:23952 · `Snow` 1544:24010 · `user` 1544:24108 · `user-add` 1544:24145 · `user-remove` 1544:24199 · `user-tick` 1544:24252 · `user-minus` 1544:24301 · `user-search` 1544:24348 · `user-edit` 1544:24396 · `user-tag` 1544:24444 · `user-octagon` 1544:24488 · `user-cirlce-add` 1544:24532 · `user-square` 1544:24593 · `profile` 1544:24636 · `profile-2user` 1544:24673 · `profile-remove` 1544:24722 · `profile-tick` 1544:24764 · `profile-add` 1544:24806 · `profile-delete` 1544:24853 · `profile-circle` 1544:24900 · `tag-user` 1544:24942 · `people` 1544:24991 · `folder` 1544:25062 · `folder-cross` 1544:25096 · `folder-add` 1544:25139 · `folder-minus` 1544:25182 · `folder-favorite` 1544:25220 · `folder-2` 1544:25258 · `folder-open` 1544:25296 · `folder-cloud` 1544:25336 · `directbox-default` 1544:25382 · `directbox-default-2` 1544:25422 · `directbox-receive` 1544:25472 · `directbox-send` 1544:25526 · `direct-normal` 1544:25580 · `direct` 1544:25618 · `direct-notification` 1544:25667 · `direct-inbox` 1544:25712 · `direct-send` 1544:25762 · `message` 1544:25812 · `message-favorite` 1544:25859 · `message-notif` 1544:25913 · `message-search` 1544:25967 · `message-text` 1544:26029 · `device-message` 1544:26072 · `messages` 1544:26138 · `messages-2` 1544:26181 · `messages-3` 1544:26218 · `sms` 1544:26255 · `sms-tracking` 1544:26292 · `sms-notification` 1544:26340 · `sms-edit` 1544:26386 · `sms-star` 1544:26437 · `sms-search` 1544:26484 · `message-remove` 1544:26534 · `message-add` 1544:26588 · `message-tick` 1544:26642 · `message-time` 1544:26692 · `message-2` 1544:26742 · `messages` 1544:26779 · `message-circle` 1544:26836 · `message-square` 1544:26872 · `message-text` 1544:26908 · `message-minus` 1544:26952 · `message-add` 1544:26990 · `message-edit` 1544:27034 · `bezier` 1544:27083 · `brush` 1544:27155 · `brush-2` 1544:27205 · `magicpen` 1544:27248 · `pen-tool` 1544:27303 · `bucket` 1544:27382 · `paintbucket` 1544:27438 · `additem` 1544:27480 · `ruler` 1544:27528 · `designtools` 1544:27579 · `shapes` 1544:27643 · `lifebuoy` 1544:27680 · `pen-tool-2` 1544:27735 · `brush-square` 1544:27817 · `pen-close` 1544:27863 · `pen-add` 1544:27933 · `pen-remove` 1544:28003 · `path` 1544:28069 · `path-2` 1544:28111 · `bucket-circle` 1544:28156 · `bucket-square` 1544:28209 · `brush-4` 1544:28262 · `scissor` 1544:28310 · `glass` 1544:28357 · `ruler&pen` 1544:28394 · `color-swatch` 1544:28457 · `blend-2` 1544:28507 · `path-square` 1544:28557 · `omega-circle` 1544:28604 · `omega-square` 1544:28641 · `shapes` 1544:28678 · `size` 1544:28715 · `flash-circle` 1544:28752 · `eraser` 1544:28791 · `mask` 1544:28844 · `blur` 1544:28898 · `blend` 1544:28952 · `colorfilter` 1544:28989 · `colors-square` 1544:29031 · `mask` 1544:29080 · `brush` 1544:29115 · `layer` 1544:29154 · `copy` 1544:29197 · `copy-success` 1544:29234 · `recovery-convert` 1544:29275 · `main-component` 1544:29322 · `component` 1544:29367 · `mask` 1544:29398 · `forward-item` 1544:29448 · `backward-item` 1544:29491 · `location-minus` 1544:29538 · `location-cross` 1544:29574 · `location-tick` 1544:29615 · `location-slash` 1544:29651 · `discover` 1544:29699 · `location` 1544:29735 · `location-add` 1544:29771 · `radar` 1544:29812 · `radar-2` 1544:29846 · `global-search` 1544:29883 · `global-edit` 1544:29960 · `global-refresh` 1544:30040 · `global` 1544:30128 · `direct-up` 1544:30194 · `direct-down` 1544:30227 · `direct-left` 1544:30260 · `direct-right` 1544:30293 · `map` 1544:30326 · `gps` 1544:30380 · `gps-slash` 1544:30436 · `map` 1544:30505 · `routing` 1544:30548 · `routing-2` 1544:30603 · `arrow-square` 1544:30656 · `picture-frame` 1544:30707 · `arrow` 1544:30750 · `route-square` 1544:30818 · `bag` 1544:30862 · `bag-happy` 1544:30917 · `bag-tick` 1544:30969 · `bag-cross` 1544:31020 · `bag-timer` 1544:31075 · `bag-tick-2` 1544:31122 · `bag-cross` 1544:31169 · `bag-2` 1544:31221 · `shopping-cart` 1544:31265 · `shopping-bag` 1544:31315 · `shop-add` 1544:31357 · `shop-remove` 1544:31429 · `shop` 1544:31493 · `barcode` 1544:31547 · `3d-rotate` 1544:31624 · `3d-square` 1544:31690 · `truck-remove` 1544:31740 · `truck-time` 1544:31816 · `truck-tick` 1544:31884 · `truck-fast` 1544:31952 · `truck` 1544:32027 · `box-search` 1544:32082 · `box` 1544:32146 · `box-time` 1544:32202 · `box-tick` 1544:32264 · `box-remove` 1544:32326 · `box-add` 1544:32395 · `convert-3d-cube` 1544:32461 · `3d-cube-scan` 1544:32550 · `box` 1544:32610 · `search-normal` 1544:32658 · `search-zoom-in` 1544:32695 · `search-zoom-out` 1544:32742 · `search-favorite` 1544:32784 · `search-status` 1544:32827 · `search-normal` 1544:32875 · `search-zoom-in` 1544:32912 · `search-zoom-out` 1544:32959 · `search-favorite` 1544:33001 · `search-status` 1544:33044 · `aquarius` 1544:33097 · `gemini` 1544:33138 · `gemini-2` 1544:33189 · `sagittarius` 1544:33243 · `vuesax` 1544:33285 · `woman` 1544:33326 · `building` 1544:33375 · `courthouse` 1544:33433 · `house` 1544:33493 · `house-2` 1544:33551 · `buildings` 1544:33605 · `bank` 1544:33668 · `buildings-2` 1544:33743 · `building-3` 1544:33804 · `building-4` 1544:33865 · `buliding` 1544:33929 · `hospital` 1544:34003 · `chart-success` 1544:34062 · `chart-fail` 1544:34125 · `chart-2` 1544:34184 · `graph` 1544:34226 · `activity` 1544:34265 · `home-trend-up` 1544:34302 · `home-trend-down` 1544:34345 · `home-hashtag` 1544:34388 · `trend-up` 1544:34438 · `trend-down` 1544:34481 · `hashtag` 1544:34524 · `chart` 1544:34574 · `personalcard` 1544:34623 · `status-up` 1544:34681 · `diagram` 1544:34738 · `presention-chart` 1544:34779 · `chart` 1544:34833 · `health` 1544:34889 · `chart` 1544:34928 · `favorite-chart` 1544:34977 · `call` 1544:35026 · `call-calling` 1544:35061 · `call-incoming` 1544:35108 · `call-outgoing` 1544:35148 · `call-add` 1544:35188 · `call-minus` 1544:35234 · `call-remove` 1544:35274 · `call-received` 1544:35320 · `call-slash` 1544:35360 · `cpu` 1544:35409 · `cpu-charge` 1544:35506 · `cpu-setting` 1544:35607 · `printer` 1544:35696 · `printer-slash` 1544:35749 · `monitor` 1544:35817 · `monitor-recorder` 1544:35861 · `monitor-mobbile ` 1544:35915 · `headphone` 1544:35970 · `airpod` 1544:36006 · `speaker` 1544:36052 · `driver` 1544:36094 · `driver` 1544:36167 · `driver-refresh` 1544:36241 · `cloud-add` 1544:36312 · `cloud-remove` 1544:36361 · `external-drive` 1544:36418 · `cloud-connection` 1544:36477 · `music-play` 1544:36531 · `devices` 1544:36577 · `airpods` 1544:36648 · `headphones` 1544:36709 · `folder-connection` 1544:36785 · `game` 1544:36833 · `weight` 1544:36900 · `keyboard` 1544:36936 · `mouse` 1544:36987 · `clock` 1544:37028 · `ram` 1544:37076 · `ram-2` 1544:37118 · `simcard` 1544:37173 · `simcard-2` 1544:37221 · `lamp` 1544:37258 · `mobile` 1544:37299 · `electricity` 1544:37338 · `mirroring-screen` 1544:37384 · `microscope` 1544:37437 · `simcard` 1544:37494 · `keyboard-open` 1544:37541 · `airdrop` 1544:37605 · `gameboy` 1544:37657 · `watch` 1544:37714 · `watch-status` 1544:37765 · `bluetooth` 1544:37832 · `bluetooth-2` 1544:37868 · `bluetooth-circle` 1544:37916 · `bluetooth-rectangle` 1544:37954 · `cloud-change` 1544:37993 · `star` 1544:38051 · `star-slash` 1544:38083 · `heart` 1544:38127 · `like` 1544:38159 · `dislike` 1544:38197 · `star` 1544:38235 · `ranking` 1544:38288 · `magic-star` 1544:38344 · `heart-edit` 1544:38387 · `heart-tick` 1544:38433 · `heart-search` 1544:38479 · `heart-slash` 1544:38526 · `heart-remove` 1544:38570 · `heart-add` 1544:38620 · `smileys` 1544:38673 · `like-dislike` 1544:38742 · `like-tag` 1544:38797 · `24-support` 1544:38840 · `like-shapes` 1544:38887 · `message-question` 1544:38931 · `medal-star` 1544:38974 · `lovely` 1544:39017 · `medal` 1544:39061 · `unlimited` 1544:39098 · `like` 1544:39134 · `heart-circle` 1544:39173 · `timer` 1544:39214 · `clock` 1544:39248 · `timer` 1544:39284 · `timer-pause` 1544:39326 · `timer-start` 1544:39379 · `security-time` 1544:39428 · `calendar` 1544:39478 · `calendar-tick` 1544:39559 · `calendar-search` 1544:39631 · `calendar-remove` 1544:39700 · `calendar-add` 1544:39776 · `calendar-edit` 1544:39852 · `calendar-2` 1544:39923 · `calendar-circle` 1544:39987 · `calendar` 1544:40040 · `trash` 1544:40098 · `battery-empty` 1544:40151 · `battery-empty 2` 1544:40188 · `battery-2` 1544:40230 · `battery-full` 1544:40277 · `battery-charging` 1544:40329 · `battery-disable` 1544:40377 · `home` 1544:40426 · `home-2` 1544:40462 · `more-square` 1544:40498 · `tick-circle` 1544:40544 · `add-circle` 1544:40581 · `minus-cirlce` 1544:40624 · `close-circle` 1544:40661 · `more-circle` 1544:40703 · `info-circle` 1544:40749 · `danger` 1544:40790 · `add` 1544:40831 · `minus` 1544:40869 · `add-square` 1544:40902 · `minus-square` 1544:40944 · `tick-square` 1544:40981 · `close-square` 1544:41018 · `sort` 1544:41060 · `send` 1544:41103 · `send-2` 1544:41139 · `share` 1544:41176 · `share` 1544:41237 · `flash-slash` 1544:41269 · `flash-circle` 1544:41313 · `slash` 1544:41349 · `cake` 1544:41388 · `grammerly` 1544:41455 · `crown` 1544:41493 · `crown-2` 1544:41526 · `close` 1544:41568 · `flag` 1544:41611 · `flag-2` 1544:41649 · `cup` 1544:41687 · `emoji-happy` 1544:41743 · `emoji-normal` 1544:41789 · `emoji-sad` 1544:41835 · `tag-cross` 1544:41881 · `menu` 1544:41923 · `cd` 1544:41966 · `chart` 1544:41999 · `archive` 1544:42040 · `chrome` 1544:42083 · `instagram` 1544:42135 · `coffee` 1544:42176 · `pet` 1544:42235 · `happyemoji` 1544:42290 · `reserve` 1544:42326 · `sticker` 1544:42373 · `computing` 1544:42410 · `verify` 1544:42462 · `information` 1544:42498 · `auto-brightness` 1544:42540 · `triangle` 1544:42583 · `3dcube` 1544:42627 · `glass` 1544:42670 · `discover` 1544:42721 · `weight` 1544:42757 · `filter` 1544:42812 · `filter-square` 1544:42849 · `sound` 1544:42885 · `story` 1544:42941 · `slider` 1544:42994 · `status` 1544:43045 · `wifi-square` 1544:43088 · `box-2` 1544:43140 · `trush-square` 1544:43193 · `wifi` 1544:43241 · `speedometer` 1544:43298 · `diamonds` 1544:43342 · `level` 1544:43378 · `judge` 1544:43424 · `lamp` 1544:43476 · `tree` 1544:43518 · `bubble` 1544:43565 · `mirror` 1544:43614 · `tag-right` 1544:43653 · `milk` 1544:43686 · `ghost` 1544:43735 · `ranking` 1544:43777 · `mouse-square` 1544:43828 · `mouse-circle` 1544:43866 · `mouse` 1544:43904 · `forbidden` 1544:43940 · `forbidden-2` 1544:43981 · `warning-2` 1544:44022 · `broom` 1544:44065 · `signpost` 1544:44123 · `filter-remove` 1544:44174 · `filter-add` 1544:44227 · `filter-search` 1544:44277 · `filter-edit` 1544:44324 · `filter-tick` 1544:44371 · `home` 1544:44414 · `smart-home` 1544:44450 · `home-wifi` 1544:44502 · `safe-home` 1544:44555 · `archive-tick` 1544:44596 · `archive` 1544:44632 · `archive-slash` 1544:44671 · `archive-add` 1544:44715 · `archive-minus` 1544:44756 · `receipt-square` 1544:44792 · `book-square` 1544:44828 · `save-2` 1544:44872 · `save-add` 1544:44912 · `save-minus` 1544:44959 · `save-remove` 1544:45002 · `book-saved` 1544:45049 · `category` 1544:45095 · `category-2` 1544:45144 · `setting` 1544:45193 · `setting-2` 1544:45229 · `setting-3` 1544:45266 · `setting-4` 1544:45328 · `setting-5` 1544:45391 · `more` 1544:45469 · `more-2` 1544:45511 · `toggle-off` 1544:45553 · `toggle-on` 1544:45589 · `toggle-off-circle` 1544:45625 · `toggle-on-circle` 1544:45661 · `menu` 1544:45697 · `candle` 1544:45748 · `settings` 1544:45801 · `candle-2` 1544:45846 · `sidebar-bottom` 1544:45904 · `sidebar-top` 1544:45947 · `sidebar-right` 1544:45989 · `sidebar-left` 1544:46031 · `scroll` 1544:46073 · `hashtag-down` 1544:46114 · `hashtag` 1544:46176 · `hashtag-up` 1544:46223 · `code` 1544:46285 · `code` 1544:46332 · `mobile-programming` 1544:46373 · `message-programming` 1544:46421 · `document-code-2` 1544:46470 · `programming-arrows` 1544:46517 · `hierarchy-3` 1544:46573 · `code-circle` 1544:46622 · `document-code` 1544:46671 · `data-2` 1544:46720 · `data` 1544:46787 · `hierarchy-square-3` 1544:46848 · `hierarchy-square-2` 1544:46901 · `hierarchy-square` 1544:46954 · `command-square` 1544:47015 · `hierarchy-2` 1544:47072 · `hierarchy` 1544:47127 · `programming-arrow` 1544:47181 · `command` 1544:47235 · `notification-bing` 1544:47294 · `notification` 1544:47336 · `notification` 1544:47378 · `notification-favorite` 1544:47416 · `notification-status` 1544:47459 · `notification-circle` 1544:47507 · `lamp-on` 1544:47545 · `lamp-charge` 1544:47582 · `lamp-slash` 1544:47624 · `menu-board` 1544:47677 · `note-favorite` 1544:47741 · `note-text` 1544:47808 · `archive-book` 1544:47866 · `document-filter` 1544:47915 · `bill` 1544:47967 · `task-square` 1544:48024 · `task` 1544:48074 · `note-add` 1544:48136 · `stickynote` 1544:48189 · `note-remove` 1544:48250 · `note` 1544:48314 · `creative-commons` 1544:48367 · `copyright` 1544:48410 · `edit-2` 1544:48447 · `edit` 1544:48491 · `document-like` 1544:48533 · `document-text` 1544:48579 · `note` 1544:48632 · `clipboard-import` 1544:48685 · `clipboard-export` 1544:48737 · `clipboard-close` 1544:48789 · `clipboard-tick` 1544:48837 · `clipboard-text` 1544:48886 · `document-normal` 1544:48934 · `document-copy` 1544:48972 · `document-cloud` 1544:49025 · `document-sketch` 1544:49080 · `document-previous` 1544:49122 · `document-forward` 1544:49171 · `document-upload` 1544:49216 · `document-download` 1544:49265 · `document-favorite` 1544:49314 · `document-text` 1544:49357 · `document` 1544:49406 · `security` 1544:49448 · `security-safe` 1544:49482 · `radar` 1544:49525 · `alarm` 1544:49582 · `lock-circle` 1544:49636 · `lock` 1544:49683 · `security-user` 1544:49738 · `scanner` 1544:49785 · `finger-cricle` 1544:49837 · `finger-scan` 1544:49882 · `scanning` 1544:49948 · `scan-barcode` 1544:50020 · `scan` 1544:50092 · `lock-slash` 1544:50155 · `unlock` 1544:50204 · `lock` 1544:50245 · `check` 1544:50286 · `key-square` 1544:50334 · `key` 1544:50379 · `shield-search` 1544:50418 · `password-check` 1544:50461 · `shield-security` 1544:50513 · `shield-slash` 1544:50553 · `shield-cross` 1544:50596 · `shield-tick` 1544:50636 · `shield` 1544:50671 · `eye-slash` 1544:50703 · `eye` 1544:50762 · `bitcoin-refresh` 1544:50802 · `bitcoin-convert` 1544:50870 · `bitcoin-card` 1544:50945 · `buy-crypto` 1544:51021 · `trade` 1544:51063 · `card-coin` 1544:51112 · `kanban` 1544:51176 · `fatrows` 1544:51213 · `row-vertical` 1544:51250 · `row-horizontal` 1544:51287 · `slider-horizontal` 1544:51324 · `slider-vertical` 1544:51367 · `slider-vertical` 1544:51410 · `slider-horizontal` 1544:51453 · `grid-4` 1544:51496 · `grid-9` 1544:51533 · `grid-2` 1544:51570 · `grid-3` 1544:51616 · `grid-5` 1544:51666 · `grid-6` 1544:51710 · `grid-7` 1544:51760 · `grid-8` 1544:51804 · `grid-1` 1544:51866 · `element-2` 1544:51930 · `element-1` 1544:51973 · `element-3` 1544:52016 · `element-4` 1544:52065 · `element-plus` 1544:52114 · `element-equal` 1544:52168 · `3square` 1544:52222 · `align-vertically` 1544:52264 · `align-horizontally` 1544:52324 · `align-left` 1544:52384 · `align-right` 1544:52427 · `align-top` 1544:52470 · `align-bottom` 1544:52513 · `maximize` 1544:52556 · `maximize-2` 1544:52608 · `maximize-3` 1544:52654 · `maximize-4` 1544:52699 · `format-circle` 1544:52746 · `format-square` 1544:52796 · `rotate-left` 1544:52846 · `rotate-right` 1544:52882 · `crop` 1544:52918 · `maximize` 1544:52968 · `convertshape` 1544:53015 · `convertshape-2` 1544:53063 · `grid-eraser` 1544:53111 · `grid-lock` 1544:53188 · `grid-edit` 1544:53265 · `calculator` 1544:53348 · `gift` 1544:53413 · `teacher` 1544:53467 · `note-2` 1544:53507 · `note` 1544:53553 · `clipboard` 1544:53589 · `bookmark-2` 1544:53630 · `book` 1544:53667 · `book` 1544:53713 · `award` 1544:53760 · `bookmark` 1544:53801 · `brifecase-cross` 1544:53845 · `brifecase-tick` 1544:53905 · `brifecase-timer` 1544:53960 · `briefcase` 1544:54015 · `microphone` 1544:54067 · `microphone-slash` 1544:54112 · `microphone-2` 1544:54170 · `microphone-slash-2` 1544:54220 · `volume-cross` 1544:54284 · `volume-slash` 1544:54327 · `volume-up` 1544:54382 · `volume-low` 1544:54426 · `volume-low` 1544:54465 · `volume-high` 1544:54503 · `volume-mute` 1544:54548 · `video` 1544:54580 · `video-slash` 1544:54621 · `video-square` 1544:54673 · `video-circle` 1544:54709 · `gallery` 1544:54745 · `gallery-favorite` 1544:54788 · `gallery-slash` 1544:54837 · `gallery-tick` 1544:54894 · `gallery-import` 1544:54943 · `gallery-export` 1544:54997 · `gallery-add` 1544:55051 · `gallery-remove` 1544:55105 · `gallery-edit` 1544:55159 · `image` 1544:55213 · `screenmirroring` 1544:55250 · `camera` 1544:55286 · `camera-slash` 1544:55327 · `play` 1544:55382 · `record` 1544:55415 · `stop` 1544:55448 · `musicnote` 1544:55481 · `music` 1544:55521 · `video-vertical` 1544:55568 · `video-horizontal` 1544:55646 · `video-play` 1544:55724 · `subtitle` 1544:55776 · `play-circle` 1544:55827 · `record-circle` 1544:55863 · `stop-circle` 1544:55899 · `pause-circle` 1544:55935 · `pause` 1544:55976 · `scissor` 1544:56013 · `backward` 1544:56064 · `forward` 1544:56101 · `previous` 1544:56139 · `next` 1544:56179 · `radio` 1544:56219 · `music-circle` 1544:56281 · `play-cricle` 1544:56360 · `play-remove` 1544:56415 · `play-add` 1544:56471 · `backward-5-seconds` 1544:56530 · `backward-10-seconds` 1544:56573 · `backward-15-seconds` 1544:56624 · `forward-5-seconds` 1544:56675 · `forward-10-seconds` 1544:56719 · `forward-15-seconds` 1544:56773 · `music-playlist` 1544:56829 · `music-filter` 1544:56897 · `music-dashboard` 1544:56969 · `music-square-remove` 1544:57028 · `music-square-add` 1544:57102 · `music-square-search` 1544:57176 · `repeate-music` 1544:57243 · `repeate-one` 1544:57287 · `shuffle` 1544:57332 · `volume` 1544:57385 · `music-library-2` 1544:57483 · `music-square` 1544:57547 · `audio-square` 1544:57600 · `note-square` 1544:57648 · `mini-music-sqaure` 1544:57698 · `video-add` 1544:57753 · `video-remove` 1544:57821 · `video-tick` 1544:57892 · `video-time` 1544:57955 · `video-octagon` 1544:58018 · `voice-square` 1544:58054 · `voice-cricle` 1544:58119 · `maximize-circle` 1544:58184 · `airplane` 1544:58248 · `car` 1544:58280 · `bus` 1544:58344 · `smart-car` 1544:58400 · `driving` 1544:58480 · `ship` 1544:58572 · `airplane-square` 1544:58620 · `gas-station` 1544:58656

</details>

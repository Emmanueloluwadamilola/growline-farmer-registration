---
name: GrowLine
description: Spray-timing advice by plain SMS, onboarding Ogun State tomato farmers in about 3 minutes.
colors:
  paper: "#F6F2E9"
  surface: "#FFFFFF"
  field: "#FDFCF8"
  sand: "#F4F0E5"
  sand-deep: "#ECE6D8"
  track: "#E6E0D2"
  ink: "#122015"
  ink-soft: "#3E4A40"
  line: "#D8D1C1"
  line-strong: "#6F7768"
  leaf: "#1B5E34"
  leaf-deep: "#0F3A20"
  leaf-tint: "#E5F0E3"
  night: "#0E1711"
  night-soft: "#B9C6B6"
  tomato: "#C2311B"
  tomato-deep: "#962413"
  lime: "#D3EC6B"
  error: "#A3200F"
  error-tint: "#FDECE8"
  sun: "#F2B705"
typography:
  display:
    fontFamily: "Bricolage Grotesque, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "clamp(40px, 11vw, 92px)"
    fontWeight: 750
    lineHeight: 0.98
    letterSpacing: "-0.03em"
  headline:
    fontFamily: "Bricolage Grotesque, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "clamp(32px, 8vw, 60px)"
    fontWeight: 750
    lineHeight: 1.1
    letterSpacing: "-0.03em"
  title:
    fontFamily: "Bricolage Grotesque, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "28px"
    fontWeight: 750
    lineHeight: 1.1
    letterSpacing: "-0.02em"
  wordmark:
    fontFamily: "Bricolage Grotesque, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "min(20.5vw, 262px)"
    fontWeight: 800
    lineHeight: 0.8
    letterSpacing: "-0.03em"
  body-lead:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Noto Sans, Helvetica, Arial, sans-serif"
    fontSize: "19px"
    fontWeight: 400
    lineHeight: 1.5
  body:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Noto Sans, Helvetica, Arial, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Noto Sans, Helvetica, Arial, sans-serif"
    fontSize: "19px"
    fontWeight: 700
    lineHeight: 1.3
  button:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Noto Sans, Helvetica, Arial, sans-serif"
    fontSize: "18px"
    fontWeight: 700
    lineHeight: 1.2
rounded:
  pill: "999px"
  frame: "28px"
  panel: "24px"
  block: "20px"
  card: "16px"
  field: "14px"
  disc: "12px"
spacing:
  inset: "10px"
  gutter: "16px"
  field: "26px"
  section: "64px"
components:
  button-primary:
    backgroundColor: "{colors.tomato}"
    textColor: "{colors.surface}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "8px 8px 8px 22px"
    height: "56px"
  button-primary-hover:
    backgroundColor: "{colors.tomato-deep}"
  button-leaf:
    backgroundColor: "{colors.leaf}"
    textColor: "{colors.surface}"
    rounded: "18px"
    padding: "8px 22px 8px 10px"
    height: "64px"
  button-leaf-hover:
    backgroundColor: "{colors.leaf-deep}"
  button-outline:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.leaf}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "8px 22px"
    height: "56px"
  button-outline-hover:
    backgroundColor: "{colors.leaf-tint}"
  input-field:
    backgroundColor: "{colors.field}"
    textColor: "{colors.ink}"
    rounded: "{rounded.field}"
    padding: "12px 16px"
    height: "58px"
  choice-card:
    backgroundColor: "{colors.field}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: "12px 14px"
    height: "76px"
  choice-card-selected:
    backgroundColor: "{colors.leaf-tint}"
  band-action:
    backgroundColor: "{colors.tomato}"
    textColor: "{colors.surface}"
    rounded: "{rounded.frame}"
  panel-night:
    backgroundColor: "{colors.night}"
    textColor: "{colors.surface}"
    rounded: "{rounded.frame}"
  form-shell:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.panel}"
  faq-item:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "18px"
    height: "64px"
  faq-item-open:
    backgroundColor: "{colors.leaf}"
    textColor: "{colors.surface}"
  highlight-lime:
    backgroundColor: "{colors.lime}"
    textColor: "{colors.night}"
---

# Design System: GrowLine

## Overview

**Creative North Star: "The Message in the Field"**

GrowLine looks like an SMS arriving while you stand in your crop. Rounded photo frames sit inset on warm paper. The page moves through solid grounds in a fixed order: paper, then a tomato-red band, then a near-black night panel holding a white form, then a night footer with a giant lime wordmark. Each ground is a full rounded block inset 10px from the viewport edge. Nothing runs edge to edge. This blends two reference sites the user chose: the AgriSync layout language (inset photo hero, huge type, dark panel, giant wordmark footer) and the Tomato site's bold red bands.

The page has to work for an older farmer on a low-end Android phone, outdoors in bright sun, on slow 3G. That makes it dense in contrast but generous in size. Type is large, targets are tall, and every reading surface clears WCAG AA by a wide margin. The only expressive typeface is the display face. Body and form text use the system sans, so the page reads fully even if no web font, photo or map loads. Every photo sits on a solid colour.

Motion is a single, small event. On load the phone rises 24px and fades in, typing dots show for 900ms, then the message bubble pops in. Everything else is quick state feedback on a shared ease-out curve. Reduced motion shows the final state.

**Key Characteristics:**
- Inset rounded blocks (28px) on a warm paper ground (#F6F2E9). The cream ground is user-pinned, not a default.
- Ground switches, not shadows, carry the page's structure: paper, red band, night panel, white form.
- Tomato red is the single action colour. Leaf green is the brand and the "done/selected" colour.
- Lime is a highlight fill that always carries dark text.
- Pill CTAs with a lime arrow disc. Big, plain, sunlight-legible type.

## Colors

A sun-hardened palette: warm paper and deep greens, with one hot red for action and a lime spark for emphasis.

### Primary
- **Tomato Action Red** (`tomato`): The one action colour. Used on the primary pill CTA, the full "How it works" band, and the step-node icons. White text on it is 5.6:1. Hover and pressed states darken to **Fired Tomato** (`tomato-deep`), which also marks the "DO NOT spray" emphasis inside the SMS bubble.

### Secondary
- **Deep Leaf** (`leaf`): The brand green. Used for links, the "Mark my farm location" button, selected radio cards and segments, filled progress segments, the open FAQ item, the success message and the done card. **Forest Shade** (`leaf-deep`) is its hover state and the colour of section headings on paper.
- **Leaf Wash** (`leaf-tint`): Selected-card fill, icon tiles inside choice cards, outline-button hover, the loading message.

### Tertiary
- **Field Lime** (`lime`): A highlight fill. Used for the arrow disc on CTAs, the pin disc, step-number badges, the brand mark, the open-FAQ toggle, text selection, the skip link and config placeholders. It also appears as text on night and leaf grounds (the footer wordmark, the `strong` on the done card, links in an open FAQ).

### Neutral
- **Warm Paper** (`paper`): The page ground. User-pinned.
- **Clean Sheet** (`surface`): The form shell, FAQ items, nav pill, outline buttons.
- **Field Ink** (`ink`): Primary text on light grounds.
- **Soft Ink** (`ink-soft`): Secondary text and hints on paper (8.6:1).
- **Night Soil** (`night`): Dark panels (register panel, footer), the "then" pill on the red band, and the browser theme colour.
- **Night Mist** (`night-soft`): Secondary text on night (9.8:1).
- **Paper Rule** (`line`): Dividers between steps and about blocks, and the progress-bar bottom border.
- **Strong Rule** (`line-strong`): The 2px stroke on every input, choice card, consent box and dashed add-farm box.

### Status
- **Alarm Red** (`error`) on **Alarm Wash** (`error-tint`): Field errors and location errors. Always paired with a drawn warning icon and bold text, never colour alone.
- **Sun Ring** (`sun`): The focus ring on every ground.

### Named Rules
**The One Action Colour Rule.** Tomato means "do this". It goes on the CTA, the how-it-works band and nowhere decorative. Errors use the distinct, deeper `error` red with a tint and an icon, so an error never reads as a button.

**The Lime Carries Dark Ink Rule.** Lime is a fill under `night` or `leaf-deep` text, or a text colour only on `night` or `leaf` grounds. Never put lime text on paper or white, and never put white text on lime.

**The Sun Ring Rule.** Every focusable element gets the same 3px `sun` outline with a 3px offset (2px on fields and cards). It stays visible on paper, red, night, leaf and white grounds alike.

## Typography

**Display Font:** Bricolage Grotesque (opsz 12–96, wght 600–800, `display=swap`), falling back to system-ui
**Body Font:** system-ui, -apple-system, Segoe UI, Roboto, Noto Sans, Helvetica, Arial, sans-serif

**Character:** A chunky, slightly quirky optical grotesque for headings and the wordmark, set tight. The phone's own sans does all the reading and form work, so nothing practical waits on a font download.

### Hierarchy
- **Display** (750, clamp 40–92px, 0.98, −0.03em): The hero headline only. White, bottom-left over the photo gradient, at most 11ch wide.
- **Headline** (750, clamp 32–60px, 1.1, −0.03em): Section headings. The register panel heading scales up to clamp(36px, 10vw, 72px). The about headings scale down to clamp(28px, 6.4vw, 44px). Heading text uses `leaf-deep` on paper and white on red or night.
- **Title** (750, 28px, 1.1, −0.02em): Form step titles. The same voice carries farm titles (24px), the three how-it-works step names (23px, 30px on desktop) and the numerals in discs.
- **Wordmark** (800, min(20.5vw, 262px), 0.8): The lime GrowLine wordmark that closes the page. It is used once, in the footer.
- **Body Lead** (400, 19px, 1.5): The hero subhead, the lead about paragraph and the done message. Maximum about 33em.
- **Body** (400, 17px, 1.55): Default reading text. Supporting paragraphs on paper are 18px in `ink-soft`, about 36em wide. Hints are 16px, the floor.
- **Label** (700, 19px): Form labels and fieldset legends.
- **Button** (700, 18px, 1.2): All buttons. Big actions (location, submit) go to 19px. Text-link buttons are 17px, underlined at 2px with a 4px offset.

### Named Rules
**The Two Voices Rule.** Bricolage Grotesque is only for headings, the brand, the wordmark and numerals in discs. Everything a farmer reads or types uses the system sans. The page must stay fully usable with the display font blocked.

**The Sunlight Floor Rule.** Text never goes below 16px, form labels stay at 19px, and every control is at least 52px tall (inputs 58px, buttons 56–64px, choice cards 76px).

## Layout

Content sits in a centred wrap (max 1160px) with a 16px side gutter. The major blocks (hero frame, red band, night panel, footer) are inset 10px from the viewport edge, never full-bleed. Paper sections between them breathe at 64px vertical padding. The red band uses 56px top and 48px bottom on mobile, and 80px and 72px from 860px up. The form shell is capped at 720px inside the night panel. On phones under 520px, the panel narrows its own wrap to 8px so the form gets the width.

The design starts from mobile and stacks to a single column. Breakpoints observed in the build:
- **389px and below**: the hero nav, brand and phone stage tighten.
- **520px and below**: the register panel narrows its gutters.
- **560px**: radio choices go to two columns.
- **640px**: buttons stop being full-width.
- **860px**: about goes to two columns (1fr 1fr, 64px gap), and the 3-step path goes horizontal with a dashed connector.
- **900px**: the hero becomes a row with the phone at bottom-right, and the FAQ goes to 5fr/7fr with a sticky photo.

Form rhythm: fields are spaced 26px apart, steps are divided by a 2px `line` rule with 30px top padding, and the progress bar is sticky at the top of the form shell.

## Elevation & Depth

Depth comes mostly from switching grounds, not from shadows: paper, then the red band, then the night panel, then the white form shell, then the warm farm blocks (`sand`, #F4F0E5) inside it. Shadows are reserved for a few objects that physically sit above their ground.

### Shadow Vocabulary
- **CTA lift** (`box-shadow: 0 2px 4px rgba(14,23,17,.18), 0 10px 22px rgba(14,23,17,.16)`): The primary tomato pill only.
- **Shell drop** (`box-shadow: 0 30px 60px rgba(0,0,0,.35)`): The white form shell lifting off the night panel.
- **Node lift** (`box-shadow: 0 6px 16px rgba(14,23,17,.2)`): The white step nodes on the red band.
- **Segment lift** (`box-shadow: 0 2px 6px rgba(15,58,32,.25)`): The selected segment in the unit picker.
- **Hairline** (`box-shadow: 0 1px 2px rgba(14,23,17,.06)`): Closed FAQ items on paper.
- **Phone glow** (`box-shadow: 0 -2px 0 1px #3A4237 inset, 0 -18px 50px rgba(0,0,0,.35)`): The SMS phone rising out of the hero frame.

### Named Rules
**The Grounds Not Shadows Rule.** To separate a section, change its ground. Add a shadow only when an object sits on top of another surface: a button, the form shell, a node or a selected segment.

## Shapes

The shapes are soft and generous, and the radius steps down as surfaces nest. Frames are 28px (hero, band, panel, footer). Photos, the form shell and the done card are 24px. Farm blocks and the add-farm box are 20px. The FAQ items are 18px, and so is the location button. Choice cards are 16px, inputs and messages 14px, icon tiles and the pin disc 12px. CTAs and the nav link are full pills. Discs (arrow, brand mark, step nodes, numbered instruction markers, status icons) are true circles. The SMS bubble uses a speech-tail corner (20px with a 6px bottom-left corner).

Borders are thick and honest: 2px solid `line-strong` on every input and card, and 2px dashed for "add another" and for the step connectors on the red band.

**The Inset Frame Rule.** A major block is a rounded 28px frame inset 10px from the screen edge. If a new section needs its own ground, it becomes another inset frame, not a full-bleed stripe.

## Components

### Buttons
Big, round, thumb-first.
- **Shape:** Full pill (999px), at least 56px tall, full-width on phones and auto from 640px.
- **Primary:** Tomato with white 18px bold text and the CTA lift shadow. With an arrow, the label sits left and a 42px lime disc with a drawn night arrow sits right. On hover the fill goes to `tomato-deep` and the arrow nudges 3px and turns −45°.
- **Location (leaf):** Leaf green, 64px tall, 18px radius, left-aligned 19px text, led by a 46px lime pin tile (12px radius). Hover goes to `leaf-deep`.
- **Outline:** White with a 2px leaf border and leaf text. Hover fills with `leaf-tint`.
- **Text link button:** Leaf, bold 17px, 2px underline at a 4px offset, 48px tap height. `error` coloured for "remove".
- **Press / disabled:** All buttons scale to 0.98 on press. An `aria-disabled` primary goes to a pale tomato (#F2D9D2) with #7A2414 text and no shadow.

### Chips and highlights
- **Lime highlight:** A lime fill with night text and a 5px radius marks config placeholders. Lime also fills the step-number badges, which sit offset on the top-right of the step nodes.
- **"Then" pill:** A night pill on the red band with a 40px lime SMS disc. It closes the 3-step path.

### Cards / Containers
- **Form shell:** White, 24px radius, shell drop shadow, max 720px. It carries a sticky progress header: "Step N of 3: label" and a 3-segment bar, 8px tall, in leaf when filled and `track` (#E6E0D2) when empty.
- **Farm block:** A warm `sand` (#F4F0E5) fill, 20px radius, 22px/16px padding, with no border.
- **Add-farm box:** 2px dashed `line-strong`, 20px radius, 20px padding.
- **Done card:** Leaf ground, 24px radius, centred, with an 80px lime check disc.

### Inputs / Fields
- **Style:** Near-white `field` (#FDFCF8) fill, 2px `line-strong` stroke, 14px radius, 58px tall, 18px text. Selects use a drawn leaf chevron.
- **Focus:** On focus the border turns leaf, the fill goes to white and a 4px soft leaf halo appears (rgba(27,94,52,.15)). On keyboard focus the `sun` ring is added.
- **Error:** The border turns `error` on an `error-tint` fill, with a bold 16px `error` message led by a masked warning icon.
- **Choice cards (radio):** 76px tall, 16px radius, 2px stroke, a 48px leaf-tint icon tile and a 28px tick circle. When checked: leaf border plus a 1px inset leaf ring, a leaf-tint fill, a lime icon tile and a solid leaf tick with a white check.
- **Segmented picker:** A `sand-deep` (#ECE6D8) track with 16px radius and 4px padding, holding 52px segments with 12px radius. The selected segment is leaf with white text and the segment lift.
- **Consent box:** A choice-card-styled label with a 28px native checkbox in the leaf accent colour.

### Navigation
- **Hero nav:** The white brand (36px lime disc mark plus the 22px display wordmark) sits at the top-left of the hero frame. A white 44px pill link in night text sits at the top-right and turns lime on hover. There is no other site navigation. A lime skip link appears on focus.

### Location status message
A rounded 14px strip with a 26px status disc. It is announced through aria-live. Its states:
- **Loading:** leaf-tint fill, `leaf-deep` text and a spinner.
- **Success:** a solid leaf fill with 18px extra-bold white text and a lime check disc.
- **Error:** `error-tint` fill with a 2px inset #E9B4A9 ring.
- **Info:** a #FFF5D6 fill with #4D3B00 text and a 2px inset #EBD38A ring.

### FAQ accordion
White 18px-radius items, 64px minimum summary height, bold 18px. A 36px leaf-tint disc carries a drawn plus. When open, the whole item flips to leaf with light text, and the disc turns lime and rotates 45° into a close mark.

### Signature: the SMS phone
A dark phone (#1A1F1A, 40px top radius) rises out of the hero frame's bottom edge. On mobile it sits centre-bottom, from 900px bottom-right. Its screen shows a GrowLine thread: a leaf avatar with a lime "G", and a #E1E8DA tail bubble whose `strong` text is `tomato-deep`. It plays once on load (the rise, then the typing dots, then the pop) and shows its final state under reduced motion.

## Do's and Don'ts

### Do:
- **Do** set every major section as an inset 28px frame on `paper`, and change the ground (red, night, white) to start a new chapter.
- **Do** keep tomato for the single primary action per view, and pair it with the lime arrow disc.
- **Do** put dark text (`night` or `leaf-deep`) on every lime fill.
- **Do** keep body at 17px or more, labels at 19px and controls at 52px or taller, so the page reads outdoors in sun.
- **Do** use drawn inline SVG icons inside tinted or lime discs and tiles. Status messages always pair the icon with bold text.
- **Do** give every focusable element the 3px `sun` ring.
- **Do** run motion on the shared ease-out curve, cubic-bezier(.16, 1, .3, 1), and collapse it to the final state under reduced motion.

### Don't:
- **Don't** use tomato for errors or decoration. Errors use `error` with a tint and an icon.
- **Don't** set lime text on paper or white, or white text on lime.
- **Don't** use emoji or typed glyphs as icons. Icons are drawn SVG.
- **Don't** add eyebrow or kicker labels above headings. Step context lives in the sticky progress header and the screen-reader legend.
- **Don't** make anything essential depend on Bricolage Grotesque, a photo or the map loading. Every photo sits on a solid colour.
- **Don't** run blocks full-bleed or use shadows to separate sections.

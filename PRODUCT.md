# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Static: one self-contained HTML file (HTML + CSS + vanilla JS, no build step). Leaflet from a CDN only for the confirmation map pin. (Set by the user's original brief.)

## Users

Tomato farmers in Ogun State, South-West Nigeria, registering for the GrowLine pilot. Many are older, use mid-range or low-end Android phones on slow 3G/4G, and do not know terms like GPS, latitude or coordinates. Some register with help from an Extension Agent. They often stand in the middle of their farm, outdoors in bright sun, while filling in the form.

## Product Purpose

GrowLine sends a short SMS telling a farmer when it is safe to spray, based on the weather at their farm. This page onboards farmers into the pilot. It collects their details, the centre point of each farm (one tap while standing in the middle), and a size guess used to estimate the footprint. Success means a farmer finishes in about 3 minutes with a usable location.

## Positioning

Spray-timing advice by plain SMS for the farmer's own farm location. No smartphone is needed to receive it, and the pilot is free.

## Capabilities and Constraints

- Copy comes verbatim from the team's Word document (GrowLine Farmer Registration Landing Page.docx). Do not rewrite it or add marketing copy.
- Location needs HTTPS. Accuracy handling and the Extension Agent fallback are required.
- State and LGA come from the farm's GPS point (all 37 states and 774 LGAs, GRID3 boundaries in geo/, built by tools/geoprep.py). The farmer can correct them with "Not right? Change", and picks them by hand when there's no GPS point. The page now ships as index.html plus the geo/ folder (user decision, 2026-10-14).
- One farm per registration (user decision, 2026-10-14). A farmer with more farms registers again with the same phone number. The thank-you screen offers "Register another farm" and pre-fills their name, phone, LGA and town.
- 1 plot = 50 ft × 100 ft = 464.5 m², defined once. Call the area an "estimated footprint", never a "farm boundary".
- Registrations save to the GrowLine API (`POST https://glowlineapi.up.railway.app/farm/register-form/`). The old Apps Script receiver is kept in google-apps-script/ for reference. The FAQ contact details are still a placeholder.

## Brand Commitments

Name: GrowLine. Tomato red is the action colour; deep leaf green is the brand colour. Footer: "GrowLine · Pilot in Ogun State · Built by Group 8, AltSchool Africa". The user chose a visual blend of two reference sites in this folder: the AgriSync layout language (rounded inset photo hero, huge type, dark panel, giant wordmark footer) and the Tomato site's bold red bands. Lime is allowed as a highlight. Use 2–3 lightweight photos.

## Evidence on Hand

No real pilot data, testimonials, farmer counts or partner logos. Do not invent stats, testimonials or claims. Photos are illustrative stock, not GrowLine farmers.

## Product Principles

1. Plain words, big targets, and readable in sunlight.
2. Light enough for slow 3G. Nothing essential depends on an image, a font or a map loading.
3. Honest: no raw coordinates shown, an estimate labelled as an estimate, and no invented proof.

## Accessibility & Inclusion

WCAG AA or better, a 16px body minimum, form labels at 18px or more, controls at least 52px tall, full keyboard use, aria-live location status, and respect for reduced motion.

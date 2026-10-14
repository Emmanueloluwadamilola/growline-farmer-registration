# GrowLine · Farmer Registration

Pilot sign-up page for tomato farmers in Ogun State, Nigeria. GrowLine sends a short SMS saying when it is safe to spray, based on the weather at the farm. A farmer registers in about 3 minutes, marking the farm by standing in the middle of it and tapping one button.

Built by Group 8, AltSchool Africa.

## What's here

| Path | What it is |
|---|---|
| `index.html` | The page: HTML, CSS and vanilla JS, no build step. |
| `geo/` | State and LGA boundaries (GRID3 2022, CC BY 4.0) used to work out the State and LGA from the farm's GPS point. **Deploy next to `index.html`.** |
| `google-apps-script/` | `Code.gs` saves registrations to a Google Sheet. `SETUP.md` explains how to deploy it. |
| `tools/geoprep.py` | Rebuilds `geo/` from geoBoundaries' GRID3 GeoJSON. |
| `DATA_SCHEMA.md` | Every stored field and its type, the request format, and a suggested Postgres schema. |
| `PRODUCT.md`, `DESIGN.md` | Product notes and the design system. |

## Run locally

Location sharing only works on `https://` or `http://localhost`, so serve the folder rather than opening the file directly:

```bash
python3 -m http.server 8790
```

Then open http://localhost:8790.

## Configure

At the top of the `<script>` in `index.html`:

- `API_ENDPOINT`: the Apps Script web app URL (`…/exec`). Leave it empty for demo mode, which saves nothing.
- `CONTACT_TEXT` / `CONTACT_HREF`: fill in the `[contact]` placeholder in the FAQ.
- `PLOT_M2`: the size of one plot (464.5 m², 50 ft × 100 ft), used everywhere.

## Credits

State and LGA boundaries: GRID3 via geoBoundaries (CC BY 4.0). Satellite imagery © Esri. Photos: Unsplash.

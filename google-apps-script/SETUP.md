# Saving registrations to a Google Sheet

About 10 minutes. You need a Google account that will own the data. Use a team account, not a personal one, so access survives people leaving.

## 1. Create the sheet

1. Go to sheets.new and name it, for example **GrowLine Pilot Registrations**.
2. Open **Extensions → Apps Script**.
3. Delete what's in `Code.gs`, paste in the whole of [`Code.gs`](Code.gs) from this folder, and click **Save**.
4. Optional: choose `setup` in the function dropdown and click **Run**. This creates the two tabs with headers. If you skip this, they're created on the first registration. The first run asks you to authorise the script: choose your account, then **Advanced → Go to (project name)**, then **Allow**.

## 2. Deploy it as a web app

1. Click **Deploy → New deployment**.
2. Click the gear icon, choose **Web app**, and set:
   - **Execute as:** Me
   - **Who has access:** Anyone

   "Anyone" lets farmers' phones send data without a Google login. It does **not** let anyone read the sheet. The script only adds rows.
3. Click **Deploy** and copy the **Web app URL**. It ends in `/exec`.
4. Optional check: open that URL in a browser. You should see `{"ok":true,"service":"GrowLine registrations"}`.

## 3. Connect the page

In `index.html`, near the top of the `<script>`, paste the URL:

```js
var API_ENDPOINT = 'https://script.google.com/macros/s/XXXXXXXX/exec';
```

Host the page on HTTPS (location sharing needs it). Then do one test registration from a phone and check that the rows appear. Delete the test rows afterwards.

## What lands in the sheet

**Registrations** has one row per farmer: `registration_id`, `received_at`, `submitted_at`, name, phone (`+234…`), LGA, town, crop stage, consent, `needs_agent_help`, `farm_count`, `repeat_phone`, then `state`, `lga_source`, `detected_state` and `detected_lga`.

- `state` and `lga` come from the farm's GPS point, using GRID3 boundaries for all 37 states and 774 LGAs.
- `lga_source` says where they came from:
  - `gps`: detected and accepted;
  - `changed`: the farmer tapped "Not right? Change" and picked something else;
  - `chosen`: there was no GPS point, or detection failed, so the farmer picked by hand.
- `detected_state` and `detected_lga` keep what GPS gave, even when the farmer changed it. That makes border mistakes easy to review.
- LGA names follow GRID3 spelling, for example `Yewa North` and `Ado Odo/Ota`. Older rows may use the previous dropdown names, such as `Egbado North (Yewa North)`.

- The page registers **one farm per form**. A farmer with several farms submits once per farm with the same phone number, so filter by `phone_e164` to see all of one farmer's farms.
- `repeat_phone` is `yes` if this phone number already registered. That happens if someone registers twice, or taps again after a slow connection. Check these rows before contacting the farmer.

**Farms** has one row per farm, linked by `registration_id`. Each row has the farmer's name, phone and LGA, plus `lat`, `lng`, `gps_accuracy_m`, the size and unit, `estimated_area_m2`, `estimated_radius_m`, a Google Maps link, `estimated_perimeter_m`, and `estimated_footprint_geojson`.

- `estimated_footprint_geojson` holds 16 points on a circle around the farm centre, with the same area as the size the farmer gave. It's a GeoJSON Polygon of `[longitude, latitude]` pairs, and the last point repeats the first to close the ring. `estimated_perimeter_m` is that circle's perimeter.
- **These are estimates, not the farm's real edge.** We only know the centre and the size, not the shape or which way it faces, so never call them a "farm boundary". Phone GPS can also be off by 5–30 m.
- **To view the outlines on a map:** paste a cell's value into geojson.io. For GIS tools (QGIS, Google Earth via conversion), export the column.
- The column is empty for a farm with no location yet (`needs_agent_help = TRUE`).

- A farm with an empty location and `needs_agent_help = TRUE` needs an Extension Agent visit to mark it.

The script re-checks every registration (phone format, LGA, consent, GPS accuracy no worse than 100 m) and rejects anything malformed. Text that starts with `=`, `+`, `-` or `@` is stored as plain text, so nobody can inject a formula. This is also why phone numbers show a leading `'` in the edit bar.

## Updating the script later

**If your sheet was created before newer columns were added** (outline, state and LGA source), the script adds the new column names on the right of each tab on the next registration. Old rows keep their place.

**Deploy the page and the script together.** The current script rejects registrations without a `state`, so a phone with the old page still open would get the error message until it reloads.

After editing `Code.gs`, use **Deploy → Manage deployments → Edit (pencil) → Version: New version → Deploy**. That keeps the same URL. **New deployment** would give you a new URL, which you'd have to paste into the page again.

## Privacy

The sheet holds names, phone numbers and exact farm locations, which counts as personal data under Nigeria's Data Protection Act 2023.

- Share it only with the people who need it, as **Viewer** where possible. Never use "Anyone with the link".
- Use it only for what the consent box says: weather advice and improving the service.
- Agree who deletes it, and when, after the pilot ends.

## Limits worth knowing

- **Spam:** the form has a hidden spam-trap box (a "honeypot"). People never see it or reach it with the keyboard, and screen readers skip it. Bots that fill in every box fill it too. When it has text, the script answers "ok" but saves nothing, so the bot doesn't try again. This stops automated form-filling bots. It won't stop someone who reads the page's code and posts directly to the URL. If correct-looking fake rows still appear, a shared key or a rate limit can be added.
- **Volume:** Apps Script handles a pilot easily, up to thousands of registrations a day. Writes are queued, so two farmers submitting at once never mix rows.
- **First request:** the first registration after a quiet spell can take 2–5 seconds while Google starts the script. The page shows "Saving…" and waits up to 30 seconds.

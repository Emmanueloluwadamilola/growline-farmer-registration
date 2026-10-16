# GrowLine registration data

The request the page sends to the GrowLine API, plus what the old Google Sheet receiver (`google-apps-script/Code.gs`, no longer used by the page) stored.

The page itself stores nothing. Each submission writes **one row to `Registrations`** and **one row per farm to `Farms`**, linked by `registration_id`. The page registers **one farm per form**, so it's one Farms row per Registrations row; the script would accept up to 5. A farmer has no ID: `phone_e164` is what ties several registrations together. An empty cell means null.

## Tab 1: `Registrations` (16 columns)

| # | Column | Type | Null | Rules / notes | Example |
|---|---|---|---|---|---|
| 1 | `registration_id` | string, UUID v4 | no | Made by the script. Primary key. | `3f2b…9c1d` |
| 2 | `received_at` | datetime, ISO 8601 UTC | no | Time the script received it (server time). | `2026-10-14T08:53:20.491Z` |
| 3 | `submitted_at` | datetime, ISO 8601 UTC | no | Time the farmer tapped submit (phone time, may be wrong). | `2026-10-14T08:53:18.002Z` |
| 4 | `full_name` | string | no | 2–100 chars, trimmed, spaces collapsed. | `Bisi Ojo` |
| 5 | `phone_e164` | string | no | `^\+234(70\|80\|81\|90\|91)\d{8}$` | `+2348091112222` |
| 6 | `lga` | string | no | Must belong to `state` (see list). | `Abeokuta South` |
| 7 | `town_or_village` | string | no | 2–100 chars, typed by the farmer. | `Olodo` |
| 8 | `crop_stage` | enum | no | `vegetative`, `flowering`, `fruit_set`, `harvesting` | `flowering` |
| 9 | `consent` | boolean | no | Always `TRUE`; anything else is rejected. | `TRUE` |
| 10 | `needs_agent_help` | boolean | no | `TRUE` when the farm has no GPS point and the farmer asked for Extension Agent help. | `FALSE` |
| 11 | `farm_count` | integer | no | Farms in this submission. Now always `1`. | `1` |
| 12 | `repeat_phone` | string `yes`/`no` | no | `yes` if the phone was already in an earlier row when this one was saved. | `no` |
| 13 | `state` | string | no* | One of 37 (see list). | `Ogun` |
| 14 | `lga_source` | enum | no* | `gps`: detected and kept. `changed`: farmer used "Not right? Change". `chosen`: no GPS point or detection failed, so picked by hand. | `gps` |
| 15 | `detected_state` | string | yes | What GPS gave, even if the farmer changed it. Empty if nothing was detected. | `Ogun` |
| 16 | `detected_lga` | string | yes | Same, for the LGA. | `Abeokuta South` |

\* Null only in rows saved before these columns existed.

## Tab 2: `Farms` (18 columns)

| # | Column | Type | Null | Rules / notes | Example |
|---|---|---|---|---|---|
| 1 | `registration_id` | string, UUID | no | Links to `Registrations.registration_id`. | `3f2b…` |
| 2 | `farm_no` | integer | no | Position in the submission, 1-based. Now always `1`. | `1` |
| 3 | `full_name` | string | no | Copied from the registration. | `Bisi Ojo` |
| 4 | `phone_e164` | string | no | Copied from the registration. | `+2348091112222` |
| 5 | `lga` | string | no | Copied from the registration. | `Abeokuta South` |
| 6 | `town_or_village` | string | no | Copied from the registration. | `Olodo` |
| 7 | `lat` | decimal(9,6) | yes | −90 to 90. Empty when the farm wasn't marked. | `7.1557` |
| 8 | `lng` | decimal(9,6) | yes | −180 to 180. | `3.3451` |
| 9 | `gps_accuracy_m` | decimal, 1 dp | yes | Metres, 0–100. Worse readings are never saved. | `12.0` |
| 10 | `needs_agent_help` | boolean | no | `TRUE` when this farm has no GPS point. | `FALSE` |
| 11 | `size_value` | decimal | no | Greater than 0, at most 100,000, as typed. | `3` |
| 12 | `size_unit` | enum | no | `plots`, `acres`, `hectares` | `plots` |
| 13 | `estimated_area_m2` | decimal, 1 dp | no | size × unit (1 plot = 464.5 m², 1 acre = 4,046.86 m², 1 ha = 10,000 m²). | `1393.5` |
| 14 | `estimated_radius_m` | decimal, 1 dp | no | √(area / π) | `21.1` |
| 15 | `map_link` | string, URL | yes | `https://www.google.com/maps?q={lat},{lng}`. Empty without a point. | |
| 16 | `estimated_perimeter_m` | decimal, 1 dp | yes | 2πr | `132.3` |
| 17 | `estimated_footprint_geojson` | string, GeoJSON | yes | Polygon of 17 `[lng, lat]` points: 16 around the centre (north first, clockwise, every 22.5°) plus the first point again to close it. 6 decimals. Empty without a point. | `{"type":"Polygon","coordinates":[[…]]}` |
| 18 | `state` | string | yes* | Copied from the registration. | `Ogun` |

The footprint is an **estimate** made from the centre and the size, not a measured farm edge. Never call it a "boundary".

## Fixed lists

- **`state` and `lga`:** all 37 states (including `Federal Capital Territory`) and 774 LGAs, using GRID3 2022 spelling. The full list is in [`geo/names.json`](geo/names.json) as `{ "State": ["LGA", …] }`.
  - Some LGA names appear in more than one state (`Surulere` is in both Lagos and Oyo), so always key an LGA by **(state, lga)**.
  - Rows saved before GPS detection used the old Ogun-only dropdown spelling, e.g. `Egbado North (Yewa North)` = `Yewa North`, `Egbado South (Yewa South)` = `Yewa South`, and `Ado-Odo/Ota` = `Ado Odo/Ota`.
- **`crop_stage`:** `vegetative` (Growing leaves and stems, no flowers yet), `flowering`, `fruit_set` (Small tomatoes forming), `harvesting`.
- **`size_unit`:** `plots`, `acres`, `hectares`.

## Reading the sheet

- **Leading apostrophe:** the phone number, and any text starting with `=`, `+`, `-` or `@`, is stored with a hidden leading `'` so it stays text. The Sheets API returns it without the `'`, but CSV exports may include it. Strip a leading `'`.
- **Booleans** are `TRUE`/`FALSE`, but `repeat_phone` is the text `yes`/`no`.
- **Timestamps** are written as ISO text. Sheets may turn them into dates depending on locale, so parse both forms.
- **Column order:** newer columns were added on the right, so older sheets keep their row layout. Read columns by header name, not by position.
- **The `hp` spam-trap field** is never stored. Submissions that fill it are dropped.

## What the page sends

`POST https://glowlineapi.up.railway.app/farm/register-form/` with `Content-Type: application/json`. The API answers the CORS preflight for `https://emmanueloluwadamilola.github.io`. Each farm carries **only** its estimated footprint; it is `null` when the farmer has no GPS point.

```json
{
  "full_name": "Adewumi Gboyega",
  "phone_e164": "+2348117176443",
  "state": "Ondo",
  "lga": "Akure South",
  "lga_source": "gps",
  "detected_state": "Ondo",
  "detected_lga": "Akure South",
  "town_or_village": "Apatapiti",
  "crop_stage": "flowering",
  "consent": true,
  "needs_agent_help": false,
  "submitted_at": "2026-10-14T08:53:18.002Z",
  "hp": "",
  "farms": [{
    "estimated_footprint": { "type": "Polygon", "coordinates": [[[5.1845, 7.21769], "… 16 more …"]] }
  }]
}
```

- **No GPS point:** `estimated_footprint` is `null`, `needs_agent_help` is `true`, `lga_source` is `chosen`, and `detected_*` are `null`.
- **Footprint:** 17 `[lng, lat]` points (16 around the centre every 22.5°, north first, clockwise, plus the first again), 6 decimals. An estimate from the centre and the typed size, never a measured boundary.
- **`hp`** is a spam trap; real farmers leave it empty.

### Reply

A saved registration is any HTTP 2xx whose body has an `id`:

```json
{
  "id": "c1ff1241-d70e-4430-b646-e8e8118005a8",
  "code": "FMR-CAXJ",
  "farmer_created": false,
  "farms_added": 1,
  "farms_skipped_as_duplicates": 0,
  "farms": [{ "id": "73607e76-…", "code": "FM-F4K0", "name": "Farm 1" }]
}
```

- The page shows `code` on the thank-you screen as the farmer's GrowLine code.
- `farms_added` 0 with `farms_skipped_as_duplicates` > 0 shows "This farm was already registered" instead of "We have saved your farm".
- Any other status or body shows "We could not save your details…" and the farmer can tap the button again.

## Suggested database layout (Postgres + PostGIS)

```sql
CREATE TYPE crop_stage AS ENUM ('vegetative','flowering','fruit_set','harvesting');
CREATE TYPE size_unit  AS ENUM ('plots','acres','hectares');
CREATE TYPE lga_source AS ENUM ('gps','changed','chosen');

CREATE TABLE lgas (                       -- load from geo/names.json
  state text NOT NULL,
  lga   text NOT NULL,
  PRIMARY KEY (state, lga)
);

CREATE TABLE farmers (
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  phone_e164  text UNIQUE NOT NULL CHECK (phone_e164 ~ '^\+234(70|80|81|90|91)[0-9]{8}$'),
  full_name   text NOT NULL,
  created_at  timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE registrations (
  id               uuid PRIMARY KEY,
  farmer_id        uuid NOT NULL REFERENCES farmers(id),
  received_at      timestamptz NOT NULL,
  submitted_at     timestamptz NOT NULL,
  state            text NOT NULL,
  lga              text NOT NULL,
  lga_source       lga_source NOT NULL,
  detected_state   text,
  detected_lga     text,
  town_or_village  text NOT NULL,
  crop_stage       crop_stage NOT NULL,
  consent          boolean NOT NULL CHECK (consent),
  needs_agent_help boolean NOT NULL,
  FOREIGN KEY (state, lga) REFERENCES lgas (state, lga)
);

CREATE TABLE farms (
  id                    uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  registration_id       uuid NOT NULL REFERENCES registrations(id),
  centre                geography(Point, 4326),           -- NULL when not marked
  gps_accuracy_m        numeric(5,1) CHECK (gps_accuracy_m BETWEEN 0 AND 100),
  size_value            numeric NOT NULL CHECK (size_value > 0),
  size_unit             size_unit NOT NULL,
  estimated_area_m2     numeric(12,1) NOT NULL,
  estimated_radius_m    numeric(9,1) NOT NULL,
  estimated_perimeter_m numeric(10,1),
  estimated_footprint   geography(Polygon, 4326),          -- NULL when not marked
  needs_agent_help      boolean GENERATED ALWAYS AS (centre IS NULL) STORED
);
```

In this layout, `repeat_phone` becomes "the farmer has more than one registration", and `map_link` can be built from `centre` when needed, so neither needs its own column. With PostGIS you could also re-check `state` and `lga` on the server by loading the GRID3 polygons and testing `ST_Contains` against `centre`.

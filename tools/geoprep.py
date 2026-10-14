"""Build GrowLine's admin-area lookup files from GRID3/geoBoundaries (CC BY 4.0).
Usage: python3 -I geoprep.py <adm1.geojson> <adm2.geojson> <out_dir>
Writes: <out>/states.json, <out>/lga/<CODE>.json, <out>/names.json
"""
import json, sys, os, math

ADM1, ADM2, OUT = sys.argv[1:4]
STATE_TOL = float(sys.argv[4]) if len(sys.argv) > 4 else 0.004   # degrees (0.001 ≈ 110 m)
LGA_TOL = float(sys.argv[5]) if len(sys.argv) > 5 else 0.0012
DP = 4  # coordinate decimals (~11 m)
RENAME = {'Abuja Federal Capital Territory': 'Federal Capital Territory'}

def polys_of(geom):
    if geom['type'] == 'Polygon': return [geom['coordinates']]
    if geom['type'] == 'MultiPolygon': return geom['coordinates']
    raise ValueError(geom['type'])

def dp(points, tol):
    """Douglas-Peucker on an open polyline."""
    if len(points) < 3: return points[:]
    keep = [False] * len(points); keep[0] = keep[-1] = True
    stack = [(0, len(points) - 1)]
    while stack:
        a, b = stack.pop()
        (x1, y1), (x2, y2) = points[a], points[b]
        dx, dy = x2 - x1, y2 - y1; L = math.hypot(dx, dy)
        best, idx = -1, -1
        for i in range(a + 1, b):
            x0, y0 = points[i]
            d = abs(dy * x0 - dx * y0 + x2 * y1 - y2 * x1) / L if L else math.hypot(x0 - x1, y0 - y1)
            if d > best: best, idx = d, i
        if best > tol:
            keep[idx] = True; stack += [(a, idx), (idx, b)]
    return [p for p, k in zip(points, keep) if k]

def simplify_ring(ring, tol):
    pts = ring[:-1] if ring[0] == ring[-1] else ring[:]
    # split the closed ring at its farthest point so DP keeps the shape
    far = max(range(len(pts)), key=lambda i: (pts[i][0] - pts[0][0]) ** 2 + (pts[i][1] - pts[0][1]) ** 2)
    out = dp(pts[:far + 1], tol)[:-1] + dp(pts[far:] + [pts[0]], tol)
    out = [[round(x, DP), round(y, DP)] for x, y in out]
    dedup = [out[0]] + [p for i, p in enumerate(out[1:], 1) if p != out[i - 1]]
    if dedup[-1] != dedup[0]: dedup.append(dedup[0])
    return dedup if len(dedup) >= 4 else None

def simplify(polys, tol):
    res = []
    for poly in polys:
        rings = [simplify_ring(r, tol) for r in poly]
        if rings[0]: res.append([r for r in rings if r])
    return res

def bbox(polys):
    xs = [p[0] for poly in polys for r in poly for p in r]; ys = [p[1] for poly in polys for r in poly for p in r]
    return [round(min(xs), DP), round(min(ys), DP), round(max(xs), DP), round(max(ys), DP)]

def inside(x, y, polys):
    c = False
    for poly in polys:
        for ring in poly:
            j = len(ring) - 1
            for i in range(len(ring)):
                xi, yi = ring[i]; xj, yj = ring[j]
                if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi) + xi: c = not c
                j = i
    return c

def interior_points(polys, n=9):
    x0, y0, x1, y1 = bbox(polys); pts = []
    for k in range(1, 40):
        for i in range(k):
            for j in range(k):
                x = x0 + (x1 - x0) * (i + .5) / k; y = y0 + (y1 - y0) * (j + .5) / k
                if inside(x, y, polys) and (x, y) not in pts: pts.append((x, y))
        if len(pts) >= n: break
    return pts[:n]

a1 = json.load(open(ADM1)); a2 = json.load(open(ADM2))
states = []
for f in a1['features']:
    name = RENAME.get(f['properties']['shapeName'], f['properties']['shapeName'])
    states.append({'name': name, 'code': f['properties']['shapeISO'].split('-')[1], 'full': polys_of(f['geometry'])})

lgas_by_state = {s['code']: [] for s in states}
unassigned = []
for f in a2['features']:
    full = polys_of(f['geometry'])
    votes = {}
    for x, y in interior_points(full):
        for s in states:
            if inside(x, y, s['full']): votes[s['code']] = votes.get(s['code'], 0) + 1; break
    if not votes: unassigned.append(f['properties']['shapeName']); continue
    code = max(votes, key=votes.get)
    lgas_by_state[code].append({'name': f['properties']['shapeName'], 'full': full})

os.makedirs(os.path.join(OUT, 'lga'), exist_ok=True)
SRC = 'GRID3 2022 via geoBoundaries (CC BY 4.0). Simplified for phones.'
out_states = []
for s in states:
    g = simplify(s['full'], STATE_TOL)
    out_states.append({'name': s['name'], 'code': s['code'], 'bbox': bbox(g), 'polys': g})
json.dump({'source': SRC, 'states': sorted(out_states, key=lambda s: s['name'])}, open(os.path.join(OUT, 'states.json'), 'w'), separators=(',', ':'))

names = {}
for s in states:
    items = []
    for l in lgas_by_state[s['code']]:
        g = simplify(l['full'], LGA_TOL)
        items.append({'name': l['name'], 'bbox': bbox(g), 'polys': g})
    items.sort(key=lambda l: l['name'])
    json.dump({'source': SRC, 'state': s['name'], 'code': s['code'], 'lgas': items},
              open(os.path.join(OUT, 'lga', s['code'] + '.json'), 'w'), separators=(',', ':'))
    names[s['name']] = [l['name'] for l in items]
names = dict(sorted(names.items()))
json.dump(names, open(os.path.join(OUT, 'names.json'), 'w'), separators=(',', ':'), ensure_ascii=False)

print('unassigned LGAs:', unassigned)
print('LGAs per state:', {k: len(v) for k, v in sorted(names.items())})
print('total LGAs:', sum(len(v) for v in names.values()))

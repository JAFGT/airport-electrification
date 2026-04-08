import streamlit as st
from PIL import Image
import numpy as np
import math
from collections import deque
from streamlit_image_coordinates import streamlit_image_coordinates

st.set_page_config(layout="wide")

# images
original_map = np.array(Image.open('SavannahRegions.png').convert("RGB"))
display_map_original = np.array(Image.open('unmarkedSavannahPixelCount.png').convert("RGB"))
height, width, _ = original_map.shape

# constants
FT_PER_PIXEL = int(9351 / 290)
NUM_PVS = 1000 #subject to change based on input from their code 
PV_AREA_FT2 = 30
SOLAR_NEEDED = NUM_PVS * PV_AREA_FT2
SOLAR_PIXELS = math.ceil(SOLAR_NEEDED / FT_PER_PIXEL)
SOLAR_COLOR = np.array([100, 149, 237])   

NUM_TANKS = 50 #also subject to change based on input from their code 
TANK_AREA_FT2 = 200
TANK_NEEDED = NUM_TANKS * TANK_AREA_FT2
TANK_PIXELS = math.ceil(TANK_NEEDED / FT_PER_PIXEL)
TANK_COLOR = np.array([220, 50, 200])   

GROUND_COLOR  = np.array([255, 255,   0])
ROOF_COLOR    = np.array([  0, 255,   0])
PARKING_COLOR = np.array([  0,   0, 255])
BLOCKED_COLOR = np.array([255,   0,   0])

DISPLAY_W = 600 #changes size of the map

# color coding map
def to_grayscale_rgb(arr):
    lum = (0.299 * arr[:, :, 0] +
           0.587 * arr[:, :, 1] +
           0.114 * arr[:, :, 2]).astype(np.uint8)
    return np.stack([lum, lum, lum], axis=2)

display_map_gray = to_grayscale_rgb(display_map_original)

_LIGHT_GOLD    = np.array([255, 213, 100], dtype=float)
_SOFT_GREEN    = np.array([130, 210, 130], dtype=float)
_SOFT_BLUE     = np.array([130, 150, 230], dtype=float)
_SOFT_RED      = np.array([230, 120, 120], dtype=float)

_REGION_OVERLAY = [
    (GROUND_COLOR,  _LIGHT_GOLD),
    (ROOF_COLOR,    _SOFT_GREEN),
    (PARKING_COLOR, _SOFT_BLUE),
    (BLOCKED_COLOR, _SOFT_RED),
]

def build_region_display_map(region_map, alpha=0.35):
    base = display_map_gray.astype(float)
    out  = base.copy()
    for src_color, display_color in _REGION_OVERLAY:
        mask = np.all(region_map == src_color, axis=2)
        out[mask] = base[mask] * (1.0 - alpha) + display_color * alpha
    return out.astype(np.uint8)

for key, default in [
    ("solar_anchor", None),   # (i, j) pixel — where BFS fill starts
    ("tank_anchor",  None),
    ("last_solar_coords", None),
    ("last_tank_coords",  None),
    ("ground",  True),
    ("roof",    True),
    ("parking", True),
]:
    if key not in st.session_state:
        st.session_state[key] = default

def get_solar_map():
    f = original_map.copy()
    if not st.session_state.ground:
        f[np.all(f == GROUND_COLOR, axis=2)] = BLOCKED_COLOR
    if not st.session_state.roof:
        f[np.all(f == ROOF_COLOR, axis=2)] = BLOCKED_COLOR
    if not st.session_state.parking:
        f[np.all(f == PARKING_COLOR, axis=2)] = BLOCKED_COLOR
    return f


def get_tank_map():
    f = original_map.copy()
    f[np.all(f == ROOF_COLOR,    axis=2)] = BLOCKED_COLOR
    f[np.all(f == PARKING_COLOR, axis=2)] = BLOCKED_COLOR
    if not st.session_state.ground:
        f[np.all(f == GROUND_COLOR, axis=2)] = BLOCKED_COLOR
    return f


def compute_auto_fill(region_map, cap, exclude, anchor=None):
    filled = set()

    if anchor is not None:
        ai, aj = anchor
        queue   = deque([(ai, aj)])
        visited = set()

        while queue and len(filled) < cap:
            r, c = queue.popleft()
            if (r, c) in visited:
                continue
            visited.add((r, c))

            if (r, c) not in exclude and not np.array_equal(region_map[r, c], BLOCKED_COLOR):
                filled.add((r, c))

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < height and 0 <= nc < width and (nr, nc) not in visited:
                    queue.append((nr, nc))

    else:
        # default: top-left → bottom-right raster scan
        for i in range(height):
            for j in range(width):
                if len(filled) >= cap:
                    break
                if (i, j) not in exclude and not np.array_equal(region_map[i, j], BLOCKED_COLOR):
                    filled.add((i, j))
            if len(filled) >= cap:
                break

    return filled


def coords_to_ij(coords):
    scale = width / DISPLAY_W
    i = int(min(coords["y"] * scale, height - 1))
    j = int(min(coords["x"] * scale, width - 1))
    return i, j


def handle_click(region_map, anchor_key, new_coords, last_key):
    if new_coords is None:
        return False

    coord_tuple = (new_coords["x"], new_coords["y"])
    if coord_tuple == st.session_state[last_key]:
        return False                          # same click, ignore

    st.session_state[last_key] = coord_tuple
    i, j = coords_to_ij(new_coords)

    if np.array_equal(region_map[i, j], BLOCKED_COLOR):
        st.warning("⚠️ This area is unavailable.")
        return False

    st.session_state[anchor_key] = (i, j)   # move fill anchor here
    return True


solar_region_map = get_solar_map()
tank_region_map  = get_tank_map()

# Solar fills first; tank excludes whatever solar claimed
solar_pixels = compute_auto_fill(
    solar_region_map,
    SOLAR_PIXELS,
    exclude=set(),
    anchor=st.session_state.solar_anchor,
)

tank_pixels = compute_auto_fill(
    tank_region_map,
    TANK_PIXELS,
    exclude=solar_pixels,
    anchor=st.session_state.tank_anchor,
)

_SOLAR_ALPHA = 0.50
_TANK_ALPHA  = 0.60
_SOLAR_BLUE  = np.array([100, 149, 237], dtype=float)
_MAGENTA     = np.array([220,  50, 200], dtype=float)

def _apply_overlay(base_float, pixels, color, alpha):
    if not pixels:
        return
    rows, cols = zip(*pixels)
    rows = np.array(rows)
    cols = np.array(cols)
    base_float[rows, cols] = base_float[rows, cols] * (1.0 - alpha) + color * alpha

def build_solar_region_with_fill():
    # Start with the region-colored map, then overlay the fill on top
    out = build_region_display_map(solar_region_map).astype(float)
    _apply_overlay(out, solar_pixels, _SOLAR_BLUE, _SOLAR_ALPHA)
    return out.astype(np.uint8)

def build_tank_region_with_fill():
    # Start with the region-colored map, then overlay the fill on top
    out = build_region_display_map(tank_region_map).astype(float)
    _apply_overlay(out, tank_pixels, _MAGENTA, _TANK_ALPHA)
    return out.astype(np.uint8)

def build_combined_display():
    out = display_map_gray.astype(float)
    _apply_overlay(out, solar_pixels, _SOLAR_BLUE, _SOLAR_ALPHA)
    _apply_overlay(out, tank_pixels,  _MAGENTA,    _TANK_ALPHA)
    return out.astype(np.uint8)

st.header("Solar Filters")
st.checkbox("Ground",   key="ground")
st.checkbox("Rooftop",  key="roof")
st.checkbox("Parking",  key="parking")

# combined map
st.subheader("🗺️ Combined Placement Map")
st.markdown(
    '<span style="background:#6495ed;padding:2px 10px;border-radius:3px">&nbsp;</span> Solar Panels &nbsp;&nbsp;'
    '<span style="background:#dc32c8;padding:2px 10px;border-radius:3px">&nbsp;</span> Hydrogen & SAF Tanks',
    unsafe_allow_html=True
)
st.image(Image.fromarray(build_combined_display()), width=DISPLAY_W * 2)
st.markdown("---")

# solar panels
st.subheader("☀️ Solar Panels")
st.caption("Auto-filled outward from your click. Click anywhere to relocate the fill.")

st.markdown(
    '<span style="background:#d4c87a;padding:2px 10px;border-radius:3px">&nbsp;</span> Ground &nbsp;&nbsp;'
    '<span style="background:#82d482;padding:2px 10px;border-radius:3px">&nbsp;</span> Roof &nbsp;&nbsp;'
    '<span style="background:#8296e0;padding:2px 10px;border-radius:3px">&nbsp;</span> Parking &nbsp;&nbsp;'
    '<span style="background:#e07878;padding:2px 10px;border-radius:3px">&nbsp;</span> Unavailable &nbsp;&nbsp;'
    '<span style="background:#6495ed;padding:2px 10px;border-radius:3px">&nbsp;</span> Solar panels placed',
    unsafe_allow_html=True
)
solar_coords = streamlit_image_coordinates(
    Image.fromarray(build_solar_region_with_fill()),
    width=DISPLAY_W,
    key="solar_map"
)

if handle_click(solar_region_map, "solar_anchor", solar_coords, "last_solar_coords"):
    st.rerun()

s_ft2 = len(solar_pixels) * FT_PER_PIXEL
s_pct = min(s_ft2 / SOLAR_NEEDED * 100, 100)
st.progress(s_pct / 100)
st.write(f"Solar filled: **{s_ft2:,.0f} ft²** / {SOLAR_NEEDED:,.0f} ft² needed ({s_pct:.1f}%)")

st.markdown("---")

# tanks
st.subheader("⚗️ Hydrogen & SAF Tanks")
st.caption("Auto-filled outward from your click. Click anywhere to relocate the fill.")

st.markdown(
    '<span style="background:#d4c87a;padding:2px 10px;border-radius:3px">&nbsp;</span> Ground (valid) &nbsp;&nbsp;'
    '<span style="background:#e07878;padding:2px 10px;border-radius:3px">&nbsp;</span> Unavailable &nbsp;&nbsp;'
    '<span style="background:#dc32c8;padding:2px 10px;border-radius:3px">&nbsp;</span> Tanks placed',
    unsafe_allow_html=True
)
tank_coords = streamlit_image_coordinates(
    Image.fromarray(build_tank_region_with_fill()),
    width=DISPLAY_W,
    key="tank_map"
)

if handle_click(tank_region_map, "tank_anchor", tank_coords, "last_tank_coords"):
    st.rerun()

t_ft2 = len(tank_pixels) * FT_PER_PIXEL
t_pct = min(t_ft2 / TANK_NEEDED * 100, 100)
st.progress(t_pct / 100)
st.write(f"Tank filled: **{t_ft2:,.0f} ft²** / {TANK_NEEDED:,.0f} ft² needed ({t_pct:.1f}%)")

st.markdown("---")

#reset
if st.button("🔄 Reset All Placements"):
    st.session_state.solar_anchor = None
    st.session_state.tank_anchor  = None
    st.rerun()
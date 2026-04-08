import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import numpy as np
from PIL import Image
import math
from collections import deque
from streamlit_image_coordinates import streamlit_image_coordinates

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Airport Electrification Dashboard", page_icon="✈️", layout="wide"
)

# --- ASSETS & CONSTANTS ---
@st.cache_data
def load_maps():
    # Ensure these files are in your working directory
    orig = np.array(Image.open('SavannahRegions.png').convert("RGB"))
    disp = np.array(Image.open('unmarkedSavannahPixelCount.png').convert("RGB"))
    return orig, disp

original_map, display_map_original = load_maps()
height, width, _ = original_map.shape

FT_PER_PIXEL = int(9351 / 290)
PV_AREA_FT2 = 30
TANK_AREA_FT2 = 200
DISPLAY_W = 600

GROUND_COLOR  = np.array([255, 255,   0])
ROOF_COLOR    = np.array([  0, 255,   0])
PARKING_COLOR = np.array([  0,   0, 255])
BLOCKED_COLOR = np.array([255,   0,   0])
SOLAR_COLOR   = np.array([100, 149, 237]) 
TANK_COLOR    = np.array([220, 50, 200])

# --- STYLING ---
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f0c29 0%, #0a203c 50%, #05172a 100%);
        color: #ffffff;
    }
    .stButton > button {
        background-color: rgba(10, 32, 60, 0.7);
        color: #ffffff;
        border-radius: 12px;
        transition: all 0.3s ease;
    }
    .timeline-container { width: 100%; margin-top: 10px; }
    .row-container { display: flex; align-items: center; margin-bottom: 10px; }
    .row-title { width: 100px; font-weight: bold; color: #ff4b4b; }
    .bar-container { flex-grow: 1; display: flex; height: 30px; border-radius: 8px; overflow: hidden; border: 1px solid rgba(255,255,255,0.3); }
    .segment { display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 14px; }
    .seg-dark-blue { background-color: #1a5b7a; } .seg-light-blue { background-color: #a2cce3; color: #1a5b7a; }
    .seg-light-green { background-color: #e2f4c7; color: black; } .seg-dark-green { background-color: #3b7a2e; }
</style>
""", unsafe_allow_html=True)

# --- IMAGE PROCESSING HELPERS ---
def to_grayscale_rgb(arr):
    lum = (0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]).astype(np.uint8)
    return np.stack([lum, lum, lum], axis=2)

display_map_gray = to_grayscale_rgb(display_map_original)

def build_region_display_map(region_map, alpha=0.35):
    base = display_map_gray.astype(float)
    out = base.copy()
    regions = [(GROUND_COLOR, [255, 213, 100]), (ROOF_COLOR, [130, 210, 130]), 
               (PARKING_COLOR, [130, 150, 230]), (BLOCKED_COLOR, [230, 120, 120])]
    for src, disp in regions:
        mask = np.all(region_map == src, axis=2)
        out[mask] = base[mask] * (1.0 - alpha) + np.array(disp) * alpha
    return out.astype(np.uint8)

def compute_auto_fill(region_map, cap, exclude, anchor=None):
    filled = set()
    if anchor:
        ai, aj = anchor
        queue, visited = deque([(ai, aj)]), set()
        while queue and len(filled) < cap:
            r, c = queue.popleft()
            if (r, c) in visited: continue
            visited.add((r, c))
            if (r, c) not in exclude and not np.array_equal(region_map[r, c], BLOCKED_COLOR):
                filled.add((r, c))
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < height and 0 <= nc < width and (nr, nc) not in visited:
                    queue.append((nr, nc))
    else:
        for i in range(height):
            for j in range(width):
                if len(filled) >= cap: break
                if (i, j) not in exclude and not np.array_equal(region_map[i, j], BLOCKED_COLOR):
                    filled.add((i, j))
    return filled

def apply_overlay(base_float, pixels, color, alpha):
    if not pixels: return
    rows, cols = zip(*pixels)
    base_float[np.array(rows), np.array(cols)] = base_float[np.array(rows), np.array(cols)] * (1.0 - alpha) + color.astype(float) * alpha

# --- INITIALIZE STATE ---
years = ["2040", "2050", "2060", "2070"]
if "presets_applied" not in st.session_state:
    for sc in ["A", "B", "C", "D"]:
        st.session_state[f"{sc}_pvc"] = 1000
        st.session_state[f"{sc}_tanks"] = 50
        st.session_state[f"{sc}_anchor_s"] = None
        st.session_state[f"{sc}_anchor_t"] = None
        st.session_state[f"{sc}_target"] = "2050"
    st.session_state.explored_card = "A"
    st.session_state.presets_applied = True

# --- SIDEBAR & NAVIGATION ---
page = st.sidebar.selectbox("**Select Page**", ["Input Metrics", "Decision Dashboard", "Graphical Performance"])

# --- PAGE 2: DECISION DASHBOARD (Integrated with Mapping) ---
if page == "Decision Dashboard":
    st.markdown('## ✈️ Scenario Decision Dashboard ⚡️')
    
    sc_ids = ["A", "B", "C", "D"]
    labels = ["S1: Optimistic", "S2: Baseline", "S3: Conservative", "S4: Custom"]
    card_cols = st.columns(4)
    for i, sc_id in enumerate(sc_ids):
        if card_cols[i].button(labels[i], key=f"btn_nav_{sc_id}"):
            st.session_state.explored_card = sc_id

    sc = st.session_state.explored_card
    st.divider()
    st.subheader(f"Strategy Analysis: {labels[sc_ids.index(sc)]}")

    # INPUT BOXES FOR NUM_PVCs and NUM_TANKS
    col_in1, col_in2 = st.columns(2)
    with col_in1:
        n_pvc = st.number_input("Number of PV Panels", min_value=0, value=st.session_state[f"{sc}_pvc"], key=f"in_pvc_{sc}")
        st.session_state[f"{sc}_pvc"] = n_pvc
    with col_in2:
        n_tanks = st.number_input("Number of Storage Tanks", min_value=0, value=st.session_state[f"{sc}_tanks"], key=f"in_tks_{sc}")
        st.session_state[f"{sc}_tanks"] = n_tanks

    # SPATIAL MAPPING LOGIC
    solar_needed_px = math.ceil((n_pvc * PV_AREA_FT2) / FT_PER_PIXEL)
    tank_needed_px = math.ceil((n_tanks * TANK_AREA_FT2) / FT_PER_PIXEL)

    # Filters
    f1, f2, f3 = st.columns(3)
    g_on = f1.toggle("Ground Allowed", value=True, key=f"tg_g_{sc}")
    r_on = f2.toggle("Roof Allowed", value=True, key=f"tg_r_{sc}")
    p_on = f3.toggle("Parking Allowed", value=True, key=f"tg_p_{sc}")

    def get_map_filter(is_tank=False):
        m = original_map.copy()
        if not g_on: m[np.all(m == GROUND_COLOR, axis=2)] = BLOCKED_COLOR
        if not r_on or is_tank: m[np.all(m == ROOF_COLOR, axis=2)] = BLOCKED_COLOR
        if not p_on or is_tank: m[np.all(m == PARKING_COLOR, axis=2)] = BLOCKED_COLOR
        return m

    solar_map = get_map_filter()
    tank_map = get_map_filter(is_tank=True)

    # BFS Fills
    solar_px = compute_auto_fill(solar_map, solar_needed_px, set(), st.session_state[f"{sc}_anchor_s"])
    tank_px = compute_auto_fill(tank_map, tank_needed_px, solar_px, st.session_state[f"{sc}_anchor_t"])

    # Map Rendering
    tab1, tab2, tab3 = st.tabs(["☀️ Solar Layout", "⚗️ Tank Layout", "🗺️ Combined"])
    scale = width / DISPLAY_W

    with tab1:
        st.caption("Click map to relocate Solar Array")
        img_s = build_region_display_map(solar_map).astype(float)
        apply_overlay(img_s, solar_px, SOLAR_COLOR, 0.5)
        out_s = streamlit_image_coordinates(Image.fromarray(img_s.astype(np.uint8)), width=DISPLAY_W, key=f"map_s_{sc}")
        if out_s:
            new_anchor = (int(out_s["y"]*scale), int(out_s["x"]*scale))
            if new_anchor != st.session_state[f"{sc}_anchor_s"]:
                st.session_state[f"{sc}_anchor_s"] = new_anchor
                st.rerun()

    with tab2:
        st.caption("Click map to relocate Storage Tanks")
        img_t = build_region_display_map(tank_map).astype(float)
        apply_overlay(img_t, tank_px, TANK_COLOR, 0.6)
        out_t = streamlit_image_coordinates(Image.fromarray(img_t.astype(np.uint8)), width=DISPLAY_W, key=f"map_t_{sc}")
        if out_t:
            new_anchor = (int(out_t["y"]*scale), int(out_t["x"]*scale))
            if new_anchor != st.session_state[f"{sc}_anchor_t"]:
                st.session_state[f"{sc}_anchor_t"] = new_anchor
                st.rerun()
    
    with tab3:
        img_c = display_map_gray.astype(float)
        apply_overlay(img_c, solar_px, SOLAR_COLOR, 0.5)
        apply_overlay(img_c, tank_px, TANK_COLOR, 0.6)
        st.image(Image.fromarray(img_c.astype(np.uint8)), width=DISPLAY_W)

    # TIMELINE SECTION (Original functionality)
    st.divider()
    target_year = st.selectbox("Target Year", years, index=years.index(st.session_state[f"{sc}_target"]), key=f"t_yr_{sc}")
    st.session_state[f"{sc}_target"] = target_year
    
    for yr in [y for y in years if int(y) <= int(target_year)]:
        c_v = st.columns([1, 2])
        with c_v[0]:
            mix = st.slider(f"Hybrid Mix {yr} (%)", 0, 100, 50, key=f"sl_{sc}_{yr}")
        with c_v[1]:
            st.markdown(f"""<div class="bar-container"><div class="segment seg-dark-blue" style="width:{mix}%">{mix}%</div><div class="segment seg-light-blue" style="width:{100-mix}%"></div></div>""", unsafe_allow_html=True)

# (Rest of pages: Input Metrics & Graphical Performance remain standard)
elif page == "Input Metrics":
    st.title("Input Metrics")
    st.write("Configure global assumptions here.")
elif page == "Graphical Performance":
    st.title("Performance Data")
    st.write("Analytics based on placements and scenario inputs.")

# -----------------------------------------------------------
# PAGE 1: INPUT METRICS
# -----------------------------------------------------------
elif page == "Input Metrics":
    st.markdown('<p style="font-size: 44px; color: #ffffff; font-weight: bold; margin-bottom: 30px;">✈️ Airport Electrification Dashboard ⚡️</p>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1.2, 1, 1], gap="large")
    with col1:
        st.markdown('<p style="font-size: 28px; color: #b0a36f; font-weight: bold;">Scenario Configuration</p>', unsafe_allow_html=True)
        st.markdown("**Load Facilities**")
        f_cols = st.columns(2)
        for i, sector in enumerate(load_facilities):
            key = f"global_load_{sector.replace(' ', '_')}"
            if key not in st.session_state: st.session_state[key] = False
            with f_cols[i % 2]:
                is_active = st.session_state[key]
                bg = '#b0a36f !important' if is_active else '#0a203c'
                with stylable_container(key=f"fac_{sector}", css_styles=f"button {{ background-color: {bg}; border: 1px solid #ffffff; min-height: 40px !important; }}"):
                    if st.button(sector, key=f"btn_global_load_{sector}"):
                        st.session_state[key] = not st.session_state[key]
                        st.rerun()
        st.write("")
        st.selectbox("**Target Year**", years, index=1, key="global_target_year")
        st.markdown("**Fleet Transition Pathway**")
        st.slider("HE 2040 Mix (%)", 0, 100, 50, key="global_he_slider")
        st.slider("H2-SAF 2050 Mix (%)", 0, 100, 20, key="global_h2_slider")
    with col2:
        st.markdown('<p style="font-size: 28px; color: #b0a36f; font-weight: bold;">Economic & Tech Presets</p>', unsafe_allow_html=True)
        create_preset_row("Demand Growth Scenario", ["Low", "Baseline", "High"], "demand", "Global")
        st.write("")
        create_preset_row("PV Innovation/ Tech Growth", ["Conservative", "Moderate", "Advanced"], "pv", "Global")
        st.write("")
        create_preset_row("H2 Import Price", ["Low", "Baseline", "High"], "h2", "Global")
        st.write("")
        create_preset_row("Electricity Price Escalation", ["Low", "Baseline", "High"], "elec", "Global")
    with col3:
        st.markdown('<p style="font-size: 28px; color: #b0a36f; font-weight: bold;">Incentives & Constraints</p>', unsafe_allow_html=True)
        st.toggle("**Federal ITC (30%)**", value=True, key="global_itc_toggle")
        st.write("---")
        st.slider("**Land Available (Acres)**", 0, 500, 250, key="global_land")
        st.slider("**Grid Capacity (MW)**", 0, 100, 50, key="global_grid")
#

elif page == "Graphical Performance":
    st.title("📊 Graphical Performance")
    st.write("Charts based on scenario configurations.")
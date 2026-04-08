import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import numpy as np

# PAGE CONFIG
st.set_page_config(
    page_title="Airport Electrification Dashboard", page_icon="✈️", layout="wide"
)

# CSS THEME & CUSTOM STYLING
st.markdown(
    """
<style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f0c29 0%, #0a203c 50%, #05172a 100%);
        color: #ffffff;
    }
    [data-testid="stHeader"] {background: rgba(0,0,0,0);}

    .stButton > button {
        background-color: rgba(10, 32, 60, 0.7);
        color: #ffffff;
        border-radius: 12px;
        width: 100% !important; 
        transition: all 0.3s ease;
    }
    
    .timeline-container { width: 100%; margin-top: 10px; font-family: sans-serif; }
    .timeline-labels { display: flex; justify-content: space-around; color: #ffffff; font-weight: bold; margin-bottom: 5px; }
    .row-container { display: flex; align-items: center; margin-bottom: 15px; }
    .row-title { width: 120px; font-size: 16px; font-weight: bold; color: #ff4b4b; }
    .bar-container { flex-grow: 1; display: flex; height: 45px; border-radius: 12px; overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.4); }
    .seg-dark-blue { background-color: #1a5b7a; color: white; }
    .seg-light-blue { background-color: #a2cce3; color: #1a5b7a; }
    .seg-light-green { background-color: #e2f4c7; color: black; }
    .seg-dark-green { background-color: #3b7a2e; color: white; }
    .segment { display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 16px; height: 100%; }
    .block-splitter { width: 12px; background-color: #000000; height: 100%; }
</style>
""",
    unsafe_allow_html=True,
)

# INITIALIZE MASTER VARIABLES
years = ["2040", "2050", "2060", "2070"]
scenarios = ["Scenario A", "Scenario B", "Scenario C"]
load_facilities = ["Terminal", "Aircraft", "GSE", "Manufacturing Plant"]

# PRESET INITIALIZATION FROM SENSITIVITY TABLE
if "presets_applied" not in st.session_state:
    # S1: Optimistic (Scenario A)
    st.session_state["A_demand"] = "High"; st.session_state["A_pv"] = "Advanced"; st.session_state["A_h2"] = "Low"
    st.session_state["A_elec"] = "Low"; st.session_state["A_itc"] = True; st.session_state["A_target"] = "2050"
    st.session_state["val_A_comm_2040"] = 100; st.session_state["val_A_comm_2050"] = 100 # HE by 2040
    
    # S2: Baseline (Scenario B)
    st.session_state["B_demand"] = "Baseline"; st.session_state["B_pv"] = "Moderate"; st.session_state["B_h2"] = "Baseline"
    st.session_state["B_elec"] = "Baseline"; st.session_state["B_itc"] = True; st.session_state["B_target"] = "2060"
    st.session_state["val_B_comm_2050"] = 100 # HE by 2050
    
    # S3: Conservative (Scenario C)
    st.session_state["C_demand"] = "Low"; st.session_state["C_pv"] = "Conservative"; st.session_state["C_h2"] = "High"
    st.session_state["C_elec"] = "High"; st.session_state["C_itc"] = False; st.session_state["C_target"] = "2070"
    st.session_state["val_C_comm_2060"] = 100 # HE by 2060
    
    st.session_state["presets_applied"] = True

if "explored_card" not in st.session_state:
    st.session_state.explored_card = None

# HELPER: PRESET BUTTONS
def create_preset_row(label, options, key_prefix, sc_id):
    st.markdown(f"**{label}**")
    cols = st.columns(len(options))
    state_key = f"{sc_id}_{key_prefix}"
    for i, option in enumerate(options):
        is_active = (st.session_state.get(state_key) == option)
        bg = '#b0a36f !important' if is_active else '#0a203c'
        with cols[i]:
            with stylable_container(key=f"c_{sc_id}_{key_prefix}_{option}", css_styles=f"button {{ background-color: {bg}; border: 1px solid #ffffff; }}"):
                if st.button(option, key=f"btn_{sc_id}_{key_prefix}_{option}"):
                    st.session_state[state_key] = option
                    st.rerun()

# HELPER: TIMELINE
def render_timeline(year, sc_id):
    st.markdown(f"### Projections for Year {year}")
    c1, c2 = st.columns([1, 1.5])
    comm_key = f"val_{sc_id}_comm_{year}"
    if comm_key not in st.session_state: st.session_state[comm_key] = 50
    with c1:
        comm_val = st.slider("Commercial Hybrid-Electric Mix (%)", 0, 100, key=f"sl_{sc_id}_{year}", value=st.session_state[comm_key])
        st.session_state[comm_key] = comm_val
        biz_val = 90
    rem_c, rem_b = 100-comm_val, 100-biz_val
    with c2:
        st.html(f'<div class="timeline-container"><div class="timeline-labels"><span>2040</span><span>2050</span><span>2060</span><span>2070</span></div><hr style="border-color:#69ff47;"><div class="row-container"><div class="row-title">Commercial</div><div class="bar-container"><div class="segment seg-dark-blue" style="width:{comm_val}%;">{comm_val}%</div><div class="block-splitter"></div><div class="segment seg-light-blue" style="width:{rem_c}%;">{rem_c}%</div></div></div><div class="row-container"><div class="row-title">Business</div><div class="bar-container"><div class="segment seg-light-green" style="width:{biz_val}%;">{biz_val}%</div><div class="block-splitter"></div><div class="segment seg-dark-green" style="width:{rem_b}%;">{rem_b}%</div></div></div></div>')

# PAGE SELECTOR
page = st.sidebar.selectbox("**Select Page**", ["Input Metrics", "Decision Dashboard", "Graphical Performance"])

# -----------------------------------------------------------
# ORIGINAL INPUT METRICS PAGE
# -----------------------------------------------------------
if page == "Input Metrics":
    st.markdown('<p style="font-size: 44px; color: #ffffff; font-weight: bold; margin-bottom: 30px;">✈️ Airport Electrification Dashboard ⚡️</p>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1.2, 1, 1], gap="large")
    with col1:
        st.markdown('<p style="font-size: 28px; color: #b0a36f; font-weight: bold;">Scenario Configuration</p>', unsafe_allow_html=True)
        st.markdown("**Load Facilities**")
        f_cols = st.columns(2)
        for i, sector in enumerate(load_facilities):
            with f_cols[i % 2]:
                with stylable_container(key=f"fac_{sector}", css_styles="button { background-color: #0a203c; border: 1px solid #ffffff; }"):
                    st.button(sector)
        st.selectbox("**Target Year**", years, index=1)
        st.slider("HE 2040 Mix (%)", 0, 100, 50)
    with col2:
        st.markdown('<p style="font-size: 28px; color: #b0a36f; font-weight: bold;">Economic & Tech Presets</p>', unsafe_allow_html=True)
        create_preset_row("Demand Growth", ["Low", "Baseline", "High"], "p_demand", "Global")
        create_preset_row("PV Innovation", ["Conservative", "Moderate", "Advanced"], "p_pv", "Global")
    with col3:
        st.markdown('<p style="font-size: 28px; color: #b0a36f; font-weight: bold;">Incentives & Logistics</p>', unsafe_allow_html=True)
        st.toggle("**Federal ITC (30%)**", value=True)
        st.slider("**Land Available (Acres)**", 0, 500, 250)

# -----------------------------------------------------------
# MODIFIED DECISION DASHBOARD (Scenario Presets)
# -----------------------------------------------------------
elif page == "Decision Dashboard":
    st.markdown('<p style="font-size: 48px; color: #ffffff; font-weight: bold; margin-bottom: 20px;">✈️ Scenario Decision Suite ⚡️</p>', unsafe_allow_html=True)
    card_cols = st.columns(3)
    labels = ["S1: Optimistic", "S2: Baseline", "S3: Conservative"]
    sc_ids = ["A", "B", "C"]
    for i, sc in enumerate(sc_ids):
        is_active = st.session_state.explored_card == sc
        bg = "rgba(176, 163, 111, 0.2)" if is_active else "rgba(255, 255, 255, 0.05)"
        with card_cols[i]:
            with stylable_container(key=f"card_{sc}", css_styles=f"button {{ background-color: {bg} !important; border: 2px solid #b0a36f !important; min-height: 120px !important; }}"):
                if st.button(f"**{labels[i]}**", key=f"btn_sc_{sc}"):
                    st.session_state.explored_card = sc
                    st.rerun()

    if st.session_state.explored_card:
        sc = st.session_state.explored_card
        st.markdown("---")
        m1, m2, m3 = st.columns(3)
        with m1:
            st.selectbox("Target Year", years, index=years.index(st.session_state[f"{sc}_target"]), key=f"targ_{sc}")
            st.toggle("Federal ITC", value=st.session_state[f"{sc}_itc"], key=f"itc_{sc}")
        with m2:
            create_preset_row("Demand Growth", ["Low", "Baseline", "High"], "demand", sc)
            create_preset_row("PV Tech (NREL)", ["Conservative", "Moderate", "Advanced"], "pv", sc)
        with m3:
            create_preset_row("H2 Price", ["Low", "Baseline", "High"], "h2", sc)
            create_preset_row("Elec Escalation", ["Low", "Baseline", "High"], "elec", sc)
        
        st.markdown("---")
        render_timeline(st.session_state[f"{sc}_target"], sc)

elif page == "Graphical Performance":
    st.title("📊 Graphical Performance")
    st.write("Charts based on scenario configurations.")
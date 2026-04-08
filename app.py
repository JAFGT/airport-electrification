import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import numpy as np

# PAGE CONFIG
st.set_page_config(
    page_title="Airport Electrification Dashboard", page_icon="✈️", layout="wide"
)

# CSS THEME & CUSTOM CARD STYLING
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
        min-height: 120px;
        transition: all 0.3s ease;
        text-align: center;
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

# SENSITIVITY PRESET MAPPING
if "presets_initialized" not in st.session_state:
    # Scenario A (Optimistic)
    st.session_state["Scenario A_demand"] = "High"
    st.session_state["Scenario A_pv"] = "Advanced"
    st.session_state["Scenario A_h2"] = "Low" # Cheap
    st.session_state["Scenario A_elec"] = "Low" # Cheap
    st.session_state["Scenario A_itc"] = True
    st.session_state["Scenario A_target"] = "2050"
    
    # Scenario B (Baseline)
    st.session_state["Scenario B_demand"] = "Baseline"
    st.session_state["Scenario B_pv"] = "Moderate"
    st.session_state["Scenario B_h2"] = "Baseline"
    st.session_state["Scenario B_elec"] = "Baseline"
    st.session_state["Scenario B_itc"] = True
    st.session_state["Scenario B_target"] = "2060"
    
    # Scenario C (Conservative)
    st.session_state["Scenario C_demand"] = "Low"
    st.session_state["Scenario C_pv"] = "Conservative"
    st.session_state["Scenario C_h2"] = "High" # Expensive
    st.session_state["Scenario C_elec"] = "High" # Expensive
    st.session_state["Scenario C_itc"] = False
    st.session_state["Scenario C_target"] = "2070"

    # Fleet Logic based on Sensitivity table
    # S1: HE by 2040, H2 by 2050 | S2: HE by 2050, H2 by 2060 | S3: HE by 2060, H2 by 2070
    st.session_state["val_Scenario A_comm_2040"] = 100; st.session_state["val_Scenario A_comm_2050"] = 100
    st.session_state["val_Scenario B_comm_2040"] = 0;   st.session_state["val_Scenario B_comm_2050"] = 100
    st.session_state["val_Scenario C_comm_2040"] = 0;   st.session_state["val_Scenario C_comm_2050"] = 0; st.session_state["val_Scenario C_comm_2060"] = 100

    st.session_state.presets_initialized = True

if "explored_card" not in st.session_state:
    st.session_state.explored_card = None

# -----------------------------------------------------------
# HELPERS
# -----------------------------------------------------------

def create_preset_row(label, options, key_prefix, scenario):
    st.markdown(f"**{label}**")
    cols = st.columns(len(options))
    state_key = f"{scenario}_{key_prefix}"
    
    for i, option in enumerate(options):
        is_active = (st.session_state.get(state_key) == option)
        bg = '#b0a36f !important' if is_active else '#0a203c'
        border = '2px solid #ffffff' if is_active else '1px solid #b0a36f'
        
        with cols[i]:
            with stylable_container(key=f"{scenario}_{key_prefix}_{option}", css_styles=f"button {{ background-color: {bg}; border: {border}; color: white; min-height: 40px !important;}}"):
                if st.button(option, key=f"btn_{scenario}_{key_prefix}_{option}"):
                    st.session_state[state_key] = option
                    st.rerun()

def render_timeline(selected_year, scenario):
    st.markdown(f"### Projections for Year {selected_year}")
    col_sliders, col_visual = st.columns([1, 1.5], gap="medium")
    
    comm_key = f"val_{scenario}_comm_{selected_year}"
    if comm_key not in st.session_state: st.session_state[comm_key] = 50
    
    with col_sliders:
        comm_pct = st.slider(f"Commercial Hybrid-Electric Mix (%)", 0, 100, key=f"sl_{scenario}_{selected_year}", value=st.session_state[comm_key])
        st.session_state[comm_key] = comm_pct
        biz_pct = st.slider(f"Business 100% SAF Mix (%)", 0, 100, key=f"biz_{scenario}_{selected_year}", value=90)

    rem_comm = 100 - comm_pct
    rem_biz = 100 - biz_pct

    with col_visual:
        st.html(f"""
        <div class="timeline-container">
            <div class="timeline-labels"><span>2040</span><span>2050</span><span>2060</span><span>2070</span></div>
            <hr style="border-color: #69ff47; margin-bottom: 25px;">
            <div class="row-container">
                <div class="row-title">Commercial</div>
                <div class="bar-container">
                    <div class="segment seg-dark-blue" style="width: {comm_pct}%;">{comm_pct}%</div>
                    <div class="block-splitter"></div>
                    <div class="segment seg-light-blue" style="width: {rem_comm}%;">{rem_comm}%</div>
                </div>
            </div>
            <div class="row-container">
                <div class="row-title">Business</div>
                <div class="bar-container">
                    <div class="segment seg-light-green" style="width: {biz_pct}%;">{biz_pct}%</div>
                    <div class="block-splitter"></div>
                    <div class="segment seg-dark-green" style="width: {rem_biz}%;">{rem_biz}%</div>
                </div>
            </div>
        </div>
        """)

# -----------------------------------------------------------
# NAVIGATION
# -----------------------------------------------------------
page = st.sidebar.selectbox("**Select Page**", ["Input Metrics", "Decision Dashboard", "Graphical Performance"])

if page == "Input Metrics":
    st.markdown('<p style="font-size: 44px; color: #ffffff; font-weight: bold; margin-bottom: 30px;">✈️ Airport Electrification Dashboard ⚡️</p>', unsafe_allow_html=True)
    st.info("💡 Note: These inputs define the 'Global' baseline. Use the Decision Dashboard to customize Scenario A, B, and C specifically.")
    
    col1, col2, col3 = st.columns([1.2, 1, 1], gap="large")
    with col1:
        st.markdown('<p style="font-size: 28px; color: #b0a36f; font-weight: bold;">Configuration</p>', unsafe_allow_html=True)
        st.multiselect("**Load Facilities**", load_facilities, default=load_facilities)
        st.selectbox("**Target Year**", years, index=1)
        st.slider("HE 2040 Mix (%)", 0, 100, 50)
    with col2:
        st.markdown('<p style="font-size: 28px; color: #b0a36f; font-weight: bold;">Presets</p>', unsafe_allow_html=True)
        create_preset_row("Demand Growth", ["Low", "Baseline", "High"], "demand", "Global")
        create_preset_row("PV Innovation", ["Conservative", "Moderate", "Advanced"], "pv", "Global")
    with col3:
        st.markdown('<p style="font-size: 28px; color: #b0a36f; font-weight: bold;">Constraints</p>', unsafe_allow_html=True)
        st.toggle("Federal ITC (30%)", value=True)
        st.slider("Land Available (Acres)", 0, 500, 250)

elif page == "Decision Dashboard":
    st.markdown('<p style="font-size: 48px; color: #ffffff; font-weight: bold; margin-bottom: 20px;">✈️ Scenario Decision Suite ⚡️</p>', unsafe_allow_html=True)
    
    cols = st.columns(3)
    titles = ["Scenario A: Optimistic", "Scenario B: Baseline", "Scenario C: Conservative"]
    for i, sc in enumerate(scenarios):
        is_active = st.session_state.explored_card == sc
        bg = "rgba(176, 163, 111, 0.2)" if is_active else "rgba(255, 255, 255, 0.05)"
        with cols[i]:
            with stylable_container(key=f"card_{sc}", css_styles=f"button {{ background-color: {bg} !important; border: 1px solid #b0a36f !important; }}"):
                if st.button(f"**{titles[i]}**", key=f"btn_{sc}"):
                    st.session_state.explored_card = sc
                    st.rerun()

    if st.session_state.explored_card:
        sc = st.session_state.explored_card
        st.markdown("---")
        st.subheader(f"Customizing {sc}")
        
        m1, m2, m3 = st.columns(3)
        with m1:
            st.selectbox("Target Year", years, index=years.index(st.session_state[f"{sc}_target"]), key=f"tg_{sc}")
            st.toggle("Federal ITC", value=st.session_state[f"{sc}_itc"], key=f"itc_{sc}")
        with m2:
            create_preset_row("Demand Growth", ["Low", "Baseline", "High"], "demand", sc)
            create_preset_row("PV Tech (NREL)", ["Conservative", "Moderate", "Advanced"], "pv", sc)
        with m3:
            create_preset_row("H2 Import Price", ["Low", "Baseline", "High"], "h2", sc)
            create_preset_row("Elec Price Escalation", ["Low", "Baseline", "High"], "elec", sc)

        st.markdown("---")
        render_timeline(st.session_state[f"{sc}_target"], sc)

elif page == "Graphical Performance":
    st.title("📊 Graphical Performance")
    st.write("Performance analysis plots based on scenario selections.")
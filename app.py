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

    /* Global styling for buttons used as cards */
    .stButton > button {
        background-color: rgba(10, 32, 60, 0.7);
        color: #ffffff;
        border-radius: 12px;
        width: 100% !important; 
        min-height: 120px;
        padding: 20px;
        transition: all 0.3s ease;
        text-align: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        margin-bottom: 0px !important;
    }
    
    /* Timeline CSS */
    .timeline-container {
        width: 100%;
        margin-top: 10px;
        font-family: sans-serif;
    }
    .timeline-labels {
        display: flex;
        justify-content: space-around;
        color: #ffffff;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .row-container {
        display: flex;
        align-items: center;
        margin-bottom: 15px;
    }
    .row-title {
        width: 120px;
        font-size: 16px;
        font-weight: bold;
        color: #ff4b4b; 
    }
    .bar-container {
        flex-grow: 1;
        display: flex;
        height: 45px;
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.4);
    }
    .seg-dark-blue { background-color: #1a5b7a; color: white; }
    .seg-light-blue { background-color: #a2cce3; color: #1a5b7a; }
    .seg-light-green { background-color: #e2f4c7; color: black; }
    .seg-dark-green { background-color: #3b7a2e; color: white; }
    
    .segment {
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 16px;
        height: 100%;
        transition: width 0.4s ease;
    }
    .block-splitter {
        width: 12px;
        background-color: #000000;
        height: 100%;
    }
</style>
""",
    unsafe_allow_html=True,
)

# INITIALIZE MASTER VARIABLES
years = ["2040", "2050", "2060", "2070"]
scenarios = ["Scenario A", "Scenario B", "Scenario C"]
load_facilities = ["Terminal", "Aircraft", "GSE", "Manufacturing Plant"]

if "explored_card" not in st.session_state:
    st.session_state.explored_card = None

# Discrete values for all sliders.
for sc in scenarios:
    for yr in years:
        comm_val_key = f"val_{sc}_comm_{yr}"
        biz_val_key = f"val_{sc}_biz_{yr}"
        
        if comm_val_key not in st.session_state:
            st.session_state[comm_val_key] = 50
        if biz_val_key not in st.session_state:
            st.session_state[biz_val_key] = 90


# DEFINE CALLBACK FUNCTIONS 
def save_comm_value(scenario, year):
    slider_key = f"slider_{scenario}_comm_{year}"
    state_key = f"val_{scenario}_comm_{year}"
    st.session_state[state_key] = st.session_state[slider_key]

def save_biz_value(scenario, year):
    slider_key = f"slider_{scenario}_biz_{year}"
    state_key = f"val_{scenario}_biz_{year}"
    st.session_state[state_key] = st.session_state[slider_key]


# HELPER FOR PRESET BUTTONS
def create_preset_row(label, options, key_prefix):
    st.markdown(f"**{label}**")
    cols = st.columns(len(options))
    for i, option in enumerate(options):
        key = f"{key_prefix}_{option.lower()}"
        if key not in st.session_state:
            st.session_state[key] = (option in ["Baseline", "Moderate"])
        
        is_active = st.session_state[key]
        bg = '#b0a36f !important' if is_active else '#0a203c'
        border = '2px solid #ffffff' if is_active else '1px solid #b0a36f'
        
        with cols[i]:
            with stylable_container(
                key=f"cont_{key}",
                css_styles=f"button {{ background-color: {bg}; border: {border}; color: white; min-height: 40px !important;}}"
            ):
                if st.button(option, key=f"btn_{key}"):
                    for opt in options:
                        st.session_state[f"{key_prefix}_{opt.lower()}"] = False
                    st.session_state[key] = True
                    st.rerun()


# DEFINE REUSABLE TIMELINE FUNCTION
def render_timeline(selected_year, scenario):
    st.markdown(f"### Projections for Year {selected_year}")

    col_sliders, col_visual = st.columns([1, 1.5], gap="medium")

    comm_val_key = f"val_{scenario}_comm_{selected_year}"
    biz_val_key = f"val_{scenario}_biz_{selected_year}"
    
    current_comm_val = st.session_state[comm_val_key]
    current_biz_val = st.session_state[biz_val_key]

    with col_sliders:
        commercial_pct = st.slider(
            f"Commercial Hybrid-Electric Mix (%)",
            0, 100, 
            value=current_comm_val,
            step=5,
            key=f"slider_{scenario}_comm_{selected_year}",
            on_change=save_comm_value,
            args=(scenario, selected_year)
        )

        business_saf_pct = st.slider(
            f"Business 100% SAF Mix (%)",
            0, 100, 
            value=current_biz_val,
            step=5,
            key=f"slider_{scenario}_biz_{selected_year}",
            on_change=save_biz_value,
            args=(scenario, selected_year)
        )

    comm_remaining = 100 - commercial_pct
    biz_remaining = 100 - business_saf_pct

    with col_visual:
        st.html(
            f"""
        <div class="timeline-container">
            <div class="timeline-labels">
                <span>2040</span>
                <span>2050</span>
                <span>2060</span>
                <span>2070</span>
            </div>
            
            <hr style="border-color: #69ff47; margin-bottom: 25px;">

            <div class="row-container">
                <div class="row-title">Commercial</div>
                <div class="bar-container">
                    <div class="segment seg-dark-blue" style="width: {commercial_pct}%;">{commercial_pct}%</div>
                    <div class="block-splitter"></div>
                    <div class="segment seg-light-blue" style="width: {comm_remaining}%;">{comm_remaining}%</div>
                </div>
            </div>

            <div class="row-container">
                <div class="row-title">Business</div>
                <div class="bar-container">
                    <div class="segment seg-light-green" style="width: {business_saf_pct}%;">{business_saf_pct}%</div>
                    <div class="block-splitter"></div>
                    <div class="segment seg-dark-green" style="width: {biz_remaining}%;">{biz_remaining}%</div>
                </div>
            </div>
        </div>
        """
        )

    st.markdown("---")


# PAGE SELECTOR
page = st.sidebar.selectbox(
    "**Select Page**",
    ["Input Metrics", "Decision Dashboard", "Graphical Performance"],
)

# -----------------------------------------------------------
# INPUT METRICS
# -----------------------------------------------------------
if page == "Input Metrics":

    st.markdown('<p style="font-size: 44px; color: #ffffff; font-weight: bold; margin-bottom: 30px;">✈️ Airport Electrification Dashboard ⚡️</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1.2, 1, 1], gap="large")

    # COLUMN 1: LOAD & YEAR
    with col1:
        st.markdown('<p style="font-size: 28px; color: #b0a36f; font-weight: bold;">Scenario Configuration</p>', unsafe_allow_html=True)
        
        # Load Facilities Multi-select logic
        st.markdown("**Load Facilities**")
        f_cols = st.columns(2)
        for i, sector in enumerate(load_facilities):
            key = f"load_{sector.replace(' ', '_')}"
            if key not in st.session_state: st.session_state[key] = False
            with f_cols[i % 2]:
                is_active = st.session_state[key]
                bg = '#b0a36f !important' if is_active else '#0a203c'
                with stylable_container(key=f"c_{key}", css_styles=f"button {{ background-color: {bg}; border: 1px solid #ffffff; min-height: 40px !important;}}"):
                    if st.button(sector, key=f"btn_{key}"):
                        st.session_state[key] = not st.session_state[key]
                        st.rerun()

        st.write("")
        target_year = st.selectbox("**Target Year**", years, index=1)
        
        st.markdown("**Fleet Transition Pathway**")
        st.slider("HE 2040 Mix (%)", 0, 100, 50, key="global_he_slider")
        st.slider("H2-SAF 2050 Mix (%)", 0, 100, 20, key="global_h2saf_slider")

    # COLUMN 2: PRESETS
    with col2:
        st.markdown('<p style="font-size: 28px; color: #b0a36f; font-weight: bold;">Economic & Tech Presets</p>', unsafe_allow_html=True)
        create_preset_row("Demand Growth Scenario", ["Low", "Baseline", "High"], "p_demand")
        st.write("")
        create_preset_row("PV Innovation/Tech Scenario", ["Conservative", "Moderate", "Advanced"], "p_pv")
        st.write("")
        create_preset_row("H2 Import Price", ["Low", "Baseline", "High"], "p_h2")
        st.write("")
        create_preset_row("Electricity Price Escalation", ["Low", "Baseline", "High"], "p_elec")

    # COLUMN 3: INCENTIVES
    with col3:
        st.markdown('<p style="font-size: 28px; color: #b0a36f; font-weight: bold;">Incentives & Logistics</p>', unsafe_allow_html=True)
        itc_toggle = st.toggle("**Federal ITC (30%)**", value=True)
        st.info(f"ITC Status: {'On (30%)' if itc_toggle else 'Off (0%)'}")
        
        st.write("---")
        st.slider("**Land Available (Acres)**", 0, 500, 250, key="global_land_acres")
        st.slider("**Grid Capacity (MW)**", 0, 100, 50, key="global_grid_mw")

    # BOTTOM
    st.markdown("---")


# -----------------------------------------------------------
# DECISION DASHBOARD
# -----------------------------------------------------------
elif page == "Decision Dashboard":
    st.markdown(
        """
        <p style="font-size: 48px; color: #ffffff; font-weight: bold; margin-bottom: 20px;">
        ✈️ Airport Electrification Dashboard ⚡️
        </p>
    """,
        unsafe_allow_html=True,
    )

    scenario_a, scenario_b, scenario_c = st.columns(3, gap="medium")

    # --- SCENARIO A CARD ---
    with scenario_a:
        is_active = st.session_state.explored_card == "Scenario A"
        bg_color = "rgba(176, 163, 111, 0.2)" if is_active else "rgba(255, 255, 255, 0.05)"
        border_style = "2px solid #b0a36f" if is_active else "1px solid rgba(255, 255, 255, 0.2)"
        shadow = "0 0 15px rgba(176, 163, 111, 0.4)" if is_active else "none"

        with stylable_container(
            key="scenario_a",
            css_styles=f"button {{ background-color: {bg_color} !important; border: {border_style} !important; box-shadow: {shadow} !important; min-height: 120px !important;}}",
        ):
            if st.button("**Scenario A**", key="scenario_a_btn"):
                st.session_state.explored_card = "Scenario A"
                st.rerun()

    # --- SCENARIO B CARD ---
    with scenario_b:
        is_active = st.session_state.explored_card == "Scenario B"
        bg_color = "rgba(176, 163, 111, 0.2)" if is_active else "rgba(255, 255, 255, 0.05)"
        border_style = "2px solid #b0a36f" if is_active else "1px solid rgba(255, 255, 255, 0.2)"
        shadow = "0 0 15px rgba(176, 163, 111, 0.4)" if is_active else "none"

        with stylable_container(
            key="scenario_b",
            css_styles=f"button {{ background-color: {bg_color} !important; border: {border_style} !important; box-shadow: {shadow} !important; min-height: 120px !important;}}",
        ):
            if st.button("**Scenario B**", key="scenario_b_btn"):
                st.session_state.explored_card = "Scenario B"
                st.rerun()

    # --- SCENARIO C CARD ---
    with scenario_c:
        is_active = st.session_state.explored_card == "Scenario C"
        bg_color = "rgba(176, 163, 111, 0.2)" if is_active else "rgba(255, 255, 255, 0.05)"
        border_style = "2px solid #b0a36f" if is_active else "1px solid rgba(255, 255, 255, 0.2)"
        shadow = "0 0 15px rgba(176, 163, 111, 0.4)" if is_active else "none"

        with stylable_container(
            key="scenario_c",
            css_styles=f"button {{ background-color: {bg_color} !important; border: {border_style} !important; box-shadow: {shadow} !important; min-height: 120px !important;}}",
        ):
            if st.button("**Scenario C**", key="scenario_c_btn"):
                st.session_state.explored_card = "Scenario C"
                st.rerun()

    st.markdown("---")

    # -----------------------------------------------------------
    # SCENARIO MODIFIERS
    # -----------------------------------------------------------
    if st.session_state.explored_card is None:
        st.info("Click on any of the three cards above to explore and modify its metrics.")

    elif st.session_state.explored_card in scenarios:
        current_scenario = st.session_state.explored_card
        st.subheader(f"🛠️ Modifying: {current_scenario}")

        for year in years:
            render_timeline(year, current_scenario)

        # Global Legend
        st.markdown(
            """
        <div style="display: flex; justify-content: center; gap: 20px; margin-top: 10px; margin-bottom: 30px; font-weight: bold;">
            <span><span style="color: #a2cce3;">■</span> JetA</span>
            <span><span style="color: #1a5b7a;">■</span> Hybrid-electric</span>
            <span><span style="color: #3b7a2e;">■</span> H2-SAF</span>
            <span><span style="color: #e2f4c7;">■</span> 100% SAF</span>
        </div>
        """,
            unsafe_allow_html=True,
        )

        # ADDITIONAL METRICS
        col_left, col_right = st.columns(2)
        with col_left:
            st.write("**Scenario Load Focus**")
            term_val = st.checkbox("Airport Terminal", key=f"{current_scenario}_term")
            plant_val = st.checkbox("Manufacturing Plant", key=f"{current_scenario}_plant")
            gse_val = st.checkbox("GSE", key=f"{current_scenario}_gse")
            other_val = st.checkbox("Other Facilities", key=f"{current_scenario}_other")

        with col_right:
            target_yr_val = st.selectbox("Select Target Year", years, key=f"{current_scenario}_target_yr")
            fleet_val = st.radio("Fleet Transition Type", ["Hybrid-Electric", "H2-SAF Combustion"], key=f"{current_scenario}_fleet_type")
            land_val = st.slider("**Land (Acres)**", 0, 100, 75, key=f"{current_scenario}_sld_land")
            gc_val = st.slider("**Grid Cap (MW)**", 0, 100, 75, key=f"{current_scenario}_sld_gc")

        
        st.markdown("---")
        
        # CSV EXPORT
        csv_lines = ["Scenario,Year,Commercial_Pct,Business_Pct,Terminal_Selected,Plant_Selected,GSE_Selected,Other_Facilities_Selected,Target_Year_Selected,Fleet_Type,Land_Acres,Grid_Cap_MW"]
        
        for yr in years:
            comm_pct = st.session_state[f"val_{current_scenario}_comm_{yr}"]
            biz_pct = st.session_state[f"val_{current_scenario}_biz_{yr}"]
            
            #CHECKBOX VALS
            t_str = "YES" if term_val else "NO"
            p_str = "YES" if plant_val else "NO"
            g_str = "YES" if gse_val else "NO"
            o_str = "YES" if other_val else "NO"
            
            line = f"{current_scenario},{yr},{comm_pct},{biz_pct},{t_str},{p_str},{g_str},{o_str},{target_yr_val},{fleet_val},{land_val},{gc_val}"
            csv_lines.append(line)
            
        csv_data = "\n".join(csv_lines)
        
        col_space, col_dl = st.columns([3, 1])
        with col_dl:
            st.download_button(
                label=f"📥 Export {current_scenario} to CSV",
                data=csv_data,
                file_name=f"{current_scenario.lower().replace(' ', '_')}_metrics.csv",
                mime="text/csv",
                use_container_width=True
            )


# -----------------------------------------------------------
# GRAPHICAL PERFORMANCE
# -----------------------------------------------------------
elif page == "Graphical Performance":
    st.title("📊 Graphical Performance")
    st.write("Craft graphs (in NUMPY) from ReOPT metrics.")
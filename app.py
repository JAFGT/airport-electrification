import streamlit as st
from streamlit_extras.stylable_container import stylable_container

# PAGE CONFIG
st.set_page_config(page_title="Airport Electrification Dashboard", page_icon="✈️", layout="wide")

# CSS THEME & CUSTOM CARD STYLING
st.markdown("""
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
</style>
""", unsafe_allow_html=True)

# INITIALIZE SESSION STATE (CARDS)
if "explored_card" not in st.session_state:
    st.session_state.explored_card = None

# Dummy data needed for your layout
years = ["2030", "2040", "2050", "2060", "2070"]

# PAGE SELECTOR
page = st.sidebar.selectbox(
    "**Select Page**",
    ["Decision Dashboard", "Capacity Analytics", "System Performance"]
)

if page == "Decision Dashboard":
    st.markdown("""
        <p style="font-size: 48px; color: #ffffff; font-weight: bold; margin-bottom: 20px;">
        ✈️ Airport Electrification Dashboard ⚡️
        </p>
    """, unsafe_allow_html=True)

    
    scenario_a, scenario_b, scenario_c = st.columns(3, gap="medium")

    # SCENARIO A 
    with scenario_a:
        is_active = (st.session_state.explored_card == "Scenario A")
        bg_color = "rgba(176, 163, 111, 0.2)" if is_active else "rgba(255, 255, 255, 0.05)"
        border_style = "2px solid #b0a36f" if is_active else "1px solid rgba(255, 255, 255, 0.2)"
        shadow = "0 0 15px rgba(176, 163, 111, 0.4)" if is_active else "none"

        with stylable_container(
            key="scenario_a",
            css_styles=f"button {{ background-color: {bg_color} !important; border: {border_style} !important; box-shadow: {shadow} !important; }}"
        ):
            if st.button("**SCENARIO A**", key="scenario_a"):
                st.session_state.explored_card = "Scenario A"
                st.rerun()

    # SCENARIO B
    with scenario_b:
        is_active = (st.session_state.explored_card == "Scenario B")
        bg_color = "rgba(176, 163, 111, 0.2)" if is_active else "rgba(255, 255, 255, 0.05)"
        border_style = "2px solid #b0a36f" if is_active else "1px solid rgba(255, 255, 255, 0.2)"
        shadow = "0 0 15px rgba(176, 163, 111, 0.4)" if is_active else "none"

        with stylable_container(
            key="scenario_b",
            css_styles=f"button {{ background-color: {bg_color} !important; border: {border_style} !important; box-shadow: {shadow} !important; }}"
        ):
            if st.button("📊\n\n**Capacity Analytics**\n\nReview power demands & generation setups", key="scenario_b"):
                st.session_state.explored_card = "Scenario B"
                st.rerun()

    # SCENARIO C
    with scenario_c:
        is_active = (st.session_state.explored_card == "Scenario C")
        bg_color = "rgba(176, 163, 111, 0.2)" if is_active else "rgba(255, 255, 255, 0.05)"
        border_style = "2px solid #b0a36f" if is_active else "1px solid rgba(255, 255, 255, 0.2)"
        shadow = "0 0 15px rgba(176, 163, 111, 0.4)" if is_active else "none"

        with stylable_container(
            key="scenario_c",
            css_styles=f"button {{ background-color: {bg_color} !important; border: {border_style} !important; box-shadow: {shadow} !important; }}"
        ):
            if st.button("📈\n\n**System Performance**\n\nEvaluate grid resilience & metrics", key="scenario_c"):
                st.session_state.explored_card = "Scenario C"
                st.rerun()

    st.markdown("---")

    # 3. DYNAMIC EXPLORATION AREA
    # This section shows up ONLY based on the card that was clicked above.
    
    if st.session_state.explored_card is None:
        st.info("Click on any of the three cards above to explore and modify its metrics.")
        
    elif st.session_state.explored_card == "Scenario A":
        st.subheader("🛠️ Modifying: Scenario A")
        
        col_left, col_right = st.columns(2)
        with col_left:
            st.write("**Energy Load Sectors**")
            st.checkbox("Airport Terminal")
            st.checkbox("Manufacturing Plant")
            st.checkbox("GSE")
            st.checkbox("Other Facilities")
            
        with col_right:
            st.selectbox("Select Target Year", years)
            st.radio("Fleet Transition Type", ["Hybrid-Electric", "H2-SAF Combustion"])
            st.slider("**Land (Acres)**", 0, 100, 75, key="sld_land")
            st.slider("**Grid Cap (MW)**", 0, 100, 75, key="sld_gc")
            
    elif st.session_state.explored_card == "Scenario B":
        st.subheader("🛠️ Modifying: Scenario B")
        # Put the inputs/metrics specific to Scenario B here
        st.number_input("Target Peak Capacity (MW)", value=50.0)
        st.number_input("Storage Capacity (MWh)", value=100.0)
        st.success("You can place graphs or data frames here.")

    elif st.session_state.explored_card == "Scenario C":
        st.subheader("🛠️ Modifying: Scenario C")
        # Put the inputs/metrics specific to Scenario C here
        st.slider("Reliability Target (%)", 90.0, 100.0, 99.5)
        st.metric(label="Calculated Autonomy Fraction", value="85%", delta="5%")
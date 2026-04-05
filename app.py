import streamlit as st
from streamlit_extras.stylable_container import stylable_container

# 1. PAGE CONFIG
st.set_page_config(
    page_title="Airport Electrification Dashboard", page_icon="✈️", layout="wide"
)

# 2. CSS THEME & CUSTOM CARD STYLING
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

# 3. INITIALIZE SESSION STATE (For Cards)
if "explored_card" not in st.session_state:
    st.session_state.explored_card = None

# COMMON DATA
years = ["2030", "2040", "2050", "2060", "2070"]

# PAGE SELECTOR
page = st.sidebar.selectbox(
    "**Select Page**",
    ["Decision Dashboard", "Capacity Analytics", "System Performance"],
)

# -----------------------------------------------------------
# PAGE 1 — DECISION DASHBOARD
# -----------------------------------------------------------
if page == "Decision Dashboard":
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
        bg_color = (
            "rgba(176, 163, 111, 0.2)"
            if is_active
            else "rgba(255, 255, 255, 0.05)"
        )
        border_style = (
            "2px solid #b0a36f" if is_active else "1px solid rgba(255, 255, 255, 0.2)"
        )
        shadow = "0 0 15px rgba(176, 163, 111, 0.4)" if is_active else "none"

        with stylable_container(
            key="scenario_a",
            css_styles=f"button {{ background-color: {bg_color} !important; border: {border_style} !important; box-shadow: {shadow} !important; }}",
        ):
            if st.button("**SCENARIO A**", key="scenario_a_btn"):
                st.session_state.explored_card = "Scenario A"
                st.rerun()

    # --- SCENARIO B CARD ---
    with scenario_b:
        is_active = st.session_state.explored_card == "Scenario B"
        bg_color = (
            "rgba(176, 163, 111, 0.2)"
            if is_active
            else "rgba(255, 255, 255, 0.05)"
        )
        border_style = (
            "2px solid #b0a36f" if is_active else "1px solid rgba(255, 255, 255, 0.2)"
        )
        shadow = "0 0 15px rgba(176, 163, 111, 0.4)" if is_active else "none"

        with stylable_container(
            key="scenario_b",
            css_styles=f"button {{ background-color: {bg_color} !important; border: {border_style} !important; box-shadow: {shadow} !important; }}",
        ):
            if st.button(
                "📊\n\n**Capacity Analytics**\n\nReview power demands & generation setups",
                key="scenario_b_btn",
            ):
                st.session_state.explored_card = "Scenario B"
                st.rerun()

    # --- SCENARIO C CARD ---
    with scenario_c:
        is_active = st.session_state.explored_card == "Scenario C"
        bg_color = (
            "rgba(176, 163, 111, 0.2)"
            if is_active
            else "rgba(255, 255, 255, 0.05)"
        )
        border_style = (
            "2px solid #b0a36f" if is_active else "1px solid rgba(255, 255, 255, 0.2)"
        )
        shadow = "0 0 15px rgba(176, 163, 111, 0.4)" if is_active else "none"

        with stylable_container(
            key="scenario_c",
            css_styles=f"button {{ background-color: {bg_color} !important; border: {border_style} !important; box-shadow: {shadow} !important; }}",
        ):
            if st.button(
                "📈\n\n**System Performance**\n\nEvaluate grid resilience & metrics",
                key="scenario_c_btn",
            ):
                st.session_state.explored_card = "Scenario C"
                st.rerun()

    st.markdown("---")

    # --- CARD MODIFIERS (DYNAMIC WORKSPACE) ---

    if st.session_state.explored_card is None:
        st.info(
            "Click on any of the three cards above to explore and modify its metrics."
        )

    # --- SCENARIO A ACTIVE ---
    elif st.session_state.explored_card == "Scenario A":
        st.subheader("🛠️ Modifying: Scenario A")

        # Function to render timeline per year
        def render_timeline(selected_year):
            st.markdown(f"### 📅 Projections for Year {selected_year}")

            col_sliders, col_visual = st.columns([1, 1.5], gap="medium")

            with col_sliders:
                commercial_pct = st.slider(
                    f"Commercial Hybrid-Electric Mix (%)",
                    0,
                    100,
                    50,
                    step=5,
                    key=f"comm_pct_{selected_year}",
                )
                business_saf_pct = st.slider(
                    f"Business 100% SAF Mix (%)",
                    0,
                    100,
                    90,
                    step=5,
                    key=f"biz_pct_{selected_year}",
                )

            comm_remaining = 100 - commercial_pct
            biz_remaining = 100 - business_saf_pct

            with col_visual:
                st.html(
                    f"""
                <div class="timeline-container">
                    <div class="timeline-labels">
                        <span>2030</span>
                        <span>2040</span>
                        <span>2050</span>
                        <span>2060</span>
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

        # Render all timelines stacked on top of each other
        for year in years:
            render_timeline(year)

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

        # Bottom Resumed Metrics
        col_left, col_right = st.columns(2)
        with col_left:
            st.write("**Energy Load Sectors**")
            st.checkbox("Airport Terminal")
            st.checkbox("Manufacturing Plant")
            st.checkbox("GSE")
            st.checkbox("Other Facilities")

        with col_right:
            st.selectbox("Select Target Year", years, key="shared_target_yr")
            st.radio(
                "Fleet Transition Type", ["Hybrid-Electric", "H2-SAF Combustion"]
            )
            st.slider("**Land (Acres)**", 0, 100, 75, key="sld_land")
            st.slider("**Grid Cap (MW)**", 0, 100, 75, key="sld_gc")

    # --- SCENARIO B ACTIVE ---
    elif st.session_state.explored_card == "Scenario B":
        st.subheader("🛠️ Modifying: Scenario B")
        st.number_input("Target Peak Capacity (MW)", value=50.0)
        st.number_input("Storage Capacity (MWh)", value=100.0)
        st.success(
            "Capacity Analytics layout ready. You can place graphs or data frames here."
        )

    # --- SCENARIO C ACTIVE ---
    elif st.session_state.explored_card == "Scenario C":
        st.subheader("🛠️ Modifying: Scenario C")
        st.slider("Reliability Target (%)", 90.0, 100.0, 99.5)
        st.metric(label="Calculated Autonomy Fraction", value="85%", delta="5%")


# -----------------------------------------------------------
# STANDALONE PAGES
# -----------------------------------------------------------
elif page == "Capacity Analytics":
    st.title("📊 Capacity Analytics")
    st.write(
        "This page will contain capacity modeling, load curves, and charts."
    )

elif page == "System Performance":
    st.title("⚙️ System Performance")
    st.write(
        "This page will contain performance KPIs, uptime analytics, resilience, etc."
    )
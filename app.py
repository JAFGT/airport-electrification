import streamlit as st
from streamlit_extras.stylable_container import stylable_container

# PAGE CONFIG
st.set_page_config(
    page_title="Airport Electrification Dashboard", page_icon="✈️", layout="wide"
)

# CSS THEME
st.markdown(
    """
<style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f0c29 0%, #0a203c 50%, #05172a 100%);
        color: #ffffff;
    }
    [data-testid="stHeader"] {background: rgba(0,0,0,0);}

    div[data-testid="stVerticalBlock"] > div:has(div.stSlider) {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(176, 163, 111, 0.3);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 5px;
        backdrop-filter: blur(10px);
    }

    .stButton > button {
        background-color: rgba(10, 32, 60, 0.7);
        color: #b0a36f;
        border: 1px solid #b0a36f;
        border-radius: 8px;
        width: 100% !important; 
        padding: 10px 20px;
        font-weight: 600;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 20px !important;
    }
    .stButton > button:hover {
        border-color: #ffffff;
        color: #ffffff;
        box-shadow: 0 0 12px rgba(176,163,111,0.5);
        transform: translateY(-2px);
    }
</style>
""",
    unsafe_allow_html=True,
)


# PAGE SELECTOR
page = st.sidebar.selectbox(
    "**Select Page**",
    ["Decision Dashboard", "Capacity Analytics", "System Performance"],
)


# COMMON DATA
sectors = ["Airport Terminal", "GSE", "Manufacturing Plant", "Other Facilities"]
years = ["2030", "2040", "2050", "2060", "2070"]
ftts = ["Hybrid-Electric", "H2-SAF Combustion"]

# TOGGLE SESSION STATES
for name in sectors + years + ftts:
    key = name.replace(" ", "_")
    if key not in st.session_state:
        st.session_state[key] = False


# BUTTON FUNCTIONS
def create_general_button(label):
    key = label.replace(" ", "_")
    is_active = st.session_state[key]
    bg = "#b0a36f !important" if is_active else "#0a203c"
    border = (
        "2px solid #ffffff !important" if is_active else "1px solid #b0a36f"
    )
    color = "#ffffff !important" if is_active else "#b0a36f"
    glow = "inset 0 0 15px #b0a36f" if is_active else "none"

    with stylable_container(
        key=f"wrap_{key}",
        css_styles=f"""
        button {{
            background-color:{bg};
            border:{border};
            color:{color};
            box-shadow:{glow};
        }}""",
    ):
        if st.button(label, key=f"btn_{key}"):
            st.session_state[key] = not st.session_state[key]
            st.rerun()


def create_year_button(year):
    key = year.replace(" ", "_")
    is_active = st.session_state[key]
    border = (
        "2px solid #69ff47 !important" if is_active else "1px solid #ffffff"
    )
    color = "#69ff47 !important" if is_active else "#ffffff"
    glow = "inset 0 0 15px #69ff47" if is_active else "none"

    with stylable_container(
        key=f"wrap_{key}",
        css_styles=f"""
        button {{
            border:{border};
            color:{color};
            box-shadow:{glow};
        }}""",
    ):
        if st.button(year, key=f"btn_{key}"):
            st.session_state[key] = not st.session_state[key]
            st.rerun()


# PAGE 1 — DECISION DASHBOARD
# -----------------------------------------------------------
if page == "Decision Dashboard":

    st.markdown(
        """
        <p style="font-size: 48px; color: #ffffff; font-weight: bold;">
        ✈️ Airport Electrification Dashboard ⚡️
        </p>
    """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3, gap="large")

    # -- Column 1: Scenario Inputs --
    with col1:
        st.markdown(
            '<p style="font-size: 32px; color: #b0a36f; text-align:center;">Scenario Inputs</p>',
            unsafe_allow_html=True,
        )

        st.subheader("Energy Load Sectors")
        left, right = st.columns(2)
        with left:
            create_general_button("Airport Terminal")
            create_general_button("Manufacturing Plant")
        with right:
            create_general_button("GSE")
            create_general_button("Other Facilities")

        st.subheader("Target Year")
        cy = st.columns(len(years))
        for i, year in enumerate(years):
            with cy[i]:
                create_year_button(year)

        st.subheader("Fleet Transition Type")
        ct1, ct2 = st.columns(2)
        with ct1:
            create_general_button("Hybrid-Electric")
        with ct2:
            create_general_button("H2-SAF Combustion")

        st.slider("**Land (Acres)**", 0, 100, 75, key="sld_land")
        st.slider("**Grid Cap (MW)**", 0, 100, 75, key="sld_gc")

    # -- Column 2: Capacity Analytics (Dynamic based on buttons) --
    with col2:
        st.markdown(
            '<p style="font-size: 32px; color: #b0a36f; text-align:center;">Capacity Analytics</p>',
            unsafe_allow_html=True,
        )

        # Check which energy load sectors are active
        active_sectors = [s for s in sectors if st.session_state[s.replace(" ", "_")]]

        if not active_sectors:
            st.info("👈 Select one or more Energy Load Sectors to view capacity metrics.")
        else:
            for sector in active_sectors:
                st.markdown(f"#### 📊 {sector} Metrics")
                
                # Render dummy metrics or controls based on the selected card
                if sector == "Airport Terminal":
                    st.metric(label="Peak Demand", value="15 MW", delta="2 MW")
                    st.metric(label="Required Solar Array", value="45 Acres", delta="-5 Acres")
                elif sector == "GSE":
                    st.metric(label="Fleet Charging Load", value="8 MW")
                    st.metric(label="Chargers Needed", value="42 Units")
                elif sector == "Manufacturing Plant":
                    st.metric(label="Plant Baseload", value="32 MW", delta="High")
                elif sector == "Other Facilities":
                    st.metric(label="Baseline Energy Use", value="5 MW")
                
                st.markdown("---")

    # -- Column 3: System Performance (Dynamic based on buttons) --
    with col3:
        st.markdown(
            '<p style="font-size: 32px; color: #b0a36f; text-align:center;">System Performance</p>',
            unsafe_allow_html=True,
        )

        if not active_sectors:
            st.info("👈 Select sectors to view system performance indicators.")
        else:
            for sector in active_sectors:
                st.markdown(f"#### ⚙️ {sector} Analytics")
                
                if sector == "Airport Terminal":
                    st.success("Grid Reliability: 99.9%")
                    st.progress(0.85, text="Terminal Autonomy Fraction")
                elif sector == "GSE":
                    st.success("Smart charging reduces peak by 30%")
                    st.progress(0.95, text="Fleet Readiness Score")
                elif sector == "Manufacturing Plant":
                    st.warning("High risk of peak overloads.")
                    st.progress(0.40, text="Plant Autonomy Fraction")
                elif sector == "Other Facilities":
                    st.success("Stable baseline.")
                    st.progress(0.60, text="Facilities Uptime")
                
                st.markdown("---")

    st.markdown("---")


# PAGE 2 — CAPACITY ANALYTICS (Standalone Page)
# -----------------------------------------------------------
elif page == "Capacity Analytics":
    st.title("📊 Capacity Analytics")
    st.write(
        "This page will contain capacity modeling, load curves, and charts."
    )


# PAGE 3 — SYSTEM PERFORMANCE (Standalone Page)
# -----------------------------------------------------------
elif page == "System Performance":
    st.title("⚙️ System Performance")
    st.write(
        "This page will contain performance KPIs, uptime analytics, resilience, etc."
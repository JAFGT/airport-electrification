import streamlit as st
from streamlit_extras.buy_me_a_coffee import button as coffee_button
from streamlit_extras.annotated_text import annotated_text
from streamlit_extras.stylable_container import stylable_container

# PAGE CONFIG
st.set_page_config(page_title="Airport Electrification Dashboard", page_icon="✈️", layout="wide")

# CSS STYLING
st.markdown("""
<style>
    /* BACKGROUND GRADIENT */
    [data-testid="stAppViewContainer"] {background: linear-gradient(135deg, #0f0c29 0%, #0a203c 50%, #05172a 100%); color: #ffffff;}
    
    /* TRANSPARENT HEADER */
    [data-testid="stHeader"] {background: rgba(0,0,0,0);}

    /* CARD STYLING (SLIDERS) */
    div[data-testid="stVerticalBlock"] > div:has(div.stSlider) {background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(176, 163, 111, 0.3); border-radius: 15px; padding: 10px; backdrop-filter: blur(10px); margin-bottom: 5px;}

    div[data-testid="stVerticalBlock"] > div:has(div.stColumn]) {padding: 20px !important}
    
    /* Base Button Style */
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

    /* Hover State */
    .stButton > button:hover {
        border-color: #ffffff;
        color: #ffffff;
        box-shadow: 0 0 12px rgba(176, 163, 111, 0.5);
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

# DATA SETUP
sectors = ["Airport Terminal", "GSE", "Manufacturing Plant", "Other Facilities"]
years = ["2030","2040","2050","2060","2070"]
ftts = ["Hybrid-Electric", "H2-SAF Combustion"]

# INITIALIZE SESSION STATE
for sector in sectors:
    key = f"{sector.replace(' ', '_')}"
    if key not in st.session_state:
        st.session_state[key] = False
for year in years:
    key = f"{year.replace(' ', '_')}"
    if key not in st.session_state:
        st.session_state[key] = False
for ftt in ftts:
    key = f"{ftt.replace(' ', '_')}"
    if key not in st.session_state:
        st.session_state[key] = False


# CREATE GENERAL BUTTON
def create_general_button(general):
    clean_name = general.replace(' ', '_')
    key = f"{clean_name}"
    is_active = st.session_state[key]
    # SECTOR BUTTON STYLING
    bg_color = '#b0a36f !important' if is_active else '#0a203c'
    border_style = '2px solid #ffffff !important' if is_active else '1px solid #b0a36f'
    text_color = '#ffffff !important' if is_active else '#b0a36f'
    glow = 'inset 0 0 15px #b0a36f' if is_active else 'none'
    with stylable_container(
        key=f"container_{key}",
        css_styles=f"""
            button {{ background-color: {bg_color}; border: {border_style}; color: {text_color}; box-shadow: {glow};}}
        """
    ):
        if st.button(general, key=f"btn_{key}"):
            st.session_state[key] = not st.session_state[key]
            st.rerun()

# CREATE YEAR BUTTON
def create_year_button(year):
    clean_name = year.replace(' ', '_')
    key = f"{clean_name}"
    is_active = st.session_state[key]
    # YEAR BUTTON STYLING
    bg_color = '#0a203c !important' if is_active else '#0a203c'
    border_style = '2px solid #69ff47 !important' if is_active else '1px solid #ffffff'
    text_color = '#69ff47 !important' if is_active else '#ffffff'
    glow = 'inset 0 0 15px #69ff47' if is_active else 'none'
    with stylable_container(
        key=f"container_{key}",
        css_styles=f"""
            button {{ background-color: {bg_color}; border: {border_style}; color: {text_color}; box-shadow: {glow};}}
        """
    ):
        if st.button(year, key=f"btn_{key}"):
            st.session_state[key] = not st.session_state[key]
            st.rerun()

# UI Layout
st.markdown('<p style="font-size: 48px; color: #ffffff; font-weight: bold; text-align: left; margin-bottom: 30px;">✈️ Airport Electrification Dashboard ⚡️</p>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown('<p style="font-size: 32px; color: #b0a36f; font-weight: bold;text-align: center;">Scenario Inputs</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 24px; color: #ffffff; font-weight: bold;">Energy Load Sectors</p>', unsafe_allow_html=True)
    left, right = st.columns(2)
    with left:
        create_general_button("Airport Terminal")
        create_general_button("Manufacturing Plant")
    with right:
        create_general_button("GSE")
        create_general_button("Other Facilities")

    st.markdown('<p style="font-size: 24px; color: #ffffff; font-weight: bold; margin-top: 20px;">Target Year</p>', unsafe_allow_html=True)
    cy = st.columns(5)
    for i, year in enumerate(years):
        with cy[i]: create_year_button(year)

    st.markdown('<p style="font-size: 24px; color: #ffffff; font-weight: bold; margin-top: 20px;">Fleet Transition Type</p>', unsafe_allow_html=True)
    ct1, ct2 = st.columns(2)
    with ct1: create_general_button("Hybrid-Electric")
    with ct2: create_general_button("H2-SAF Combustion")   

    st.slider("**Land (Acres)**", 0, 100, 75, key="sld_land")
    st.slider("**Grid Cap (MW)**", 0, 100, 75, key="sld_gc")



with col2:
    st.markdown("### Gate B")
    st.slider("Capacity B", 0, 100, 30, key="sld_b")

with col3:
    st.markdown("### Gate C")
    st.slider("Capacity C", 0, 100, 75, key="sld_c")

# 7. SUMMARY DISPLAY
st.markdown("---")
st.subheader("📊 Monitoring Summary")

checked_list = [s for s in sectors if st.session_state[f"{s.replace(' ', '_')}"]]

if checked_list:
    display_args = ["Gate A Status: "]
    for item in checked_list:
        display_args.append((item, "ACTIVE", "#b0a36f"))
        display_args.append("  ")
    annotated_text(*display_args)
else:
    st.write("*No sectors active in Gate A*")

st.markdown("<br>", unsafe_allow_html=True)

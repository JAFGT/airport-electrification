import streamlit as st
from streamlit_extras.buy_me_a_coffee import button as coffee_button
from streamlit_extras.annotated_text import annotated_text
from streamlit_extras.stylable_container import stylable_container

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="Airport Electrification Dashboard",
    page_icon="✈️",
    layout="wide"
)

# 2. CSS FOR BASE STYLING
st.markdown("""
<style>
    /* Main Background Gradient */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f0c29 0%, #0a203c 50%, #05172a 100%); 
        color: #ffffff;
    }
    
    /* Transparent Header */
    [data-testid="stHeader"] {background: rgba(0,0,0,0);}

    /* Card Styling for Sliders */
    div[data-testid="stVerticalBlock"] > div:has(div.stSlider) {
        background: rgba(255, 255, 255, 0.05); 
        border: 1px solid rgba(176, 163, 111, 0.3); 
        border-radius: 15px; 
        padding: 20px; 
        backdrop-filter: blur(10px); 
        margin-bottom: 10px;
    }

    /* Base Button Style */
    .stButton > button {
        background-color: rgba(10, 32, 60, 0.7);
        color: #b0a36f;
        border: 1px solid #b0a36f;
        border-radius: 8px;
        width: 100%;
        padding: 10px 20px;
        font-weight: 600;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
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

# 3. DATA SETUP
sectors = ["Airport Terminal", "GSE", "Manufacturing Plant", "Other Facilities"]
gate_id = "sec1"

# 4. INITIALIZE SESSION STATE
for sector in sectors:
    key = f"{gate_id}_{sector.replace(' ', '_')}"
    if key not in st.session_state:
        st.session_state[key] = False

# 5. HELPER FUNCTION (Corrected F-String Syntax)
def create_sector_button(gate_id, sector):
    clean_name = sector.replace(' ', '_')
    key = f"{gate_id}_{clean_name}"
    is_active = st.session_state[key]
    
    # Python requires double {{ }} to render a literal { } in an f-string
    bg_color = 'rgba(176, 163, 111, 0.4) !important' if is_active else 'rgba(10, 32, 60, 0.7)'
    border_style = '2px solid #ffffff !important' if is_active else '1px solid #b0a36f'
    text_color = '#ffffff !important' if is_active else '#b0a36f'
    glow = 'inset 0 0 15px rgba(176, 163, 111, 0.3)' if is_active else 'none'

    with stylable_container(
        key=f"container_{key}",
        css_styles=f"""
            button {{
                background-color: {bg_color};
                border: {border_style};
                color: {text_color};
                box-shadow: {glow};
            }}
        """
    ):
        if st.button(sector, key=f"btn_{key}"):
            st.session_state[key] = not st.session_state[key]
            st.rerun()

# 6. UI LAYOUT
st.title("✈️ Airport Dashboard")

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("### Gate A")
    st.slider("Capacity A", 0, 100, 50, key="sld_a")
    st.write("#### Energy Sectors")
    for sector in sectors:
        create_sector_button("sec1", sector)

with col2:
    st.markdown("### Gate B")
    st.slider("Capacity B", 0, 100, 30, key="sld_b")
    st.info("Managed via Gate A")

with col3:
    st.markdown("### Gate C")
    st.slider("Capacity C", 0, 100, 75, key="sld_c")
    st.info("Managed via Gate A")

# 7. SUMMARY DISPLAY
st.markdown("---")
st.subheader("📊 Monitoring Summary")

checked_list = [s for s in sectors if st.session_state[f"sec1_{s.replace(' ', '_')}"]]

if checked_list:
    display_args = ["Gate A Status: "]
    for item in checked_list:
        display_args.append((item, "ACTIVE", "#b0a36f"))
        display_args.append("  ")
    annotated_text(*display_args)
else:
    st.write("*No sectors active in Gate A*")

st.markdown("<br>", unsafe_allow_html=True)

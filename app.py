import streamlit as st
from streamlit_extras.buy_me_a_coffee import button as coffee_button
from streamlit_extras.annotated_text import annotated_text

# 1. Page Configuration
st.set_page_config(
    page_title="Airport Energy Dashboard",
    page_icon="✈️",
    layout="wide"
)

# 2. Enhanced CSS for "Nice" Buttons and Glassmorphism
st.markdown("""
<style>
    /* Main Background Gradient */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f0c29 0%, #0a203c 50%, #05172a 100%);
        color: #ffffff;
    }

    /* Transparent Header */
    [data-testid="stHeader"] {
        background: rgba(0,0,0,0);
    }

    /* Gate Container Styling (Cards) */
    div[data-testid="stVerticalBlock"] > div:has(div.stButton) {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(176, 163, 111, 0.3);
        border-radius: 15px;
        padding: 20px;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }

    /* The "Nice" Button Styling */
    .stButton > button {
        background-color: rgba(10, 32, 60, 0.7);
        color: #b0a36f;
        border: 1px solid #b0a36f;
        border-radius: 8px;
        width: 100%;
        padding: 10px 0;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    /* Hover Effect */
    .stButton > button:hover {
        background-color: #1a3a5f;
        border-color: #ffffff;
        color: #ffffff;
        box-shadow: 0 0 12px rgba(176, 163, 111, 0.5);
        transform: translateY(-2px);
    }

    /* Active/Pressed State */
    .stButton > button:active {
        background-color: #b0a36f !important;
        color: #0f0c29 !important;
        transform: translateY(0);
    }

    /* Specific style for "Checked" buttons (using the emoji as a hook) */
    button:has(p:contains("✅")) {
        background-color: rgba(176, 163, 111, 0.2) !important;
        border: 1.5px solid #b0a36f !important;
        box-shadow: inset 0 0 10px rgba(176, 163, 111, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# 3. Data Setup
sectors = ["Airport Terminal", "GSE", "Manufacturing Plant", "Other Facilities"]
gate_keys = {"Gate A": "sec1", "Gate B": "sec2", "Gate C": "sec3"}

# 4. Initialize Session State
for g_id in gate_keys.values():
    for sector in sectors:
        key = f"{g_id}_{sector.replace(' ', '_')}"
        if key not in st.session_state:
            st.session_state[key] = False

# 5. Logic: Helper function for the buttons
def create_sector_button(gate_id, sector):
    clean_name = sector.replace(' ', '_')
    key = f"{gate_id}_{clean_name}"
    
    # Toggle label based on state
    label = f"✅ {sector}" if st.session_state[key] else sector
    
    if st.button(label, key=f"btn_{key}"):
        st.session_state[key] = not st.session_state[key]
        st.rerun()

# 6. UI Layout
st.title("✈️ Airport Dashboard")
st.markdown("Monitor and toggle energy sectors across terminal gates.")

col1, col2, col3 = st.columns(3, gap="large")

# Gate A
with col1:
    st.markdown("### Gate A")
    st.slider("Capacity A", 0, 100, 50, key="sld_a")
    st.write("#### Energy Sectors")
    for sector in sectors:
        create_sector_button("sec1", sector)

# Gate B
with col2:
    st.markdown("### Gate B")
    st.slider("Capacity B", 0, 100, 30, key="sld_b")
    st.write("#### Energy Sectors")
    for sector in sectors:
        create_sector_button("sec2", sector)

# Gate C
with col3:
    st.markdown("### Gate C")
    st.slider("Capacity C", 0, 100, 75, key="sld_c")
    st.write("#### Energy Sectors")
    for sector in sectors:
        create_sector_button("sec3", sector)

# 7. Summary Display with Annotated Text
st.markdown("---")
st.subheader("📊 Monitoring Summary")

has_any_checked = False
for gate_name, gate_id in gate_keys.items():
    checked_list = [s for s in sectors if st.session_state[f"{gate_id}_{s.replace(' ', '_')}"]]
    
    if checked_list:
        has_any_checked = True
        # Build the annotated text arguments
        args = [f"{gate_name}: "]
        for item in checked_list:
            args.append((item, "ACTIVE", "#b0a36f"))
            args.append("  ")
        annotated_text(*args)
    else:
        st.write(f"*{gate_name}: No sectors active*")

# 8. Footer Extra
if not has_any_checked:
    st.info("Select energy sectors above to begin monitoring.")

st.markdown("<br>", unsafe_allow_html=True)
coffee_button(username="yourname", floating=False, text="Support Dashboard")

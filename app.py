import streamlit as st
from streamlit_extras.buy_me_a_coffee import button as coffee_button
from streamlit_extras.annotated_text import annotated_text

# PAGE CONFIG
st.set_page_config(page_title="Airport Electrification Dashboard",page_icon="✈️", layout="wide")

# CSS FOR STULING
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {background: linear-gradient(135deg, #0f0c29 0%, #0a203c 50%, #05172a 100%); color: #ffffff;}
    [data-testid="stHeader"] {background: rgba(0,0,0,0);}

    /* Gate Container Styling 
    div[data-testid="stVerticalBlock"] > div:has(div.stButton), 
    div[data-testid="stVerticalBlock"] > div:has(div.stSlider) {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(176, 163, 111, 0.3);
        border-radius: 15px;
        padding: 20px;
        backdrop-filter: blur(10px);
        margin-bottom: 10px;
    }*/

    .stButton > button {
        background-color: rgba(10, 32, 60, 0.7);
        color: #b0a36f;
        border: 1px solid #b0a36f;
        border-radius: 8px;
        width: 100%;
        padding: 10px 0;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        border-color: #ffffff;
        color: #ffffff;
        box-shadow: 0 0 12px rgba(176, 163, 111, 0.5);
        transform: translateY(-2px);
    }

    /* Active State Style */
    button:has(p:contains("✅")) {
        background-color: rgba(176, 163, 111, 0.2) !important;
        border: 1.5px solid #b0a36f !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Data Setup
sectors = ["Airport Terminal", "GSE", "Manufacturing Plant", "Other Facilities"]
# We only need the key for sec1 (Gate A) now
gate_id = "sec1"

# 4. Initialize Session State for Gate A only
for sector in sectors:
    key = f"{gate_id}_{sector.replace(' ', '_')}"
    if key not in st.session_state:
        st.session_state[key] = False

# 5. Logic: Helper function
def create_sector_button(gate_id, sector):
    clean_name = sector.replace(' ', '_')
    key = f"{gate_id}_{clean_name}"
    label = f"✅ {sector}" if st.session_state[key] else sector
    
    if st.button(label, key=f"btn_{key}"):
        st.session_state[key] = not st.session_state[key]
        st.rerun()

# 6. UI Layout
st.title("✈️ Airport Dashboard")

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("### Gate A")
    st.slider("Capacity A", 0, 100, 50, key="sld_a")
    st.write("#### Energy Sectors")
    # Buttons ONLY rendered here
    for sector in sectors:
        create_sector_button("sec1", sector)

with col2:
    st.markdown("### Gate B")
    st.slider("Capacity B", 0, 100, 30, key="sld_b")
    st.info("Sectors managed via Primary Terminal (Gate A)")

with col3:
    st.markdown("### Gate C")
    st.slider("Capacity C", 0, 100, 75, key="sld_c")
    st.info("Sectors managed via Primary Terminal (Gate A)")

# 7. Summary Display
st.markdown("---")
st.subheader("📊 Monitoring Summary")

checked_list = [s for s in sectors if st.session_state[f"sec1_{s.replace(' ', '_')}"]]

if checked_list:
    args = ["Gate A Active: "]
    for item in checked_list:
        args.append((item, "ACTIVE", "#b0a36f"))
        args.append("  ")
    annotated_text(*args)
else:
    st.write("*No sectors active in Gate A*")

st.markdown("<br>", unsafe_allow_html=True)
coffee_button(username="yourname", floating=False, text="Support Dashboard")

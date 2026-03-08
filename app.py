import streamlit as st

st.set_page_config(layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f0c29 0%, #0a203c 50%, #05172a 100%);
    color: #ffffff;
}
[data-testid="stHeader"] {background: rgba(0,0,0,0);}
.st-key-blc {
    background-color: #102f54; 
    border: 2px solid #b0a36f; 
    border-radius: 12px; 
    padding: 20px; 
    margin-bottom: 20px; 
    backdrop-filter: blur(5px);
}
.stButton>button {
    background-color: #0a203c;
    color: #b0a36f;
    border-radius: 8px;
    border: 2px solid #b0a36f;
    width: 100%;
    padding: 8px 0;
    font-weight: bold;
    margin-bottom: 5px;
}
.stButton>button:active {
    background-color: #b0a36f;
    color: #102f54;
}
</style>
""", unsafe_allow_html=True)

st.title("Airport Dashboard")

# ---------- Energy sectors ----------
sectors = ["Airport Terminal", "GSE", "Manufacturing Plant", "Other Facilities"]

# ---------- Pre-assign session state and keys ----------
buttons = {
    "sec1": {s: f"sec1_{s}_btn" for s in sectors},
    "sec2": {s: f"sec2_{s}_btn" for s in sectors},
    "sec3": {s: f"sec3_{s}_btn" for s in sectors}
}

# Initialize session state
for container, sector_keys in buttons.items():
    for sector, key in sector_keys.items():
        state_key = f"{container}_{sector}"
        if state_key not in st.session_state:
            st.session_state[state_key] = False

# ---------- Helper function ----------
def toggle(container, sector):
    state_key = f"{container}_{sector}"
    widget_key = buttons[container][sector]
    label = f"✅ {sector}" if st.session_state[state_key] else sector
    if st.button(label, key=widget_key):
        st.session_state[state_key] = not st.session_state[state_key]

# ---------- Columns ----------
col1, col2, col3 = st.columns([1,1,1], gap="medium")

# Container 1
with col1:
    with st.container():
        st.write("### Gate A")
        st.slider("Capacity A", 0, 100, 50)
        st.write("#### Energy Sectors")
        for sector in sectors:
            toggle("sec1", sector)

# Container 2
with col2:
    with st.container():
        st.write("### Gate B")
        st.slider("Capacity B", 0, 100, 30)
        st.write("#### Energy Sectors")
        for sector in sectors:
            toggle("sec2", sector)

# Container 3
with col3:
    with st.container():
        st.write("### Gate C")
        st.slider("Capacity C", 0, 100, 75)
        st.write("#### Energy Sectors")
        for sector in sectors:
            toggle("sec3", sector)

# Display checked sectors
st.markdown("---")
st.write("**Checked Sectors:**")
for container in ["sec1","sec2","sec3"]:
    checked = [s for s in sectors if st.session_state[f"{container}_{s}"]]
    st.write(f"{container}: {checked}")

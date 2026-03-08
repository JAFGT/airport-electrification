import streamlit as st

st.set_page_config(layout="wide")

# CSS (same as yours)
st.markdown("""
<style>
div[data-testid="stContainer"][data-key^="blc"] {
    background-color: #102f54;
    border: 2px solid #b0a36f;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 20px;
    width: 100%;
    box-sizing: border-box;
}

.stButton>button:active {
    background-color: #b0a36f;
    color: #102f54;
}
</style>
""", unsafe_allow_html=True)

st.title("Airport Dashboard")

# Energy sectors
sectors = ["Airport Terminal", "GSE", "Manufacturing Plant", "Other Facilities"]

# ---------- Columns ----------
col1, col2, col3 = st.columns([1,1,1], gap="medium")

# Container 1
with col1:
    with st.container(key="blc1"):
        st.write("### Gate A")
        st.slider("Capacity A", 0, 100, 50)

        for sector in sectors:
            # Make a unique key per container + sector
            button_key = f"blc1_{sector}"

            # Initialize state if not present
            if button_key not in st.session_state:
                st.session_state[button_key] = False

            # Label depends on checked state
            label = f"✅ {sector}" if st.session_state[button_key] else sector

            if st.button(label, key=button_key):
                st.session_state[button_key] = not st.session_state[button_key]

# Container 2
with col2:
    with st.container(key="blc2"):
        st.write("### Gate B")
        st.slider("Capacity B", 0, 100, 30)

# Container 3
with col3:
    with st.container(key="blc3"):
        st.write("### Gate C")
        st.slider("Capacity C", 0, 100, 75)

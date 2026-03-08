import streamlit as st

st.set_page_config(layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>
/* PAGE BACKGROUND */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f0c29 0%, #0a203c 50%, #05172a 100%);
    color: #ffffff;
}

/* HEADER TRANSPARENCY */
[data-testid="stHeader"] {background: rgba(0,0,0,0);}

/* CONTAINER STYLES */
.st-key-blc1, .st-key-blc2, .st-key-blc3 {
    background-color: #102f54; 
    border: 2px solid #b0a36f; 
    border-radius: 12px; 
    padding: 20px; 
    margin-bottom: 20px; 
    backdrop-filter: blur(5px);
}

/* RADIO BUTTON STYLING TO LOOK LIKE BUTTONS */
div[data-baseweb="radio"] label {
    display: block;
    background-color: #0a203c;
    color: #b0a36f;
    border: 2px solid #b0a36f;
    border-radius: 8px;
    padding: 8px 0;
    margin-bottom: 5px;
    text-align: center;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.2s ease-in-out;
}

div[data-baseweb="radio"] input:checked + label {
    background-color: #b0a36f !important;
    color: #102f54 !important;
}
</style>
""", unsafe_allow_html=True)

st.title("Airport Dashboard")

# Energy sectors
sectors = ["Airport Terminal", "GSE", "Manufacturing Plant", "Other Facilities"]

# Columns
col1, col2, col3 = st.columns([1,1,1], gap="medium")

# ---------- Container 1 ----------
with col1:
    with st.container(key="blc1"):
        st.write("### Gate A")
        st.slider("Capacity A", 0, 100, 50)
        st.write("#### Energy Sector")
        selected_sector_1 = st.radio("Select one sector:", sectors, key="radio_blc1")
        st.write(f"Selected: {selected_sector_1}")

# ---------- Container 2 ----------
with col2:
    with st.container(key="blc2"):
        st.write("### Gate B")
        st.slider("Capacity B", 0, 100, 30)
        st.write("#### Energy Sector")
        selected_sector_2 = st.radio("Select one sector:", sectors, key="radio_blc2")
        st.write(f"Selected: {selected_sector_2}")

# ---------- Container 3 ----------
with col3:
    with st.container(key="blc3"):
        st.write("### Gate C")
        st.slider("Capacity C", 0, 100, 75)
        st.write("#### Energy Sector")
        selected_sector_3 = st.radio("Select one sector:", sectors, key="radio_blc3")
        st.write(f"Selected: {selected_sector_3}")

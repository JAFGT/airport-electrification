import streamlit as st

# CSS 
st.markdown("""
<style>
/* Page Background */
[data-testid="stAppViewContainer"] {
    background: #05172a;
    color: #ffffff;
}

/* Header Transparency */
[data-testid="stHeader"] {
    background: #00000000;
}

/* Container Styles */
.st-key-blc1, .st-key-blc2, .st-key-blc3, .st-key-blc4 {
    background-color: #102f54;
    border: 2px solid #b0a36f; 
    border-radius: 12px; 
    padding: 20px; 
    margin-bottom: 20px;
}

/* Titles */
h1, h3 {
    color: #ecf0f1 !important;
}

/* --- SLIDER COLOR OVERRIDE (HEX ONLY) --- */

/* 1. The Active Line (Left of knob) */
.stSlider [data-baseweb="slider"] > div > div > div > div {
    background-color: #b0a36f !important;
}

/* 2. The Knob (The circle) */
.stSlider [data-baseweb="slider"] > div > div > div > div > div {
    background-color: #b0a36f !important;
    border: 2px solid #b0a36f !important;
    box-shadow: none !important;
}

/* 3. The Inactive Line (Right of knob) */
/* Using a dark hex to provide contrast */
.stSlider [data-baseweb="slider"] > div > div {
    background-color: #1c3a5e !important;
}

/* 4. The Value Bubble (Number that pops up) */
div[data-testid="stThumbValue"] {
    background-color: #b0a36f !important;
    color: #05172a !important;
}

/* 5. Removing the red 'ticks' at the start/end */
[data-testid="stTickBarMin"], [data-testid="stTickBarMax"], [data-testid="stSliderTickBar"] {
    color: #1c3a5e !important;
}

</style>
""", unsafe_allow_html=True)

st.title("Airport Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(key="blc1"):
        st.write("### Gate A")
        st.slider("Capacity A", 0, 100, 50, key="s1")

with col2:
    with st.container(key="blc2"):
        st.write("### Gate B")
        st.slider("Capacity B", 0, 100, 30, key="s2")

with col3:
    with st.container(key="blc3"):
        st.write("### Gate C")
        st.slider("Capacity C", 0, 100, 75, key="s3")

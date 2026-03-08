import streamlit as st

# 1. Simple CSS: Target any container with the key "blue_box"
st.markdown("""
<style>
    div[data-element-to-transition-back-to="section_blue_box"] {
        background-color: #102f54;
        padding: 20px;
        border: 2px solid #3498db;
        border-radius: 10px;
    }
    /* Fix text color so it's readable */
    div[data-element-to-transition-back-to="section_blue_box"] p, 
    div[data-element-to-transition-back-to="section_blue_box"] label {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("Airport Dashboard")

# 2. The Container + Slider
with st.container(key="blue_box"):
    st.write("### Control Panel")
    val = st.slider("Select Capacity", 0, 100, 50)
    st.write(f"Current Value: {val}")

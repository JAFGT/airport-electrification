import streamlit as st

# ---------- CSS Styling ----------
# We target the specific container using the key "blue_container"
css = """
<style>
    /* Target the container with the specific key */
    [data-testid="stElementContainer"]:has(div[data-element-to-transition-back-to="section_blue_container"]) {
        background-color: #102f54;
        border: 2px solid #3498db !important;
        border-radius: 8px;
        padding: 25px;
        color: white;
    }

    /* Force text inside this specific container to be white */
    [data-element-to-transition-back-to="section_blue_container"] p, 
    [data-element-to-transition-back-to="section_blue_container"] h2,
    [data-element-to-transition-back-to="section_blue_container"] label {
        color: white !important;
    }
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# ---------- App Content ----------
st.title("Airport Electrification Dashboard")

# ---------- The Styled Blue Container ----------
with st.container(key="blue_container"):
    st.header("Control Panel")
    st.write("Adjust the electrification parameters below:")
    
    # Adding the sliders inside
    param1 = st.slider("Charging Station Capacity (kW)", 0, 500, 150)
    param2 = st.slider("Grid Integration Factor", 0.0, 1.0, 0.4)
    
    st.info(f"Current Settings: {param1}kW at {int(param2*100)}% integration.")

# ---------- Standard Content Below ----------
st.divider()
st.subheader("Data Analysis")
st.write("This section is outside the styled container and uses default theme colors.")

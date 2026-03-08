import streamlit as st

# ---------- CSS Styling ----------
# This targets the container and forces the background color and text visibility
css = """
<style>
    /* Target the container wrapper with the specific key */
    [data-testid="stVerticalBlockBorderWrapper"]:has(div[data-testid="stVerticalBlock"] > div > div > [data-element-to-transition-back-to="section_blue_box"]) {
        background-color: #102f54;
        border: 2px solid #3498db;
        border-radius: 10px;
        padding: 20px;
    }

    /* Ensure all text inside the blue box is white */
    [data-element-to-transition-back-to="section_blue_box"] *,
    [data-element-to-transition-back-to="section_blue_box"] label p {
        color: white !important;
    }
</style>
"""

st.markdown(css, unsafe_allow_html=True)

st.title("Airport Electrification")

# ---------- The Styled Container ----------
# Everything inside this 'with' block will be inside the blue box
with st.container(key="blue_box"):
    st.subheader("⚡ System Settings")
    
    # This slider is now inside the container
    ev_count = st.slider("Number of Electric Ground Vehicles", 0, 500, 125)
    
    st.write(f"Current deployment target: **{ev_count} vehicles**")

# Standard text outside the box
st.write("This text is outside the styled container.")

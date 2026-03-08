import streamlit as st

# ---------- CSS ----------
css = """
<style>
[data-testid="stVerticalBlockBorderWrapper"]:has(div[data-testid="stVerticalBlock"] > div > div > [data-element-to-transition-back-to="section_blc"]) {
    background-color: #102f54;
    border: 2px solid #3498db;
    border-radius: 8px;
    padding: 20px;
    color: white;
}
/* Fix label colors for dark background */
[data-testid="stVerticalBlockBorderWrapper"] label {
    color: white !important;
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

st.title("Airport Electrification Dashboard")

# ---------- Styled Container ----------
with st.container(key="blc"):
    st.header("Control Panel")
    st.write("Adjust the parameters below:")

    param1 = st.slider("Parameter 1", 0, 100, 50)
    param2 = st.slider("Parameter 2", 0.0, 1.0, 0.5)
    param3 = st.slider("Parameter 3", 10, 500, 100)

    st.write(f"Values selected: {param1}, {param2}, {param3}")

# This was likely where your error was:
st.divider() # Correct way to add a horizontal line

# ---------- Unstyled container ----------
with st.container():
    st.header("Normal Container")
    st.write("This one won't have the blue styling.")

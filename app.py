import streamlit as st

# ---------- CSS ----------
css = """
<style>
.st-key-blc {
    background-color: #102f54; /* Dark blue background */
    border: 2px solid #3498db; /* Blue border */
    border-radius: 8px;         /* Rounded corners */
    padding: 20px;              /* Space inside the container */
    margin-bottom: 20px;        /* Space below the container */
    color: white;               /* Make text readable */
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# ---------- App Title ----------
st.title("Airport Electrification Dashboard")

# ---------- Styled Container ----------
st.header("Control Panel")
st.write("Adjust the parameters below:")

# Sliders inside the styled container
param1 = st.slider("Parameter 1", 0, 100, 50)
param2 = st.slider("Parameter 2", 0.0, 1.0, 0.5)
param3 = st.slider("Parameter 3", 10, 500, 100)

st.write(f"Values selected: Param1={param1}, Param2={param2}, Param3={param3}")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Unstyled container for comparison ----------
with st.container(key):
    st.header("This is an unstyled container")
    st.write("Just normal Streamlit elements here.")
    param1 = st.slider("Parameter 1", 0, 100, 50)

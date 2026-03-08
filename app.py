import streamlit as st

# ---------- CSS ----------
# We target the data-testid or the specific key-based div
css = """
<style>
[data-element-to-transition-back-to="section_blc"] {
    background-color: #102f54;
    border: 2px solid #3498db;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 20px;
    color: white;
}

/* Ensure labels inside the dark container are readable */
[data-element-to-transition-back-to="section_blc"] label {
    color: white !important;
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# ---------- App Title ----------
st.title("Airport Electrification Dashboard")

# ---------- Styled Container ----------
# We use the 'key' parameter which Streamlit uses to identify the div
with st.container(key="blc"):
    st.header("Control Panel")
    st.write("Adjust the parameters below:")

    # Sliders are now logically and visually inside the container
    param1 = st.slider("Parameter 1", 0, 100, 50)
    param2 = st.slider("Parameter 2", 0.0, 1.0, 0.5)
    param3 = st.slider("Parameter 3", 10, 500, 100)

    st.write(f"**Values selected:** {param1}, {param2}, {param3}")

---

### Key Changes Made:
* **The `with` Statement:** I moved the sliders inside the `with st.container(key="blc"):` block. This ensures they are physically nested within the div that carries your custom key.
* **CSS Selector:** Streamlit applies the key to a specific attribute. While `.st-key-blc` sometimes works in older versions, using the attribute selector `[data-element-to-transition-back-to="section_blc"]` or simply targeting the `stVerticalBlock` via the key is more robust for current versions.
* **Label Visibility:** I added a small CSS rule to make sure the slider labels turn white, otherwise, they might be hard to read against that dark blue background.

Would you like me to show you how to add a "Reset" button that clears all these sliders back to their defaults?

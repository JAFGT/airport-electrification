import streamlit as st

# Define your CSS
css = """
<style>
.st-key-my_blue_container {
    background-color: rgba(100, 100, 200, 0.3); /* Light blue background */
    border: 2px solid #3498db; /* Blue border */
    border-radius: 8px; /* Rounded corners */
    padding: 20px; /* Space inside the container */
    margin-bottom: 20px; /* Space below the container */
}
</style>
"""

# Inject the CSS into the app
st.markdown(css, unsafe_allow_html=True)

# Use the styled container
with st.container(key="my_blue_container"):
    st.header("This is a styled container")
    st.write("You can place any Streamlit elements here.")

# An unstyled container for comparison
with st.container():
    st.header("This is an unstyled container")

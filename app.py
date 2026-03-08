import streamlit as st

# Add CSS to target containers
st.markdown("""
    <style>
    .custom-container {
        background-color: #001f3f;
        padding: 20px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit container
with st.container():
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    st.write("This container has a blue background and contains widgets")
    st.slider("Slide me", 0, 100)
    st.markdown('</div>', unsafe_allow_html=True)

import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Dashboard", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.card-container {
    background-color: #001f3f;
    padding: 20px;
    border-radius: 12px;
    color: white;
    margin-bottom: 20px;
}
.card-container .stSlider, 
.card-container .stMetric {
    color: white;
}
.card-footer {
    height: 70px;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #0054a3;
    color: white;
    border-radius: 12px;
    margin-top: 50px;
}
.card-footer a {
    color: white;
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# ---------- GRID WITH "CARDS" ----------
col1, col2, col3 = st.columns(3)

with col1:
    container = st.container()
    container.markdown('<div class="card-container">', unsafe_allow_html=True)
    st.metric("Metric 1", "123", "+5%")
    st.slider("Slider 1", 0, 100, 50)
    container.markdown('</div>', unsafe_allow_html=True)

with col2:
    container = st.container()
    container.markdown('<div class="card-container">', unsafe_allow_html=True)
    st.metric("Metric 2", "456", "-2%")
    st.slider("Slider 2", 0, 100, 30)
    container.markdown('</div>', unsafe_allow_html=True)

with col3:
    container = st.container()
    container.markdown('<div class="card-container">', unsafe_allow_html=True)
    st.metric("Metric 3", "789", "+12%")
    st.slider("Slider 3", 0, 100, 70)
    container.markdown('</div>', unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("""
<div class="card-footer">
    For more information, visit <a href='https://www.snowflake.com'>www.snowflake.com</a>
</div>
""", unsafe_allow_html=True)

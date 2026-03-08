import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Airport Electrification Dashboard",
    layout="wide"
)

# ---------- HEADER ----------
st.markdown(
    '<h1 style="color:#ebaa01; font-family:\'Roboto Slab\', serif;">Airport Electrification Dashboard</h1>',
    unsafe_allow_html=True
)
st.markdown("---")

# ---------- CUSTOM CSS FOR CONTAINERS ----------
st.markdown("""
<style>
.stContainer {
    padding: 10px;
}

.card {
    background-color: #001f3f;
    padding: 20px;
    border-radius: 12px;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------- MAIN GRID ----------
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.metric("Metric 1", "123", "+5%")
        st.slider("Slider 1", 0, 100, 50)
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.metric("Metric 2", "456", "-2%")
        st.slider("Slider 2", 0, 100, 30)
        st.markdown('</div>', unsafe_allow_html=True)

with col3:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.metric("Metric 3", "789", "+12%")
        st.slider("Slider 3", 0, 100, 70)
        st.markdown('</div>', unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("""
<div style="
    height: 70px;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #0054a3;
    color: white;
    border-radius: 12px;
    margin-top: 50px;">
    For more information, visit <a href='https://www.snowflake.com' style='color:white; text-decoration:underline;'>www.snowflake.com</a>
</div>
""", unsafe_allow_html=True)

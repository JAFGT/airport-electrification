import streamlit as st

# CSS
st.markdown("""
<style>
/* 1. Change the page background */
[data-testid="stAppViewContainer"] {
    background-color: #0e1117;
}

/* 2. Change the slider color (Track and Thumb) */
/* The track (the line) */
.stSlider [data-baseweb="slider"] > div > div > div > div {
    background-color: #3498db !important;
}

/* The thumb (the circle) */
.stSlider [data-baseweb="slider"] > div > div > div > div > div {
    background-color: #3498db !important;
}

/* 3. Your original container styles */
.st-key-blc1, .st-key-blc2, .st-key-blc3, .st-key-blc4 {
    background-color: rgba(100, 100, 200, 0.3);
    border: 2px solid #3498db; 
    border-radius: 9px; 
    padding: 20px; 
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.title("Airport Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(key="blc1"):
        st.write("### Gate A")
        st.slider("Capacity A", 0, 100, 50, key="s1")

with col2:
    with st.container(key="blc2"):
        st.write("### Gate B")
        st.slider("Capacity B", 0, 100, 30, key="s2")

with col3:
    with st.container(key="blc3"):
        st.write("### Gate C")
        st.slider("Capacity C", 0, 100, 75, key="s3")

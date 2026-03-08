import streamlit as st

# CSS 
st.markdown("""
<style>
/* 1. Change the full page background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f0c29 0%, ##0a203c 50%, #05172a 100%);
    color: #ffffff;
}

/* 2. Make the header transparent */
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

/* Your existing container styles */
.st-key-blc1, .st-key-blc2, .st-key-blc3, .st-key-blc4 {
    background-color: rgba(100, 100, 200, 0.2);
    border: 2px solid #3498db; 
    border-radius: 12px; 
    padding: 20px; 
    margin-bottom: 20px;
    backdrop-filter: blur(5px); /* Adds a nice frosted glass effect */
}

/* Optional: Make titles stand out */
h1, h3 {
    color: #ecf0f1 ! deprivation;
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

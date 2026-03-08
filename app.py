import streamlit as st

st.set_page_config(layout="wide")

# CSS
st.markdown("""
<style>
/* Page Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f0c29 0%, #0a203c 50%, #05172a 100%);
    color: #ffffff;
}

/* Header Transparency */
[data-testid="stHeader"] {background: rgba(0,0,0,0);}

/* Containers targeted by key */
div[data-testid="stContainer"][data-key="blc1"],
div[data-testid="stContainer"][data-key="blc2"],
div[data-testid="stContainer"][data-key="blc3"] {
    background-color: #102f54;
    border: 2px solid #b0a36f;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 20px;
    width: 100%;          /* fill column */
    box-sizing: border-box;
}

/* Titles inside containers */
h1, h3 {color: #ecf0f1 !important;}
</style>
""", unsafe_allow_html=True)

st.title("Airport Dashboard")

# Columns
col1, col2, col3 = st.columns([1,1,1], gap="medium")

# Containers with sliders
with col1:
    with st.container(key="blc1"):
        st.write("### Gate A")
        st.slider("Capacity A", 0, 100, 50)

with col2:
    with st.container(key="blc2"):
        st.write("### That's Crazy LOL")
        st.slider("Capacity B", 0, 100, 30)

with col3:
    with st.container(key="blc3"):
        st.write("### Gate C")
        st.slider("Capacity C", 0, 100, 75)

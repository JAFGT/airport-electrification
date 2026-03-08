import streamlit as st

st.set_page_config(layout="wide")

# CSS

st.markdown("""
<style>

/* PAGE BACKGROUND */
[data-testid="stAppViewContainer"] {background: linear-gradient(135deg, #0f0c29 0%, #0a203c 50%, #05172a 100%); color: #ffffff;}

/* HEADER TRANSPARENCY */
[data-testid="stHeader"] {background: rgba(0,0,0,0);}

/*CONTAINER STYLES*/
.st-key-blc1, .st-key-blc2, .st-key-blc3, .st-key-blc4 {
    background-color: #102f54; border: 2px solid #b0a36f; border-radius: 12px; padding: 20px; margin-bottom: 20px; 
    backdrop-filter: blur(5px); /* Adds a nice frosted glass effect */
}

/* BUTTON */
.stButton>button:active {background-color: #b0a36f; color: #102f54;}

</style>
""", unsafe_allow_html=True) 

#ENERGY LOAD SECTORS
sectors = ["Airport Terminal", "GSE", "Manufacturing Plant", "Other Facilities"]
for sector in sectors:
    if sector not in st.session_state:
        st.session_state[sector] = False  # unchecked by default


st.title("Airport Dashboard")

# Columns
col1, col2, col3 = st.columns([1,1,1], gap="medium")

# Containers with sliders
with col1:
    with st.container(key="blc1"):
        st.write("### Gate A")
        st.slider("Capacity A", 0, 100, 50)
        for sector in sectors:
            label = f"✅ {sector}" if st.session_state[sector] else sector
            if st.button(label, key=f"btn_{sector}"):
                st.session_state[sector] = not st.session_state[sector]

with col2:
    with st.container(key="blc2"):
        st.write("### That's Crazy LOL")
        st.slider("Capacity B", 0, 100, 30)

with col3:
    with st.container(key="blc3"):
        st.write("### Gate C")
        st.slider("Capacity C", 0, 100, 75)

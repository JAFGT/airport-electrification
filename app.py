import streamlit as st

# 1. Simple CSS: Target any container with the key "blue_box"
st.markdown("""
<style>
 .st-key-blc {background-color: rgba(100, 100, 200, 0.3);
 border: 2px solid #3498db; 
 /* Blue border */ border-radius: 8px; 
 /* Rounded corners */ padding: 30px; 
 /* Space inside the container */ margin-bottom: 20px; }
    }
</style>
""", unsafe_allow_html=True)
st.title("Airport Dashboard")
with st.container(key="blc"):
    st.write("### Control Panel")
    val = st.slider("Select Capacity", 0, 100, 50)
    st.write(f"Current Value: {val}")

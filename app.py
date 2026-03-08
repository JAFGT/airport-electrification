import streamlit as st

# ---------- CSS ----------
st.markdown("""
<style>
/* Target multiple keys by separating them with commas */
.st-key-blc1, .st-key-blc2, .st-key-blc3 {
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
    # Unique key for the container
    with st.container(key="blc1"):
        st.write("### Gate A")
        st.slider("Capacity A", 0, 100, 50, key="s1")

with col2:
    # Unique key for the container
    with st.container(key="blc2"):
        st.write("### Gate B")
        st.slider("Capacity B", 0, 100, 30, key="s2")

with col3:
    # Unique key for the container
    with st.container(key="blc3"):
        st.write("### Gate C")
        st.slider("Capacity C", 0, 100, 75, key="s3")

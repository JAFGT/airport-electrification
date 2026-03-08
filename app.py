import streamlit as st

# ---------- CSS ----------
st.markdown("""
<style>
/* This targets any container with the key 'blc' */
.st-key-blc {
    background-color: rgba(100, 100, 200, 0.3);
    border: 2px solid #3498db; 
    border-radius: 9px; 
    padding: 20px; 
    margin-bottom: 20px;
    height: 300px; /* Optional: keeps boxes even if content differs */
}
</style>
""", unsafe_allow_html=True)

st.title("Airport Dashboard")

# ---------- Layout: Three Columns ----------
col1, col2, col3 = st.columns(3)

with col1:
    with st.container(key="blc"):
        st.write("### Gate A")
        val1 = st.slider("Capacity A", 0, 100, 50, key="s1")
        st.write(f"Value: {val1}")

with col2:
    with st.container(key="blc"):
        st.write("### Gate B")
        val2 = st.slider("Capacity B", 0, 100, 30, key="s2")
        st.write(f"Value: {val2}")

with col3:
    with st.container(key="blc"):
        st.write("### Gate C")
        val3 = st.slider("Capacity C", 0, 100, 75, key="s3")
        st.write(f"Value: {val3}")

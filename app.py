import streamlit as st

st.set_page_config(layout="wide")

# ---------- HEADER ----------
st.markdown('<h1 style="color:#ebaa01; font-family:\'Roboto Slab\', serif;">Airport Electrification Dashboard</h1>', unsafe_allow_html=True)
st.markdown("---")

# ---------- CSS for card-like containers ----------
st.markdown("""
<style>
.card {
    background-color: #001f3f;  /* dark blue */
    padding: 20px;
    border-radius: 15px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
    margin-bottom: 20px;
    color: white;
}
.card h2, .card h3, .card p {
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------- MAIN GRID ----------
col1, col2, col3 = st.columns([1,1.3,1])

# ---------- SCENARIO INPUTS ----------
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Scenario Inputs")
    energy_load = st.slider("Energy Load (MW)", 50, 500, 120)
    sector = st.radio("Energy Load Sector", ["Airport Terminal", "Manufacturing Plant", "Other Facilities"])
    year = st.radio("Target Year", ["2030","2040","2050","2060","2070"])
    fleet = st.radio("Fleet Transition Type", ["Hybrid Electric","H2-SAF Combustion"])
    hydrogen = st.radio("Hydrogen Supply Strategy", ["On-Site Electrolysis","Pipeline Import"])
    land = st.number_input("Land (Acres)", value=120)
    grid_cap = st.number_input("Grid Cap (MW)", value=15)
    st.button("Run Analysis")
    st.markdown('</div>', unsafe_allow_html=True)

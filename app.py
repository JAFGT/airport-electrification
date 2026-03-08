import streamlit as st

st.set_page_config(layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
/* Card styling */
.streamlit-card {
    background-color: #102f54;
    border-radius: 20px;
    padding: 20px;
    color: white;
    font-family: 'Roboto Slab', serif;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.4);
    margin-bottom: 20px;
}
.streamlit-card h2 {
    color: #ebaa01;
    margin-bottom: 15px;
}

/* Placeholder styling */
.placeholder {
    height: 120px;
    border-radius: 10px;
    background: #1f2937;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<h1 style="color:#ebaa01; font-family:\'Roboto Slab\', serif;">Airport Electrification Dashboard</h1>', unsafe_allow_html=True)
st.markdown("---")

# ---------------- MAIN GRID ----------------
col1, col2, col3 = st.columns([1, 1.3, 1])

# ---------------- SCENARIO INPUTS ----------------
with col1:
    with st.container():
        st.markdown('<div class="streamlit-card">', unsafe_allow_html=True)
        st.markdown("<h2>Scenario Inputs</h2>", unsafe_allow_html=True)
        
        energy_load = st.slider("Energy Load (MW)", 50, 500, 120)
        sector = st.radio("Energy Load Sector", ["Airport Terminal","Manufacturing Plant","Other Facilities"])
        year = st.radio("Target Year", ["2030","2040","2050","2060","2070"])
        fleet = st.radio("Fleet Transition Type", ["Hybrid Electric","H2-SAF Combustion"])
        hydrogen = st.radio("Hydrogen Supply Strategy", ["On-Site Electrolysis","Pipeline Import"])
        land = st.number_input("Land (Acres)", value=120)
        grid_cap = st.number_input("Grid Cap (MW)", value=15)
        st.button("Run Analysis")
        
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- CAPACITY ANALYTICS ----------------
with col2:
    with st.container():
        st.markdown('<div class="streamlit-card">', unsafe_allow_html=True)
        st.markdown("<h2>Capacity Analytics</h2>", unsafe_allow_html=True)
        
        st.markdown("Required: 140 MW")
        st.markdown("Generated: 185 MW")
        st.markdown("Net Surplus")
        st.markdown('<div class="placeholder"></div>', unsafe_allow_html=True)
        st.markdown("Safety Buffer")
        st.markdown('<div class="placeholder"></div>', unsafe_allow_html=True)
        st.markdown("Hydrogen Infrastructure")
        st.markdown('<div class="placeholder"></div>', unsafe_allow_html=True)
        st.markdown("Electric Transition")
        st.markdown('<div class="placeholder"></div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- SYSTEM PERFORMANCE ----------------
with col3:
    with st.container():
        st.markdown('<div class="streamlit-card">', unsafe_allow_html=True)
        st.markdown("<h2>System Performance</h2>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Total CAPEX","$2.8B")
        with c2:
            st.metric("Emissions","0 Tons")
        
        c3, c4 = st.columns(2)
        with c3:
            st.metric("PV Arrays","24 Units")
        with c4:
            st.metric("H2 Tanks","42 Units")
        
        st.markdown("### Tech Growth")
        st.metric("Battery Density","+140%")
        st.metric("PV Degradation","-0.5%")
        
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- LOWER DASHBOARD ----------------
st.markdown("---")
bottom1, bottom2 = st.columns([1,1])

# Decadal ROI
with bottom1:
    with st.container():
        st.markdown('<div class="streamlit-card">', unsafe_allow_html=True)
        st.markdown("<h2>Decadal ROI Projection</h2>", unsafe_allow_html=True)
        st.markdown('<div class="placeholder" style="height:150px;"></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Procurement & Layout
with bottom2:
    with st.container():
        st.markdown('<div class="streamlit-card">', unsafe_allow_html=True)
        st.markdown("<h2>Procurement & Final Layout</h2>", unsafe_allow_html=True)
        st.markdown('<div class="placeholder" style="height:150px;"></div>', unsafe_allow_html=True)
        st.markdown("""
**Procurement**
Electrolyzer Hub - x8  
PV Modules - x45k  
Liquid H2 Storage - x12  
BESS Mega-Pack - x20  
""")
        st.markdown('</div>', unsafe_allow_html=True)

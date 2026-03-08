import streamlit as st

st.set_page_config(layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {background-color: #05172a;}
[data-testid="stSidebar"] {background-color: #05172a;}
.block-container {padding-top: 1rem; color: #ebaa01;}
.card {
    background-color: #102f54; 
    padding: 20px; 
    border-radius: 12px; 
    border: 1px solid #1f2937; 
    color: white; 
    font-family: 'Roboto Slab', serif;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.3);
    margin-bottom: 15px;
}
.h1 {font-size: 50px !important; color: #ebaa01 !important; font-family: 'Roboto', sans-serif !important; font-weight: bold !important; margin-bottom: 20px !important;}
.h2 {font-size: 32px !important; color: #ffffff !important; font-weight: bold !important; margin-bottom: 15px !important;}
.h3 {font-size: 24px !important; color: #00ff00 !important; font-weight: 600 !important; margin-bottom: 10px !important;}
.placeholder {height: 120px; border-radius: 10px; background: #1f2937;}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<h1 class="h1">Airport Electrification Dashboard</h1>', unsafe_allow_html=True)
st.markdown("---")

# ---------------- MAIN GRID ----------------
col1, col2, col3 = st.columns([1, 1.3, 1])

# ---------------- SCENARIO INPUTS ----------------
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2 class="h2">Scenario Inputs</h2>', unsafe_allow_html=True)
    
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
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2 class="h2">Capacity Analytics</h2>', unsafe_allow_html=True)
    
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
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2 class="h2">System Performance</h2>', unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.metric("Total CAPEX","$2.8B")
    with c2:
        st.metric("Emissions","0 Tons")
    
    c3, c4 = st.columns(2)
    with c3:
        st.metric("PV Arrays","24 Units")
    with c4:
        st.metric("H₂ Tanks","42 Units")
    
    st.markdown("### Tech Growth")
    st.metric("Battery Density","+140%")
    st.metric("PV Degradation","-0.5%")
    
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- LOWER DASHBOARD ----------------
st.markdown("---")
bottom1, bottom2 = st.columns([1,1])

with bottom1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2 class="h2">Decadal ROI Projection</h2>', unsafe_allow_html=True)
    st.markdown('<div class="placeholder"></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with bottom2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2 class="h2">Procurement & Final Layout</h2>', unsafe_allow_html=True)
    st.markdown('<div class="placeholder" style="height:200px"></div>', unsafe_allow_html=True)
    st.markdown("""
    st.markdown('</div>', unsafe_allow_html=True)

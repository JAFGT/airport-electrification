import streamlit as st

st.set_page_config(layout="wide")

# ---------- DARK STYLE ----------
st.markdown("""
<style>

body {
    background-color: #0b1120;
}

.block-container {
    padding-top: 1rem;
}

.card {
    background-color:#111827;
    padding:20px;
    border-radius:12px;
    border:1px solid #1f2937;
}

.section-title {
    font-size:20px;
    font-weight:600;
    margin-bottom:10px;
}

.placeholder {
    height:120px;
    border-radius:10px;
    background:#1f2937;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.title("Net Zero Infrastructure Planner")

st.markdown("---")

# ---------- MAIN GRID ----------
col1, col2, col3 = st.columns([1,1.3,1])

# =========================================================
# SCENARIO INPUTS
# =========================================================

with col1:
    st.markdown("### Scenario Inputs")

    st.markdown("**Energy Load Sector**")
    st.radio("",["Airport Terminal","Manufacturing Plant","Other Facilities"])

    st.markdown("**Target Year**")
    st.radio("",["2030","2040","2050","2060","2070"])

    st.markdown("**Fleet Transition Type**")
    st.radio("",["Hybrid Electric","H2-SAF Combustion"])

    st.markdown("**Hydrogen Supply Strategy**")
    st.radio("",["On-Site Electrolysis","Pipeline Import"])

    st.number_input("Land (Acres)", value=120)
    st.number_input("Grid Cap (MW)", value=15)

    st.button("Run Analysis")

# =========================================================
# CAPACITY ANALYTICS
# =========================================================

with col2:

    st.markdown("### Capacity Analytics")

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

# =========================================================
# SYSTEM PERFORMANCE
# =========================================================

with col3:

    st.markdown("### System Performance")

    c1,c2 = st.columns(2)

    with c1:
        st.metric("Total CAPEX","$2.8B")

    with c2:
        st.metric("Emissions","0 Tons")

    c3,c4 = st.columns(2)

    with c3:
        st.metric("PV Arrays","24 Units")

    with c4:
        st.metric("H₂ Tanks","42 Units")

    st.markdown("### Tech Growth")

    st.metric("Battery Density","+140%")
    st.metric("PV Degradation","-0.5%")

# =========================================================
# LOWER DASHBOARD
# =========================================================

st.markdown("---")

bottom1, bottom2 = st.columns([1,1])

with bottom1:
    st.markdown("### Decadal ROI Projection")
    st.markdown('<div class="placeholder"></div>', unsafe_allow_html=True)

with bottom2:
    st.markdown("### Procurement & Final Layout")
    st.markdown('<div class="placeholder" style="height:200px"></div>', unsafe_allow_html=True)

    st.markdown("""
    **Procurement**

    Electrolyzer Hub — x8  
    PV Modules — x45k  
    Liquid H₂ Storage — x12  
    BESS Mega-Pack — x20  
    """)

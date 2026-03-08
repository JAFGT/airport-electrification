import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# ---------------------------------------------------
# GLOBAL CSS
# ---------------------------------------------------

st.markdown("""
<style>

/* Background */

[data-testid="stAppViewContainer"] {
background: linear-gradient(135deg,#0f1b2d,#081321);
color:white;
}

/* Remove header background */

[data-testid="stHeader"]{
background: rgba(0,0,0,0);
}

/* Cards */

.card {

background: linear-gradient(145deg,#16283f,#0f1f33);

border-radius:14px;

border:1px solid rgba(255,255,255,0.05);

padding:25px;

box-shadow:
0 10px 30px rgba(0,0,0,0.4),
inset 0 0 0 1px rgba(255,255,255,0.03);

}

/* Titles */

.section-title{

color:#e6c76c;

font-weight:700;

letter-spacing:1px;

margin-bottom:20px;

}

/* Metric Tiles */

.metric-box{

background:#0f2136;

border-radius:12px;

padding:20px;

text-align:center;

border:1px solid rgba(255,255,255,0.05);

}

.metric-title{

font-size:12px;

color:#7f9bc0;

}

.metric-value{

font-size:28px;

font-weight:700;

color:#6db2ff;

}

/* Pills */

.pill {

display:inline-block;

padding:8px 16px;

border-radius:20px;

border:1px solid #2f5f9e;

color:#8fb8ff;

margin:4px;

}

/* Progress bar */

.progress {

height:18px;

border-radius:10px;

background:#1b2c44;

overflow:hidden;

}

.progress-fill{

height:100%;

background:linear-gradient(90deg,#0dbb84,#36e0a2);

box-shadow:0 0 10px rgba(0,255,170,0.6);

}

/* Timeline */

.timeline {
display:flex;
justify-content:space-between;
align-items:center;
padding:20px 10px;
margin-bottom:30px;
}

.timeline-step{
text-align:center;
color:#7aa6d6;
font-weight:500;
}

.timeline-dot{
width:16px;
height:16px;
border-radius:50%;
border:2px solid #3a6ea5;
margin:auto;
}

.timeline-active{
background:#f2c94c;
box-shadow:0 0 10px #f2c94c;
border:none;
}

.timeline-line{
flex-grow:1;
height:2px;
background:#2a4b73;
margin:0 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("Airport Electrification Dashboard")

# ---------------------------------------------------
# TIMELINE
# ---------------------------------------------------

st.markdown("""
<div class="timeline">

<div class="timeline-step">
<div class="timeline-dot"></div>
2030<br>Initial
</div>

<div class="timeline-line"></div>

<div class="timeline-step">
<div class="timeline-dot"></div>
2040<br>Growth
</div>

<div class="timeline-line"></div>

<div class="timeline-step">
<div class="timeline-dot"></div>
2050<br>Net Zero
</div>

<div class="timeline-line"></div>

<div class="timeline-step">
<div class="timeline-dot"></div>
2060<br>Scale
</div>

<div class="timeline-line"></div>

<div class="timeline-step">
<div class="timeline-dot timeline-active"></div>
2070<br>Maturity
</div>

</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# MAIN GRID
# ---------------------------------------------------

col1, col2, col3 = st.columns([1,1,1])

# ---------------------------------------------------
# SCENARIO INPUTS
# ---------------------------------------------------

with col1:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown('<div class="section-title">SCENARIO INPUTS</div>', unsafe_allow_html=True)

    st.write("Energy Load Sectors")

    st.markdown("""
    <span class="pill">Airport Terminal</span>
    <span class="pill">GSE</span>
    <span class="pill">Manufacturing</span>
    <span class="pill">Other Facilities</span>
    """, unsafe_allow_html=True)

    st.write("")

    target = st.slider("Target Year",2030,2070,2070)

    st.write("Fleet Transition")

    st.selectbox("",["Hybrid Electric","Hydrogen Combustion"])

    st.write("Hydrogen Supply")

    st.selectbox("",["On-site Electrolysis","Pipeline Import"])

    land = st.number_input("Land (Acres)",value=120)

    grid = st.number_input("Grid Cap (MW)",value=15)

    st.button("Run Analysis")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# CAPACITY ANALYTICS
# ---------------------------------------------------

with col2:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown('<div class="section-title">CAPACITY ANALYTICS</div>', unsafe_allow_html=True)

    st.write("Required: 140 MW | Generated: 185 MW")

    st.markdown("""
    <div class="progress">
    <div class="progress-fill" style="width:85%"></div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.write("Net Surplus: +45 MW")

    st.write("Safety Buffer: 32%")

    st.write("")

    st.write("Hydrogen Infrastructure")

    st.markdown("""
    <div class="progress">
    <div class="progress-fill" style="width:100%"></div>
    </div>
    """, unsafe_allow_html=True)

    st.write("Electric Transition")

    st.markdown("""
    <div class="progress">
    <div class="progress-fill" style="width:100%"></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# SYSTEM PERFORMANCE
# ---------------------------------------------------

with col3:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown('<div class="section-title">SYSTEM PERFORMANCE</div>', unsafe_allow_html=True)

    c1,c2 = st.columns(2)

    with c1:
        st.markdown("""
        <div class="metric-box">
        <div class="metric-title">TOTAL CAPEX</div>
        <div class="metric-value">$2.8B</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="metric-box">
        <div class="metric-title">EMISSIONS</div>
        <div class="metric-value">0 Tons</div>
        </div>
        """, unsafe_allow_html=True)

    c3,c4 = st.columns(2)

    with c3:
        st.markdown("""
        <div class="metric-box">
        <div class="metric-title">PV ARRAYS</div>
        <div class="metric-value">24 Units</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="metric-box">
        <div class="metric-title">H2 TANKS</div>
        <div class="metric-value">42 Units</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# BOTTOM SECTION
# ---------------------------------------------------

col4, col5 = st.columns([1,2])

# ROI Chart

with col4:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown('<div class="section-title">DECADAL ROI PROJECTION</div>', unsafe_allow_html=True)

    years=[2030,2040,2050,2060,2070]
    roi=[7,4,3,6,8]

    fig, ax = plt.subplots()

    colors=["#ff4d4d","#ff6b6b","#3b82f6","#2563eb","#eab308"]

    ax.bar(years,roi,color=colors)

    ax.set_facecolor("#0f1f33")
    fig.patch.set_facecolor("#0f1f33")

    ax.tick_params(colors="white")

    st.pyplot(fig)

    st.markdown("</div>", unsafe_allow_html=True)

# Procurement

with col5:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown('<div class="section-title">PROCUREMENT & FINAL LAYOUT</div>', unsafe_allow_html=True)

    st.image("https://upload.wikimedia.org/wikipedia/commons/8/88/Atlanta_airport_satellite_image.jpg")

    st.write("Electrolyzer Hub — x8")

    st.write("PV Modules — x45k")

    st.write("Liquid H2 Storage — x12")

    st.write("BESS Mega Pack — x20")

    st.markdown("</div>", unsafe_allow_html=True)

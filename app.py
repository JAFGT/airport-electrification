import streamlit as st
from streamlit_extras.stateful_button import button

st.set_page_config(layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f0c29 0%, #0a203c 50%, #05172a 100%);
    color: #ffffff;
}
[data-testid="stHeader"] {background: rgba(0,0,0,0);}
.st-key-blc {
    background-color: #102f54; 
    border: 2px solid #b0a36f; 
    border-radius: 12px; 
    padding: 20px; 
    margin-bottom: 20px; 
    backdrop-filter: blur(5px);
}
.stButton>button {
    background-color: #0a203c;
    color: #b0a36f;
    border-radius: 8px;
    border: 2px solid #b0a36f;
    width: 100%;
    padding: 8px 0;
    font-weight: bold;
    margin-bottom: 5px;
}
.stButton>button:active {
    background-color: #b0a36f;
    color: #102f54;
}
</style>
""", unsafe_allow_html=True)

st.title("Airport Dashboard")

# ---------- Energy sectors ----------
sectors = ["Airport Terminal", "GSE", "Manufacturing Plant", "Other Facilities"]

# ---------- Initialize session state ----------
for gate in ["sec1", "sec2", "sec3"]:
    for sector in sectors:
        key = f"{gate}_{sector.replace(' ','_')}"
        if key not in st.session_state:
            st.session_state[key] = False

# ---------- Helper to create a button ----------
def create_button(gate, sector):
    key = f"{gate}_{sector.replace(' ','_')}"
    label = f"✅ {sector}" if st.session_state[key] else sector
    if st.button(label, key=f"{key}_btn"):
        st.session_state[key] = not st.session_state[key]

# ---------- Layout ----------
col1, col2, col3 = st.columns([1,1,1], gap="medium")

# Gate A
with col1:
    with st.container():
        st.write("### Gate A")
        st.slider("Capacity A", 0, 100, 50)
        st.write("#### Energy Sectors")
        for sector in sectors:
            create_button("sec1", sector)

# Gate B
with col2:
    with st.container():
        st.write("### Gate B")
        st.slider("Capacity B", 0, 100, 30)
        st.write("#### Energy Sectors")
        for sector in sectors:
            create_button("sec2", sector)

# Gate C
with col3:
    with st.container():
        st.write("### Gate C")
        st.slider("Capacity C", 0, 100, 75)
        st.write("#### Energy Sectors")
        for sector in sectors:
            create_button("sec3", sector)

columns = st.columns(10)

icons = ["🍎", "🍌", "🍇", "🍓", "🍒", "🍑", "🥭", "🍍", "🥥", "🥝"]

selected_icons = []

for index, column in enumerate(columns):
    with column:
        if button(icons[index], key=f"button_{index}"):
            selected_icons.append(icons[index])

st.write("Selected icons:", selected_icons)


# ---------- Display checked sectors ----------
st.markdown("---")
st.write("**Checked Sectors:**")
for gate in ["sec1","sec2","sec3"]:
    checked = [s for s in sectors if st.session_state[f"{gate}_{s.replace(' ','_')}"]]
    st.write(f"{gate}: {checked}")




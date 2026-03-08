import streamlit as st

# --- CSS STYLING ---
st.markdown("""
<style>
/* 1. Page Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    color: #ffffff;
}

/* 2. Transparent Header */
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

/* 3. Gate Containers (Glassmorphism) */
.st-key-blc1, .st-key-blc2, .st-key-blc3, .st-key-blc4 {
    background-color: rgba(100, 100, 200, 0.15);
    border: 2px solid #3498db; 
    border-radius: 12px; 
    padding: 20px; 
    margin-bottom: 20px;
    backdrop-filter: blur(10px);
}

/* 4. Custom Slider Colors */
/* The track (the line) */
.stSlider [data-baseweb="slider"] > div > div > div > div {
    background-color: #00f2fe !important;
}

/* The thumb (the circle) */
.stSlider [data-baseweb="slider"] > div > div > div > div > div {
    background-color: #00f2fe !important;
    border: 2px solid #ffffff;
    box-shadow: 0px 0px 10px rgba(0, 242, 254, 0.8);
}

/* The thumb hover effect */
.stSlider [data-baseweb="slider"] > div > div > div > div > div:hover {
    transform: scale(1.2);
    transition: 0.2s ease-in-out;
}

/* Slider labels and numbers */
.stSlider label, .stSlider [data-testid="stTickBarMin"], .stSlider [data-testid="stTickBarMax"] {
    color: #ffffff !important;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# --- DASHBOARD CONTENT ---

import streamlit as st

st.set_page_config(layout="wide")

st.title("Airport Dashboard")

sectors = ["Airport Terminal", "GSE", "Manufacturing Plant", "Other Facilities"]

# ---------- Columns ----------
col1, col2, col3 = st.columns([1,1,1], gap="medium")

# Container 1
with col1:
    with st.container(key="blc1"):
        st.write("### Gate A")
        st.slider("Capacity A", 0, 100, 50)

        for sector in sectors:
            # Use a separate session_state key for checked state
            state_key = f"blc1_checked_{sector}"
            if state_key not in st.session_state:
                st.session_state[state_key] = False

            # Create a button with a unique widget key
            widget_key = f"blc1_btn_{sector}"
            label = f"✅ {sector}" if st.session_state[state_key] else sector

            if st.button(label, key=widget_key):
                # Toggle state safely
                st.session_state[state_key] = not st.session_state[state_key]

# Container 2
with col2:
    with st.container(key="blc2"):
        st.write("### Gate B")
        st.slider("Capacity B", 0, 100, 30)

# Container 3
with col3:
    with st.container(key="blc3"):
        st.write("### Gate C")
        st.slider("Capacity C", 0, 100, 75)

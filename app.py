import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Airport Electrification Dashboard",
    layout="wide"
)

# ---------- HEADER ----------
st.markdown(
    '<h1 style="color:#ebaa01; font-family:\'Roboto Slab\', serif;">Airport Electrification Dashboard</h1>',
    unsafe_allow_html=True
)
st.markdown("---")

# ---------- MAIN GRID WITH CONTAINERS ----------
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.container()  # optional container for organization
    st.markdown(
        """
        <div style="
            padding: 20px;
            background-color: #001f3f;
            border-radius: 12px;
            color: white;
        ">
            <h4>Metric 1</h4>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.slider("Slider 1", 0, 100, 50)
    st.metric("Metric 1 Value", "123", "+5%")

with col2:
    st.container()
    st.markdown(
        """
        <div style="
            padding: 20px;
            background-color: #001f3f;
            border-radius: 12px;
            color: white;
        ">
            <h4>Metric 2</h4>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.slider("Slider 2", 0, 100, 30)
    st.metric("Metric 2 Value", "456", "-2%")

with col3:
    st.container()
    st.markdown(
        """
        <div style="
            padding: 20px;
            background-color: #001f3f;
            border-radius: 12px;
            color: white;
        ">
            <h4>Metric 3</h4>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.slider("Slider 3", 0, 100, 70)
    st.metric("Metric 3 Value", "789", "+12%")

# ---------- OTHER CONTENT ----------
st.markdown("---")
st.write("Additional dashboard content can go here.")

# ---------- FOOTER ----------
st.markdown(
    """
    <div style="
        height: 70px;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: #0054a3;
        color: white;
        border-radius: 12px;
        margin-top: 50px;
    ">
        For more information, visit <a href='https://www.snowflake.com' style='color:white; text-decoration:underline;'>www.snowflake.com</a>
    </div>
    """,
    unsafe_allow_html=True
)

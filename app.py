import streamlit as st
import streamlit_extras as ste  # import all extras

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
    with ste.stylable_container.stylable_container(
        key="col1_container",
        css_styles="""
        {
            .element-container {
                padding: 20px;
                background-color: #001f3f;
                border-radius: 12px;
                color: white;
            }
        }
        """
    ):
        st.metric("Metric 1", "123", "+5%")
        st.slider("Slider 1", 0, 100, 50)

with col2:
    with ste.stylable_container.stylable_container(
        key="col2_container",
        css_styles="""
        {
            .element-container {
                padding: 20px;
                background-color: #001f3f;
                border-radius: 12px;
                color: white;
            }
        }
        """
    ):
        st.metric("Metric 2", "456", "-2%")
        st.slider("Slider 2", 0, 100, 30)

with col3:
    with ste.stylable_container.stylable_container(
        key="col3_container",
        css_styles="""
        {
            .element-container {
                padding: 20px;
                background-color: #001f3f;
                border-radius: 12px;
                color: white;
            }
        }
        """
    ):
        st.metric("Metric 3", "789", "+12%")
        st.slider("Slider 3", 0, 100, 70)

# ---------- OTHER CONTENT ----------
st.markdown("---")
st.write("Additional dashboard content can go here.")

# ---------- FOOTER ----------
with ste.stylable_container.stylable_container(
    key="footer_container",
    css_styles="""
    {
        padding-top: 50px;
        box-sizing: border-box;

        .element-container {
            height: 70px;
            display: flex;
            justify-content: center;
            color: #ffffff;
            text-align: center;
            align-items: center;
            background-color: #0054a3;
            border-radius: 12px;

            a {
                color: #ffffff;
                text-decoration: underline;
            }
        }
    }
    """,
):
    st.write("For more information, visit [www.snowflake.com](https://www.snowflake.com)")

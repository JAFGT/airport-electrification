with stylable_container(
    key="footer_container",
    css_styles="""
    {
        padding-top: 100px;
        box-sizing: border-box;

        .element-container {
            height: 70px;
            display: flex;
            color: #ffffff;
            text-align: center;
            align-items: center;
            background-color: #0054a3;

            a {
                color: #ffffff;
            }
        }
    }
    """,
):
    st.write("For more information, visit www.snowflake.com")

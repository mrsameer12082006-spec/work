import streamlit as st

def show_insights():

    st.title("Insights")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("High Demand", "—")
    col2.metric("Medium Demand", "—")
    col3.metric("Low Demand", "—")
    col4.metric("Critical", "—")

    st.divider()

    st.markdown("<div class='card' style='height:400px;'>Detailed Recommendations Placeholder</div>", unsafe_allow_html=True)

    st.divider()

    st.markdown("<div class='card' style='height:200px;'>General Best Practices Placeholder</div>", unsafe_allow_html=True)

import streamlit as st

def show_trends():

    st.title("Trends")

    col1, col2, col3 = st.columns(3)
    col1.metric("Time Period", "—")
    col2.metric("Revenue Trend", "—")
    col3.metric("Daily Average", "—")

    st.divider()

    st.markdown("<div class='card' style='height:300px;'>Revenue Trend Graph Placeholder</div>", unsafe_allow_html=True)

    st.markdown("<div class='card' style='height:300px;'>Category Trend Graph Placeholder</div>", unsafe_allow_html=True)

    st.markdown("<div class='card' style='height:300px;'>Top Products Trend Placeholder</div>", unsafe_allow_html=True)

import streamlit as st

def show_products():

    st.title("Products")

    col1, col2, col3 = st.columns(3)
    col1.metric("High Demand", "—")
    col2.metric("Medium Demand", "—")
    col3.metric("Low Demand", "—")

    st.divider()

    st.markdown("<div class='card' style='height:400px;'>Product Table Placeholder</div>", unsafe_allow_html=True)

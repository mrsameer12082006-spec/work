import streamlit as st

def show_dashboard():

    st.title("Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Revenue", "—")
    col2.metric("Units Sold", "—")
    col3.metric("Products", "—")
    col4.metric("Avg Transaction", "—")

    st.divider()

    colA, colB = st.columns(2)

    with colA:
        st.markdown("<div class='card' style='height:300px;'>Revenue Chart Placeholder</div>", unsafe_allow_html=True)

    with colB:
        st.markdown("<div class='card' style='height:300px;'>Category Distribution Placeholder</div>", unsafe_allow_html=True)

    st.divider()

    st.markdown("<div class='card' style='height:300px;'>Top Products Placeholder</div>", unsafe_allow_html=True)

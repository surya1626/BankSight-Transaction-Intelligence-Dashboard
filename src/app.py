import streamlit as st

st.set_page_config(
    page_title="BankSight",
    page_icon="🏦",
    layout="wide"
)

st.sidebar.title("BankSight Navigation 🏦")

if st.sidebar.button("🔄 Hard Refresh"):
    st.cache_data.clear()
    st.cache_resource.clear()
    st.rerun()

pages = {
    "intro": "🏠 Introduction",
    "tables": "📚 View Tables",
    "filter": "🔍 Filter Data",
    "crud": "✏️ CRUD Operation",
    "cr-dr": "💰 Credit / Debit Stimulation",
    "analysis": "🧠 Analytical Insights",
    "creator": "👨🏻‍💻About Creator"

}

page = st.sidebar.radio(
    "Go to",
    options=list(pages.keys()),
    format_func=lambda x: pages[x]
)

if page == "intro":
    import Paging.Intro as index
    index.app()

elif page == "tables":
    import Paging.viewTables as page1
    page1.app()

elif page == "filter":
    import Paging.filterData as page2
    page2.app()

elif page == "crud":
    import Paging.crud as page3
    page3.app()

elif page == "cr-dr":
    import Paging.creditDebit as page4
    page4.app()

elif page == "analysis":
    import Paging.analysis as page5
    page5.app()

elif page == "creator":
    import Paging.creator as page6
    page6.app()

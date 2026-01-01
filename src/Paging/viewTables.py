import streamlit as st
from db import get_connection
from utils.dbFunctions import get_tables

def app():
    st.header("🛢 View Database Tables")
    tables = get_tables()
    option = st.selectbox(
        "Select a Table",
        tables,
        index=None,
        placeholder="Select a Table to view:"
    )

    if not option:
        st.info("Please select a table")
        return

    st.write("You selected:", option)

    conn = get_connection()
   
    query = f"SELECT * FROM {option}"

    with st.spinner("Fetching data..."):
        with conn.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()

    if rows:
        st.dataframe(rows, width='stretch')
    else:
        st.warning("No data found")

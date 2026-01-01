import streamlit as st
from db import get_connection
import pandas as pd
from utils.analyticalQueries import queries

def app():
    st.header("🧠 Analytical Insights")
    st.write(
        "Explore key SQL-driven insights from the BankSight database. "
        "Select a question to run the corresponding query."
    )

    selected_question = st.selectbox(
        "Select an analytical question",
        list(queries.keys()),
        index=None,
        placeholder="Choose a question"
    )

    if not selected_question:
        st.info("Please select a question")
        return

    query = queries[selected_question]

    st.subheader("📄 SQL Query")
    st.code(query, language="sql")
    conn = get_connection()
    with st.spinner("Running query..."):
        with conn.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
    if rows:
        df = pd.DataFrame(rows)
        st.dataframe(df, width="stretch")
    else:
        st.warning("No data returned")

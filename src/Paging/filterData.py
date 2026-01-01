import streamlit as st
from db import get_connection
from utils.dbFunctions import get_tables,get_columns,get_column_values
from datetime import datetime, date


def app():
    st.header("🔍 Filter Data")

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

    st.markdown("Select Columns and Values to filter. ")

    conn = get_connection()
    columns  = get_columns(option)
    filters = {}
    where_clause = ""

    for column in columns:
        columnValues = get_column_values(option, column)
        selectedColumnValue = st.selectbox(
            f"Select a {column}",
            columnValues,
            index= None,
            placeholder="Select a Value to filter:"
      )
        if selectedColumnValue is not None:
             filters[column] = f"'{selectedColumnValue}'" if isinstance(selectedColumnValue, (str,datetime,date))  else selectedColumnValue
    
    if filters:
        conditions = []
        for col, val in filters.items():
            conditions.append(f"{col} = {val}")
        where_clause = " WHERE " + " AND ".join(conditions)

    query = f"SELECT * FROM {option}{where_clause}"

    st.code(query, language="sql")

    with st.spinner("Fetching data..."):
        with conn.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()

    if rows:
        st.dataframe(rows, width='stretch')
    else:
        st.warning("No data found")

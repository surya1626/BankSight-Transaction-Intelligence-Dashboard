import streamlit as st
from db import get_connection
from utils.dbFunctions import get_tables,get_columns,get_column_values
from datetime import datetime, date

def app():
    st.header("✏️ CRUD Operation")
    tables = get_tables()
    option = st.selectbox(
        "Select a Table",
        tables,
        index=None,
        placeholder="Select a Table:"
    )

    if not option:
        st.info("Please select a table")
        return

    action = st.radio(
        "Select Action",
        ["View", "Add", "Update","Delete"],
        index=None,
    )
    if action is not None:
        if action == "View":
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
        elif action == "Add":
            columns  = get_columns(option,True)
            st.subheader(f"➕ Add New Record in {option}")
            insertedData ={}
            for col in columns:
                if col["type"] == "int"  or col["type"] == "decimal(12,2)"  :
                   ColumnValue = st.number_input(
                        f"Enter {col["name"]}",
                        value= None,
                        step=1,
                        min_value=0,
                        placeholder=f"Enter {col["name"]}:"
                    )
                elif col["type"] == "timestamp":
                   ColumnValue = st.datetime_input(
                        f"Enter {col["name"]}",
                        value=None,
                    )
                else:
                   ColumnValue = st.text_input(
                        f"Enter {col["name"]}",
                        value=None,
                        placeholder=f"Enter {col["name"]}:"
                    )
                if ColumnValue is not None:
                    insertedData[col["name"]] = ColumnValue

            if st.button("Insert"):
                if not insertedData:
                    st.warning("Please enter at least one value")
                    return
                
                col_names = ", ".join(insertedData.keys())
                col_values = ", ".join(
                    [f"'{v}'" if isinstance(v,(str,datetime,date)) else str(v) for v in insertedData.values()]
                )
                query = f"""
                    INSERT INTO {option} ({col_names})
                    VALUES ({col_values})
                """
                conn = get_connection()
                try:
                    with conn.cursor() as cursor:
                        cursor.execute(query)
                    conn.commit()
                    st.success("✅ Record inserted successfully")
                except Exception as e:
                    st.error(f"❌ Unexpected error: {e}")
                         
        elif action == "Update":
            columns  = get_columns(option,True)
            st.subheader(f"✏️ Update Record in {option}")
            primary_key = None
            primary_key_column = None
            otherColumns = [] 
            for col in columns:
                if col['key'] == 'PRI':
                    primary_key_column = col['name']
                    primaryKeyValues = get_column_values(option, col['name'])
                    selectedPk_value = st.selectbox(
                        f"Select a {col['name']} to Update",
                        primaryKeyValues,
                        index=None,
                        placeholder="Select a value:"
                    )
                else:
                    otherColumns.append(col)
       
            columnToUpdate = st.selectbox(
                "Select a Column to Update",
                otherColumns,
                format_func=lambda col: col['name'],
                index=None,
                placeholder="Select a Value:"
            )
            if columnToUpdate:
                if columnToUpdate["type"] == "int" or columnToUpdate["type"] == "decimal(12,2)"  :
                   ColumnValue = st.number_input(
                        f"Enter {columnToUpdate["name"]}",
                        value= None,
                        step=1,
                        min_value=0,
                        placeholder=f"Enter {columnToUpdate["name"]}:"
                    )
                elif columnToUpdate["type"] == "timestamp":
                   ColumnValue = st.datetime_input(
                        f"Enter {columnToUpdate["name"]}",
                        value=None,
                    )
                else:
                   ColumnValue = st.text_input(
                        f"Enter {columnToUpdate["name"]}",
                        value=None,
                        placeholder=f"Enter {columnToUpdate["name"]}:"
                    )


            if st.button("Update Record"):
                if ColumnValue is None:
                    st.warning("Please enter value")
                    return
                
                if isinstance(ColumnValue,(str,datetime,date)):
                    ColumnValue = f"'{ColumnValue}'"

                query = f"""
                    UPDATE  {option} SET {columnToUpdate['name']} = {ColumnValue} 
                    WHERE ( {primary_key_column}= "{selectedPk_value}")
                """
                conn = get_connection()
                try:
                    with conn.cursor() as cursor:
                        cursor.execute(query)
                    conn.commit()
                    st.success("✅ Record Updated successfully")
                except Exception as e:
                    st.error(f"❌ Unexpected error: {e}")


        elif action == "Delete":
            st.subheader("🗑️ Delete  Record")
            columns  = get_columns(option,True)
            for col in columns:
                if col['key'] == 'PRI':
                    primary_key_column = col['name']
                    primaryKeyValues = get_column_values(option, col['name'])
                    selectedPk_value = st.selectbox(
                        f"Select a {col['name']} to Update",
                        primaryKeyValues,
                        index=None,
                        placeholder="Select a Value:"
                    )
            if st.button("Delete Record"):
                if selectedPk_value is None:
                    st.warning("Please enter value")
                    return
                query = f"""
                    DELETE FROM {option}
                    WHERE ( {primary_key_column}= "{selectedPk_value}")
                """
                st.code(query,"sql")
                conn = get_connection()
                try:
                    with conn.cursor() as cursor:
                        cursor.execute(query)
                    conn.commit()
                    st.success("✅ Record Deleted successfully")
                    st.warning(
                        "⚠️ Cannot delete this record because it is linked to other data.\n\n"
                        "Please delete dependent records first (e.g., accounts, transactions)."
                    )

                except Exception as e:
                    st.error(f"❌ Unexpected error: {e}")



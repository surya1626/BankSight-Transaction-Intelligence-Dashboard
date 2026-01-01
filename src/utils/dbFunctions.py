from db import get_connection
import streamlit as st

def get_tables():

    conn = get_connection()

    with conn.cursor() as cursor:
        cursor.execute("SHOW TABLES")
        result = cursor.fetchall()
    tables = [list(row.values())[0] for row in result]
    return tables

def get_columns(table_name,withType=False):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute(f"DESCRIBE {table_name}")
        result = cursor.fetchall()
    if withType:
        return [
            {
                "name": row["Field"],
                "type": row["Type"],
                "key": row["Key"]
            }
            for row in result
        ]
    return [row["Field"] for row in result]    


def get_columns_with_field(table_name):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute(f"DESCRIBE {table_name}")
        result = cursor.fetchall()
    print(result)
    return [row["Field"] for row in result]  

def get_column_values(table, column):
    conn = get_connection()

    query = f"""
        SELECT DISTINCT {column}
        FROM {table}
        WHERE {column} IS NOT NULL
    """

    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return [row[column] for row in result] 


def getCustomerBalance(customerId):
    conn = get_connection()

    query = f"""
        SELECT account_balance 
        FROM accounts
        WHERE customer_id = "{customerId}"
    """

    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()
        if result is None: 
            st.error("Please Enter a Valid Customer ID")
            return
    return result['account_balance'] if result is not None else None

def updateBalance(currentBalance,amount,customerId,action):
    conn = get_connection()
    if action == 'Deposit':
        updatedBalance = currentBalance + amount
    elif action == 'Withdraw':
        updatedBalance = currentBalance - amount
    else:
        return None
    query = f"""
        UPDATE accounts 
        SET `account_balance` = {updatedBalance} , `last_updated` = NOW()
        WHERE customer_id = "{customerId}"
    """
    with conn.cursor() as cursor:
        cursor.execute(query)
    conn.commit()

    return updatedBalance
  
import streamlit as st

def app():
    # Main page content
    st.title("BankSight: Transaction Intelligence Dashboard 🏦")

    st.header("Project Overview")

    st.markdown("Banksight is a financial analytics system built using python, streamlit and mysql. It allows users to explore customers,account,transaction,loan and support data, perform crud operation, stimulate deposit and withdrawl and view analytical insights.")

    st.header("Objectives:")

    st.markdown("""
        - Understand customer and transaction  behaviour
        - Detect Anamolies and potential fraud
        - Enable CRUD operation on all Datasets
        - Stimulate Banking Transaction (credit/debit)
        """)

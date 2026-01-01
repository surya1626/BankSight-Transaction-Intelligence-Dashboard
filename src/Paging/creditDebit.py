import streamlit as st
from db import get_connection
from utils.dbFunctions import getCustomerBalance,updateBalance

def app():
    st.header("💰 Deposit / Withdraw Money")

    customer_id = st.text_input(
        "Enter AccountID", 
        value=None,
        placeholder = "Enter AccountID",
        )

    if not customer_id:
        st.info("Please Enter a Customer ID")
        return
    
    amount = st.number_input(
        "Enter Amount (₹)", 
        value=None, 
        placeholder="Enter Amount (₹)",    
        min_value = 0,
        step=1,
    )

    action = st.radio(
        "Select Action",
        ["Check Balance", "Deposit", "Withdraw"],
        index=None,
    )
    
    actionTrigger = st.button("Submit", type="primary")
    if actionTrigger:
        if action is None: 
            st.error("Please Enter any Action")
            return
        balance = getCustomerBalance(customer_id)
        if (action == 'Check Balance'):
            if balance is not None:
                st.info(f"Your Account Balance:{balance}")
        if (action == 'Deposit'):
            if balance is not None:
                new_balance = updateBalance(balance,amount,customer_id,action)
                st.info(f"The Updated Balance: {new_balance}")
        if (action == 'Withdraw'):
            if balance < amount:
                st.info(f"""Transaction Declined due to Insufficient Fund.
                        Available Balance:{balance}
                        """)
                
            if balance is not None and balance >= amount:
                new_balance = updateBalance(balance,amount,customer_id,action)
                st.info(f"The Updated Balance: {new_balance}") 



queries = {
    "Q1: How many customers exist per city, and what is their average account balance?": """
        SELECT 
            c.city, 
            COUNT(c.customer_id) AS `Customer Count Per City`,
            AVG(a.account_balance) AS avg_account_balance
        FROM banksight.customers c
        JOIN banksight.accounts a
            ON c.customer_id = a.customer_id
        GROUP BY c.city
        ORDER BY `Customer Count Per City` DESC;
    """,

    "Q2: Which account type (Savings, Current, Loan, etc.) holds the highest total balance?": """
        SELECT
            c.account_type,
            SUM(a.account_balance) AS total_balance
        FROM banksight.customers c
        JOIN banksight.accounts a
            ON c.customer_id = a.customer_id
        GROUP BY c.account_type
        ORDER BY total_balance DESC
        LIMIT 1;
    """,

    "Q3: Who are the top 10 customers by total account balance across all account types?": """
        SELECT
            c.customer_id,
            c.name,
            SUM(a.account_balance) AS total_balance
        FROM banksight.customers c
        JOIN banksight.accounts a
            ON c.customer_id = a.customer_id
        GROUP BY c.customer_id
        ORDER BY total_balance DESC
        LIMIT 10;
    """,

    "Q4:  Which customers opened accounts in 2023 with a balance above ₹1,00,000?": """
        SELECT 
            c.customer_id,
            c.name,
            c.join_date,
            a.account_balance
        FROM banksight.customers c
        JOIN banksight.accounts a 
            ON c.customer_id = a.customer_id
        WHERE c.join_date >= '2023-01-01'
            AND c.join_date < '2024-01-01'
            AND a.account_balance > 100000;
    """,

    "Q5: What is the total transaction volume (sum of amounts) by transaction type?": """
        SELECT txn_type, SUM(amount) AS `Total Transaction Amount`
        FROM transaction
        GROUP BY txn_type
        ORDER BY `Total Transaction Amount` DESC;
    """,

    "Q6: How many failed transactions occurred for each transaction type?": """
        SELECT txn_type, COUNT(*) AS `Failed Transaction`
        FROM transaction
        WHERE status = 'failed'
        GROUP BY txn_type
        ORDER BY `Failed Transaction` DESC;
    """,

    "Q7: What is the total number of transactions per transaction type?": """
        SELECT txn_type, COUNT(*) AS `Transaction`
        FROM transaction
        GROUP BY txn_type
        ORDER BY `Transaction` DESC;
    """,

    "Q8: Which accounts have 5 or more high-value transactions above ₹20,000?": """
        SELECT customer_id, COUNT(*) AS transaction_count
        FROM transaction
        WHERE amount >= 20000
        GROUP BY customer_id
        HAVING COUNT(*) >= 5;
    """,

    "Q9: What is the average loan amount and interest rate by loan type (Personal, Auto, Home, etc.)?": """
        SELECT 
            Loan_Type,
            AVG(Loan_Amount) AS `Average Loan Amount`,
            AVG(Interest_Rate) AS `Average Interest Rate`
        FROM banksight.loans
        GROUP BY Loan_Type;
    """,

    "Q10: Which customers currently hold more than one active or approved loan?": """
        SELECT 
            Customer_ID,
            COUNT(*) AS active_approved_loan_count
        FROM banksight.loans
        WHERE Loan_Status IN ('Active', 'Approved')
        GROUP BY Customer_ID
        HAVING COUNT(*) > 1;
    """,

    "Q11: Who are the top 5 customers with the highest outstanding (non-closed) loan amounts?": """
        SELECT 
            customer_id,
            COUNT(*) AS total_loans,
            SUM(loan_amount) AS total_outstanding_amount
        FROM banksight.loans
        WHERE Loan_Status <> 'Closed'
        GROUP BY customer_id
        ORDER BY total_outstanding_amount DESC
        LIMIT 5;
    """,

    "Q12: What is the average loan amount per branch?": """
        SELECT 
            Branch,
            AVG(Loan_Amount) AS `Average Loan Amount By Branch`
        FROM banksight.loans
        GROUP BY Branch
        ORDER BY `Average Loan Amount By Branch` DESC;
    """,

    "Q13: How many customers exist in each age group (e.g., 18–25, 26–35, etc.)?": """
        SELECT 
            CASE
                WHEN age BETWEEN 18 AND 25 THEN '18–25'
                WHEN age BETWEEN 26 AND 35 THEN '26–35'
                WHEN age BETWEEN 36 AND 45 THEN '36–45'
                WHEN age BETWEEN 46 AND 55 THEN '46–55'
                WHEN age BETWEEN 56 AND 65 THEN '56–65'
                ELSE '66+'
            END AS age_group,
            COUNT(*) AS `Count of Each Age`
        FROM banksight.customers
        GROUP BY age_group
        ORDER BY age_group;
    """,

    "Q14: Which issue categories have the longest average resolution time?": """
        SELECT 
            Issue_Category,
            AVG(DATEDIFF(Date_Closed, Date_Opened)) AS `Average Resolution Days`
        FROM banksight.support_tickets
        WHERE Date_Closed IS NOT NULL
            AND status = 'Closed'
        GROUP BY Issue_Category
        ORDER BY `Average Resolution Days` DESC;
    """,

    "Q15: Which support agents have resolved the most critical tickets with high customer ratings (≥4)?": """
        SELECT 
            Support_Agent,
            COUNT(*) AS `Critical Ticket Resolved`
        FROM banksight.support_tickets
        WHERE Priority = 'Critical'
            AND status = 'Resolved'
            AND Customer_Rating >= 4
        GROUP BY Support_Agent
        ORDER BY `Critical Ticket Resolved` DESC;
    """
}

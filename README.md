# 🏦 BankSight – Transaction Intelligence Dashboard

BankSight is a **data-driven banking analytics and management dashboard** built using **Streamlit**, **Python**, and **MySQL**.
It provides CRUD operations, analytical insights, and safe data handling for banking datasets such as customers, accounts, loans, transactions, and support tickets.

---

## 🚀 Features

### 🔹 Core Modules

* 📊 **Analytical Insights** – Predefined SQL queries for business intelligence
* 🗂️ **Dynamic Table Viewer** – View data from any table
* ✏️ **CRUD Operations** – Add, Update, Delete records dynamically
* 🔍 **Dynamic Filters** – Filter data using column-based selection
* 🔍 **Credit / Debit Stimulation** – Credit and Debit of Money.

---

## 🛠️ Tech Stack

| Layer         | Technology                     |
| ------------- | ------------------------------ |
| Frontend      | Streamlit                      |
| Backend       | Python                         |
| Database      | MySQL                          |
| Connector     | PyMySQL                        |
| Data Handling | Pandas                         |

---

## 📂 Project Structure

```
BankSight-Transaction-Intelligence-Dashboard/
├── Data/
│   ├── Accounts.csv
│   ├── branches.csv
│   ├── credit-cards.json
│   ├── customers.csv
│   ├── loans.csv
│   ├── support_tickets.csv
│   ├── transaction.csv
│
├── src/
│   ├── utils/
│       ├── dbFunctions.py
│       ├── analyticalQuries.py
│
│   ├── .streamlit/
│       ├── secrets.toml
│
│   ├── Paging/
│       ├── analysis.py
│       ├── creator.py
│       ├── creditDebit.py
│       ├── crud.py
│       ├── filterData.py
│       ├── Intro.py
│       ├── viewTables.py

│   ├── app.py
│   ├── db.py

│
└── index.ipynb ------ For 15 Question 
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-repo/banksight.git
cd BankSight-Transaction-Intelligence-Dashboard/
```

### 2️⃣ Install dependencies

Install Python,mysql,pymysql,pandas,streamlit

### 3️⃣ Configure Database

Update **`db.py`** with your MySQL credentials:

```python
host="localhost"
user="root"
password="your_password"
database="banksight"
```

### 4️⃣ Run the application

```bash
streamlit run app.py
```

---





## 👨🏻‍💻 About the Creator

**👤 Name:** Suryakumar Veeraraghavan
**💼 Role:** Full Stack Developer
**🛠️ Expertise:** Drupal, PHP, Python, MySQL

📧 **Email:** [suryalv16@gmail.com](mailto:suryalv16@gmail.com)
🔗 **LinkedIn:** [Suryakumar Veeraraghavan](https://www.linkedin.com/in/suryakumar-veeraraghavan/)


---


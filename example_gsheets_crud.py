import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.title("Read Google Sheet as DataFrame")

# Replace (KEYWORD) below with the word corresponding to the database you want to access, from the following:
# appointments (Note, this doesn't work yet because aames hasnt sent his gsheets file) 
# survey
# user

conn = st.connection("(KEYWORD)", type=GSheetsConnection)
conn.query()

updated_orders = pd.DataFrame({
    'OrderID': [101, 102, 103, 104, 105],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'ProductList': ['ProductA, ProductB', 'ProductC', 'ProductA, ProductC', 'ProductB, ProductD', 'ProductD'],
    'TotalPrice': [200, 150, 250, 300, 100],
    'OrderDate': ['2023-08-18', '2023-08-19', '2023-08-19', '2023-08-20', '2023-08-20']
})

# QUERY THE DATABASE
if st.button("Calculate Total Orders Sum"):
    sql = 'SELECT SUM("TotalPrice") as "TotalOrdersPrice" FROM Orders;'
    total_orders = conn.query(sql=sql)  # default ttl=3600 seconds / 60 min
    st.dataframe(total_orders)

# CLEAR ALL DATA
if st.button("Clear Worksheet"):
    conn.clear(worksheet="Sheet1")
    st.success("Worksheet Cleared")

# UPDATE THE ENTIRE WORKSHEET (this means all existing rows are DELETED and the rows you pass in are written to the worksheet.)
if st.button("Update Worksheet"):
    conn.update(worksheet="Sheet1", data=updated_orders)
    st.success("Worksheet Updated")

# READ THE ENTIRE WORKSHEET
df = conn.read(worksheet = "Sheet1", ttl = 0)

st.dataframe(df)
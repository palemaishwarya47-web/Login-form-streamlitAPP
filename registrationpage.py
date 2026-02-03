import streamlit as st
from mysql import connector

conn = connector.connect(
    host="localhost",
    user="root",
    password="#admin12",
    database="streamlit"
)

print("Connection successful")


with st.form("registration_form"):
    st.header("User Registration")
    name = st.text_input("name")
    age = st.number_input("age", min_value=1, max_value=120)
    email = st.text_input("Email")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit_button = st.form_submit_button("Register")

    if submit_button:
        cursor = conn.cursor()
        insert_query = "INSERT INTO user1(name,age,email,username,password) VALUES (%s, %s, %s, %s, %s)"
        values = (name, age, email, username, password)
        cursor.execute(insert_query, values)
        conn.commit()
        st.success("Registration successful!")
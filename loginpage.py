import streamlit as st
st.header("LOGIN PAGE")
st.text_input("USERNAME")
st.text_input("PASSWORD", type="password")
if st.button("LOGIN"):
    st.success("LOGIN SUCCESSFUL")
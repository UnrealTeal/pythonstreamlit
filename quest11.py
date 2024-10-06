import streamlit as st

ATM = 250
attempts = 3
username = st.text_input("Insert Username")
password = st.text_input("type password")


if password == "alex" and username == "alex":
    st.write("“Welcome Alex,” What would you like to do today?")
else:
    st.write("Incorrect password. You have",attempts," attempts left.")
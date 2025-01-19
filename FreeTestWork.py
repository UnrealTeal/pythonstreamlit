import streamlit as st
import pandas as pd
st.set_page_config(page_title="Upload Files",page_icon="📻")
menu = st.sidebar.selectbox("Choose an option",["Fill Forum","Admin Settings"])

if menu == "Fill Forum":
    pass

if menu == "Admin Settings":
    adminPassword = st.sidebar.text_input("Insert Admin password")
    if adminPassword:
        if adminPassword == "password":
            st.sidebar.write("Access Granted")
        else:
            st.sidebar.write("Access Denied, Tries left:")
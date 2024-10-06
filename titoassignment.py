import streamlit as st
st.set_page_config(layout="wide")
menu = st.sidebar.selectbox("Menu",["House Page","House Database"])

if menu == "House Page":
    st.subheader("Registration")
    colm1,colm2 = st.columns(2)
    colm3,colm4 = st.columns(2)

    with colm1:#user_fn
        user_fn = st.text_input("First Name")
    with colm2:#user_salary
        user_us = st.number_input("yearly Salary",0,1000000,step=1000)
    with colm2:#user_salary
        btn = st.button("Click for result")

    if btn:
        if user_us < 99999:
            st.write("You can buy or rent an apartment")
        if user_us > 99999 or user_us < 500001:
            st.write("You can buy a duplex")
        if user_us > 499999 or user_us < 1000001:
            st.write("You can buy a mansion")
        if user_us > 999999 or user_us < 5000001:
            st.write("You can buy a estate")

if menu == "House Database":
    print("Nothing")
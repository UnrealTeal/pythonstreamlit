# Write a Python program for car buyers. Create a menu for the "Buy Car" page and the "Car Database" page.


# Ask for the buyer's name.
# Ask for their yearly salary.
# Based on their yearly salary, determine what type of car they can afford:
# If they earn below $30,000, they can buy a used car.
# If they earn between $30,000-$60,000, they can buy an economy car.
# If they earn between $60,000-$100,000, they can buy a mid-range car.
# If they earn between $100,000-$200,000, they can buy a luxury car.
# If they earn above $200,000, they can buy a supercar.
# Implement the program so that it displays the appropriate message to the buyer based on their salary.



import streamlit as st
st.set_page_config(layout="wide")
menu = st.sidebar.selectbox("Menu",["Buy Car","Car Database"])

if menu == "Buy Car":
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
        if user_us < 30001:
            st.write("You can buy or rent a used car")
        elif user_us > 29999 or user_us < 600001:
            st.write("You can buy an economy car")
        elif user_us > 59999 or user_us < 100001:
            st.write("You can buy a mid-range car")
        elif user_us > 999999 or user_us < 2000001:
            st.write("You can buy a luxury car")
        elif user_us < 2000001:
            st.write("You can buy a supercar")

if menu == "Car Database":
    print("Nothing")
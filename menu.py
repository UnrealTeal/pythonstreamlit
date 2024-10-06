# Homework:
# Create a simple python program that
# -create a menu for student details and students database
# -Ask for student name on the left column and their age on the right column
# -create a submit button
# - save this in a csv file
# show the dataframe in database page

import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
csvfile = pd.read_csv('submission.csv')

menu = st.sidebar.selectbox("menu",["student details","students database"])

if menu == "student details":
    st.subheader("Start Applying Here")
    colm1,colm2 = st.columns(2)
    colm3,colm4 = st.columns(2)

    with colm1:
        user_name = st.text_input("Insert name here: ")
    with colm2:
        user_age = st.number_input("Insert age here: ",14,18)
    with colm3:
        btn = st.button("Get result")

        if btn:
            st.write(user_name,"has applied for Kildonan East, at the age of",user_age)
            btn_dict = {"Name":[user_name],"Age":[user_age]}
            studentdict = pd.DataFrame(btn_dict)
            table = pd.concat([csvfile,studentdict],ignore_index=True)
            table.to_csv("submission.csv",index=False)

if menu == "students database":
    st.table(csvfile)
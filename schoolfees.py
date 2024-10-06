#create a simple page for a school.
#Show on the page the Elementary fee is 5000 dollars and the college fee is 15000 dollars

#Ask how many kids the parent have for elementary and ask if they have for college

#create a dictionary and convert all information to a dataframe after clicking a submit button

#Then show them their total tuition fee

import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
csvfile = pd.read_csv("tuifee.csv")
menu = st.sidebar.selectbox("Menu",["Elementary","College","Tuition Fees"])

if menu == "Elementary": #Elementary Tab
    st.subheader("Elemetary Sign-up")
    colm1,colm2 = st.columns(2)
    colm3,colm4 = st.columns(2)
    colm9,colm10 = st.columns(2)

    school1 = "Elementary"

    with colm1: #child name
        child_name = st.text_input("Insert child name")
    with colm2: #child age
        child_age = st.number_input("Insert child age",3,8)
    with colm3: #child enlisting
        child_num = st.number_input("Insert children enlisting",1,4)
    with colm9: #button for result
        btn1 = st.button("Get Result")
    with colm4: #parent name
        par_name = st.text_input("Insert parent name")

    if btn1: #button code
        st.write(par_name,"is enlisting",child_name,"They're going to",school1,"at the age of ",child_age,"enlisted",child_num,"child(ren)")
        elemdict = {"Child name" : [child_name],"Age" : [child_age],"Parent name" : [par_name],"School section" : [school1]}
        elemtable = pd.DataFrame(elemdict)
        elemtable = pd.concat([csvfile,elemtable],ignore_index=True)
        elemtable.to_csv("tuifee.csv",index=False)

if menu == "College": #college Tab
    st.subheader("College Sign-up")
    colm5,colm6 = st.columns(2)
    colm7,colm8 = st.columns(2)
    colm11,colm12 = st.columns(2)

    school2 = "College"

    with colm5: #child name
        kid_name = st.text_input("Insert child name")
    with colm6: #child age
        kid_age = st.number_input("Insert child age",18,28)
    with colm7: #child name
        kid_num = st.number_input("Insert children enlisting",1,4)
    with colm8: #parent
        gar_name = st.text_input("Insert parent name here")
    with colm11: #button for result
        btn2 = st.button("Get Result")

    if btn2: #button script
        st.write(gar_name,"is enlisting",kid_name,"They're going to",school2,"at the age of ",kid_age,"enlisted",kid_num,"child(ren)")
        colldict = {"Child name" : [kid_name],"Age" : [kid_age],"Parent name" : [gar_name],"School section" : [school2]}
        colltable = pd.DataFrame(colldict)
        colltable = pd.concat([csvfile,colltable],ignore_index=True)
        colltable.to_csv("tuifee.csv",index=False)

if menu == "Tuition Fees": #Tuition Tab
    st.subheader("Tuition fees")
    st.table(csvfile)
#create 2 menu pages
#PAGE 1 
#for USER REGISTRATION PAGE WITH FILLING OF INFOMATION:
#-IMAGE UPLOAD
#-name -email
#-number - country -state
#PAGE 2
#THEN A PAGE TO SHOW USER INFORMATION AFTER LOGIN (PICTURE ETC)
#This will be for each user

import streamlit as st
import pandas as pd

menu = st.sidebar.selectbox("Select an option",["Registeration","Information"])

if menu == "Registeration":
    st.subheader("Pls fill the form")
    a,b = st.columns(2)
    
    with a:
        uploadImg = st.file_uploader("Kindly add a profile picture (images)",type=["jpeg","jpg","png"])
        name = st.text_input("Insert your name")
        email = st.text_input("Type your email")
    with b:
        number = st.text_input("Write your phone number")
        country = st.text_input("Enter your country's name")
        state = st.text_input("Input the state of your country")
    if st.button("Register"):
        st.success("Successfully")



if menu == "Information":
    pass
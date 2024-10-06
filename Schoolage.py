# write a python program for students age 
# Ask them for their name
# ask them for their age
# Create a button to check the persons class
# If they are between 0-4 they should be in Reception class
# If they are between 5-11 they should be in elementary school
# if they are between 12-19 they should be in college

import streamlit as st

name = st.text_input("Pls insert your name here")
age = st.number_input("Pls insert your age here",0,20)

if st.button("Reveal Classroom"):
    if age > -1 and age < 5:
        st.write("The student",name," is in the Reception class")
    elif age > 4 and age < 12:
        st.write("The student",name," is allowed to go to elementary school")
    elif age > 11 and age < 20:
        st.write("The student",name," is admitted into college")

# Similar Question: University Scholarship Eligibility
# Write a Python program for students to check their scholarship eligibility. Create a menu for the "Check Scholarship" page and the "Scholarship Database" page.

# Ask for the student's name.
# Ask for 5 subjects GPA.
# Based on their average GPA, determine what type of scholarship they are eligible for:
# If their GPA is below 2.5, they are not eligible for a scholarship.
# If their GPA is between 2.5-3.0, they are eligible for a partial scholarship.
# If their GPA is between 3.0-3.5, they are eligible for a half scholarship.
# If their GPA is between 3.5-4.0, they are eligible for a full scholarship.
# Implement the program so that it displays the appropriate message to the student based on their GPA.

import streamlit as st
st.set_page_config(layout="wide")

st.title("Scholarship eligibility")
st.subheader("Check if you are eligible to get into university")
colm1,colm2 = st.columns(2)
colm3,colm4 = st.columns(2)
colm5,colm6 = st.columns(2)
colm7,colm8 = st.columns(2)
colm9,colm10 = st.columns(2)

with colm1:
    Name = st.text_input("Insert your Name here")
with colm2:
    GPA1 = st.number_input("Insert a GPA subject",0,5)
with colm4:
    GPA2 = st.number_input("type a GPA subject",0,5)
with colm6:
    GPA3 = st.number_input("Input a GPA subject",0,5)
with colm8:
    GPA4 = st.number_input("input a GPA subject",0,5)
with colm10:
    GPA5 = st.number_input("insert a GPA subject",0,5)

with colm3:
    btn = st.button("Get Result")
result = (GPA1+GPA2+GPA3+GPA4+GPA5) / 5
if btn:
    with colm5:
        st.subheader("Your Results")
        if result < 2.5:
            st.text(result)
            st.write("^Your result^")
            st.write(Name,"I'm sorry to say but you are not applicable to gain a scholarship")
        elif result > 2.4 or result < 3.1:
            st.text(result)
            st.write("^Your result^")
            st.write(Name,"You are eligible for a partial scholarship")
        elif result > 2.9 or result < 3.6:
            st.text(result)
            st.write("^Your result^")
            st.write(Name,"You are eligible for a half scholarship")
        elif result > 3.4 or result < 4.1:
            st.text(result)
            st.write("^Your result^")
            st.write(Name,"You are eligible for a full scholarship")
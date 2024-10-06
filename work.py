# first page (REGISTER STUDENT)
# -ask to register student
# name, class, parentname, email, phone, address

import streamlit as st
import pandas as pd

csvfile = pd.read_csv("work2.csv")
st.set_page_config(page_title="School Registeration",page_icon="📕") # Website Title
Student_id = "Student-" + str(len(csvfile)+1)

menu = st.sidebar.selectbox("Menu",["Register Student","Payment Option","Install Reciepts","Admin Options"])

with st.form("School Registeration",clear_on_submit=True): #Creates form
    if menu == "Register Student":
        st.header("Register Student")
        st.divider() #divide
        A,B = st.columns(2)
        with A:
            Name = st.text_input("**Type student's full name here:**")
            parentname = st.text_input("**Type parent/guardians full name:**")
            phone = st.text_input("**Type your phone number:**")
        with B:
            Class = st.selectbox("**Select your grade:**",["Grade 1","Grade 2","Grade 3","Grade 4"
                                                       ,"Grade 5","Grade 6","Grade 7","Grade 8","Grade 9","Grade 10","Grade 11","Grade 12"])
            email = st.text_input("**Type your email:**")
            address = st.text_input("**Type your current address:**")
        st.success("^ THE INFORMATION ABOVE SHOULD BE FILLED BY A GUARDIAN OR PARENT ^") 
        st.divider() #divide
        st.text("Does your child have any sort of allergies?")
        allergies = st.text_input("**State the allergy/ies that your child may have, type No if they dont**")
        if st.form_submit_button("Submit Student Form"): # Submit Button
                st.write("Your application has been submitted")
                StudentRegist = {"Student-":[Student_id],"Name":[Name],"ParentName":[parentname],"PhoneNumber":[phone],"Class":[Class],"Email":[email],"Address":[address],"Allergies":[allergies]}
                add2table_two = pd.DataFrame(StudentRegist)
                both_tables = pd.concat([csvfile,add2table_two], ignore_index= True)
                both_tables.to_csv("work2.csv", index= False)   

if menu == "Payment Option":
    C,D,E = st.columns(3)
    with E:
        st.subheader("Student Payment Details")
        Searchbox = st.text_input("Insert Student's ID")
        button = st.button("Find Student")

  
    if button:
        if Searchbox:  
            searchresult = csvfile[csvfile["Student-ID"] == Searchbox]
            getname = searchresult["Name"].iloc[0] #
            getgrade = searchresult["Class"].iloc[0] #

            st.subheader(f":orange[**Student Name: {getname}**]")
            st.write("**Student Grade:**",getgrade)


if menu == "Install Reciepts":
    pass

if menu == "Admin Options":
     adminPassword = st.sidebar.text_input("Insert Admin password")
     if adminPassword:
        if adminPassword == "password":
            st.sidebar.write("Correct")
        else:
            st.sidebar.write("Incorrect Password")
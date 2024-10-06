import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
menu = st.sidebar.selectbox("Menu",["Form", "Recieved"])
setpageuser_config = 0

table_one = pd.read_csv("form.csv")

if menu == "Form":
    st.title("Doctor Appointment Request Form") # title for webpage
    st.write("Fill the form below and we will get back to you for more updates and plan your appointment.") # text subheader below the title
    colm1, colm2, colm3 = st.columns(3)
    colm1b,colm2b = st.columns(2)
    colm1c,colm2c = st.columns(2)
    # V USERS FIRST AND LAST NAME V
    with colm1: # asks for users first name (User_Name)
        User_Name = st.text_input("**First Name**") 
    with colm2: # asks for users last name (User_LastName)
        User_LastName = st.text_input("**Last Name**") 
    # V DATE OF BIRTH V
    with colm3: # asks for users date of birth (DOB)
        DOB = st.date_input("**Date of birth**")
    # V GENDER AND PHONE NUMBER V
    with colm1c:  # asks for users Gender (Gender)
        Gender = st.selectbox("**Gender**",["Male","Female"])
    with colm2c:   # asks for users phone number (User_PhoneNumber)
        User_PhoneNumber = st.text_input("**Phone Number**")
    # V ADDRESS V
    User_StreetAddress = st.text_input("**Street Address**")  # asks for users street address (User_StreetAddress)
    User_StreetAddressLine2 = st.text_input("**Street Address Line 2**")  # asks for users 2nd street address (User_StreetAddress2)
    cal1,cal2 = st.columns(2)
    # V EXTRA ADDRESS INFO V
    with cal1:  # asks for users city (User_City)
        User_City = st.text_input("**City**")
    with cal2:  # asks for users state and province (User_StateProvince)
        User_StateProvince = st.text_input("**State / Province**")
    User_PostalZip = st.text_input("**Postal / Zip Code**")  # asks for users Postal or Zip Code (User_PostalZip)
    cal3,cal4 = st.columns(2)
    cal5,cal6 = st.columns(2)
    f1,f2,f3 = st.columns(3)
    # V EMAIL AND MORE V
    with cal3:  # asks for users email and if user has applied here before (User_Email , InfoReq)
        User_Email = st.text_input("**Email**")
    with cal4: # ^
        st.write("")
        Info_Req = st.radio("**Have you ever applied to our facility before?**",["Yes","No"],horizontal=True)
    with cal5:
        Info_Req2 = st.text_input("Which department would you like to get an appoinment from?")
        Info_Req3 = st.selectbox("Which procedure do you want to make an appointment for?",["Surgery","Check-Up","Vaccination","Other"])
        st.write("**Preferred Appointment Date**")

    with f2:
        if st.button("Submit"):
            st.success("The information given has been sent")
            USERSINFO = {"First Name": [User_Name], "Last Name": [User_LastName], "Date Of Birth": [DOB], "Gender": [Gender], "Phone Number": [User_PhoneNumber],
                      "Street Address": [User_StreetAddress], "Email": [User_Email],  "City": [User_City], "State/Province": [User_StateProvince],
                        "Postal/ZipCode": [User_PostalZip], "Has Been Here?": [Info_Req],"Job Info":[Info_Req2],"Appointment Info":[Info_Req3]}
            st.write(USERSINFO)
            table_two = pd.DataFrame(USERSINFO)
            st.table(table_two)
            bothtable = pd.concat([table_one,table_two],ignore_index=True)
            bothtable.to_csv("form.csv", index=False)


if menu == "Recieved":
    rec1,rec2 = st.columns(2)
    # V Asks user for there username and password if they work here V
    with rec1:
        Login_Username = st.text_input("**Write the username given to you in this bracket**")
    with rec2:
        Login_Password = st.text_input("**Write the password given to you in this bracket**")       

    if Login_Password == "1234567890" and Login_Username == "1234567890":
        st.header("User's Submittion Logs")
        st.write("Only Workers Are Permitted To View This Area")

        if st.button("Check all current users information"):
            setpageuser_config +=1
        if setpageuser_config == 1:
            st.write(table_one) # still under config
import streamlit as st

menu = st.sidebar.selectbox("Menu",["Apply","Results"])

if menu == "Apply":
    st.header("Register for Membership")
    a,b = st.columns(2)
    with a:
        st.subheader("Personal information")
    fullname = st.text_input("Insert full name here")
    address = st.text_input("Insert address here")
    c,d = st.columns(2)
    with c:
        dob = st.date_input("Select your date of birth")
        phonenumber = st.number_input("Insert Phone Number",0)
    with d:
        gender = st.radio("",["Male","Female"],horizontal=True)
        st.write("")
        email = st.text_input("Insert Email")
    st.subheader("Membership Type")
    e,f = st.columns(2)
    with e:
        st.checkbox("Individual Membership")
        st.checkbox("Family Membership")
    with f:
        st.checkbox("Student Membership")
        st.checkbox("Senior Citizen Membership")
    st.subheader("Emergency Contact Information")
    emergfullname = st.text_input("Full Name")
    g,h = st.columns(2)
    with g:
        emergphonenumber = st.number_input("Insert Number",0)
    with h:
        emergemail = st.text_input("Email")
    st.subheader("Additional Information")
    st.write("Please indicate any specific intrests, skills, or areas of experience you would like to contribute to the organization")
    extra = st.text_input("")
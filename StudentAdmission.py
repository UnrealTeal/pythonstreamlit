import streamlit as st
import pandas as pd

csv = pd.read_csv("sadmistion.csv")
countrycsv = pd.read_csv("country.csv")
menu = st.sidebar.selectbox("Menu",["Enrollment","Form Submittions"])
countrylist = countrycsv['Country']

with st.form("School enrollment",clear_on_submit=True):
    if menu == "Enrollment":
        st.header(f":blue[Student Admission]")
        st.divider()
        uploadpassport = st.file_uploader("Upload Child's Passport")
        a,b,c = st.columns(3)
        d,e = st.columns(2)
        with a:
            childfname = st.text_input("name")
        with b:
            childmname = st.text_input("middle name")
        with c:
            childlname = st.text_input("last name")
        with d:
            nationality = st.selectbox("Choose Nationality",countrylist)
        with e:
            childclass = st.selectbox("Class",["Kindergaten","Grade 1","Grade 2","Grade 3","Grade 4","Grade 5","Grade 6","Grade 7","Grade 8"])
        st.divider()
        st.header(f":red[Parent Information]")
        f,g = st.columns(2)
        with f:
            parentfname = st.text_input("parent first name")
            email = st.text_input("Email Adress")
        with g:
            parentlname = st.text_input("parent last name")
            phonenumber = st.text_input("phone number")
        address = st.text_input("address")
        h,i = st.columns(2)
        with h:
            if st.form_submit_button("Submit"):
                with i:
                    st.success("successfully submitted")


if menu == "Form Submittions":
    pass
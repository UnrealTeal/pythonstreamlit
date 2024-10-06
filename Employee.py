import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
csvfile = pd.read_csv("SDatabase.csv")
menu = st.sidebar.selectbox("Menu",["Register Staff","Staff Database","Staff File"])
User_id = "User-" + str(len(csvfile)+1)

if menu == "Register Staff":  #staff registration
    st.subheader("Registration")
    colm1,colm2 = st.columns(2)
    colm3,colm4 = st.columns(2)
    colm5,colm6 = st.columns(2)
    colm7,colm8 = st.columns(2)

    with colm1:#user_fn
        user_fn = st.text_input("First Name")
    with colm2:#user_ln
        user_ln = st.text_input("Last Name")
    with colm3:#user_email
        user_email = st.text_input("Email Address")
    with colm4:#user_gen
        user_gen = st.selectbox("Gender",["Male","Female"])
    with colm7:#user_dep
         user_dep = st.selectbox("Department",["Management","Accounting","Engineering"
                                               ,"Security","Medical","Transportation"])
    with colm8:#user_jt
        user_jt = st.selectbox("Job Title",["Board Of Directors","Supervisor","Senior Staff",
                                            "Junior Staff","Paid Intern","Unpaid Intern"])
    with colm5:#user_cs
        user_cs = st.selectbox("Contract Status",["Full Time",'Half Time'])
    with colm6:#user_mi
        user_mi = st.number_input("Monthly Income",1000,step=1000)
    user_ed = st.selectbox("Educational Degree",["None","Associate Degree","Bachelor Degree"
                                                 ,"Graduate Degree","Professional Degree","Doctoral Degree"])
    user_empd = st.date_input("Emploment Date")

    btn = st.button("Submit Employee Data")

    if btn:
        colm9,colm10 = st.columns(2)
        with colm9:
            st.success("Employee Information has been saved.")
        with colm10:
            st.write("")
        btndict = {"User_Id":[User_id],"First Name":[user_fn],"Last Name":[user_ln],"Email":[user_email] #full btn list
                   ,"Gender":[user_gen],"Department":[user_dep],"Job Title":[user_jt]
                   ,"Contract Status":[user_cs],"Monthly Income":[user_mi]
                   ,"Educational Degree":[user_ed],"Employment Date":[user_empd]}
        stafftable = pd.DataFrame(btndict)
        staff = pd.concat([csvfile,stafftable],ignore_index=True)
        staff.to_csv("SDatabase.csv",index=False)

if menu == "Staff Database":
    st.table(csvfile)
if menu == "Staff File":
    colma1,colma2,colma3 = st.columns(3)
    with colma3:
        st.subheader("Find Employee Details")
        Emp_id = st.text_input("Insert Employee's ID")
        findemp = st.button("Find Employee")

    if findemp:
        if Emp_id:
            searchinput = csvfile[ csvfile["User_Id"] == Emp_id]
            #st.table(searchinput)
            getfn = searchinput["First Name"].iloc[0]
            getln = searchinput["Last Name"].iloc[0]
            getem = searchinput["Email"].iloc[0]
            getgen = searchinput["Gender"].iloc[0]
            getdep = searchinput["Department"].iloc[0]
            getjt = searchinput["Job Title"].iloc[0]
            getcs = searchinput["Contract Status"].iloc[0]
            getmi = searchinput["Monthly Income"].iloc[0]
            geted = searchinput["Educational Degree"].iloc[0]
            getepd = searchinput["Employment Date"].iloc[0]
            fullname = getfn + " " + getln
            st.subheader(fullname)
            st.divider()
            add1,add2,add3 = st.columns(3)
            with add1:
                st.write("**Email**")
                st.text(getem)
            with add2:
                st.write("**Gender**")
                st.text(getgen)
            with add3:
                st.write("**Department**")
                st.text(getdep)
            st.divider()
            Add1,Add2,Add3 = st.columns(3)
            with Add1:
                st.write("**Job Title**")
                st.text(getjt)
            with Add2:
                st.write("**Contract Status**")
                st.text(getcs)
            with Add3:
                st.write("**Monthly Income**")
                st.text(getmi)
            st.divider()
            add4,add6,add5 = st.columns(3)
            with add4:
                st.write("**Educational Degree**")
                st.text(geted)
            with add5:
                st.write("**Employment Date**")
                st.text(getepd)
            
        else:
            with colma3:
                st.error("Pls enter a User Id")
import streamlit as st
import pandas as pd
from fpdf import FPDF
import base64

csvfile = pd.read_csv("SDatabase.csv")
st.set_page_config(layout="wide",page_title="Emplotee DB",page_icon="📃")
menu = st.sidebar.selectbox("Menu",["Register Staff","Staff Database","Staff File"])
User_id = "User-" + str(len(csvfile)+1)


st.sidebar.info("Made by Temi")

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
        findemp = st.checkbox("Find Employee")

    if findemp:
        if Emp_id:
            try:
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
                    str(getmi)
                    st.write("**Monthly Income**")
                    st.text(f"${getmi:,}")
                st.divider()
                add4,add6,add5 = st.columns(3)
                with add4:
                    st.write("**Educational Degree**")
                    st.text(geted)
                with add5:
                    st.write("**Employment Date**")
                    st.text(getepd)

                def Generate_file():
                    file = FPDF()

                    file.add_page()
                    file.set_font("Courier",size=12,style="B")

                    colx = 10
                    coly = 20
                    colw = 90
                    #line
                    file.set_line_width(0.5)
                    file.line(colx,coly+35.5, colx+75,coly+35.5)
                    #full name
                    file.set_font("Courier",size=30,style="B")
                    file.set_xy(x=colx-5,y=coly+30)
                    file.cell(colw,txt=f'{getfn} {getln}',ln=True)
                    #email
                    file.set_font("Courier",size=14,style="B")
                    file.set_xy(x=colx,y=coly+50)
                    file.cell(colw,txt=f'Email',ln=True)

                    file.set_font("Courier",size=10,style="B")
                    file.set_xy(x=colx,y=coly+55)
                    file.cell(colw,txt=f'{getem}',ln=True)
                    #Gender
                    file.set_font("Courier",size=14,style="B")
                    file.set_xy(x=colx+75,y=coly+50)
                    file.cell(colw,txt=f'Gender',ln=True)

                    file.set_font("Courier",size=10,style="B")
                    file.set_xy(x=colx+75,y=coly+55)
                    file.cell(colw,txt=f'{getgen}',ln=True)
                    #Department
                    file.set_font("Courier",size=14,style="B")
                    file.set_xy(x=colx+140,y=coly+50)
                    file.cell(colw,txt=f'Job Title',ln=True)

                    file.set_font("Courier",size=10,style="B")
                    file.set_xy(x=colx+140,y=coly+55)
                    file.cell(colw,txt=f'{getdep}',ln=True)
                    #Job Title
                    file.set_font("Courier",size=14,style="B")
                    file.set_xy(x=colx,y=coly+70)
                    file.cell(colw,txt=f'Job Title',ln=True)

                    file.set_font("Courier",size=10,style="B")
                    file.set_xy(x=colx,y=coly+75)
                    file.cell(colw,txt=f'{getjt}',ln=True)
                    #Contact Status
                    file.set_font("Courier",size=14,style="B")
                    file.set_xy(x=colx+75,y=coly+70)
                    file.cell(colw,txt=f'Contract Status',ln=True)

                    file.set_font("Courier",size=10,style="B")
                    file.set_xy(x=colx+75,y=coly+75)
                    file.cell(colw,txt=f'{getcs}',ln=True)
                    #monthly income
                    file.set_font("Courier",size=14,style="B")
                    file.set_xy(x=colx+140,y=coly+70)
                    file.cell(colw,txt=f'Monthly Income',ln=True)

                    file.set_font("Courier",size=10,style="B")
                    file.set_xy(x=colx+140,y=coly+75)
                    str(getmi)
                    file.cell(colw,txt=f'${getmi:,}',ln=True)
                    #Educational Degree
                    file.set_font("Courier",size=14,style="B")
                    file.set_xy(x=colx,y=coly+90)
                    file.cell(colw,txt=f'Educational Degree',ln=True)

                    file.set_font("Courier",size=10,style="B")
                    file.set_xy(x=colx,y=coly+95)
                    file.cell(colw,txt=f'{geted}',ln=True)
                    #Employment Date
                    file.set_font("Courier",size=14,style="B")
                    file.set_xy(x=colx+140,y=coly+90)
                    file.cell(colw,txt=f'Employment Date',ln=True)

                    file.set_font("Courier",size=10,style="B")
                    file.set_xy(x=colx+140,y=coly+95)
                    file.cell(colw,txt=f'{getepd}',ln=True)

                    #saving the file to return the file
                    file_output = 'employeefile.pdf'
                    file.output(file_output)
                    return file_output
                file_Function = Generate_file()

                with open(file_Function, "rb") as binary:
                    read_file = binary.read()
                st.sidebar.download_button(label="Download Employee File",data=read_file,file_name="EmployeeFile.pdf",mime="application/pdf")


                #if st.sidebar.button('View User File'):
                    
                        #write_file  = base64.b64encode(read_file).decode("utf-8")

                        #view_file = f'<embed src="data:application/pdf;base64,{write_file}" type="application/pdf" width="100%" height="600px" />'

                        #st.markdown(view_file,unsafe_allow_html=True)

                


            except IndexError:
                st.error('User not found')
        else:
            with colma3:
                st.error("Pls enter a User Id")



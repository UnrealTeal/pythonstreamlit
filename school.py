import streamlit as st
import pandas as pd
from fpdf import FPDF
import base64

adminpass = "123456"
try:
    csvfile = pd.read_csv("schoolDataBase.csv")
except:
    csvfile = pd.DataFrame()

menu = st.sidebar.selectbox("Menu",["Registration","View Student Profile"])
StudentId = "Student-" + str(len(csvfile)+1)

if menu == "Registration":
    with st.form("Student Registration",clear_on_submit=True):
        studentpic = st.file_uploader("Upload/Update student picture here", ["jpeg","jpg","png"])
        aa,bb = st.columns(2)
        with aa:
            st.subheader("Student Information")
           
        with bb:
            if studentpic:
                st.image(studentpic)

        a,b,c = st.columns(3)
        d,e,f = st.columns(3)
        with a:
            StudFName = st.text_input("First Name:",key=1)
        with b:
            StudLName = st.text_input("Last Name:",key=2)
        with c:
            StudGrade = st.selectbox("Grade: ",["Grade 1","Grade 2","Grade 3","Grade 4","Grade 5","Grade 6","Grade 7","Grade 8","Grade 9",])
        with d:
            StudGender = st.radio("Gender",["Male","Female"],horizontal=True)
        with e:
            StudDOB = st.text_input("Date Of Birth")
        with f:
            StudEmail = st.text_input("Student Email")

        st.subheader("Parents Information")

        g,h,i = st.columns(3)
        j,k = st.columns(2)
        l,m,n = st.columns(3)
        with g:
            PareFName = st.text_input("First Name:",key=1.1)
        with h:
            PareLName = st.text_input("Last Name:",key=2.1)
        with i:
            PareRelat = st.text_input("Relationship Status:")
        with j:
            PareConta = st.text_input("Parent Contact:")
        with k:
            PareEmail = st.text_input("Parent Email:")
        with l:
            PareAddr = st.text_input("Address:")
        with m:
            st.write("")
            st.write("")
            if st.form_submit_button("Submit Student Information"):
                with n:
                    if studentpic:
                        picname = StudentId
                        with open(picname,'wb') as writepic:
                            writepic.write(studentpic.getbuffer())
                    st.success("successfully submitted")
                InformationDict = {"Student Id":[StudentId],"Student Picture":[picname],"Student First Name":[StudFName],"Student Last Name":[StudLName],"Student Grade":[StudGrade],
                                   "Student Gender":[StudGender],"Student Date Of Birth":[StudDOB],"Student Email":[StudEmail],"Parent First Name":[PareFName],
                                   "Parent Last Name":[PareLName],"Parent Relationship Status":[PareRelat],"Parent Contact":[PareConta],"Parent Email":[PareEmail],
                                   "Parent Address":[PareAddr]}
                infoTable = pd.DataFrame(InformationDict)
                bind = pd.concat([csvfile,infoTable],ignore_index=True)
                bind.to_csv("schoolDataBase.csv",index=False)

if menu == "View Student Profile":
    userName = st.sidebar.text_input("Type User Name:")
    loginPass = st.sidebar.text_input("Type Admin Password:")
    if st.sidebar.checkbox("Enter"):
        if userName:

            if loginPass == adminpass:
                usersearch = csvfile[csvfile["Student Id"].str.lower() == userName.lower()]

                getusername = usersearch["Student Id"].iloc[0]
                getStudPic = usersearch["Student Picture"].iloc[0]
                getStudFN = usersearch["Student First Name"].iloc[0]
                getStudLN = usersearch['Student Last Name'].iloc[0]
                getStudGrade = usersearch['Student Grade'].iloc[0]
                getStudGender = usersearch['Student Gender'].iloc[0]
                getStudDOB = usersearch['Student Date Of Birth'].iloc[0]
                getStudEmail = usersearch['Student Email'].iloc[0]
                getPareFN = usersearch['Parent First Name'].iloc[0]
                getPareLN = usersearch['Parent Last Name'].iloc[0]
                getPareRS = usersearch['Parent Relationship Status'].iloc[0]
                getPareContact = usersearch['Parent Contact'].iloc[0]
                getPareEmail = usersearch['Parent Email'].iloc[0]
                getPareAdd = usersearch['Parent Address'].iloc[0]

                a1,a2,a3 = st.columns(3)

                with a1:
                    st.write(getusername)
                    st.divider()
                    st.write(getStudGrade)
                    st.divider()
                    st.write(getStudEmail)
                    st.divider()
                    st.write(getPareRS)
                    st.divider()
                    st.image(getStudPic)
                
                with a2:
                    st.write(getStudFN)
                    st.divider()
                    st.write(getStudGender)
                    st.divider()
                    st.write(getPareFN)
                    st.divider()
                    st.write(getPareContact)
                    st.divider()

                with a3:
                    st.write(getStudLN)
                    st.divider()
                    st.write(getStudDOB)
                    st.divider()
                    st.write(getPareLN)
                    st.divider()
                    st.write(getPareEmail)
                    st.divider()
                    st.write(getPareAdd)

                def Generate_StudFile():
                    file = FPDF()

                    file.add_page()
                    file.set_font("Courier",size=12,style="B")

                    colx = 10
                    coly = 20
                    colw = 90

                    #--TopBar Info
                    file.set_font("Courier",size=30,style="B")
                    file.set_xy(x=colx-5,y=coly-10)
                    file.cell(colw,txt=f'{getStudLN}, {getStudFN}',ln=True)
                    #--line
                    file.set_line_width(0.25)
                    file.line(colx-5,coly+5, colx+195,coly+5)
                    #---#
                    file.set_font("Courier",size=14,style="B")
                    file.set_xy(x=colx-5,y=coly)
                    file.cell(colw,txt=f'{getStudGrade}',ln=True)
                    #--Top Frame
                    file.set_font("Courier",size=18,style="B")
                    file.set_xy(x=colx+45,y=coly+11)
                    file.cell(colw,txt="Student Info",ln=True)
                    file.set_font("Courier",size=14,style="B")
                    file.set_xy(x=colx+47,y=coly+20)
                    file.cell(colw,txt=f'First Name: "{getStudFN}", Last Name: "{getStudLN}"',ln=True)
                    file.set_xy(x=colx+47,y=coly+27)
                    file.cell(colw,txt=f'Display Name: "{getStudFN}, {getStudLN}"',ln=True)
                    file.set_xy(x=colx+47,y=coly+34)
                    file.cell(colw,txt=f'Birth Date: "{getStudDOB}"',ln=True)
                    file.set_xy(x=colx+47,y=coly+41)
                    file.cell(colw,txt=f'Grade Level: "{getStudGrade}"',ln=True)
                    file.set_xy(x=colx+47,y=coly+48)
                    file.cell(colw,txt=f'Gender: "{getStudGender}"',ln=True)
                    file.set_xy(x=colx+47,y=coly+55)
                    file.cell(colw,txt=f'User ID: "{userName}"',ln=True)
                    #--line[Box {Student Info}]
                    file.set_line_width(0.25)
                    file.line(colx+45,coly+15, colx+195,coly+15)
                    file.line(colx+45,coly+15, colx+45,coly+65)
                    file.line(colx+45,coly+65, colx+195,coly+65)
                    file.line(colx+195,coly+15, colx+195,coly+65)
                    #--Lower Frame
                    file.set_font("Courier",size=18,style="B")
                    file.set_xy(x=colx+45,y=coly+75)
                    file.cell(colw,txt="Parent Info",ln=True)
                    file.set_font("Courier",size=14,style="B")
                    file.set_xy(x=colx+47,y=coly+85)
                    file.cell(colw,txt=f'First Name: "{getStudFN}", Last Name: "{getStudLN}"',ln=True)
                    file.set_xy(x=colx+47,y=coly+92)
                    file.cell(colw,txt=f'Display Name: "{getStudFN}, {getStudLN}"',ln=True)
                    file.set_xy(x=colx+47,y=coly+99)
                    file.cell(colw,txt=f'Birth Date: "{getStudDOB}"',ln=True)
                    file.set_xy(x=colx+47,y=coly+106)
                    file.cell(colw,txt=f'Grade Level: "{getStudGrade}"',ln=True)
                    file.set_xy(x=colx+47,y=coly+113)
                    file.cell(colw,txt=f'Gender: "{getStudGender}"',ln=True)
                    file.set_xy(x=colx+47,y=coly+120)
                    file.cell(colw,txt=f'User ID: "{userName}"',ln=True)
                    #--line[Box {Parent Info}]
                    file.set_line_width(0.25)
                    file.line(colx+45,coly+80, colx+195,coly+80)
                    file.line(colx+45,coly+80, colx+45,coly+135)
                    file.line(colx+45,coly+135, colx+195,coly+135)
                    file.line(colx+195,coly+80, colx+195,coly+135)
                    #--save file
                    StudFile_Output = "Studentpage.pdf"
                    file.output(StudFile_Output)
                    return StudFile_Output
                StudFile_Function = Generate_StudFile()

                with open(StudFile_Function, "rb") as binary:
                    read_StudFile = binary.read()
                st.sidebar.download_button(label="Download Student File", data=read_StudFile, file_name="Studentpage.pdf",mime="application/pdf")

                if st.sidebar.button('View User File'):
                    
                        write_file  = base64.b64encode(read_StudFile).decode("utf-8")

                        view_file = f'<embed src="data:application/pdf;base64,{write_file}" type="application/pdf" width="100%" height="600px" />'

                        st.markdown(view_file,unsafe_allow_html=True)

    #create a login section (username and adnin password with a submit button ) under the student profile in the sidebar

    # table = csvfile.to_html(index=False)
    # st.markdown(table, unsafe_allow_html=True)


#---------------------------------------------------------------------------------------

#Design an app for a school to register them
#Students can use their username and password to view their page

#Registration:
#-where the school can upload their profile picture
#- studentID
#-first and last names
#-grade (selectbox)
#-gender (radio)
#DOB (date_input)
#-student email

#-parent name
#-relationship
#-parent contact
#-Parent email
#-address
# create an app for your friends on how much they know you or know something or general quiz
# asks the user to enter his/her name on the questionnaire page
# the questionnaire page can be arranged in 3 or more columns (use your own ideas(-radio - selecbox))
# a button under after all to submit and this checks the right questions and add the scores and save the user score under the user name

# the other page plots the charts of all users who answered and shows their scores

# session state is a permanent storage in streamlit. anything saved her does not erase unless you reload the pag or close the page

import streamlit as st
import pandas as pd

adminpass = "123456"
percent = 0
savename = ""

if "CurrentSlide" not in st.session_state:
    st.session_state.CurrentSlide = "Frontpage"

try:
    csvfile = pd.read_csv("questions.csv")
except:
    csvfile = pd.DataFrame()

st.set_page_config("General Questions","❗","wide")
Sidebar = st.sidebar.selectbox("",["Questionnaire"])

if Sidebar == "Questionnaire":
    def FrontPage():
        a,b,c = st.columns(3, gap="Small",vertical_alignment="center")
        with a:
            pass
        with c:
            pass
        with b:
            st.header("Welcome to my questionnaire")
            Username = st.text_input("**What is your name? (Full Name Not Required)**",placeholder="Type your name above before clicking the button")
            SendButton = st.checkbox("Start the quiz")
            if SendButton:
                if Username:
                    savename = Username
                    st.success("**Success**",icon="✅")
                    st.session_state.CurrentSlide = "q1"
                    st.rerun()
                    
                else:
                    st.warning("**Type your name**", icon="⚠️")

    def Question5():
        st.header("Question 5")
        st.subheader("what does st.balloons do?")
        ee = st.radio("",["Makes balloons fly upwards","Pops balloons","Balloon noises are played"],horizontal=True)
        if st.button("Finish Quiz",key=5):
            UserInfo = {"Name":[savename],"Percentage":["5 out of ",percent]}
            info = pd.DataFrame(UserInfo)
            concact = pd.concat([info,csvfile],ignore_index=True)
            concact.to_csv("questions.csv",index=False)
            st.session_state.CurrentSlide = "your result"

    def Question4():
        st.header("Question 4")
        st.subheader("What does st.divider do?")
        dd = st.radio("",["Makes a line across the screen","Spaces numbers and letters","Used in csv files only"],horizontal=True)
        if st.button("Submit Answer",key=4):
            if dd == "Makes a line across the screen":
                st.session_state.CurrentSlide = "q5"
                
    def Question3():
        st.header("Question 3")
        st.subheader("What is '1' + 1")
        cc = st.radio("",["2","Error","'2'"],horizontal=True)
        if st.button("Submit Answer",key=3):
            st.session_state.CurrentSlide = "q4"

    def Question2():
        st.header("Question 2")
        st.subheader("Is python able to read letters?")
        bb = st.radio("",["Yes","No"],horizontal=True)
        if st.button("Submit Answer",key=2):
            st.session_state.CurrentSlide = "q3"

    def Question1():
        st.header("Question 1")
        st.subheader("What do you use to make comments in python?")
        aa = st.radio("",["--","A hashtag","There are no comments","notepad"],horizontal=True)
        if st.button("Submit Answer",key=1):
            st.session_state.CurrentSlide = "q2"

if st.session_state.CurrentSlide == "Frontpage":
    FrontPage()
elif st.session_state.CurrentSlide == "q1":
    Question1()  
elif st.session_state.CurrentSlide == "q2":
    Question2()  
elif st.session_state.CurrentSlide == "q3":
    Question3()  
elif st.session_state.CurrentSlide == "q4":
    Question4()  
elif st.session_state.CurrentSlide == "q5":
    Question5()
elif st.session_state.CurrentSlide == "your result":
    st.header("Your Score",divider="gray")
    #st.table(csvfile)
    if st.button("See all other results"):
        st.session_state.CurrentSlide = "all results"

elif st.session_state.CurrentSlide == "all results":
    st.header("All Participants [Top 20]",divider="rainbow")
    st.table(csvfile)
    if st.button("See your results"):
        st.session_state.CurrentSlide = "your result"
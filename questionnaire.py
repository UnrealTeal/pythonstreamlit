# create an app for your friends on how much they know you or know something or general quiz
# asks the user to enter his/her name on the questionnaire page
# the questionnaire page can be arranged in 3 or more columns (use your own ideas(-radio - selecbox))
# a button under after all to submit and this checks the right questions and add the scores and save the user score under the user name

# the other page plots the charts of all users who answered and shows their scores

# session state is a permanent storage in streamlit. anything saved here does not erase unless you reload the page or close the page

import streamlit as st
import pandas as pd

if "CurrentSlide" not in st.session_state:
    st.session_state.CurrentSlide = "Frontpage"

if "Name" not in st.session_state:
    st.session_state.Name = ""

if "Score" not in st.session_state:
    st.session_state.Score = 0

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
                st.session_state.Name = Username
                if st.session_state.Name:
                    st.success("**Success**",icon="✅")
                    st.session_state.CurrentSlide = "q1"
                    st.rerun()
                    
                else:
                    st.warning("**Type your name**", icon="⚠️")

    def Question1():
        st.header("Question 1")
        st.subheader("What do you use to make comments in python?")
        aa = st.radio("",["--","A hashtag","There are no comments","notepad"],horizontal=True)
        if st.button("Submit Answer",key=1):
            if aa == "A hashtag":
                st.session_state.Score += 1
            st.session_state.CurrentSlide = "q2"
            st.rerun()

    def Question2():
        st.header("Question 2")
        st.subheader("Is python able to read letters?")
        bb = st.radio("",["Yes","No"],horizontal=True)
        if st.button("Submit Answer",key=2):
            if bb == "No":
                st.session_state.Score += 1
            st.session_state.CurrentSlide = "q3"
            st.rerun()

    def Question3():
        st.header("Question 3")
        st.subheader("What is '1' + 1")
        cc = st.radio("",["2","Error","'2'"],horizontal=True)
        if st.button("Submit Answer",key=3):
            if cc == "Error":
                st.session_state.Score += 1
            st.session_state.CurrentSlide = "q4"
            st.rerun()

    def Question4():
        st.header("Question 4")
        st.subheader("What does st.divider do?")
        dd = st.radio("",["Makes a line across the screen","Spaces numbers and letters","Used in csv files only"],horizontal=True)
        if st.button("Submit Answer",key=4):
            if dd == "Makes a line across the screen":
                st.session_state.Score += 1
            st.session_state.CurrentSlide = "q5"
            st.rerun()

    def Question5():
        st.header("Question 5")
        st.subheader("What sport is known as 'The Beautiful Game'?")
        cc = st.radio("",["Soccer (Football)","Baseball","Rugby"],horizontal=True)
        if st.button("Submit Answer",key=3):
            if cc == "Soccer (Football)":
                st.session_state.Score += 1
            st.session_state.CurrentSlide = "q6"
            st.rerun()

    def Question6():
        st.header("Question 6")
        st.subheader("What is the largest mammal in the world?")
        cc = st.radio("",["Blue Whale","Elephants","Sharks"],horizontal=True)
        if st.button("Submit Answer",key=3):
            if cc == "Blue Whale":
                st.session_state.Score += 1
            st.session_state.CurrentSlide = "q7"
            st.rerun()

    def Question7():
        st.header("Question 7")
        st.subheader("Which ancient civilization built the pyramids?")
        cc = st.radio("",["Americans","Egyptians","Africans"],horizontal=True)
        if st.button("Submit Answer",key=3):
            if cc == "Egyptians":
                st.session_state.Score += 1
            st.session_state.CurrentSlide = "q8"
            st.rerun()

    def Question8():
        st.header("Question 8")
        st.subheader("What planet is known as the Red Planet?")
        cc = st.radio("",["Syruis","The Sun","Mars"],horizontal=True)
        if st.button("Submit Answer",key=3):
            if cc == "Mars":
                st.session_state.Score += 1
            st.session_state.CurrentSlide = "q9"
            st.rerun()

    def Question9():
        st.header("Question 9")
        st.subheader("Which European country has the largest population?")
        cc = st.radio("",["China","Russia","India"],horizontal=True)
        if st.button("Submit Answer",key=3):
            if cc == "Russia":
                st.session_state.Score += 1
            st.session_state.CurrentSlide = "q10"
            st.rerun()

    def Question10():
        st.header("Question 10")
        st.subheader("Who painted the Mona Lisa?")
        cc = st.radio("",["Mahatma Gandhi","Leonardo da Vinci","Marie Curie"],horizontal=True)
        if st.button("Submit Answer",key=3):
            if cc == "Leonardo da Vinci":
                st.session_state.Score += 1
            st.session_state.CurrentSlide = "q11"
            st.rerun()

    def Question11():
        st.header("Question 11")
        st.subheader("What is the main ingredient of the title in 'Green Eggs and Ham'?")
        cc = st.radio("",["Bacon","Ham","Eggs"],horizontal=True)
        if st.button("Submit Answer",key=3):
            if cc == "Eggs":
                st.session_state.Score += 1
            st.session_state.CurrentSlide = "q12"
            st.rerun()

    def Question12():
        st.header("Question 12")
        st.subheader("What is the largest organ in the human body?")
        cc = st.radio("",["Skin","Femur","Liver"],horizontal=True)
        if st.button("Submit Answer",key=3):
            if cc == "Skin":
                st.session_state.Score += 1
            st.session_state.CurrentSlide = "q13"
            st.rerun()


    def Question13():
        st.header("Question 13")
        st.subheader("Which American civil rights leader delivered the 'I Have a Dream' speech?")
        cc = st.radio("",["HMS Beagle","Yuri Gagarin","Martin Luther King Jr."],horizontal=True)
        if st.button("Submit Answer",key=3):
            if cc == "Martin Luther King Jr.":
                st.session_state.Score += 1
            st.session_state.CurrentSlide = "q14"
            st.rerun()

    def Question14():
        st.header("Question 14")
        st.subheader("Who is the CEO of Tesla, Inc.?")
        cc = st.radio("",["Mark Twain","Elon Musk","Alexander Fleming"],horizontal=True)
        if st.button("Submit Answer",key=3):
            if cc == "Elon Musk":
                st.session_state.Score += 1
            st.session_state.CurrentSlide = "q15"
            st.rerun()


    def Question15():
        st.header("Question 15")
        st.subheader("what does st.balloons do?")
        ee = st.radio("",["Makes balloons fly upwards","Pops balloons","Balloon noises are played"],horizontal=True)
        if st.button("Finish Quiz",key=5):
            if ee == "Makes balloons fly upwards":
                st.session_state.Score += 1
            UserInfo = {"Name":[st.session_state.Name],"Percentage":[st.session_state.Score]}
            info = pd.DataFrame(UserInfo)
            concact = pd.concat([csvfile,info],ignore_index=True)
            concact.to_csv("questions.csv",index=False)
            st.session_state.CurrentSlide = "your result"
            st.rerun()
                
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
elif st.session_state.CurrentSlide == "q6":
    Question6()  
elif st.session_state.CurrentSlide == "q7":
    Question7()  
elif st.session_state.CurrentSlide == "q8":
    Question8()  
elif st.session_state.CurrentSlide == "q9":
    Question9()  
elif st.session_state.CurrentSlide == "q10":
    Question10()
elif st.session_state.CurrentSlide == "q11":
    Question11()
elif st.session_state.CurrentSlide == "q12":
    Question12()
elif st.session_state.CurrentSlide == "q13":
    Question13()
elif st.session_state.CurrentSlide == "q14":
    Question14()
elif st.session_state.CurrentSlide == "q15":
    Question15()
elif st.session_state.CurrentSlide == "your result":
    st.header("Your Score",divider="gray")
    #st.table(csvfile)
    if st.button("See all other results"):
        st.session_state.CurrentSlide = "all results"
        st.rerun()

elif st.session_state.CurrentSlide == "all results":
    st.header("All Participants [Top 20]",divider="rainbow")
    st.table(csvfile)
    if st.button("See your results"):
        st.session_state.CurrentSlide = "your result"
        st.rerun()
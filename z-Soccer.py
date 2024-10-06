#HOMEWORK:
#-CREATE A NEW FILE AND ASK STUDENTS FOR THEIR BEST FOOTBALL TEAMS/CLUBS (ASK FOR NAME OF USER AND FOOTBALL CLUB HE IS SUPPORTING)
#-SAVE IN A CSV FILE
#-SHOW THE DICTIONARY OF THE RESPONSE
#-SHOW THE TABLE OF THE RESPONSE
#-SHOW THE TABLE FROM THE CSV FILE AT THE TOP (ABOUT 10 SAVED RESPONSES)
#-PLOT A BARCHART OF THE CLUBS
#-PUT A COMMENT IN EVERY LINE TO EXPLAIN WHAT THE CODE DOES

import streamlit as st # responsible for what shows on your page
import pandas as pd # read, convert join tables and csv files
import plotly.express as px # this is used for plot charts

list_one = pd.read_csv("z-Soccer.csv") # a variable to recieve csv data

menu = st.sidebar.selectbox("Menu",["Questions", "Responses"]) # menu tabs

if menu == "Questions":
    st.header("Answer the questions given below") # title head
    Name = st.text_input("Insert your name:") # asks for name of user
    Team = st.text_input("what is your best soccer team/club:") # asks for what team they support

    if st.button("Send Responce"): # button
        st.success("Your response has been sent") # sends a message to the user
        TeamDict = {"Name":[Name],"Team":[Team]} # adds result to a dictionary
        list_two = pd.DataFrame(TeamDict) # this converts from the dictionary
        both_lists = pd.concat([list_one,list_two], ignore_index= True) # both tables joined together
        both_lists.to_csv("z-Soccer.csv", index= False) # saves in the csv file
        st.write(TeamDict)

if menu == "Responses":
    st.write(list_one)# Shows the table on line 1 giving in the z-Soccer.csv file
    teamtable = list_one['Team'].value_counts().reset_index() #Displays only the teams columns to this table
    renameteamtable = teamtable.rename(columns= {"count":"Members"}) # Renames the index and 0 to Name and Teams
    teambarchat = px.bar(renameteamtable, x= 'Team', y= "Members") # It sets the x and y value to what is set in the "renameteamtable"
    st.plotly_chart(teambarchat) # Shows the bar chat
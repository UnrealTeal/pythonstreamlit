#Max is a football coach who wants to track the performance of his players over the season.
#He needs to collect data on various metrics like goals scored, assists, tackles, and passes for each player.
# This information will be saved to a CSV file and visualized using bar charts to identify areas of improvement and top performers.

#Max’s tasks involve several steps:

#Max needs to collect performance metrics for each player in his team.
#Each player has metrics like goals scored, assists, tackles, and passes.
#Save Data to CSV:

#After collecting the data, Max will save this information to a CSV file named player_performance.csv.
#Visualize Performance Data:

#Max wants to create bar charts to visualize the average performance metrics for each player.
#Let’s create a Python program to help Max with his tasks.

import streamlit as st
import pandas as pd
import plotly.express as px

table_one = pd.read_csv("z-csvchart.csv")

menu = st.sidebar.selectbox("Menu",["Input Data","Bar Chart"])

if menu == "Input Data":
    st.header("Type players performance")
    a1,a2 = st.columns(2)
    with a1:
        PlayerName = st.text_input("Insert Player Name")
    with a2:
        PlayerGoals = st.number_input("Insert Player's Goal Scored this season",0)
    if st.button("Send Result"):
        st.success("Results have been displayed")
        Userinfo = {"Name":[PlayerName],"Goals":[PlayerGoals]}
        table_two = pd.DataFrame(Userinfo)
        both_table = pd.concat([table_one,table_two], ignore_index= True)
        both_table.to_csv("z-csvchart.csv", index= False)

if menu == "Bar Chart":
    st.write(table_one)
   
    teamtablechart = px.bar(table_one, x= "Name",y= "Goals")
    st.plotly_chart(teamtablechart)
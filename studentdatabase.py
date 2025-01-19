import streamlit as st # responsible for what shows on your page
import pandas as pd # read, convert join tables and csv files
import plotly.express as px # this is used for plot charts

table_one = pd.read_csv("StudentDataBase.csv")
totalgrade = 0
totalgradeavr = 0
totalgradelet = "A"
menu = st.sidebar.selectbox("Menu",["Student Scores", "Database/Chart", 'Student File'])


if menu == "Student Scores":
    left,right = st.columns(2)    
    with left:
        st.header("Student Scores")
        name = st.text_input("Input student name")
        math = st.number_input("Input student math score",0,100,step=10)
        hp = st.number_input("Input student health score",0,100,step=10)    
        music = st.number_input("Input student music score",0,100,step=10)    
        shops = st.number_input("Input student shops score",0,100,step=10)

    with right:
        st.header("Fill out the box below:")
        year = st.selectbox("Input student year",["Year 1", "Year 2", "Year 3", "Year 4", "Year 5", "Year 6"])
        eng = st.number_input("Input student english score",0,100,step=10)
        sci = st.number_input("Input student science score",0,100,step=10)
        gym = st.number_input("Input student gym score",0,100,step=10)
        french = st.number_input("Input student french score",0,100,step=10)

    if st.button("Send Result"):
        totalgrade = (gym + sci + eng + music + hp + math + french + shops)
        totalgradeavr = (totalgrade / 6)
        if totalgradeavr >= 75:
            totalgradelet = "A"
        elif totalgradeavr >= 51:
            totalgradelet = "B"
        elif totalgradeavr >= 41:
            totalgradelet = "C"
        elif totalgradeavr >= 25:
            totalgradelet = "D"
        elif totalgradeavr >= 10:
            totalgradelet = "E"
        elif totalgradeavr >= 0:
            totalgradelet = "F"
        result = st.write(name,"'s total score is:",totalgrade,", Average is:",totalgradeavr, ", Grade is:",totalgradelet,)
        studentDict = {"Name":[name],"Year":[year],"Math":[math],"Health":[hp],"Music":[music],"English":[eng],"Science":[sci],"Gym":[gym],"Shops":[shops],"French":[french]}
        table_two = pd.DataFrame(studentDict) # table converted from the dictionary
        both_tables = pd.concat([table_one,table_two], ignore_index= True) # both tables joined together
        both_tables.to_csv("studentDataBase.csv", index= False) # saves in this location
        st.table(studentDict)

if menu == "Database/Chart":

    with open("StudentDataBase.csv","rb") as file: # Makes the file readable as each character (byte)
        data = file.read() # Read the content
    st.sidebar.download_button(label="Download CSV file", data=data,file_name="StudentDataBase.csv")    

    st.write(table_one) # Shows the table on line 1 giving in the StudentDataBase.csv file
    subjects = ["Math","Health","Music","English","Science","Gym","Shops","French"] # Gets all the subjects 
    subjecttable = table_one[subjects].mean().reset_index() #Displays only the subject columns on this table
    renametable = subjecttable.rename(columns= {"index":"Subject",0:"Average"}) # Renames the index and 0 to Subject and Average
    #st.table(subjecttable)

    choosechart = st.radio("Choose your chart",["Bar Chart","Pie Chart"],horizontal=True)
    if choosechart == "Bar Chart":
        barchat = px.bar(renametable, x= 'Subject', y= "Average") # It sets the x and y value to what is set in the "renametable"
        st.plotly_chart(barchat) # Shows the bar chart
    else:
        piechat = px.pie(renametable, names="Subject", values="Average") # Shows pie chart result instead of bar
        st.plotly_chart(piechat) # Shows the pie chart
# -- 2/4/2024 -- #

import streamlit as st #<- Streamlit is a webpage, which helps with making developing websites

st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is a text")
#^all of that are texts

a = 1   #<- that is a variable

# -- 2/8/2024 -- #

if st.button: #<- button
    st.write("This is a button, also a text")

st.image("https://www.bing.com/ck/a?!&&p=bc91707045f21f14JmltdHM9MTcwODgxOTIwMCZpZ3VpZD0wNzVhOTk5My1hNzAzLTY1NzUtMjBmMi04ZDk2YTZhOTY0ZDAmaW5zaWQ9NTgwOA&ptn=3&ver=2&hsh=3&fclid=075a9993-a703-6575-20f2-8d96a6a964d0&u=a1L2ltYWdlcy9zZWFyY2g_cT1hbiUyMGltYWdlJkZPUk09SVFGUkJBJmlkPTAzNDUyNEQzMjUzQjNFMkQ5OTNEODMyMjkwMUQxOEM5NDY3OEM3Rjk&ntb=1") #<- put the id for it to display an image

if st.checkbox("a checkbox"): #<- a check box (basically true or false)
    st.write("this is a text")

ex1,ex2,ex3,ex4 = st.columns(4) #<- that is a column for left to right
with ex1: #<- adds stuff to that column
    if st.checkbox("yes/no"):
        st.success("Text button") #<- green background with text
with ex2: #<- adds stuff to that column
    if st.checkbox("yes/no"):
        st.success("background w text")

st.set_page_config(layout="wide") #<- sets the page layout to be full width

# -- 2/15/2024 -- #

menu = st.sidebar.selectbox("menu",["1","2","3"])  #<- makes a sibebar 

# -- 2/22/2024 -- #

# CSV files (Comma seprated values)
#CSV files are text files that each data is seperated by comma
import pandas as pd # -- helps to read and write csv files, converts to a table

csvfile = pd.read_csv('Scores.csv') # <-- name of the csv you are using for the python
st.table(csvfile) # <-- this makes a table(lists)

# -- 2/25/2024 -- #

colors = ["red","blue","yellow","green"] # <-- this is a list
colors[1] = "grey"  # <-- changes blue to grey
colors.append("purple")  # <-- adds purple to the end of the list
st.write(colors)

pickcolor = st.selectbox("Pick a color",["red","blue","yellow","green"]) # <-- allows you to pick 1/4 colors

gender = st.radio("Select your gender",["Male","Female"]) # <-- creates an option to pick from

contacts = st.sidebar.selectbox("menu",["About","Home","Contact"]) # <-- select box but with letters

playerdict = {"Name":"Ronaldo","Goals":300,"Country":"portigual","Assists":85} #<-- this is a dictionary
st.write(playerdict)

# -- 2/29/2024 -- #

datatable = pd.DataFrame(playerdict)  #<-- makes a dataframe of playerdict^
st.table(datatable) #<-- shows the table on streamlit

# -- 3/3/2024 -- #

#studentdict = {"Name":[username],"Math":[Math],"Science":[Science],"History":[History],
                   #"Geography":[Geo],"English":[English],"Total":[total],"Average":[avr],"Grade":[grade]}
#studenttable = pd.DataFrame(studentdict)
#st.table(studenttable)

#bothtable = pd.concat([csvfile,studenttable],ignore_index=True) #<-- joins old table with new table
#bothtable.to_csv("scores.csv",index=False) #<-- saves the comined tables back to csv
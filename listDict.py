import streamlit as st
import pandas as pd

colors = ["red","blue","yellow","green"] # <-- this is a list
colors[1] = "grey"  # <-- changes blue to grey
colors.append("purple")  # <-- adds purple to the end of the list
st.write(colors)

pickcolor = st.selectbox("Pick a color",["red","blue","yellow","green"]) # <-- allows you to pick 1/4 colors

gender = st.radio("Select your gender",["Male","Female"]) # <-- creates an option to pick from

contacts = st.sidebar.selectbox("menu",["About","Home","Contact"]) # <-- select box but with letters

playerdict = {"Name":["Ronaldo","Messi"],"Goals":[300,400],"Country":["portigual","Argentina"],"Assists":[85,70]} #<-- this is a dictionary
st.write(playerdict)

datatable = pd.DataFrame(playerdict)
st.table(datatable)
import streamlit as st
import pandas as pd
import plotly.express as px

table_one = pd.read_csv("studentgrade.csv")

#st.write(table_one)
list = ["Maths","Reading","Writing"]
listtable = table_one[list].mean().reset_index()
renamelisttable = listtable.rename(columns= {"index":"Subject",0:"Average"})
st.table(renamelisttable)
barchat = px.bar(renamelisttable, x= "Subject",y= "Average")
st.plotly_chart(barchat)
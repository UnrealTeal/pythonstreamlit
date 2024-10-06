import streamlit as st
import plotly_express as px
import pandas as pd

table_one = pd.read_csv("votepoll.csv")
menu = st.sidebar.selectbox("Menu",["Vote","Results"])

if menu == "Vote":

    st.header("Select a candidate you want to vote for")
    st.text("Before you vote pls write your name")
    name = st.text_input("Type your name here")
    a,b = st.columns(2)
    c,d = st.columns(2)
    e,f = st.columns(2)
    with a:
        st.subheader("Micheal")
        if st.button("**Vote For Micheal**"):
            st.write("Thank you",name,"For voting")
            add = 1
            voted_for_mch = {"Micheal":[add]," Paul":[0],"Charvi":[0],"Jacob":[0],"Yohan":[0],"Lucas":[0]}
            table_two = pd.DataFrame(voted_for_mch)
            both_tables = pd.concat([table_one,table_two], ignore_index= True)
            both_tables.to_csv("votepoll.csv", index= False)

    with b:
        st.subheader("Paul")
        if st.button("**Vote For Paul**"):
            st.write("Thank you",name,"For voting")
            add2 = 1
            voted_for_pl = {"Micheal":[0],"Paul":[add2],"Charvi":[0],"Jacob":[0],"Yohan":[0],"Lucas":[0]}
            table_two = pd.DataFrame(voted_for_pl)
            both_tables = pd.concat([table_one,table_two], ignore_index= True)
            both_tables.to_csv("votepoll.csv", index= False)           
        
    with c:
        st.subheader("Charvi")
        if st.button("**Vote For Charvi**"):
            st.write("Thank you",name,"For voting")
            add3 = 1
            voted_for_chrv = {"Micheal":[0],"Paul":[0],"Charvi":[add3],"Jacob":[0],"Yohan":[0],"Lucas":[0]}
            table_two = pd.DataFrame(voted_for_chrv)
            both_tables = pd.concat([table_one,table_two], ignore_index= True)
            both_tables.to_csv("votepoll.csv", index= False) 
        
    with d:
        st.subheader("Jacob")
        if st.button("**Vote For Jacob**"):
            st.write("Thank you",name,"For voting")
            add4 = 1
            voted_for_jcb = {"Micheal":[0],"Paul":[0],"Charvi":[0],"Jacob":[add4],"Yohan":[0],"Lucas":[0]}
            table_two = pd.DataFrame(voted_for_jcb)
            both_tables = pd.concat([table_one,table_two], ignore_index= True)
            both_tables.to_csv("votepoll.csv", index= False) 

    with e:
        st.subheader("Yohan")
        if st.button("**Vote For Yohan**"):
            st.write("Thank you",name,"For voting")
            add5 = 1
            voted_for_yhn = {"Micheal":[0],"Paul":[0],"Charvi":[0],"Jacob":[0],"Yohan":[add5],"Lucas":[0]}
            table_two = pd.DataFrame(voted_for_yhn)
            both_tables = pd.concat([table_one,table_two], ignore_index= True)
            both_tables.to_csv("votepoll.csv", index= False) 
        
    with f:
        st.subheader("Lucas")
        if st.button("**Vote For Lucas**"):
            st.write("Thank you",name,"For voting")  
            add6 = 1
            voted_for_lcs = {"Micheal":[0],"Paul":[0],"Charvi":[0],"Jacob":[0],"Yohan":[0],"Lucas":[add6]}
            table_two = pd.DataFrame(voted_for_lcs)
            both_tables = pd.concat([table_one,table_two], ignore_index= True)
            both_tables.to_csv("votepoll.csv", index= False) 


if menu == "Results":
    participants = ["Micheal","Paul","Charvi","Jacob","Yohan","Lucas"]
    ppltable = table_one[participants].sum().reset_index()
    renameppltable = ppltable.rename(columns={"index":"Voters",0:"Candidates"})
    st.table(renameppltable)

    chooseChart = st.radio("Choose a chart",["Pie Chart","Bar Chart"])
    if chooseChart == "Pie Chart":
        piechat = px.pie(renameppltable, names="Voters", values="Candidates") # Shows pie chart result instead of bar
        st.plotly_chart(piechat) # Shows the pie chart
    if chooseChart == "Bar Chart":
        barchat = px.bar(renameppltable, x= 'Voters', y= "Candidates") # It sets the x and y value to what is set in the "renametable"
        st.plotly_chart(barchat) # Shows the bar chart
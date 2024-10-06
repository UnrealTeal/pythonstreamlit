import streamlit as st
amount_cost = 0
purchase_Bible = st.text_input("Would you like to buy a Bible along with other products? (Yes or No)")
if purchase_Bible == "Yes":
    st.write("Once this step is done your bible will also be purchased")
    username = st.text_input("Type your username")
    password = st.text_input("Type your password")
    Devotional = st.radio("**pick the following devotional books:**",["Daily Devotions for $10","Bible Study Guide for $20","Prayer Journal for $15"])
    outfit = st.radio("**pick the following outfit you want to buy:**",["Outfit 1 costs $30","Outfit 2 costs $50","Outfit 3 costs $70"])
    adopt = st.number_input("**the nummber you type is how many pets you would like to adopt:**",0,3)
    artifacts = st.radio("**pick the following artifacts you want to buy:**",["Cross Necklace for $10","Rosary Beads for $20","Icon for $30"])

    if st.button("Total Cost"):
        if Devotional == "Daily Devotions for $10":
            amount_cost += 10
        elif Devotional == "Bible Study Guide for $20":
            amount_cost += 20
        elif Devotional == "Prayer Journal for $15":
            amount_cost += 15
        if outfit == "Outfit 1 costs $30":
            amount_cost += 30
        elif outfit == "Outfit 2 costs $50":
            amount_cost += 50
        elif outfit == "Outfit 3 costs $70":
            amount_cost += 70
        if adopt == 1:
            amount_cost += 25
        elif adopt == 2:
            amount_cost += 50
        elif adopt == 3:
            amount_cost += 75
        elif adopt == 0:
            amount_cost += 0
        if artifacts == "Cross Necklace for $10":
            amount_cost += 10
        elif artifacts == "Rosary Beads for $20":
            amount_cost += 20
        elif artifacts == "Icon for $30":
            amount_cost += 30
        st.write("The amount you have to pay is",amount_cost,"dollars")
elif purchase_Bible == "No":
    st.write("Thank you for your time")
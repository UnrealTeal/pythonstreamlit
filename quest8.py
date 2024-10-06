import streamlit as st

paycost = 0
buy_game = st.text_input("Would you like to purchase roblox?")
st.write("Yes or No? (Case Sensitive)")
if buy_game == "Yes":
    add_username = st.text_input("Insert your roblox username: ")
    add_password = st.text_input("Insert your roblox password: ")

    if add_username and add_password:
        purchase_vip = st.radio("Pick one of the following",["Premium: $120","vip: $50","neither"],horizontal=True)
        if purchase_vip == "neither":
            st.write("You can always buy this later")
        elif purchase_vip == "Premium: $120":
            st.write("You have successfully purchased it for $120 dollars")
            paycost += 120
        elif purchase_vip == "vip: $50":
            st.write("You have successfully bought it for $50 dollars")
            paycost += 50
        purchase_clothing = st.radio("Pick one of the following",["R6: $15","Pro: $35","Classic: $20","default"],horizontal=True)
        if purchase_clothing == "R6: $15":
            st.write("You have purchased it for $15 dollars")
            paycost += 15
        elif purchase_clothing == "Pro: $35":
            st.write("You have successfully purchased it for $35 dollars")
            paycost += 35
        elif purchase_clothing == "Classic: $20":
            st.write("You have successfully bought it for $20 dollars")
            paycost += 20
        elif purchase_clothing == "default":
            st.write("You can always change later")
        purchase_pet = st.radio("Would you like to get a pet?",["No","Yes: $40"],horizontal=True)
        if purchase_pet == "Yes":
            st.write("You have successfully bought a pet for $40 dollars")
            paycost += 40
        elif purchase_pet == "No":
            st.write("You can always buy one later")
        purchase_robux = st.selectbox("select amount",["800 Robux for $10","2000 Robux for $25","4500 Robux for $50"])
        
else:
    st.write("Responce Required")

st.write(paycost)
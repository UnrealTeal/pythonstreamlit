import streamlit as st
amount = 0
purchase_ticket = st.text_input("Would you like to buy a ticket? Yes or No")
if purchase_ticket == "Yes":
    username = st.text_input("Type your username")
    password = st.text_input("Type your password")
    seasonPass = st.radio("**pick the following season passes:**",["Standard Pass for $200","VIP Pass for $500"])
    merchandise = st.radio("**pick the following team merchandise:**",["Jersey for $60","Scarf for $30","Hat for $20"])
    food = st.radio("**pick the following food to eat:**",["Popcorn for $10","Hotdog for $15","Soda for $5"])
    subscription = st.radio("**pick the following sport channel subscription:**",["Monthly subscription for $20","Annual subscription for $200"])

    if st.button("Total Cost"):
        if seasonPass == "Standard Pass for $200":
            amount += 200
        elif seasonPass == "VIP Pass for $500":
            amount += 500
        if merchandise == "Jersey for $60":
            amount += 60
        elif merchandise == "Scarf for $30":
            amount += 30
        elif merchandise == "Hat for $20":
            amount += 20
        if food == "Popcorn for $10":
            amount += 10
        elif food == "Hotdog for $15":
            amount += 15
        elif food == "Soda for $5":
            amount += 5
        if subscription == "Monthly subscription for $20":
            amount += 20
        elif subscription == "Annual subscription for $200":
            amount += 200
        st.write("The amount you have to pay is",amount,"dollars")
elif purchase_ticket == "No":
    st.write("Thank you for your time")
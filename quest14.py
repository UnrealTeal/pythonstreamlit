import streamlit as st

john = 400

concert_cost = st.number_input("How much did you spend on a concert ticket: ")
dinner_cost = st.number_input("How much did you spend on a dinner: ")
shopping_cost = st.number_input("How much did you spend on shopping: ")
transportation_cost = st.number_input("How much did you spend on transportation: ")
movie_cost = st.number_input("How much did you spend on movie tickets: ")

total_expense = concert_cost + dinner_cost + shopping_cost + transportation_cost + movie_cost

amount_left = john - total_expense

if st.button("Total Expense"):
    if amount_left > 0:
        investment_amount = amount_left / 4
        st.write("You have", amount_left, "dollars left.")
        st.write("You can invest", investment_amount, "dollars.")
    elif amount_left == 0:
        st.write("You spent all your money.")
    elif amount_left < 0:
        st.write("You spent more than your savings.")
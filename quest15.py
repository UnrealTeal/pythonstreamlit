import streamlit as st

initial_animals = 50

sold_animals = st.number_input("How many animals have you sold to the marketplace?",0,step=10)
eaten_by_predators = st.number_input("How many animals are eaten by predators?",0,step=10)
died_from_disease = st.number_input("How many animals die from disease?",0,step=10)
stolen_animals = st.number_input("How many animals are stolen?",0,step=10)

Calc_result = (sold_animals + eaten_by_predators + died_from_disease + stolen_animals)
result = initial_animals - Calc_result
if st.button("Check animals left: "):
    if result > 0:
        st.write("You have",result,"animals alive")
    elif result == 0:
        st.write("You have no animals alive")
    elif result < 0:
        st.write("You have lost more animals that you initially had")
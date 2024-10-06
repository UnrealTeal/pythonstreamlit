# create a restaurant app
# -Add a restaurant picture
# - shows them the food selections
# -If they choose/select their meals, show them the total amount
# -Ask a question if you want to share the bill with others #use checkbox
# -if yes, then ask how many people want to share the bill
# -Then show the amount each person must contribute to pay the bill

#meal,drink,fruit
#arrange 2 items in each column^

import streamlit as st

payment = 0

st.set_page_config(layout="wide")

st.title("Temi's Food Menu")

st.image("https://cdn.pixabay.com/photo/2017/09/23/12/40/catering-2778755_1280.jpg")

st.subheader("Meal Category")
meal1,meal2,meal3,meal4 = st.columns(4)


with meal1:
    if st.checkbox("Rice & Chinese sause: $56"):
        payment += 56
        st.success("Successfully added to cart")

with meal2:
    if st.checkbox("Spag & Sauce: $30"):
        payment += 30
        st.success("Successfully added to cart")

with meal3:
    if st.checkbox("Beans & Plantain: $17"):
        payment += 17
        st.success("Successfully added to cart")

with meal4:
    if st.checkbox("Potato & Stew: $5.75"):
        payment += 5.75
        st.success("Successfully added to cart")


st.subheader("Drink Category")
drink1,drink2,drink3,drink4 = st.columns(4)


with drink1:
    if st.checkbox("Pepsi :$3.75"):
        payment += 3.75
        st.success("Successfully added to cart")

with drink2:
    if st.checkbox("Coca-Cola: $3.75"):
        payment += 3.75
        st.success("Successfully added to cart")

with drink3:
    if st.checkbox("Fanta: $3.75"):
        payment += 3.75
        st.success("Successfully added to cart")

with drink4:
    if st.checkbox("Juice Box: $1.75"):
        payment += 1.75
        st.success("Successfully added to cart")


st.subheader("Fruits Category")
fruit1,fruit2,fruit3,fruit4 = st.columns(4)


with fruit1:
    if st.checkbox("Sliced Apples :$1.50"):
        payment += 1.50
        st.success("Successfully added to cart")

with fruit2:
    if st.checkbox("Orange: $1.50"):
        payment += 1.50
        st.success("Successfull added to cart")

with fruit3:
    if st.checkbox("banana: $1.50"):
        payment += 1.50
        st.success("Successfully added to cart")

with fruit4:
    if st.checkbox("Pear Slices: $1.50"):
        payment += 1.50
        st.success("Successfully added to cart")

if st.button("Total Payment"):
    st.write("The total amount you need to pay is : $",payment)

if st.checkbox("Click to share your bill"):
    amount = st.number_input("How many people would you like to share this bill with?",1,50)
    if st.button("Click to check the bill"):
        st.write("the amount each person need to contribute to the bill is: $",payment / amount)

# -Ask a question if you want to share the bill with others #use checkbox
# -if yes, then ask how many people want to share the bill
# -Then show the amount each person must contribute to pay the bill
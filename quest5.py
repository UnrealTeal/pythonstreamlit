import streamlit as st
menu = st.sidebar.selectbox("Menu",["Addition", "Subtraction", "multiplication", "Division"])

askname = st.text_input("What is your name?")

if menu == "Addition":
    add = st.number_input("Insert any number of your choice")
    add2 = st.number_input("added by?")
    result = add + add2
    st.write("Your answer is", result)

if menu == "Subtraction":
    sub = st.number_input("Insert any number of your choice")
    sub2 = st.number_input("subtracted by?")
    result2 = sub - sub2
    st.write("Your answer is",result2)

if menu == "multiplication":
    mul = st.number_input("Insert any number of your choice")
    mul2 = st.number_input("Multipled by?")
    result3 = mul * mul2
    st.write("Your answer is",result3)

if menu == "Division":
    div = st.number_input("Insert any number of your choice")
    div2 = st.number_input("Divided by?")
    if div2 == 0:
        st.write("You can't divide by 0")
    else:
        result4 = div / div2
        st.write("Your answer is",result4)



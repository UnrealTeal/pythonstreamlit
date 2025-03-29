import streamlit as st
import pandas as pd

ToPayTotal = 0.0
BookCart = []

st.subheader("Children Books")
a,b,c,d = st.columns(4)
with a:
    st.write("The Color Monster: A Story About Emotions")
    st.image("https://m.media-amazon.com/images/I/810BnEcCkML._SY385_.jpg")
    st.text("PRICE: $11.95")
    if st.checkbox("Add to Cart", key=1):
        ToPayTotal += 11.95
        BookCart.append("The Color Monster: A Story About Emotions")
with b:
    st.write("Noisy Farm: Includes Six Sounds!")
    st.image("https://m.media-amazon.com/images/I/81SuqCn738L._SY385_.jpg")
    st.text("PRICE: $19.99")
    if st.checkbox("Add to cart", key=1.1):
        ToPayTotal += 19.99
        BookCart.append("Noisy Farm: Includes Six Sounds!")
with c:
    st.write("The Pigeon HAS to Go to School!")
    st.image("https://m.media-amazon.com/images/I/71-4uayd7PL._SY385_.jpg")
    st.text("PRICE: $22.99")
    if st.checkbox("Add to cart", key=1.2):
        ToPayTotal += 22.99
        BookCart.append("The Pigeon HAS to Go to School!")
with d:
    st.write("We All Belong: About Diversity")
    st.image("https://m.media-amazon.com/images/I/41G6apG0yDL._SX342_SY445_.jpg")
    st.text("PRICE: $19.99")
    if st.checkbox("Add to cart", key=1.3):
        ToPayTotal += 19.99
        BookCart.append("We All Belong: About Diversity")
st.subheader("Family Books")
e,f,g,h = st.columns(4)
with e:
    st.write("It's Not the Stork!")
    st.image("https://m.media-amazon.com/images/I/91BCOxpMJdL._SY425_.jpg")
    st.text("PRICE: $17.99")
    if st.checkbox("Add to cart", key=2):
        ToPayTotal += 17.99
        BookCart.append("It's Not the Stork!")
with f:
    st.write("A Family Tree")
    st.image("https://m.media-amazon.com/images/I/71hBrAJmxBL._SY385_.jpg")
    st.text("PRICE: $24.99")
    if st.checkbox("Add to cart", key=2.1):
        ToPayTotal += 24.99
        BookCart.append("A Family Tree")
with g:
    st.write("Our School is a Family")
    st.image("https://m.media-amazon.com/images/I/81X-brxAK9L._SY522_.jpg")
    st.text("PRICE: $17.85")
    if st.checkbox("Add to cart", key=2.2):
        ToPayTotal += 17.85
        BookCart.append("Our School is a Family")
with h:
    st.write("What Does Your Daddy Do All Day?")
    st.image("https://images.prismic.io/wonderbly/e1961398-d63e-405e-ba12-ae4da1027e6b_WDD_Carousel_01-1.jpg?auto=format%2Ccompress&dpr=&w=1100&h=&fit=&crop=&q=35&gif-q=90")
    st.text("PRICE: $44.99")
    if st.checkbox("Add to cart", key=2.3):
        ToPayTotal += 44.99
        BookCart.append("What Does Your Daddy Do All Day?")
st.subheader("Christian Books")
i,j,k,l = st.columns(4)
with i:
    st.write("Principles: Life and Work")
    st.image("https://m.media-amazon.com/images/I/41Dn20bdaAL._SY445_SX342_.jpg")
    st.text("PRICE: $44.27")
    if st.checkbox("Add to cart", key=3):
        ToPayTotal += 44.27
        BookCart.append("Principles: Life and Work")
with j:
    st.write("How the Christian Revolution Remade the World")
    st.image("https://m.media-amazon.com/images/I/81syQS5hHGL._SY522_.jpg")
    st.text("PRICE: $23.91")
    if st.checkbox("Add to cart", key=3.1):
        ToPayTotal += 23.91
        BookCart.append("How the Christian Revolution Remade the World")
with k:
    st.write("The God of the Woods: A Novel")
    st.image("https://m.media-amazon.com/images/I/81gHfeKi+9L._SY522_.jpg")
    st.text("PRICE: $26.93")
    if st.checkbox("Add to cart", key=3.2):
        ToPayTotal += 26.93
        BookCart.append("The God of the Woods: A Novel")
with l:
    st.write("Five Lies of Our Anti-Christian Age")
    st.image("https://m.media-amazon.com/images/I/71HfPZe83GL._SY522_.jpg")
    st.text("PRICE: $32.65")
    if st.checkbox("Add to cart", key=3.3):
        ToPayTotal += 32.65
        BookCart.append("Five Lies of Our Anti-Christian Age")
st.subheader("Science Books")
m,n,o,p = st.columns(4)
with m:
    st.write("The Power and Purpose of the Teenage Brain")
    st.image("https://m.media-amazon.com/images/I/61HYVo46E-L._SY522_.jpg")
    st.text("PRICE: $25.00")
    if st.checkbox("Add to cart", key=4.1):
        ToPayTotal += 25
        BookCart.append("The Power and Purpose of the Teenage Brain")
with n:
    st.write("Why Stories Make Us Human and How to Tell Them Better")
    st.image("https://m.media-amazon.com/images/I/51W1vk3z4aL._SY522_.jpg")
    st.text("PRICE: $23.00")
    if st.checkbox("Add to cart", key=4.2):
        ToPayTotal += 23
        BookCart.append("Why Stories Make Us Human and How to Tell Them Better")
with o:
    st.write("The Ultimate Guide to Rebuilding a Civilization")
    st.image("https://m.media-amazon.com/images/I/71oZfxNRvCL._SY522_.jpg")
    st.text("PRICE: $160.00")
    if st.checkbox("Add to cart", key=4.3):
        ToPayTotal += 160
        BookCart.append("The Ultimate Guide to Rebuilding a Civilization")
with p:
    st.write("The Stigmata and Modern Science")
    st.image("https://cdn11.bigcommerce.com/s-iuax7bpgx3/images/stencil/1280x1280/products/2651/453/453__87407.1675951611.jpg?c=1")
    st.text("PRICE: $7.95")
    if st.checkbox("Add to cart", key=4.4):
        ToPayTotal += 7.95
        BookCart.append("The Stigmata and Modern Science")

if st.button("Check Cart"):
    ToPayTotal = round(ToPayTotal,2)
    st.write("Books: ",BookCart)
    st. write("Total Cost: ",ToPayTotal)
    booksdict = {''}
if st.button("Purchase Books"):
    pass
#**3. Book Selection:**

#Children Books
#4 columns each with 2 rows
#Image and price with checkbox included
#Each book must have an image

#Family Books

#Christian Books

#Science Books

#Books in checkboxes with images, names and prices
#**Total Amount:**
#Based on your selections, the total amount will be calculated automatically.

#Mr. tee: get purchased book 

#save each click sales in the database
#load a csv file,
#Customer name, bookq, book2, book3, etc customer total bill
#Jason,15,14,12,14,700

#Hint: foodorder & studnetdb
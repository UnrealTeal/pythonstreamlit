""""
-title
-image
-categories
Men's Fashion

Women's Fashion

Children's Fashion

(each category must havedifferent types of unique items and the prices 
like shirts(long sleeves,short, round nexk, polo etc), boxers, trousers, shoes, bags etc)

Show the total bill
"""

import streamlit as st

st.set_page_config(layout="wide")

menu = st.sidebar.selectbox("Menu",["Men's Fashion","Women's Fashion","Children's Fashion"])

if menu == "Men's Fashion":
    st.title("Welcome to the men's section")
    st.image("https://cdn.pixabay.com/photo/2020/06/20/16/13/male-5321547_1280.jpg")
    men1,men2,men3 = st.columns(3)

    with men1:
        st.subheader("Men's Cloths")
        if st.checkbox("White T-Shirt: $32"): #option 1
            st.success("successfully added in cart")
            #^option1^
        if st.checkbox("white & Black office shirt: $59"): #option 2
            st.success("Successfully added to cart")
            #^option2^
    
    with men2:
        st.subheader("Men's trousers")
        if st.checkbox("grey shorts with pockets: $21"): #option 1
            st.success("successfully added to cart")
            #^option1^
        if st.checkbox("Black long sleeve pants: $24"): #option2
            st.success("Successfully added to cart")
            #^option2^

    with men3:
        st.subheader("Men's Shoes")
        if st.checkbox("Army colored crocks: $38"): #option 1
            st.success("Successfully added to cart")
            #^option1^
        if st.checkbox("Black running shoes: $46"): #option 2
            st.success("Successfully added to cart")
            #^option2^    

#----#
if menu == "Women's Fashion":
    st.title("Welcome to the women's section")
    st.image("https://cdn.pixabay.com/photo/2016/10/15/05/02/girls-1741925_1280.jpg")
    women1,women2,women3 = st.columns(3)  

    with women1:
        st.subheader("Women's Trousers")
        if st.checkbox("Baggy Jeans: $21"): #option 1
            st.success("Successfully added to cart")
        #^option1^
        if st.checkbox("Ripped Jeans: $23"): #option 2
            st.success("Successfully added to cart")
        #^option2^

    with women2:
        st.subheader("Women's Shoes")
        if st.checkbox("High Heels: $36"): #option 1
            st.success("Successfully added to cart")
        #^option1^
        if st.checkbox("Gucci shoes/black & white: $47"): #option 2
            st.success("Successfully added to cart")
        #^option2^

    with women3:
        st.subheader("Women's Bags")
        if st.checkbox("Black deisgner bag: $56"): #option 1
            st.success("Successfully added to cart")
        #^option1^
        if st.checkbox("White gucci bag: $52"): #option 2
            st.success("Successfully added to cart")
        #^option2^
            
#----#
if menu == "Children's Fashion":
    st.title("Welcome to the children's section")
    st.image("https://cdn.pixabay.com/photo/2015/06/22/08/37/children-817365_1280.jpg")
    child1,child2,child3 = st.columns(3)

    with child1:
        st.subheader("Children's clothes")
        if st.checkbox("Green dinosaur shirt: $12"): #option 1
            st.success("Successfully added to cart")
        #^option1^
        if st.checkbox("Purple unicorn shirt: 12"): #option 2
            st.success("Successfully added to cart")
        #^option2^

    with child2:
        st.subheader("children's bags")
        if st.checkbox("Paw patrol bag: $18"): #option 1
            st.success("Successfully added to cart")
        #^option1^
        if st.checkbox("Peppa pig bag: $18"): #option 2
            st.success("Successfully added to cart")
        #^option2^

    with child3:
        st.subheader("children's shoes")
        if st.checkbox("Flat nike shoes"): #option 1
            st.success("Successfully added to cart")
        #^option1^
        if st.checkbox("Addidas shoes"): #option 2
            st.success("Successfully added to cart")
        #^option2^

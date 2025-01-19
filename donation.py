import streamlit as st
import pandas as pd
csvfile = pd.read_csv("donations.csv")
csv = pd.read_csv("donationadd.csv")
menu = st.sidebar.selectbox("Select an option",["Create Donation","View Donations","Donate"])

with st.form("Donation",clear_on_submit=True):
    if menu == "Create Donation":
        st.header("Create Donation")
        st.divider()
        c1,d1 = st.columns(2)
        with c1:
            campaignTitle = st.text_input("Campaign Title")
        with d1:
            email = st.text_input("Email")
        st.divider()
        campaignDetails = st.text_area("Campaign Details",height=200)
        goalamount = st.number_input("Insert Custom Goal Amount: ",0)
    
        if st.form_submit_button("Create Campaign"):
                st.write("Your Campaign has been submitted")
                DonorRegist = {"title":[campaignTitle],"email":[email],"detail":[campaignDetails],"amount":[goalamount]}
                add2tab_two = pd.DataFrame(DonorRegist)
                both_tables = pd.concat([csvfile,add2tab_two], ignore_index= True)
                both_tables.to_csv("donations.csv", index= False)

if menu == "View Donations":
    st.header("View Donations")
    st.divider()
    alltitles = csvfile["title"]
    col1,col2 = st.columns(2)
    with col1:
        selecttitle = st.selectbox("Select Donation to view",alltitles)

    filtertitle = csvfile[csvfile["title"] == selecttitle] # filters the title column to extract only the row of selected titles
    getcontent = filtertitle["detail"].iloc[0] # extracr the first item in the details column
    getamount = filtertitle["amount"].iloc[0]
    getemail = filtertitle["email"].iloc[0]
    st.divider()
    COL1,COL2 = st.columns(2)
    with COL1:
        st.subheader("Campaign Details")
        donatecash = st.number_input("Donate to this cause",0,step=100)
        b,c = st.columns(2)
        with b:
            if st.button("Donate"):
                with c:
                    st.write("**Thanks so much**")

    with COL2:
        st.info(f":white[Total Amount: ${getamount:,}]")
        st.error(f":blue[Amount Left]")
    st.divider()
    st.write(getcontent)
    st.write(f":blue[Contact: {getemail}]")

if menu == "Donate":
    st.subheader("Select Donation")
    Donotitles = csvfile["title"].to_list()
    st.divider()
    a1,b2 = st.columns(2)
    with a1:
        selectdono = st.selectbox("Select a donation: ", Donotitles)
    st.divider()
    with b2:
        donateamount = st.number_input("Insert your donation amount: ",0)
    donatebtn = st.button("Donate")
    if donatebtn:
        donationdict = {f'{selectdono}':[donateamount]}
        donatetable = pd.DataFrame(donationdict)
        st.table(donatetable)
        st.success("Success")

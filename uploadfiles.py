import streamlit as st
import pandas as pd
st.set_page_config(page_title="Upload Files",page_icon="📻")

menu = st.sidebar.selectbox("Choose an option",["Upload CSV","Upload Audio","Upload Video","Upload Image"])
st.sidebar.write("**Made By: Temi**")
if menu == "Upload CSV":
    st.subheader("Upload CSV & View Database")
    uploadcsv = st.file_uploader("Upload your sound here")

    if uploadcsv:
        readcsv = pd.read_csv(uploadcsv)

        with st.expander("View CSV Table"): # like a toggle (open and close)
            st.table(readcsv)

if menu == "Upload Audio":
    st.subheader("Upload Audio To Play")
    uploadaudio = st.file_uploader("Upload your audio file here")
    if uploadaudio:
        st.audio(uploadaudio,format="audio/mp3")

if menu == "Upload Video":
    st.subheader("Upload Youtube Video Link")
    youtubelink = st.text_input("Paste in the video link")
    if st.button("Upload"):
        st.video(youtubelink)

if menu == "Upload Image":
    st.subheader("Upload image here")
    imageholder = st.file_uploader("image")
    if imageholder:
        st.image(imageholder)




#classwork: 
# put a button to click to play
# check to handle errors 
#ability test on uploadCSV
# use a multiselect to choose columns to plot: create a variable called columnslist = 'read your pandas file'.to_list()
# use a radio to choose statistical operators (sum,average,count) #check your previous work
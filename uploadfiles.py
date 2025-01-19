import streamlit as st
import pandas as pd
import plotly_express as px
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

        readcsvcolumns = readcsv.columns # read all columns in csv file

        selectcolumns = st.multiselect("Choose Columns to plot",readcsvcolumns)
        col1,col2 = st.columns(2)
        with col1:
            selectchart = st.radio("Choose Coloumns Stats Operator",["Average",'Sum','Count'],horizontal=True)
        with col2:
            selectoperator = st.radio("Choose Column Stats operator",["Bar Chart",'Pie Chart'],horizontal=True)
        
        if selectcolumns:
            if selectchart == 'Average':
                ave_op = readcsv[selectcolumns].mean().reset_index()
                # st.table(ave_op)

                if selectoperator == "Bar Chart":
                    barchart = px.bar(ave_op, x= 'index', y=0,labels={'index':'Subject',"0":"Average"})
                    st.plotly_chart(barchart)

                elif selectoperator == "Pie Chart":
                    piechart = px.pie(ave_op, names= 'index', values=0,labels={'index':'Subject',"0":"Average"})
                    st.plotly_chart(piechart)



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

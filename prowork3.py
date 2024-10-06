import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
csvfile = pd.read_csv("SDatabase.csv")
menu = st.sidebar.selectbox("Menu",["Register Staff","Staff Database","Staff File"])
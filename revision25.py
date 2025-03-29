import streamlit as st
import pandas as pd

readattendance = pd.read_csv("attendance.csv")


studentName = st.text_input("Insert Student's Name")
rollNumber = st.text_input("type student roll number")
tdPresent = st.number_input("Total arrivals",0)
tdAbsent = st.number_input("Total absents",0)
if st.button("Send Info"):
    attend_dict = {"Student Names":studentName,"Student Roll Numbers":[rollNumber],"Total Days Present":[tdPresent],"Total Days Absent":[tdAbsent]}
    attendance = pd.DataFrame(attend_dict)
    bothtable = pd.concat([readattendance,attendance],ignore_index=True)
    bothtable.to_csv("attendance.csv",index=False)
    st.table(readattendance)
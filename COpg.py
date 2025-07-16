import streamlit as st
def co_page():
    st.title("Co-Enrolled Participants Overview Dashboard")
    st.metric("Total Participants", 45)


    #power bi link embed 
    co_url = ""
    components.iframe(rtw_url, height=900, width=1600)

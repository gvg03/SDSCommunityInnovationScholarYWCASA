import streamlit as st
def co_page():
    st.title("Co-Enrolled Participants Overview Dashboard")
    st.metric("Total Participants", 45)


    #power bi link embed 
    co_url = "https://app.powerbi.com/view?r=eyJrIjoiOTQ4YjZiNWUtNTlhYi00MjMzLTk2YjUtZTk4ZDBjMzQ4YTBlIiwidCI6IjNhMjI4ZGZiLWM2NDctNDRjYi04ODM1LTdiMjA2MTdmYzkwNiIsImMiOjN9"
    components.iframe(rtw_url, height=900, width=1600)

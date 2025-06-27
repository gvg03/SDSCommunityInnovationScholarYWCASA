#home age setup

# Imports
import streamlit as st  # importing streamlit
import pandas as pd     # panda
import plotly
import plotly.express as px  # for interactive zip code
import json             # to load file, for zipcode
import streamlit.components.v1 as components   # to bring in PowerBi

# Page Setup, layout and title
st.set_page_config(layout="wide")

# Sidebar: Navigate + Prog Filter
st.sidebar.title("Program Explorer")
page = st.sidebar.radio("View", ["Home", "Dashboard", "Map"])
program = st.sidebar.selectbox("Select Program:", ["HRSA", "RESET", "RTW"])

#looking into powerbi integration
# 1st assigning url to variable
rtw_url = "https://app.powerbi.com/onedrive/open?pbi_source=ODSPViewer&driveId=b!8Iv-TZJnbE-jQI9PDsBIVpbpL2rVgNFHgmSPuf_pk-E9UaqGd05wQIj4gvaYQ56G&itemId=01S32MYROROB7FVF5Z5NDJIQ77UZETJPMS"

if page == "Dashboard" and program == "RTW":
    st.title("RTW Dashboard")
    components.iframe(rtw_url, height=900, width=1600)
    

########################### later can store all urls for pwr bi as a dic
#powerbi_urls = {
   # "HRSA": "https://app.powerbi.com/view?r=longlinkHRSA...",
   # "RESET": "https://app.powerbi.com/view?r=longlinkRESET...",
    #"RTW": "https://app.powerbi.com/view?r=veryLongLinkRTW..."
#}

#if page == "Dashboard":
    #st.title(f"{program} Dashboard")
   # components.iframe(powerbi_urls[program], height=900, width=1600)





# HOME page landing
if page == "Home":

    # HRSA Page
    if program == "HRSA":
        st.title("HRSA")
        st.metric("Total Participants", 100)
        st.metric("Employed Participants", 20)

        st.subheader("About")
        st.write("meh meh")

    # RESET Page
    elif program == "RESET":
        st.title("RESET")
        st.metric("Total Participants", 200)
        st.metric("Employed Participants", 40)

        st.subheader("About")
        st.write("me me me")

    # RTW Page
    elif program == "RTW":
        st.metric("Total Participants", 401)
        st.metric("Employed Participants", 50)

        st.subheader("About")
        st.write("Ready to Work is San Antonio’s premier training, education, and employment program.​\n"  
        "Ready to Work will meet you where you are and take you to the next level with skills for higher-paying jobs.")





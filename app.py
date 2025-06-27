# HOME PAGE SETUP

# Imports
import streamlit as st
import pandas as pd
import plotly
import plotly.express as px
import json
import streamlit.components.v1 as components

# Page Setup
st.set_page_config(layout="wide")
# Page color etc

# Load external CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Program Explorer")
page = st.sidebar.radio("View", ["Home", "Dashboard", "Map"])
program = st.sidebar.selectbox("Select Program:", ["-- Select a Program --", "HRSA", "RESET", "RTW"])

# Landing Page
if program == "-- Select a Program --":
    # creating columns for pics
    col1, col2 = st.columns([1, 1])

    with col1:
        st.image(
            "https://images.squarespace-cdn.com/content/v1/654d110ae6bee3661f065bbd/a0f0fdba-f230-436e-9386-8ad375390c74/logo-orange_1_.png",
            width=150 
        )
    
    with col2:
        st.image(
            "https://sds.utsa.edu//community_scholars/images/cis-for-color-background.png",
            width=200
        )

    st.divider()

    # Title and Welcome
    st.title("YWCA & UTSA SDS Community Innovation Scholars Project")
    st.subheader("Welcome!")
    st.write(
        "Please select a workforce program from the sidebar to view participant insights, dashboards, and maps. "
        "You can explore each program's impact and reach in the San Antonio community."
    )
    st.divider()

# Program Content Pages
else:
    if page == "Home":
        st.title(f"{program} - Program Overview")

        if program == "HRSA":
            st.metric("Total Participants", 100)
            st.metric("Employed Participants", 20)
            st.subheader("About")
            st.write("meh meh")

        elif program == "RESET":
            st.metric("Total Participants", 200)
            st.metric("Employed Participants", 40)
            st.subheader("About")
            st.write("me me me")

        elif program == "RTW":
            st.metric("Total Participants", 401)
            st.metric("Employed Participants", 50)
            st.subheader("About")
            st.write("""
            Ready to Work is San Antonio’s premier training, education, and employment program.  
            Ready to Work will meet you where you are and take you to the next level with skills for higher-paying jobs.
            """)

    elif page == "Dashboard":
        st.title(f"{program} Dashboard")

        if program == "RTW":
            # looking into powerbi integration
            # 1st assigning url to variable
            rtw_url = "https://app.powerbi.com/view?r=eyJrIjoiN2U0MzU0OTQtZDAxNi00YzY4LWE2ZGUtM2ZkNzBiMjY2MDY0IiwidCI6IjNhMjI4ZGZiLWM2NDctNDRjYi04ODM1LTdiMjA2MTdmYzkwNiIsImMiOjN9"
            st.subheader("Interactive Power BI Dashboard")
            components.iframe(rtw_url, height=900, width=1600)
        else:
            st.info("WIP")

    elif page == "Map":
        st.title(f"{program} - ZIP Interactive")
        st.info("Map")

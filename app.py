###############################################################################
# HOME PAGE SETUP


# Imports
import streamlit as st
import pandas as pd
import plotly.express as px
import json
import streamlit.components.v1 as components

# Page configuration 
st.set_page_config(layout="wide")

# Sidebar navigation
st.sidebar.title("Program Explorer")
page = st.sidebar.radio("View", ["Home", "Dashboard", "Map"])

# Only show program selector when not on Home
if page != "Home":
    program = st.sidebar.selectbox(
        "Select Program:",
        ["-- Select a Program --", "HRSA", "RESET", "RTW"]
    )
else:
    program = None  # not needed on Home


# HOME  (landing page)

if page == "Home":
    # logos side-by-side
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(
            "https://images.squarespace-cdn.com/content/v1/654d110ae6bee3661f065bbd/"
            "a0f0fdba-f230-436e-9386-8ad375390c74/logo-orange_1_.png",
            width=150
        )
    with col2:
        st.image(
            "https://sds.utsa.edu//community_scholars/images/cis-for-color-background.png",
            width=210
        )

    st.divider()
    st.title("YWCA & UTSA SDS Community Innovation Scholars Project")
    st.subheader("Welcome!")
    st.write(
        "Please select a workforce program from the sidebar to view participant "
        "insights, dashboards, and maps. You can explore each program's impact "
        "and reach in the San Antonio community."
    )
    st.divider()

# DASHBOARD
###############################################################################

elif page == "Dashboard":
    st.title("Dashboard")

    if program == "-- Select a Program --":
        st.warning("Please select a program from the sidebar to view the dashboard.")
    else:
        st.title(f"{program} – Dashboard Overview")

        # Overview Ex
            st.metric("Total Participants", 100)
            st.metric("Employed Participants", 20)
            st.subheader("About HRSA")
            st.write("meh")

        elif program == "RESET":
            st.metric("Total Participants", 200)
            st.metric("Employed Participants", 40)
            st.subheader("About RESET")
            st.write("meh.")

        elif program == "RTW":
            st.metric("Total Participants", 401)
            st.metric("Employed Participants", 50)
            st.subheader("About Ready to Work ")
            st.write(
                "Ready to Work is San Antonio’s premier training, education, and "
                "employment program. It meets people where they are and helps "
                "them build skills for higher-paying jobs."
            )

            # Embed Power BI 
            rtw_url = (
                "https://app.powerbi.com/view?"
                "r=eyJrIjoiN2U0MzU0OTQtZDAxNi00YzY4LWE2ZGUtM2ZkNzBiMjY2MDY0IiwidCI6"
                "IjNhMjI4ZGZiLWM2NDctNDRjYi04ODM1LTdiMjA2MTdmYzkwNiIsImMiOjN9"
            )
            st.subheader("Interactive Power BI Dashboard")
            components.iframe(rtw_url, height=900, width=1600)
        # ----------------------------------------------------------------------


# MAP
###############################################################################

elif page == "Map":
    st.title("Map")

    if program == "-- Select a Program --":
        st.warning("Please select a program from the sidebar to view the map.")
    else:
        st.title(f"{program} – ZIP Interactive Map")
        st.info("WIP "")

# End



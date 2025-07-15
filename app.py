###############################################################################
# HOME PAGE SETUP
# Imports
import streamlit as st
import pandas as pd
import plotly.express as px
import json
import streamlit.components.v1 as components
from PIL import Image
# Imports and Function calls
from RTWpg import rtw_dashboard, rtw_map
from RESETpg import reset_dashboard, reset_map
from HRSApg import hrsa_dashboard, hrsa_map


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
    col1, col2 = st.columns([1, 1])

    with col1:
        st.image(
            "https://images.squarespace-cdn.com/content/v1/654d110ae6bee3661f065bbd/"
            "a0f0fdba-f230-436e-9386-8ad375390c74/logo-orange_1_.png",
            width=150
        )

    with col2:
        st.image(
            "https://raw.githubusercontent.com/gvg03/SDSCommunityInnovationScholarYWCASA/main/logo.png",
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
    if program == "-- Select a Program --" or program is None:
        st.warning("Please select a program from the sidebar to view the dashboard.")
    else:
        st.title(f"{program} Program Overview and {page}")

        # Calling separte dashboard imports from py files
        if program == "HRSA":
            hrsa_dashboard()
        elif program == "RESET":
            reset_dashboard()
        elif program == "RTW":
            rtw_dashboard()


# MAP
###############################################################################
elif page == "Map":
    st.title("San Antonio Community Reach Map")

    st.subheader("Interactive Worforce Program Map")
    
    # Embed your actual map here
    st.components.v1.iframe(
        "https://your-map-link.com",  # Replace with your actual map link
        height=600,
        width=1000
    )

    st.caption("This map illustrates the reach and coverage of workforce programs in the San Antonio area.")



# End



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

# Sidebar Navigation
st.sidebar.title("Program Explorer")
page = st.sidebar.radio("View", ["Home", "Dashboard", "Map"])

# Landing Page (Home - mainwelcome)
if page == "Home":
    # Creating columns for logos
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




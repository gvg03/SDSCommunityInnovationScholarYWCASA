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





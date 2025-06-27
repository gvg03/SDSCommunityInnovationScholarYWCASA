
#home age setup

# Imports
import streamlit as st # importing streamlit
import pandas as pd    # panda
import plotly
import plotly.express as px # for interactive zip code
import json            # to load file, for zipcode
import streamlit.components.v1 as components   # to bring in PowerBi

# Page Setup, layout and title
st.set_page_config(layout="wide")
st.title("YWCA & UTSA SDS Innovation Scholars")

# Sidebar: Navigate + Prog Filter
st.sidebar.title("Program Explorer")
page = st.sidebar.radio("View", ["Home", "Dashboard", "Map"])

program = st.sidebar.selectbox("Select Program:", ["HRSA", "RESET", "RTW"])

# HOME page landing
if page == "Home":
    st.title("YWCA & UTSA SDS Community Innovation Scholars")
 # HRSA PAge
    if program == "HRSA":
        st.metric("Total Participants", 100)
        st.metric("Employed Participants", 20)
     
    st.subheader("About the HRSA Program")
    st.write(
        "BIO BLANK."
    )

 # RESET Page
if program == "RESET":
    st.metric("Total Participants", 200)
    st.metric("Employed Participants", 40)
     
    st.subheader("About the HRSA Program")
    st.write(
        "BIO BLANK."
    )
 
 # RTW Page
if program == "RTW":
        st.metric("Total Participants", 401)
        st.metric("Employed Participants", 50)
     
    st.subheader("About the HRSA Program")
    st.write(
        "BIO BLANK."
    )



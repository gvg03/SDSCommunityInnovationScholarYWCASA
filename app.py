
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
 
program = st.selectbox("Select a Program:", ["HRSA", "RESET", "RTW"])

# placeholder to test
if program == "HRSA":
    st.metric("Total Participants", 111)
    st.metric("Employed Participants", 30)

elif program == "RESET":
    st.metric("Total Participants", 85)
    st.metric("Employed Participants", 40)

elif program == "RTW":
    st.metric("Total Participants", 401)
    st.metric("Employed Participants", 100)
 
program_type = st.sidebar.selectbox("Select a Program to View Summary Stats:", ["HRSA", "RESET", "RTW"])



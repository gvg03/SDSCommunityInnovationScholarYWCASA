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
from RTWpg import rtw_dashboard
from RESETpg import reset_dashboard
from HRSApg import chw_dashboard
from Statisticalpg import statistical_analysis_page
from COpg import co_page

# Page configuration 
st.set_page_config(layout="wide")

# Sidebar navigation
st.sidebar.title("Program Explorer")
page = st.sidebar.radio("View", ["Home", "Dashboard", "Co-Enrolled", "Map", "About Statistical Analysis"])

# Only show program selector when not on Home
if page == "Dashboard":
    program = st.sidebar.selectbox(
        "Select Program:",
        ["-- Select a Program --", "CHW", "RESET", "RTW"]
    )
else:
    program = None  # not needed on Home

# HOME  (landing page)
if page == "Home":
    col1, col2 = st.columns([.2, .2])


    st.divider()
    st.subheader("YWCA & UTSA SDS Community Innovation Scholars Project")
    st.subheader("Welcome!")
    st.write(
        "Use the sidebar to explore participant insights across workforce programs. "
        "View dashboards, learn about co-enrollment, explore our San Antonio community map, and dive into the statistical analysis behind the data. "
    )

    st.divider()

# DASHBOARD
###############################################################################
# DASHBOARD
###############################################################################
elif page == "Dashboard":
    if program == "-- Select a Program --" or program is None:
        st.warning("Please select a program from the sidebar to view the dashboard.")
        st.markdown("""
        <p style='font-size: 0.85rem; color: #444;'> Note: (*) Indicates a statistically significant relationship based on Chi-Square analysis.</p>
        """, unsafe_allow_html=True)
    else:
        st.title(f"{program} {page}")

        # Calling separate dashboard imports from py files
        if program == "CHW":
            chw_dashboard()
        elif program == "RESET":
            reset_dashboard()
        elif program == "RTW":
            rtw_dashboard()

### CO_ENROLLED
#################################
elif page == "Co-Enrolled":
        co_page()


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

# STATISTICAL ANALYSIS PAGE
###############################################################################
elif page == "About Statistical Analysis":
    statistical_analysis_page()


# End



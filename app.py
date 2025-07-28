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


st.sidebar.header("Navigation")
page = st.sidebar.radio("Select a Page:", ["Home", "Program Dashboards", "Co-Enrolled Dashboard", "Map"])

st.sidebar.markdown("---")
st.sidebar.markdown("### Learn More")
if st.sidebar.checkbox("About Statistical Analysis"):
    page = "About Statistical Analysis"

#logo on sidebar
# Spacer to push logo down
st.sidebar.markdown(
    """
    <div style="height: 150px;"></div>
    """,
    unsafe_allow_html=True
)

# Logo at the bottom
st.sidebar.markdown(
    """
    <div style="text-align: center;">
        <img src="https://github.com/gvg03/SDSCommunityInnovationScholarYWCASA/blob/main/ywca_side_header%201%20(2).png?raw=true" width="200">
    </div>
    """,
    unsafe_allow_html=True
)

# Only show program selector when not on Home
if page == "Program Dashboards":
    program = st.sidebar.selectbox(
        "Select Program:",
        ["-- Select a Program --", "Community Health Worker", "RESET", "Ready To Work"]
    )
else:
    program = None  # not needed on Home

# HOME  (landing page)
if page == "Home":

    # Header image (collage maybe)
    st.image(
        "https://github.com/gvg03/SDSCommunityInnovationScholarYWCASA/blob/main/Slide%2016_9%20-%201%20(6).png?raw=true",
        use_container_width=True
    )


    # intro content
    st.divider()

    #columns for the subheader and logo side-by-side
    col1, col2 = st.columns([1.50, 1])

    with col1:
        st.markdown(
            """
            <h3>
                <a href="https://provost.utsa.edu/ai-cyber-computing/" style="text-decoration:none; color:black;">
                    HEB Community Innovation Scholars Program with YWCA
            </a>
        </h3>
        """,
        unsafe_allow_html=True
    )

    with col2:
        st.image(
            "https://github.com/gvg03/SDSCommunityInnovationScholarYWCASA/blob/main/Large_CIS_UW_Combined_logo%201.png?raw=true",
            width=400
        )

    st.subheader("Welcome!")

    st.write(
        "Use the sidebar to explore participant insights across workforce programs. "
        "View interactive dashboards, learn about co-enrollment across programs, explore the San Antonio community map, and dive into the statistical analysis behind the data."
    )

    st.markdown("---") 
    
    st.markdown(
    "<p style='font-size: 0.9rem;'>Created by Avery Tovar, Gabriella Gomez, and Kayla Duran</p>",
    unsafe_allow_html=True
    )



# DASHBOARD
###############################################################################
# DASHBOARD
###############################################################################
elif page == "Program Dashboards":
    if program == "-- Select a Program --" or program is None:
        st.warning("Please select a program from the sidebar to view the dashboard.")
        st.markdown("""
        <p style='font-size: 0.85rem; color: #444;'> Note: (*) Indicates a statistically significant relationship based on Chi-Square analysis.</p>
        """, unsafe_allow_html=True)
    else:
        st.title(f"{program} {page}")

        # Calling separate dashboard imports from py files
        if program == "Community Health Worker":
            chw_dashboard()
        elif program == "RESET":
            reset_dashboard()
        elif program == "Ready To Work":
            rtw_dashboard()

### CO_ENROLLED
#################################
elif page == "Co-Enrolled Dashboard":
    st.title("Co-Enrolled Dashboard")
    
    # Embed
    st.components.v1.iframe(
        "https://app.powerbi.com/view?r=eyJrIjoiOTQ4YjZiNWUtNTlhYi00MjMzLTk2YjUtZTk4ZDBjMzQ4YTBlIiwidCI6IjNhMjI4ZGZiLWM2NDctNDRjYi04ODM1LTdiMjA2MTdmYzkwNiIsImMiOjN9",  # Replace with your actual map link
        height=600,
        width=1000
    )



# MAP
###############################################################################
elif page == "Map":
    st.title("YWCA Workforce Programs Reach Map")
    st.write(" ")
    # Embed your actual map here
    st.components.v1.iframe(
        "https://app.powerbi.com/view?r=eyJrIjoiNGE1ODAxYmEtZjI1YS00NzFhLThlYjktODVjMTcyMTBkZGU1IiwidCI6IjNhMjI4ZGZiLWM2NDctNDRjYi04ODM1LTdiMjA2MTdmYzkwNiIsImMiOjN9",  # Replace with your actual map link
        height=600,
        width=1000
    )

    st.caption("This map illustrates the reach and coverage of workforce programs in the San Antonio area.")

# STATISTICAL ANALYSIS PAGE
###############################################################################
elif page == "About Statistical Analysis":
    statistical_analysis_page()


# End



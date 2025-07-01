#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 18:11:07 2025

@author: gabriellagomez
"""

import streamlit as st
import streamlit.components.v1 as components

def rtw_dashboard():
    st.metric("Total Participants", 401)
    st.metric("Employed Participants", 105)
    st.subheader("About Ready to Work")
    st.write(
        "Ready to Work is San Antonio’s premier training, education, and "
        "employment program. It meets people where they are and helps "
        "them build skills for higher-paying jobs."
    )

    rtw_url = "blank"
    st.subheader("Power BI Dashboard")
    components.iframe(rtw_url, height=900, width=1600)

import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os

def rtw_map():
    st.subheader("Participant Distribution by ZIP Code")

    # Load data
    df = pd.read_csv("data/zip_summary_rtw.csv")  # <- adjust this to your RTW CSV

    # Load geojson
    with open("data/tx_texas_zip_codes_geo.min.json") as f:
        zip_geojson = json.load(f)

    # Create map
    fig = px.choropleth(
        df,
        geojson=zip_geojson,
        locations="Zip Code",
        featureidkey="properties.ZCTA5CE10",
        color="total_participants",
        color_continuous_scale="Oranges",
        hover_data=["employed_participants"]
    )

    # Layout adjustments
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(
        margin={"r":0,"t":0,"l":0,"b":0},
        height=700
    )

    st.plotly_chart(fig, use_container_width=True)



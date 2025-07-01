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

    rtw_url = "https://app.powerbigov.us/view?r=eyJrIjoiYzlkMTYxMTctNTk5My00MWViLThmMWEtZmY2MWUwOTg4ZDk0IiwidCI6IjFhYjAyMTRmLWFjNGEtNDQwNy1hN2M2LTJlZjFlYjc2ZGFjNSJ9"
    st.subheader("Power BI Dashboard")
    components.iframe(rtw_url, height=900, width=1600)


def rtw_map():
    st.subheader("Participant Distribution by ZIP Code")
    

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 18:00:26 2025

@author: gabriellagomez
"""

import streamlit as st
import streamlit.components.v1 as components

def hrsa_dashboard():
    st.metric("Total Participants", 214)
    st.subheader("About HRSA")
    st.write(
        " meh"
    )

    hrsa_url = ""
    st.subheader("Power BI Dashboard")
    components.iframe(hrsa_url, height=900, width=1600)

def hrsa_map():
    st.subheader("Participant Distribution by ZIP Code")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 18:05:11 2025

@author: gabriellagomez
"""

import streamlit as st
import streamlit.components.v1 as components

def reset_dashboard():
    st.metric("Total Participants", 60)
    st.metric("Employed Participants", 70)
    st.subheader("About Ready to Work")
    st.write(
        ""
    )

    reset_url = ""
    st.subheader("Interactive Power BI Dashboard")
    components.iframe(rtw_url, height=900, width=1600)

def reset_map():
    st.subheader("Participant Distribution by ZIP Code")

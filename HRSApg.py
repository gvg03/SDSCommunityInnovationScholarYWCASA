#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 18:00:26 2025

@author: gabriellagomez
"""

import streamlit as st
import streamlit.components.v1 as components

def chw_dashboard():
    st.metric("Total Participants", 214)
    st.subheader("About CHW")
    st.write(
        " meh"
    )
    st.markdown("""
    <span style='font-size: 0.85rem; color: #444;'>\(*) Indicates a statistically significant relationship based on Chi-Square analysis.</span>
    """, unsafe_allow_html=True)

    hrsa_url = ""
    components.iframe(hrsa_url, height=900, width=1600)


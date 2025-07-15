#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 18:05:11 2025

@author: gabriellagomez
"""

import streamlit as st
import streamlit.components.v1 as components

def reset_dashboard():
    st.metric("Total Participants", 175)
    st.subheader("About RESET")
    st.write(
        ""
    )
    st.markdown("""
    <span style='font-size: 0.85rem; color: #444;'>\(*) Indicates a statistically significant relationship based on Chi-Square analysis.</span>
    """, unsafe_allow_html=True)
    
    reset_url = ""
    components.iframe(reset_url, height=900, width=1600)



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
    st.subheader("About Ready to Work")
    st.write(
        "Ready to Work is San Antonio’s premier training, education, and "
        "employment program. It meets people where they are and helps "
        "them build skills for higher-paying jobs."
    )

    st.markdown("""
    <span style='font-size: 0.85rem; color: #444;'>\(*) Indicates a statistically significant relationship based on Chi-Square analysis.</span>
    """, unsafe_allow_html=True)
    
    #power bi link embed 
    rtw_url = "https://app.powerbi.com/view?r=eyJrIjoiNjk1Y2ZlYTctZmIyYy00Y2NhLThiNjQtMmZiYWM0MzU0OWIxIiwidCI6IjNhMjI4ZGZiLWM2NDctNDRjYi04ODM1LTdiMjA2MTdmYzkwNiIsImMiOjN9"
    components.iframe(rtw_url, height=900, width=1600)

    

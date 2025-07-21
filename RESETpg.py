#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 18:05:11 2025

@author: gabriellagomez
"""

import streamlit as st
import streamlit.components.v1 as components

def reset_dashboard():
    st.metric("Total Participants", 182)
    st.subheader("About RESET")
    st.write(
        "RESET is designed for young women ages 16-24 who are not currently in school or working. The program supports their journey toward becoming financially, emotionally, and socially secure adults through trauma-informed case management focused on building positive connections. Through RESET, women are reengaged in education or employment by offering educational coaching and essential work readiness skills. Participants also gain access to financial literacy sessions, a women's support group, direct referrals to resources like childcare, job training, transportation, as well as life skills development in areas such as communication, self-confidence, and healthy boundaries. Enrichment opportunities, including college tours and guest speakers, are also provided to help young women successfully reconnect with their communities and move forward with confidence. "
    )
    st.markdown("""
    <span style='font-size: 0.85rem; color: #444;'>\(*) Indicates a statistically significant relationship based on Chi-Square analysis.</span>
    """, unsafe_allow_html=True)
    
    reset_url = "https://app.powerbi.com/view?r=eyJrIjoiZWM2ODNlZTgtZmE2OC00Yjg1LTg4ZGYtMzE4ZTBkMWYyMzNjIiwidCI6IjNhMjI4ZGZiLWM2NDctNDRjYi04ODM1LTdiMjA2MTdmYzkwNiIsImMiOjN9" frameborder="0" allowFullScreen="true"></iframe>"
    components.iframe(reset_url, height=900, width=1600)



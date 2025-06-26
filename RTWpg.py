#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 18:11:07 2025

@author: gabriellagomez
"""

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.title("Dashboard for RTW")

components.iframe("https://app.powerbi.com/onedrive/open?pbi_source=ODSPViewer&driveId=b!8Iv-TZJnbE-jQI9PDsBIVpbpL2rVgNFHgmSPuf_pk-E9UaqGd05wQIj4gvaYQ56G&itemId=01S32MYROROB7FVF5Z5NDJIQ77UZETJPMS", height=800, width=1200)

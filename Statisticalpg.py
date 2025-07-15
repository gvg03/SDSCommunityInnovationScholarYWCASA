
import streamlit as st

def statistical_analysis_page():
    st.title("Statistical Analysis: Chi-Squared")
    st.subheader("What is Chi-Squared?")

    st.markdown("""
    The Chi-Square Test is used to determine whether there is a **statistically significant relationship** between two categorical variables.

    In the context of this project, we use the Chi-Square test to explore whether **demographic variables** such as **age group, race, gender, or education level** are associated with **success metrics** like:
    - Program Completion
    - Job Placement
    - Earning a wage of $15/hour or more

    By analyzing the relationship between demographics and outcomes, we can better understand potential disparities or patterns that can inform how programs are delivered and supported.
    """)
    st.divider()


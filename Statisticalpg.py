
import streamlit as st

def statistical_analysis_page():
    st.title("Statistical Analysis: Chi-Squared")
    st.subheader("What is Chi-Squared?")
    
    st.markdown("""
    The **Chi-Square Test of Independence** is used to determine whether there is a **statistically significant association** between two categorical variables.

    In this project, we use the Chi-Square test to explore whether **demographic factors** — such as **age group, race, gender, or education level** — are associated with program success outcomes like:
    - **Program Completion**
    - **Job Placement**
    - **Earning a wage of $15/hour or more**

    ---

    ### Interpreting the Results:
    - A **statistically significant result** (typically *p* < 0.05) suggests there is a relationship between the two variables being tested.
    - A **non-significant result** does **not** necessarily mean there is *no relationship* — it may indicate:
    - A small sample size
    - Not enough variation in the data
    - Or that the relationship just isn't strong enough to be detected statistically

    It's important to consider **both statistical significance and real-world context**. Even if a result isn't statistically significant, it may still be **practically important** or **highlight areas worth exploring further**.
    """)

st.divider()


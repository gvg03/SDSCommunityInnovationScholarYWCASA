
import streamlit as st

def statistical_analysis_page():
    st.title("Statistical Analysis: Chi-Squared")
    st.subheader("What is Chi-Squared?")
    
    st.markdown("""
    The **Chi-Square Test of Independence** is used to determine whether there is a **statistically significant association** between two categorical variables.

    In this project, we use the Chi-Square test to explore whether **demographic factors** — such as **Age, Race, Ethnicity, Gender, Highest Education Level, or Employment Status at Intake** — are associated with program success outcomes like:
    - **Program Completion**
    - **Job Placement**
    - **Earning a wage of $15/hour or more**
    """)

    st.markdown("""
    <span style='font-size: 0.85rem; color: #444;'>In the dashboards, you may see an asterisk (*) next to certain categories. This means the relationship between that demographic and the outcome is statistically significant based on our Chi-Square test. In other words, there is a association between the demographic factor and the success outcome.</span>
    """, unsafe_allow_html=True)

    st.divider()

    st.subheader("How to Interpret the Results")

    st.markdown("""
    The Chi-Square test helps us see if there might be a meaningful connection between two categories — like a participant’s age and whether they completed the program.

    - If the test shows a **statistically significant** result, it means the connection is unlikely to be due to chance.
    - If the test is **not significant**, we can’t say for sure there’s a strong connection based on the data.

    But remember, just because something isn’t statistically significant doesn’t mean it’s unimportant. 
    """)

    st.markdown("""
    A **non-significant result** does **not** necessarily mean there is *no relationship* — it may be due to:
      - A small sample size
      - Weak of subtle association between categorical variables
      - Not enough data to meet all requirements of the test
      
      Even without statistical significance, the findings may still be practically important or highlight areas worth exploring further in real-world settings.
    """)

    

 

    with st.expander("Want to learn more about how statistical significance works?"):
        st.markdown("""
        In statistics, **'statistically significant'** usually means the result is unlikely to be due to random chance — often if the probability (called the *p-value*) is less than 5% (or 0.05).

        This threshold is just a common guideline to help decide if a pattern is real or could happen by accident. However, it’s not a hard rule — sometimes meaningful things don’t show up as statistically significant, especially with small datasets.

        Consider statistical tests as one part of the bigger picture, best used alongside practical experience and real-world understanding.
        """)



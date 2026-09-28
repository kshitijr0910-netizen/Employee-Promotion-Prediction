
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("emp_promotion_pred.joblib")

st.set_page_config(
    page_title="Employee Promotion Prediction",
    page_icon="📊"
)

st.title("Employee Promotion Prediction")

education_level = st.selectbox(
    "Education Level",
    ["Bachelor", "Master", "PhD"]
)

department = st.selectbox(
    "Department",
    ["Finance", "Sales", "Engineering", "Operations", "HR", "Marketing"]
)

years_at_company = st.number_input("Years at Company", min_value=0.0)
years_in_current_role = st.number_input("Years in Current Role", min_value=0.0)
salary = st.number_input("Salary", min_value=0.0)
salary_increase_percent = st.number_input("Salary Increase (%)", min_value=0.0)
bonus_last_year = st.number_input("Bonus Last Year", min_value=0.0)
stock_options = st.number_input("Stock Options", min_value=0.0)

attendance_rate = st.number_input(
    "Attendance Rate",
    min_value=0.0,
    max_value=1.0,
    value=0.9
)

employee_engagement_score = st.number_input(
    "Employee Engagement Score",
    min_value=0.0,
    max_value=100.0
)

job_satisfaction_score = st.number_input(
    "Job Satisfaction Score",
    min_value=0.0,
    max_value=100.0
)

internal_mobility_score = st.number_input(
    "Internal Mobility Score",
    min_value=0.0,
    max_value=100.0
)

if st.button("Predict Promotion"):

    data = pd.DataFrame([{
        "years_at_company": years_at_company,
        "years_in_current_role": years_in_current_role,
        "salary": salary,
        "salary_increase_percent": salary_increase_percent,
        "bonus_last_year": bonus_last_year,
        "stock_options": stock_options,
        "attendance_rate": attendance_rate,
        "employee_engagement_score": employee_engagement_score,
        "job_satisfaction_score": job_satisfaction_score,
        "internal_mobility_score": internal_mobility_score,
        "education_level": education_level,
        "department": department
    }])

    prediction = model.predict(data)[0]

    if prediction == 1:
        st.success("Employee is likely to be PROMOTED")
    else:
        st.error("Employee is unlikely to be PROMOTED")

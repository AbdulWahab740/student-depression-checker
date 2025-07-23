import streamlit as st
import numpy as np
import pickle
import math

# Load model
with open('student_depression_model.pkl', 'rb') as file:
    model = pickle.load(file)
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
st.title("Student Mental Health Risk Prediction")

st.markdown("### Input the following student data:")

# Input fields
academic_pressure = st.slider("Academic Pressure (1 - 10)", 1, 10, 5)
study_satisfaction = st.slider("Study Satisfaction (1 - 10)", 1, 10, 5)
sleep_duration = st.number_input("Sleep Duration (hours/day)", min_value=0.0, max_value=24.0, value=7.0)
dietary_habits = st.slider("Dietary Habits (1 - 10)", 1, 10, 5)
suicidal_thoughts = st.selectbox("Have you ever had suicidal thoughts?", ["No", "Yes"])
work_study_hours = st.number_input("Work/Study Hours (hours/day)", min_value=0.0, max_value=24.0, value=5.0)
financial_stress = st.slider("Financial Stress (1 - 10)", 1, 10, 5)
cgpa = st.number_input("CGPA (e.g., 5.0, 6.78, 7.36)/10.0", min_value=0.1, max_value=10.0, value=6.0)

# Convert inputs
suicidal_thoughts_val = 1 if suicidal_thoughts == "Yes" else 0
cgpa_log = math.log(cgpa)

# Prediction
if st.button("Predict"):
    input_data = np.array([[academic_pressure, study_satisfaction, sleep_duration,
                            dietary_habits, suicidal_thoughts_val, work_study_hours,
                            financial_stress, cgpa_log]])
    input_scale = scaler.transform(input_data)

    prediction = model.predict(input_scale)[0]

    if prediction == 1:
        st.error("⚠️ High Risk Detected: Please seek help or talk to someone you trust.")
    else:
        st.success("✅ No Risk Detected: Keep up the healthy habits!")

import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model and label encoders
model = joblib.load('model-3.pkl')
label_encoders = joblib.load('label_encoders-2.pkl')

st.set_page_config(page_title="🎯 Student Score Predictor", layout="centered")

# UI Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Student Exam Score Predictor 🎓</h1>", unsafe_allow_html=True)
st.write("### Fill the details below to predict the expected exam score:")

# Input Features
features = {
    'gender': st.selectbox("Gender", ["male", "female"]),
    'parental level of education': st.selectbox("Parental Level of Education", [
        "some high school", "high school", "some college", "associate's degree", "bachelor's degree", "master's degree"]),
    'lunch': st.selectbox("Lunch Type", ["standard", "free/reduced"]),
    'test preparation course': st.selectbox("Test Preparation", ["none", "completed"]),
    'study hours per week': st.slider("Study Hours Per Week", 0, 50, 10),
    'previous exam score': st.slider("Previous Exam Score (%)", 0, 100, 70),
    'attendance rate': st.slider("Attendance Rate (%)", 0, 100, 90),
    'internet access': st.selectbox("Internet Access at Home", ["yes", "no"]),
    'school support': st.selectbox("School Support Program", ["yes", "no"]),
    'health status': st.slider("Health Status (1=Poor, 5=Excellent)", 1, 5, 3)
}

# Convert input to dataframe
input_df = pd.DataFrame([features])

# Encode categorical columns
for col in label_encoders:
    if col in input_df.columns:
        le = label_encoders[col]
        input_df[col] = le.transform(input_df[col])

# Predict
if st.button("Predict Score"):
    prediction = model.predict(input_df)[0]
    st.success(f"🎯 Predicted Exam Score: **{prediction:.2f}%**")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>SARTHAK KA AAVISHKAR 😎</h4>", unsafe_allow_html=True)

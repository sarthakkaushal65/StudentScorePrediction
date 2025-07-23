import streamlit as st
import pandas as pd
import numpy as np
import joblib

# 📦 Load trained model and encoders
model = joblib.load("model-3.pkl")
label_encoders = joblib.load("label_encoders-2.pkl")

# 🎯 Define feature names used in training
feature_names = [
    'Hours_Studied',
    'Attendance',
    'Parental_Involvement',
    'Access_to_Resources',
    'Extracurricular_Activities',
    'Sleep_Hours',
    'Previous_Scores',
    'Motivation_Level',
    'Internet_Access',
    'Tutoring_Sessions',
    'Family_Income',
    'Teacher_Quality',
    'School_Type',
    'Peer_Influence',
    'Physical_Activity',
    'Learning_Disabilities',
    'Parental_Education_Level',
    'Distance_from_Home',
    'Gender'
]

# 🌟 Streamlit App UI
st.set_page_config(page_title="Student Score Predictor", layout="wide")

st.markdown("<h1 style='text-align: center; color: darkblue;'>Student Exam Score Prediction 🎓📊</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>SARTHAK KA AAVISHKAR 😎</h4>", unsafe_allow_html=True)
st.write("---")

# 📥 User Inputs
user_input = {}

cols = st.columns(3)
for i, feature in enumerate(feature_names):
    with cols[i % 3]:
        if feature in label_encoders:  # Use selectbox for categorical features
            options = label_encoders[feature].classes_.tolist()
            user_input[feature] = st.selectbox(f"{feature.replace('_', ' ')}", options)
        else:
            user_input[feature] = st.number_input(f"{feature.replace('_', ' ')}", min_value=0.0, format="%.2f")

# 📊 Predict
if st.button("Predict Exam Score"):
    # Encode categorical inputs
    input_df = pd.DataFrame([user_input])
    for col in input_df.columns:
        if col in label_encoders:
            le = label_encoders[col]
            input_df[col] = le.transform(input_df[col])

    # 🧠 Predict using trained model
    prediction = model.predict(input_df)[0]
    st.success(f"📈 Predicted Exam Score: **{prediction:.2f}**")

# 📌 Footer
st.markdown("---")
st.markdown("<div style='text-align: center;'>© 2025 Sarthak Kaushal</div>", unsafe_allow_html=True)

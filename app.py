import streamlit as st
import pandas as pd
import numpy as np
import joblib
import base64

# 📦 Load model and encoders
model = joblib.load("model-3.pkl")
label_encoders = joblib.load("label_encoders-2.pkl")

# 🎯 Features used in training
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

# 🔳 Add background image using base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# 🖼 Set the uploaded image as background
add_bg_from_local("study_background.jpg")

# 🌟 UI Setup
st.set_page_config(page_title="Student Score Predictor", layout="wide")

st.markdown("<h1 style='text-align: center; color: white;'>Student Exam Score Prediction 🎓📊</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: lightgray;'>SARTHAK KA AAVISHKAR 😎</h4>", unsafe_allow_html=True)
st.write("---")

# 📥 User Inputs
user_input = {}
cols = st.columns(3)
for i, feature in enumerate(feature_names):
    with cols[i % 3]:
        if feature in label_encoders:
            options = label_encoders[feature].classes_.tolist()
            user_input[feature] = st.selectbox(f"{feature.replace('_', ' ')}", options)
        else:
            user_input[feature] = st.number_input(f"{feature.replace('_', ' ')}", min_value=0.0, format="%.2f")

# 🔍 Prediction
if st.button("Predict Exam Score"):
    input_df = pd.DataFrame([user_input])
    for col in input_df.columns:
        if col in label_encoders:
            le = label_encoders[col]
            input_df[col] = le.transform(input_df[col])
    prediction = model.predict(input_df)[0]
    st.success(f"📈 Predicted Exam Score: **{prediction:.2f}**")

# 📌 Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: white;'>© 2025 Sarthak Kaushal</div>", unsafe_allow_html=True)

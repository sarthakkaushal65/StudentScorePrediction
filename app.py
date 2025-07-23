# 📦 Imports
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image
import base64

# ✅ Set Streamlit page config FIRST
st.set_page_config(
    page_title="Student Score Predictor",
    layout="centered",
    page_icon="📚"
)

# ✅ Function to set background image
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ✅ Apply background
set_background("study_background.jpg")

# ✅ Load model and encoders
model = joblib.load("model.pkl")
encoders = joblib.load("label_encoders.pkl")

# ✅ Input form title
st.title("🎯 Predict Student Exam Score")
st.subheader("Enter the details below 👇")

# ✅ Input fields — match features used in training
gender = st.selectbox("Gender", ["Male", "Female"])
lunch = st.selectbox("Lunch Type", ["Standard", "Free/Reduced"])
test_prep = st.selectbox("Test Preparation", ["Completed", "None"])
parent_edu = st.selectbox("Parental Education Level", [
    "High School", "Some College", "Associate's Degree",
    "Bachelor's Degree", "Master's Degree"
])
study_hours = st.slider("Daily Study Hours", 0, 12, 4)
attendance = st.slider("Attendance (%)", 0, 100, 75)
previous_score = st.slider("Previous Exam Score", 0, 100, 60)

# ✅ Submit button
if st.button("🔍 Predict Score"):
    # Create input DataFrame
    input_data = pd.DataFrame({
        "gender": [gender],
        "lunch": [lunch],
        "test_prep_course": [test_prep],
        "parental_level_of_education": [parent_edu],
        "daily_study_hours": [study_hours],
        "attendance": [attendance],
        "previous_scores": [previous_score]
    })

    # Apply label encoders to categorical columns
    for col in ["gender", "lunch", "test_prep_course", "parental_level_of_education"]:
        le = encoders[col]
        input_data[col] = le.transform(input_data[col])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # 🎉 Display result
    st.success(f"📘 **Predicted Exam Score:** {prediction:.2f} / 100")

# ✅ Footer
st.markdown("<br><br><h4 style='text-align: center;'>SARTHAK KA AAVISHKAR 😎</h4>", unsafe_allow_html=True)

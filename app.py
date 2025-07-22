import streamlit as st
import joblib
import numpy as np
import pandas as pd
import base64

# ✅ Set page config first
st.set_page_config(page_title="🎓 Student Exam Score Predictor", layout="centered")

# 📸 Set background image from local file
def set_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded_img = base64.b64encode(f.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_img}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# 🌄 Apply background image
set_bg_from_local("study_background.jpg")  # Ensure this file is in the same folder

# 🧠 Load trained model
model = joblib.load('student_score_predictor-2.pkl')

# 📌 Title and Description
st.title("📚 Student Exam Score Predictor")
st.markdown("Use this machine learning-powered app to predict a student's exam score based on study habits and lifestyle!")

# 📋 Sidebar for Inputs
st.sidebar.header("📝 Enter Student Details")

hours_studied = st.sidebar.slider("📖 Hours Studied", 0.0, 12.0, 4.0, 0.5)
previous_exam_score = st.sidebar.slider("📊 Previous Exam Score", 0, 100, 75)
attendance = st.sidebar.slider("🏫 Attendance (%)", 0, 100, 85)
assignments_completed = st.sidebar.slider("📂 Assignments Completed (%)", 0, 100, 80)
average_sleep_hours = st.sidebar.slider("😴 Average Sleep Hours", 0.0, 12.0, 7.0, 0.5)

study_environment = st.sidebar.selectbox("📚 Study Environment", ['Quiet', 'Moderate', 'Noisy'])
internet_access = st.sidebar.selectbox("🌐 Internet Access", ['Yes', 'No'])
parental_support = st.sidebar.selectbox("👨‍👩‍👦 Parental Support", ['Yes', 'No'])
extracurricular_involvement = st.sidebar.selectbox("🎨 Extracurricular Involvement", ['Yes', 'No'])

# 🚀 Predict Button
if st.sidebar.button("🎯 Predict Score"):
    input_df = pd.DataFrame({
        'hours_studied': [hours_studied],
        'previous_exam_score': [previous_exam_score],
        'attendance': [attendance],
        'assignments_completed': [assignments_completed],
        'average_sleep_hours': [average_sleep_hours],
        'study_environment': [study_environment],
        'internet_access': [internet_access],
        'parental_support': [parental_support],
        'extracurricular_involvement': [extracurricular_involvement]
    })

    prediction = model.predict(input_df)[0]
    st.success(f"✅ Predicted Exam Score: **{prediction:.2f}**")

# ✨ Footer
st.markdown("---")
st.markdown("<center><h4>Sarthak ka Aavishkar 💡</h4></center>", unsafe_allow_html=True)

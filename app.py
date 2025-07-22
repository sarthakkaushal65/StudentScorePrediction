import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("student_score_predictor.pkl")

# App title
st.title("Student Exam Score Predictor")

# Input sliders
hours = st.slider("Study Hours per Day", 0, 15, 5)
previous_score = st.slider("Previous Exam Score (%)", 0, 100, 70)
attendance = st.slider("Attendance (%)", 0, 100, 80)

# Predict button
if st.button("Predict Score"):
    input_data = pd.DataFrame({
        "Hours": [hours],
        "PreviousScore": [previous_score],
        "Attendance": [attendance]
    })

    prediction = model.predict(input_data)[0]

    st.subheader("Predicted Exam Score:")
    st.write(f"🎯 {prediction:.2f}%")

    st.markdown("---")
    st.write("Input Summary:")
    st.write(input_data)

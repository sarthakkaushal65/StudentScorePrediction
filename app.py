import streamlit as st
import pandas as pd
import joblib
from PIL import Image

# 🎨 Page Config
st.set_page_config(page_title="Student Score Predictor", layout="centered")

# 🖼 Background Image
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("study_background.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# 🧠 Load the trained model
model = joblib.load("student_score_predictor.pkl")

# 🎓 Title
st.markdown(
    "<h1 style='text-align: center; color: white;'>Student Exam Score Predictor 📚</h1>",
    unsafe_allow_html=True
)

# 🌟 Signature (centered, no animation)
st.markdown(
    "<h4 style='text-align: center; color: yellow;'>SARTHAK KA AAVISHKAR 😎</h4>",
    unsafe_allow_html=True
)

# 📊 Input Form
st.sidebar.header("Enter Student Details")
hours = st.sidebar.slider("Study Hours per Day", 0, 15, 5)
previous_score = st.sidebar.slider("Previous Exam Score (%)", 0, 100, 70)
attendance = st.sidebar.slider("Attendance (%)", 0, 100, 80)

# 🧮 Prediction Button
if st.sidebar.button("Predict Score"):
    input_data = pd.DataFrame(
        {"Hours": [hours], "PreviousScore": [previous_score], "Attendance": [attendance]}
    )
    prediction = model.predict(input_data)[0]

    st.success(f"📈 Predicted Exam Score: **{prediction:.2f}%**")

    # 📝 Display input summary
    st.markdown("### 📋 Student Info")
    st.write(input_data)

    # 🎯 Show status
    if prediction >= 90:
        st.balloons()
        st.success("Excellent! 🚀")
    elif prediction >= 75:
        st.info("Good job! Keep going! 💪")
    elif prediction >= 50:
        st.warning("Needs Improvement 📚")
    else:
        st.error("At Risk ⚠️ Needs Support")

# 📌 Footer
st.markdown(
    "<hr><center>Made with ❤️ using Streamlit</center>",
    unsafe_allow_html=True
)

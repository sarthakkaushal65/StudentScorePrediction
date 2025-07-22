import streamlit as st
import pandas as pd
import numpy as np
import joblib
import base64

# ✅ Load model with error handling
print("✅ Starting app")
try:
    model = joblib.load("student_score_predictor.pkl")
    print("✅ Model loaded successfully")
except Exception as e:
    st.error(f"❌ Model load failed: {e}")
    print(f"❌ Model load failed: {e}")

# ✅ Load background image and apply
try:
    with open("study_background.jpg", "rb") as img_file:
        bg_data = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{bg_data}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    print("✅ Background image applied")
except Exception as e:
    st.error(f"❌ Background image failed: {e}")
    print(f"❌ Background image failed: {e}")

# ✅ Glowing floating center text
st.markdown(
    """
    <style>
    .glow {
        font-size: 36px;
        font-weight: bold;
        color: #fff;
        text-align: center;
        animation: float 3s ease-in-out infinite;
        text-shadow: 0 0 10px #f0f, 0 0 20px #f0f, 0 0 30px #0ff;
        margin-top: 20px;
    }

    @keyframes float {
        0%   { transform: translateY(0); }
        50%  { transform: translateY(-10px); }
        100% { transform: translateY(0); }
    }
    </style>
    <div class="glow">Sarthak Ka Aavishkar 😎</div>
    """,
    unsafe_allow_html=True
)

# ✅ App Title
st.title("🎓 Student Exam Score Predictor")

# ✅ Input Form
with st.form("prediction_form"):
    st.subheader("📥 Enter Student Details:")
    hours_studied = st.number_input("Hours Studied", min_value=0.0, step=0.5)
    previous_score = st.number_input("Previous Exam Score", min_value=0.0, max_value=100.0, step=1.0)
    attendance = st.slider("Attendance (%)", min_value=0, max_value=100, step=1)
    submit = st.form_submit_button("Predict Score 🎯")

# ✅ Make Prediction
if submit:
    try:
        input_df = pd.DataFrame([[hours_studied, previous_score, attendance]],
                                columns=["Hours Studied", "Previous Score", "Attendance"])
        prediction = model.predict(input_df)[0]
        st.success(f"✅ Predicted Exam Score: **{prediction:.2f}**")
        print("✅ Prediction successful")
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")
        print(f"❌ Prediction failed: {e}")

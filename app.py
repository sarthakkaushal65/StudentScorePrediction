import streamlit as st
import pandas as pd
import joblib
import base64

# --------------------------
# 💾 Load model
model = joblib.load("student_score_predictor.pkl")

# --------------------------
# 🖼️ Set custom background image
def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    .glow {{
        font-size: 45px;
        color: #fff;
        text-align: center;
        text-shadow: 0 0 5px #00e6e6, 0 0 10px #00e6e6, 0 0 20px #00e6e6, 0 0 40px #00e6e6;
        animation: float 3s ease-in-out infinite;
        margin-bottom: 20px;
    }}

    @keyframes float {{
        0% {{ transform: translatey(0px); }}
        50% {{ transform: translatey(-20px); }}
        100% {{ transform: translatey(0px); }}
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# --------------------------
# 🎨 Set background
set_background("study_background.jpg")

# --------------------------
# 🧠 Title
st.markdown('<div class="glow">SARTHAK KA AAVISHKAR 😎</div>', unsafe_allow_html=True)
st.title("🎓 Student Exam Score Predictor")

# --------------------------
# ✍️ Input fields
st.subheader("📥 Enter Student Details")

Parental_Involvement = st.selectbox("Parental Involvement", ["Low", "Medium", "High"])
Access_to_Resources = st.selectbox("Access to Resources", ["Poor", "Average", "Good"])
Extracurricular_Activities = st.selectbox("Extracurricular Activities", ["None", "Some", "Active"])
Motivation_Level = st.selectbox("Motivation Level", ["Low", "Medium", "High"])
Internet_Access = st.selectbox("Internet Access", ["No", "Yes"])
Family_Income = st.selectbox("Family Income", ["Low", "Medium", "High"])
Teacher_Quality = st.selectbox("Teacher Quality", ["Poor", "Average", "Excellent"])
School_Type = st.selectbox("School Type", ["Public", "Private"])
Peer_Influence = st.selectbox("Peer Influence", ["Negative", "Neutral", "Positive"])
Learning_Disabilities = st.selectbox("Learning Disabilities", ["No", "Yes"])
Parental_Education_Level = st.selectbox("Parental Education Level", ["High School", "Graduate", "Post-Graduate"])
Distance_from_Home = st.selectbox("Distance from Home", ["Near", "Moderate", "Far"])
Gender = st.selectbox("Gender", ["Male", "Female"])

Tutoring_Sessions = st.slider("Tutoring Sessions per Week", 0, 10, 2)
Hours_Studied = st.slider("Hours Studied per Day", 0, 12, 3)
Previous_Scores = st.slider("Previous Exam Score", 0, 100, 70)
Attendance = st.slider("Attendance (%)", 0, 100, 90)
Sleep_Hours = st.slider("Sleep Hours per Day", 0, 12, 7)
Physical_Activity = st.slider("Physical Activity Hours/Week", 0, 14, 5)

# --------------------------
# 📊 Create input DataFrame
input_data = pd.DataFrame({
    "Parental_Involvement": [Parental_Involvement],
    "Access_to_Resources": [Access_to_Resources],
    "Extracurricular_Activities": [Extracurricular_Activities],
    "Motivation_Level": [Motivation_Level],
    "Internet_Access": [Internet_Access],
    "Family_Income": [Family_Income],
    "Teacher_Quality": [Teacher_Quality],
    "School_Type": [School_Type],
    "Peer_Influence": [Peer_Influence],
    "Learning_Disabilities": [Learning_Disabilities],
    "Parental_Education_Level": [Parental_Education_Level],
    "Distance_from_Home": [Distance_from_Home],
    "Gender": [Gender],
    "Tutoring_Sessions": [Tutoring_Sessions],
    "Hours_Studied": [Hours_Studied],
    "Previous_Scores": [Previous_Scores],
    "Attendance": [Attendance],
    "Sleep_Hours": [Sleep_Hours],
    "Physical_Activity": [Physical_Activity]
})

# --------------------------
# 🔮 Predict score
if st.button("📈 Predict Exam Score"):
    prediction = model.predict(input_data)[0]
    st.success(f"🎯 Predicted Exam Score: **{prediction:.2f}**")


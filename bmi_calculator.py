import streamlit as st
from streamlit_extras.let_it_rain import rain  # For cool animations

# Set page config
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

# Apply custom styling
st.markdown(
    """
    <style>
        .main {background-color: #f0f2f6;}
        div.stButton > button { 
            background-color: #4CAF50; 
            color: white; 
            font-size: 18px;
            border-radius: 10px;
            padding: 10px;
            width: 100%;
        }
        div.stNumberInput > label { font-size: 18px; font-weight: bold; }
    </style>
    """,
    unsafe_allow_html=True
)

# Add an icon and title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>⚖️ BMI Calculator</h1>", unsafe_allow_html=True)

# Center the input fields
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Enter your weight (kg) 🏋️", min_value=1.0, step=0.1, format="%.1f")
with col2:
    height = st.number_input("Enter your height (m) 📏", min_value=0.5, step=0.01, format="%.2f")

# Function to calculate BMI
def calculate_bmi(weight, height):
    if height > 0:
        return round(weight / (height ** 2), 2)
    return None

# Calculate BMI
if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)

    if bmi:
        st.subheader(f"💡 Your BMI: **{bmi}**")
        
        # Interpret BMI category
        if bmi < 18.5:
            st.warning("⚠️ You are **underweight**. Consider a balanced diet.")
            rain("❄️", animation_length=3)
        elif 18.5 <= bmi < 24.9:
            st.success("✅ You have a **healthy weight**. Keep it up! 💪")
            rain("✨", animation_length=3)
        elif 25 <= bmi < 29.9:
            st.warning("⚠️ You are **overweight**. Consider exercise and diet control.")
            rain("⚡", animation_length=3)
        else:
            st.error("⚠️ You are **obese**. Consult a doctor for guidance.")
            rain("🔥", animation_length=3)
    else:
        st.error("❌ Please enter valid height and weight.")

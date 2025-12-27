import streamlit as st
import numpy as np
import joblib


st.set_page_config(
    page_title="Stroke Risk Prediction",
    page_icon="🫀",
    layout="centered"
)

model = joblib.load(r"models/stroke_logistic_model3.pkl")
scaler = joblib.load(r"models/scaler.pkl")

if "predict" not in st.session_state:
    st.session_state.predict = False

st.markdown("""
<style>
.main { background-color: #f4f6f9; }

.card {
    background-color: white;
    padding: 25px;
    border-radius: 14px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

.high {
    background:#e74c3c;
    color:white;
    padding:16px;
    border-radius:12px;
    text-align:center;
    font-size:22px;
}

.low {
    background:#2ecc71;
    color:white;
    padding:16px;
    border-radius:12px;
    text-align:center;
    font-size:22px;
}

div.stButton > button {
    background-color: #ff9800;
    color: white;
    font-size: 18px;
    padding: 10px 24px;
    border-radius: 10px;
    border: none;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>Stroke Risk Prediction System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>ML based stroke risk estimation</p>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Patient Input", "Prediction Result"])

with tab1:
    # st.markdown("<div class='card'>", unsafe_allow_html=True)

    age = st.number_input("Age", 0, 120, 50)
    avg_glucose = st.number_input("Average Glucose Level", 50.0, 300.0, 100.0)
    bmi = st.number_input("BMI", 10.0, 60.0, 25.0)

    hypertension = st.selectbox("Hypertension", ["No", "Yes"])
    heart_disease = st.selectbox("Heart Disease", ["No", "Yes"])
    gender = st.selectbox("Gender", ["Female", "Male"])
    ever_married = st.selectbox("Ever Married?", ["No", "Yes"])

    work_type = st.selectbox(
        "Work Type",
        ["Govt_job", "Private", "Self-employed", "Never_worked", "children"]
    )

    residence = st.selectbox("Residence Type", ["Rural", "Urban"])

    smoking_status = st.selectbox(
        "Smoking Status",
        ["never smoked", "formerly smoked", "smokes"]
    )

    if st.button("Predict Stroke Risk"):
        st.session_state.predict = True

    st.markdown("</div>", unsafe_allow_html=True)

hypertension = 1 if hypertension == "Yes" else 0
heart_disease = 1 if heart_disease == "Yes" else 0
gender_male = 1 if gender == "Male" else 0
ever_married_yes = 1 if ever_married == "Yes" else 0
residence_urban = 1 if residence == "Urban" else 0

work_type_never = 1 if work_type == "Never_worked" else 0
work_type_private = 1 if work_type == "Private" else 0
work_type_self = 1 if work_type == "Self-employed" else 0
work_type_children = 1 if work_type == "children" else 0

smoking_never = 1 if smoking_status == "never smoked" else 0
smoking_smokes = 1 if smoking_status == "smokes" else 0

# ---- SCALE ONLY NUMERIC FEATURES ----
numeric_part = np.array([[age, avg_glucose, bmi]])   # shape (1, 3)
numeric_scaled = scaler.transform(numeric_part)

# ---- FINAL INPUT TO MODEL (ORDER MATTERS) ----
input_data_final = np.array([[
    numeric_scaled[0][0],   # age (scaled)
    hypertension,
    heart_disease,
    numeric_scaled[0][1],   # avg_glucose_level (scaled)
    numeric_scaled[0][2],   # bmi (scaled)
    gender_male,
    ever_married_yes,
    work_type_never,
    work_type_private,
    work_type_self,
    work_type_children,
    residence_urban,
    smoking_never,
    smoking_smokes
]])


with tab2:
    if st.session_state.predict:
        # st.markdown("<div class='card'>", unsafe_allow_html=True)

        # st.subheader("Input Data Check")
        # st.write({
        #     "age": age,
        #     "hypertension": hypertension,
        #     "heart_disease": heart_disease,
        #     "avg_glucose": avg_glucose,
        #     "bmi": bmi,
        #     "gender_male": gender_male,
        #     "ever_married_yes": ever_married_yes,
        #     "work_type_private": work_type_private,
        #     "work_type_self": work_type_self,
        #     "work_type_children": work_type_children,
        #     "residence_urban": residence_urban,
        #     "smoking_never": smoking_never,
        #     "smoking_smokes": smoking_smokes
        # })

        # st.write("Scaler mean:", scaler.mean_)
        # st.write("Scaler scale:", scaler.scale_)


        # input_scaled = scaler.transform(input_data_final)
        prediction = model.predict(input_data_final)
        probability = model.predict_proba(input_data_final)[0][1]



        # st.progress(int(percent))
        # st.write(f"{percent}% estimated stroke risk")

        # if st.button("Predict Again"):
        #     st.session_state.predict = False
        #     st.experimental_rerun()


        # display_probability = min(probability, 0.95)
        # percent = round(display_probability * 100, 2)

        # if probability >= 0.75:
        #     st.error("🔴 HIGH RISK OF STROKE")
        # elif probability >= 0.4:
        #     st.warning("🟠 MODERATE RISK OF STROKE")
        # else:
        #     st.success("🟢 LOW RISK OF STROKE")

        # st.progress(int(percent))
        # st.write(f"{percent}% estimated stroke risk")

        probability = model.predict_proba(input_data_final)[0][1]

        # Optional display cap (UI only)
        display_probability = min(probability, 1)
        percent = round(display_probability * 100, 2)

        # FINAL threshold logic
        # Updated threshold logic for a balanced model
        if probability >= 0.70:
            st.error(f"🔴 HIGH RISK OF STROKE ({percent}%)")
            st.markdown("---")
            st.write("⚠️ **Recommendation:** Please consult a healthcare professional immediately for a formal assessment.")
        elif probability >= 0.30:
            st.warning(f"🟠 MODERATE RISK OF STROKE ({percent}%)")
            st.write("💡 **Tip:** Maintaining a healthy diet and monitoring blood pressure can help reduce risk.")
        else:
            st.success(f"🟢 LOW RISK OF STROKE ({percent}%)")
            st.write("✅ Your metrics are within a relatively healthy range.")

        st.progress(int(percent))
        st.write(f"{percent}% estimated stroke risk")


        st.markdown("</div>", unsafe_allow_html=True)
import streamlit as st
import numpy as np
import pickle

@st.cache_resource
def load_model():
    with open("models/diabetes.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

def app():
    st.header("🩸 Diabetes Prediction")

    fields = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
              "Insulin", "BMI", "DPF", "Age"]

    inputs = {}
    for f in fields:
        inputs[f] = st.number_input(f, value=0.0)

    if st.button("Predict"):
        data = np.array(list(inputs.values())).reshape(1, -1)
        prediction = model.predict(data)[0]
        if prediction == 1:
            st.error("⚠️ You may have diabetes. Please consult a doctor.")
        else:
            st.success("✅ No diabetes detected.")

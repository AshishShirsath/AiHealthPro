import streamlit as st
import numpy as np
import pickle

@st.cache_resource
def load_model():
    with open("models/heart.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

def app():
    st.header("❤️ Heart Disease Prediction")

    fields = [
        "age", "sex", "cp", "trestbps", "chol", "fbs",
        "restecg", "thalach", "exang", "oldpeak",
        "slope", "ca", "thal"
    ]

    inputs = {}
    for f in fields:
        inputs[f] = st.number_input(f, value=0.0)

    if st.button("Predict"):
        try:
            features = np.array(list(inputs.values())).reshape(1, -1)
            prediction = model.predict(features)[0]
            if prediction == 1:
                st.error("⚠️ Likely Heart Disease detected. Please consult a doctor.")
            else:
                st.success("✅ No Heart Disease detected.")
        except Exception as e:
            st.warning(f"Error: {e}")

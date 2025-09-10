
import streamlit as st
import numpy as np
import pickle

@st.cache_resource
def load_model():
    with open("models/liver.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

def app():
    st.title("🧪 Liver Disease Prediction")

    inputs = {}
    features = ["Age", "Total_Bilirubin", "Direct_Bilirubin", "Alkaline_Phosphotase",
                "Alamine_Aminotransferase", "Aspartate_Aminotransferase", 
                "Total_Protiens", "Albumin", "Albumin_and_Globulin_Ratio", "Gender_Male"]

    for f in features:
        inputs[f] = st.text_input(f)

    if st.button("🔍 Predict"):
        try:
            data = np.array([float(inputs[f]) for f in features]).reshape(1, -1)
            prediction = model.predict(data)[0]
            if prediction == 1:
                st.error("⚠️ Likely liver disease. Please consult a doctor.")
            else:
                st.success("✅ No liver disease detected.")
        except:
            st.warning("Please enter valid numbers.")

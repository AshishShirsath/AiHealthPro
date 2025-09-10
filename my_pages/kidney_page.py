
import streamlit as st
import numpy as np
import pickle

@st.cache_resource
def load_model():
    with open("models/kidney.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

def app():
    st.title("🧪 Kidney Disease Prediction")

    inputs = {}
    features = ["Age", "Blood Pressure", "AL", "SU", "RBC", "PC", "PCC", "BA", 
                "BGR", "BU", "SC", "Pot", "WC", "HTN", "DM", "CAD", "PE", "ANE"]

    for f in features:
        inputs[f] = st.text_input(f)

    if st.button("🔍 Predict"):
        try:
            data = np.array([float(inputs[f]) for f in features]).reshape(1, -1)
            prediction = model.predict(data)[0]
            if prediction == 1:
                st.error("⚠️ You may have kidney disease. Please consult a doctor.")
            else:
                st.success("✅ You are healthy!")
        except:
            st.warning("Please enter valid numbers for all fields.")

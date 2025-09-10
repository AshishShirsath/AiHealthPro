import streamlit as st
import numpy as np
import pickle

@st.cache_resource
def load_model():
    with open("models/cancer.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

def app():
    st.header("🎗️ Cancer Prediction")

    inputs = {}
    fields = [
        "radius_mean", "texture_mean", "perimeter_mean", "area_mean", "smoothness_mean",
        "compactness_mean", "concavity_mean", "concave_points_mean", "symmetry_mean",
        "radius_se", "perimeter_se", "area_se", "compactness_se", "concavity_se",
        "concave_points_se", "fractal_dimension_se", "radius_worst", "texture_worst",
        "perimeter_worst", "area_worst", "smoothness_worst", "compactness_worst",
        "concavity_worst", "concave_points_worst", "symmetry_worst", "fractal_dimension_worst"
    ]

    cols = st.columns(3)
    for i, field in enumerate(fields):
        with cols[i % 3]:
            inputs[field] = st.number_input(field, value=0.0)

    if st.button("🔍 Predict"):
        try:
            features = np.array(list(inputs.values())).reshape(1, -1)
            prediction = model.predict(features)[0]

            if prediction == 1:
                st.error("⚠️ Malignant Cancer detected. Please consult an oncologist immediately.")
            else:
                st.success("✅ Benign Tumor detected.")
        except Exception as e:
            st.warning(f"Something went wrong: {e}")

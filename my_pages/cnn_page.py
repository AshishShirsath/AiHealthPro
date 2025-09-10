import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os

MODEL_PATH = os.path.join("models", "new_model.h5")

@st.cache_resource
def load_model():
    try:
        model = tf.keras.models.load_model(MODEL_PATH, compile=False)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()

class_mapping = {
    0: 'Brain - Alzheimer MildDemented',
    1: 'Brain - Alzheimer ModerateDemented',
    2: 'Brain - Alzheimer NonDemented',
    3: 'Brain - Alzheimer VeryMildDemented',
    4: 'Brain - No Brain Tumor',
    5: 'Brain - Glioma Brain Tumor',
    6: 'Brain - Meningioma Brain Tumor',
    7: 'Brain - Pituitary Brain Tumor',
    8: 'Chest - Covid19',
    9: 'Chest - Lung Opacity',
    10: 'Chest - Normal',
    11: 'Chest - Pneumonia',
    12: 'RF - AMD',
    13: 'RF - Cataract',
    14: 'RF - Glaucoma',
    15: 'RF - Hypertensive Retinopathy',
    16: 'RF - Mild DR',
    17: 'RF - Moderate DR',
    18: 'RF - Normal Fundus',
    19: 'RF - Proliferate DR',
    20: 'RF - Severe DR',
    21: 'Skin - akiec',
    22: 'Skin - bcc',
    23: 'Skin - bkl',
    24: 'Skin - df',
    25: 'Skin - mel',
    26: 'Skin - nv',
    27: 'Skin - vasc'
}

def classify_image(image):
    if image.mode != "RGB":
        image = image.convert("RGB")

    image = tf.image.resize(np.array(image), (120, 120))
    image = tf.cast(image, tf.float32) / 255.0
    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image, verbose=0)[0]
    return class_mapping.get(int(np.argmax(prediction)), "Unknown")

def app():
    st.header("🧠 Image Disease Classifier")
    if model is None:
        st.error("Model not loaded. Please check your TensorFlow installation or model file.")
        return

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        with st.spinner("Classifying..."):
            prediction = classify_image(image)

        st.success(f"Prediction: **{prediction}**")

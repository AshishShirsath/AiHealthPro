import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import tensorflow as tf

# Load original model
model = tf.keras.models.load_model('E:\\baknew\\IMAGE DISEASES\\Image\\new_model.h5')

# Convert to SavedModel format
model.save('E:\\baknew\\IMAGE DISEASES\\Image\\saved_model')

# Load the model once at the beginning using st.cache_resource
@st.cache_resource
def load_model():
    return tf.keras.models.load_model('E:\\baknew\\IMAGE DISEASES\\Image\\saved_model')

# Load model
model = load_model()

# Function to classify images
def classify_image(image):
    # Resize and preprocess the image
    image = tf.image.resize(image, (120, 120))
    image = tf.cast(image, tf.float32) / 255.0
    image = np.expand_dims(image, axis=0)

    # Make prediction
    prediction = model.predict(image)[0]
    predicted_class_index = np.argmax(prediction)

    # Class mapping
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

    # Get predicted class name
    predicted_class = class_mapping.get(predicted_class_index, "Unknown")
    return predicted_class

# Main function for Streamlit app
def main():
    st.title("Image Disease Classifier")
    st.write("Upload an image to classify the disease.")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        image = np.array(image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Prediction
        with st.spinner("Classifying..."):
            prediction = classify_image(image)
        st.success(f"Prediction: **{prediction}**")

# Run the Streamlit app
if __name__ == '__main__':
    main()

# AIHealthPro – AI-Based Healthcare Assistant

**AIHealthPro** is an intelligent healthcare platform that provides disease prediction, medical image diagnosis, chatbot assistance, and doctor appointment management — all integrated into a unified system powered by Machine Learning, Deep Learning, and a Java backend.

---

## Features

### Symptom-Based Disease Prediction
- Uses **Machine Learning models** to predict possible diseases based on user-entered symptoms.
- Provides a list of likely diagnoses with corresponding probabilities.

### Image-Based Diagnosis
- Employs a **Convolutional Neural Network (CNN)** to predict diseases based on uploaded images (e.g., skin conditions).
- Gives confidence scores and visual feedback for better understanding.

### AI Chatbot Integration
- Integrated a **chatbot powered by NVIDIA's AI model** to provide 24/7 interaction with users.
- Capable of answering common health queries and guiding users through platform functionalities.

### Doctor Appointment Booking System
- Allows users to **book consultations** with available doctors.
- **Java backend with MySQL** handles booking logic, user data, and appointment history securely.

### Health Guidance Module
- After prediction, the system provides **precautionary measures and preventive steps** for diagnosed conditions.
- Personalized to user input and predicted illness.

---

## Tech Stack

- **Machine Learning:** Scikit-learn, Pandas, Numpy
- **Deep Learning:** TensorFlow, Keras (CNN for image classification)
- **Backend:** Java (Spring Boot), MySQL
- **Frontend:** HTML/CSS/JavaScript or Streamlit (if applicable for frontend interface)
- **AI Chatbot:** NVIDIA-powered model (custom-trained or API-integrated)
- **Database:** MySQL

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/AIHealthPro.git
   cd AIHealthPro

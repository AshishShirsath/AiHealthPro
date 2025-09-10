
import streamlit as st

def app():
    st.markdown(
        """
        <style>
        .main {background-color: #121212; color: #f1f1f1;}
        .title-container {text-align: center; padding: 20px; background: #1f77b4; 
        color: white; border-radius: 12px; margin-bottom: 20px;}
        .expander-header {color: #f1f1f1;}
        .stExpander {background: #1e1e1e; border-radius: 10px;}
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown('<div class="title-container"><h1>🏥 Multiple Disease Prediction System</h1></div>', unsafe_allow_html=True)
    st.markdown("This app predicts various diseases based on patient data and symptoms.")

    st.markdown("### 📊 Model Accuracy")
    st.markdown("""
    - ❤️ Heart : **85.25%**  
    - 🩸 Kidney : **97.51%**  
    - 🧫 Liver : **79.66%**  
    - 🧪 Cancer : **96.59%**  
    """)

    st.markdown("### 🦠 Diseases Our Web App Can Predict")

    with st.expander("💉 Diabetes"):
        st.write("Chronic disease where body doesn’t use insulin effectively.")
        st.markdown("**Symptoms:** Increased thirst, frequent urination, extreme hunger, blurred vision")

    with st.expander("❤️ Heart Disease"):
        st.write("Includes blood vessel disease and heart rhythm problems.")
        st.markdown("**Symptoms:** Chest pain, shortness of breath, neck/jaw pain, leg coldness")

    with st.expander("🧫 Liver Disease"):
        st.write("Often includes swelling, pain, and yellowing of skin/eyes.")
        st.markdown("**Symptoms:** Yellow skin/eyes, swollen legs, nausea, vomiting")

    with st.expander("🩸 Chronic Kidney Disease"):
        st.write("Gradual loss of kidney function, leading to fluid/waste buildup.")
        st.markdown("**Symptoms:** Nausea, fatigue, high BP, loss of appetite")

    with st.expander("🎀 Breast Cancer"):
        st.write("Cancer developing in breast cells, more common in women.")
        st.markdown("**Symptoms:** Lump in breast, size change, pain, dimpling")

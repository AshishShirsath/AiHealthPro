import streamlit as st
from importlib import import_module

st.set_page_config(page_title="Medical Prediction Hub", layout="wide")

st.markdown("""
    <style>
    /* Global dark theme */
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
    }
    section[data-testid="stSidebar"] * {
        color: #c9d1d9 !important;
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #f0f6fc !important;
        font-weight: 600 !important;
    }

    /* Expanders */
    .streamlit-expanderHeader {
        background-color: #21262d !important;
        color: #f0f6fc !important;
        font-weight: 500;
        border-radius: 6px;
    }
    .streamlit-expanderContent {
        background-color: #161b22 !important;
        border-left: 2px solid #30363d;
        padding: 10px;
    }

    /* Buttons */
    div.stButton > button {
        background-color: #238636;
        color: #ffffff;
        border: none;
        border-radius: 6px;
        padding: 0.6em 1.2em;
        font-weight: 500;
        transition: 0.2s;
    }
    div.stButton > button:hover {
        background-color: #2ea043;
        transform: scale(1.02);
    }

    /* Inputs */
    input, textarea, select {
        background-color: #161b22 !important;
        color: #c9d1d9 !important;
        border: 1px solid #30363d !important;
        border-radius: 6px;
    }

    /* Success/Error messages */
    .stAlert {
        border-radius: 6px;
    }

    /* Radio buttons */
    div[role="radiogroup"] label {
        background-color: #21262d;
        border-radius: 6px;
        padding: 6px 12px;
        margin: 3px;
    }
    div[role="radiogroup"] label:hover {
        background-color: #30363d;
    }
    </style>
""", unsafe_allow_html=True)



st.sidebar.title("🩺 Medical Prediction Hub")

pages = {
    "🏠 Home": "home_page",
    "🧬 CNN Image Classifier": "cnn_page",
    "🧪 Cancer Prediction": "cancer_page",
    "💉 Diabetes Prediction": "diabetes_page",
    "❤️ Heart Disease Prediction": "heart_page",
    "🩸 Kidney Disease Prediction": "kidney_page",
    "🧫 Liver Disease Prediction": "liver_page",
    "🤖 Medical Chatbot": "chatbot_page"
}

choice = st.sidebar.radio("Navigate to", list(pages.keys()), index=0)

st.markdown('<div class="title-container"><h1>🩺 Medical Prediction Hub</h1></div>', unsafe_allow_html=True)

module = import_module(f"my_pages.{pages[choice]}")
module.app()

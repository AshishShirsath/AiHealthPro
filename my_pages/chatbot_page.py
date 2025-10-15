def app():
    import streamlit as st
    import pickle
    import pandas as pd
    from sklearn.metrics.pairwise import cosine_similarity

    with open("models/df_symptoms.pkl", "rb") as f:
        df_symptoms = pickle.load(f)
    with open("models/vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    with open("models/X.pkl", "rb") as f:
        X = pickle.load(f)

    dk = pd.read_csv("data/symptom_Description.csv")
    dm = pd.read_csv("data/cleaned_precautions.csv")

    def clean_text(text):
        return " ".join(str(text).lower().strip().split())

    def predict_diseases(user_text, df_symptoms, vectorizer, X, top_k=3):
        user_clean = clean_text(user_text)
        if not user_clean:
            return []
        v = vectorizer.transform([user_clean])
        sim = cosine_similarity(v, X)[0]
        idx = sim.argsort()[::-1][:top_k]
        results = []
        for i in idx:
            if sim[i] <= 0:
                continue
            disease = df_symptoms.iloc[i]['Disease']
            symptoms = df_symptoms.iloc[i]['All_Symptoms']
            description = dk.loc[dk['Disease'] == disease, 'Description'].values
            description = description[0] if len(description) > 0 else "No description available."
            precaution = dm.loc[dm['Disease'] == disease, 'Precaution'].values
            precaution = precaution[0] if len(precaution) > 0 else "No precautions available."
            results.append({
                "disease": disease,
                "score": sim[i],
                "description": description,
                "symptoms": symptoms,
                "precaution": precaution
            })
        return results

    st.set_page_config(page_title="🩺 Symptom → Disease Assistant", layout="wide")
    
    st.write("Enter your symptoms to find likely diseases with descriptions and precautions. (Educational use only)")

    user_input = st.text_area("Describe your symptoms:", height=100)
    top_k = st.slider("Number of top matches", 1, 5, 3)

    if st.button("Predict Diseases"):
        predictions = predict_diseases(user_input, df_symptoms, vectorizer, X, top_k)
        if not predictions:
            st.warning("No matching disease found. Try different symptoms.")
        else:
            for pred in predictions:
                with st.expander(f"{pred['disease']} (Score: {pred['score']:.3f})"):
                    st.markdown(f"**Description:** {pred['description']}")
                    st.markdown(f"**Symptoms:** {pred['symptoms']}")
                    st.markdown(f"**Precautions:** {pred['precaution']}")

import streamlit as st
from openai import OpenAI


client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="key"  
)

def app():
    st.title("Medical Chatbot")
    st.write("Ask me anything about the Health Care!")


    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []


    for role, content in st.session_state.chat_history:
        with st.chat_message(role):
            st.markdown(content)


    user_input = st.chat_input("Type your message...")
    if user_input:

        st.session_state.chat_history.append(("user", user_input))
        with st.chat_message("user"):
            st.markdown(user_input)


        try:
            completion = client.chat.completions.create(
                model="nvidia/llama-3.1-nemotron-70b-instruct",
                messages=[{"role": "user", "content": user_input}],
                temperature=0.5,
                top_p=1,
                max_tokens=512
            )
            ai_reply = completion.choices[0].message.content

        except Exception as e:
            ai_reply = f"⚠️ Error: {e}"


        st.session_state.chat_history.append(("assistant", ai_reply))
        with st.chat_message("assistant"):
            st.markdown(ai_reply)

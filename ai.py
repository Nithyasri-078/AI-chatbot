import streamlit as st
import ollama
st.title("AI CHATBOT")
st.write("HELLO...")
prompt = st.text_input("Ask something")
if st.button("submit"):
    response = ollama.chat(
        model = "llama3.2",
        messages=[
            {
                "role" : "user",
                "content": prompt
            }
        ]
)
    st.write(response["message"]["content"])
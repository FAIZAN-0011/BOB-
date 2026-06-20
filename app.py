import streamlit as st
from groq import Groq

api_key = st.secrets["GROQ_API_KEY"]

client = Groq(api_key=api_key)

st.title("BOB 2.0")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Type your message...")

if user_input:

    
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

   
    with st.chat_message("user"):
        st.write(user_input)

    
    chat_completion = client.chat.completions.create(
        messages=st.session_state.messages,
        model="llama-3.3-70b-versatile"
    )

    
    response = chat_completion.choices[0].message.content

    
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    
    with st.chat_message("assistant"):
        st.write(response)
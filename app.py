import streamlit as st
import random
import time
from gome.inbuilt_chatinterface import chat_with_me


# Streamed response emulator
def response_generator(question):
    response = chat_with_me(question= question)
    return response


st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    print(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
        time.sleep(10)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = response_generator(prompt)
        print(response)
        response = st.write(response)
    # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
import streamlit as st
import os
from src.new_chatbot.llm_service import llm_service

# Page configuration
st.set_page_config(
    page_title="Modern AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS for modern look
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stChatMessage {
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .stTextInput {
        border-radius: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 Local AI Chatbot")
st.caption(f"Powered by Local LLM: {os.getenv('LOCAL_LLM_MODEL', 'qwen2.5-coder:3b')}")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("How can I help you today?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Use the LLM service to get a streaming response
        try:
            for chunk in llm_service.get_streaming_response(st.session_state.messages):
                full_response += chunk
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
            full_response = "Sorry, I encountered an error while processing your request."
            message_placeholder.markdown(full_response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

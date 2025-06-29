import streamlit as st
from logic.chatbot import generate_feedback_response

def show():
    st.title("🗣 Citizen Feedback System")
    user_input = st.text_area("Describe your complaint or suggestion:")
    if st.button("Submit"):
        with st.spinner("Processing..."):
            response = generate_feedback_response(user_input)
            st.success(response)

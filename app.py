import streamlit as st
from ui import welcome_ui, chatbot_ui, summarizer_ui, data_ui, eco_ui

def main():
    st.set_page_config(page_title="Sustainable Smart City", layout="wide")
    
    st.sidebar.title("🌆 Sustainable Smart City")
    page = st.sidebar.radio("Navigate", [
        "Welcome",
        "City Health Dashboard",
        "Citizen Feedback",
        "Document Summarizer",
        "Eco Advice"
    ])

    if page == "Welcome":
        welcome_ui.show()
    elif page == "City Health Dashboard":
        data_ui.show()
    elif page == "Citizen Feedback":
        chatbot_ui.show()
    elif page == "Document Summarizer":
        summarizer_ui.show()
    elif page == "Eco Advice":
        eco_ui.show()

if __name__ == "__main__":
    main()


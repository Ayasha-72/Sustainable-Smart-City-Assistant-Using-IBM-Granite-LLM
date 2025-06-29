import streamlit as st
from logic.summarizer import summarize_text

def show():
    st.title("📄 Document Summarization Tool")
    text = st.text_area("Paste document content:")
    if st.button("Summarize"):
        with st.spinner("Summarizing..."):
            result = summarize_text(text)
            st.success(result)

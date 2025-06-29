import streamlit as st
from logic.eco_advice import get_eco_advice

def show():
    st.title("🌿 Eco Advice Assistant")
    topic = st.text_input("Enter topic (e.g., water, energy, pollution):")
    if st.button("Get Tip"):
        with st.spinner("Generating advice..."):
            tip = get_eco_advice(topic)
            st.success(tip)

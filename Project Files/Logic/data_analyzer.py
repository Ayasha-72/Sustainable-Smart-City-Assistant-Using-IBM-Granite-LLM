import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import Credentials

# === Static credentials ===
creds = Credentials(api_key="cjhxM8OWLyjtVflsSDuTDb4TycWNRYAl3xMkcHbuuFq4", url="https://us-south.ml.cloud.ibm.com")
model = ModelInference(
    model_id="ibm/granite-3-8b-instruct",
    credentials=creds,
    project_id="245d62b5-7b2f-477f-8bf1-ece30f3fa579"
)

def analyze_city_data(df: pd.DataFrame):
    """Auto-plot charts based on input dataframe."""
    for column in df.select_dtypes(include=['int64', 'float64']):
        st.write(f"**📊 {column} Overview**")
        st.line_chart(df[column])

    for column in df.select_dtypes(include='object'):
        if df[column].nunique() <= 10:
            st.write(f"**🧩 Category Split: {column}**")
            st.bar_chart(df[column].value_counts())

def summarize_city_data(df: pd.DataFrame) -> str:
    """Use watsonx.ai to summarize city data"""
    prompt = f"Analyze and summarize the following city data:\n{df.head(10).to_csv(index=False)}"
    return model.generate_text(prompt=prompt, params={"max_new_tokens": 200})



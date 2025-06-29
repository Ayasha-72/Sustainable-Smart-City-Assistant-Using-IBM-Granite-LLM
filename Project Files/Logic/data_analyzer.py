import os
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from dotenv import load_dotenv
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

load_dotenv()

creds = Credentials(
    api_key=os.getenv("WATSONX_API_KEY"),
    url=os.getenv("WATSONX_URL")
)

model = ModelInference(
    model_id="ibm/granite-3-8b-instruct",
    credentials=creds,
    project_id=os.getenv("WATSONX_PROJECT_ID")
)

def analyze_city_data(df: pd.DataFrame):
    for column in df.select_dtypes(include=['int64', 'float64']):
        st.write(f"**📊 {column} Overview**")
        st.line_chart(df[column])

    for column in df.select_dtypes(include='object'):
        if df[column].nunique() <= 10:
            st.write(f"**🧩 Category Split: {column}**")
            st.bar_chart(df[column].value_counts())

def summarize_city_data(df: pd.DataFrame) -> str:
    sample = df.head(10).to_csv(index=False)
    prompt = f"Analyze and summarize the following city data:\n{sample}"
    summary = model.generate_text(prompt=prompt, params={"max_new_tokens": 200})
    return summary




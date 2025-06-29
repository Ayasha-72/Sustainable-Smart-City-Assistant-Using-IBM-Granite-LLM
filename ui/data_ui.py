import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from logic.data_analyzer import analyze_city_data, summarize_city_data

def show():
    st.title("📊 City Health Dashboard")
    st.write("Paste your data below (CSV format or table):")

    raw_data = st.text_area("Paste CSV data", height=250)

    if st.button("Generate Dashboard"):
        if raw_data.strip():
            try:
                # Convert text to DataFrame
                from io import StringIO
                df = pd.read_csv(StringIO(raw_data))

                st.subheader("📄 Parsed Data Preview")
                st.dataframe(df)

                st.subheader("📈 Auto Charts")
                analyze_city_data(df)

                st.subheader("🧠 AI Overview")
                summary = summarize_city_data(df)
                st.success(summary)

            except Exception as e:
                st.error(f"Error reading data: {e}")
        else:
            st.warning("Please paste some data before submitting.")


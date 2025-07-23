import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def run_data_analysis():
    st.subheader("📊 Data Analysis & Visualization")

    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success("✅ File uploaded successfully")

        st.markdown("### 🔍 Data Preview")
        st.dataframe(df.head())

        st.markdown("### 📈 Statistical Summary")
        st.write(df.describe())

        st.markdown("### 📊 Select Columns to Visualize")
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

        if numeric_cols:
            col1 = st.selectbox("Choose X-axis", numeric_cols, key="x_axis")
            col2 = st.selectbox("Choose Y-axis", numeric_cols, key="y_axis")

            chart_type = st.radio("Chart type", ["Line", "Bar", "Scatter", "Histogram"], horizontal=True)

            fig = None
            if chart_type == "Line":
                fig = px.line(df, x=col1, y=col2)
            elif chart_type == "Bar":
                fig = px.bar(df, x=col1, y=col2)
            elif chart_type == "Scatter":
                fig = px.scatter(df, x=col1, y=col2)
            elif chart_type == "Histogram":
                fig = px.histogram(df, x=col1)

            if fig:
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No numeric columns found to visualize.")


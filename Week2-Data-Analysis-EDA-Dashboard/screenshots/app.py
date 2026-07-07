import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Netflix Data Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("data/cleaned_dataset.csv")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "Dataset Preview",
        "Data Cleaning Summary",
        "Statistical Analysis",
        "Interactive Filter",
        "Visualizations",
        "Key Insights",
        "Download Dataset"
    ]
)

# -----------------------------
# Home
# -----------------------------
if page == "Home":

    st.title("📊 Netflix Data Analysis Dashboard")

    st.write("""
    Welcome to the Netflix Data Analysis Dashboard.

    This dashboard demonstrates:

    - Data Cleaning
    - Exploratory Data Analysis
    - Data Visualization
    - Interactive Filtering
    """)

    st.metric("Rows", df.shape[0])
    st.metric("Columns", df.shape[1])

# -----------------------------
# Dataset Preview
# -----------------------------
elif page == "Dataset Preview":

    st.title("Dataset Preview")

    st.dataframe(df)

# -----------------------------
# Data Cleaning Summary
# -----------------------------
elif page == "Data Cleaning Summary":

    st.title("Data Cleaning Summary")

    st.write("Dataset Shape")

    st.write(df.shape)

    st.write("Missing Values")

    st.write(df.isnull().sum())

    st.write("Duplicate Rows")

    st.write(df.duplicated().sum())

# -----------------------------
# Statistical Analysis
# -----------------------------
elif page == "Statistical Analysis":

    st.title("Statistical Analysis")

    st.write(df.describe(include="all"))

# -----------------------------
# Interactive Filter
# -----------------------------
elif page == "Interactive Filter":

    st.title("Filter Dataset")

    selected_type = st.selectbox(
        "Select Type",
        df["Type"].unique()
    )

    filtered = df[df["Type"] == selected_type]

    st.write(filtered)

# -----------------------------
# Visualizations
# -----------------------------
elif page == "Visualizations":

    st.title("Visualizations")

    fig, ax = plt.subplots(figsize=(6,4))

    sns.countplot(
        data=df,
        x="Type",
        ax=ax
    )

    plt.title("Movies vs TV Shows")

    st.pyplot(fig)

    fig2, ax2 = plt.subplots(figsize=(8,5))

    df.groupby("Release_Year").size().plot(ax=ax2)

    plt.title("Content Released Over Time")

    st.pyplot(fig2)

# -----------------------------
# Insights
# -----------------------------
elif page == "Key Insights":

    st.title("Key Insights")

    st.write("""
    • Movies are more common than TV Shows.

    • Most content was released after 2015.

    • TV-MA is the most frequent rating.

    • USA contributes the highest number of titles.

    • Drama is among the most common genres.
    """)

# -----------------------------
# Download Dataset
# -----------------------------
elif page == "Download Dataset":

    st.title("Download Cleaned Dataset")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download CSV",
        csv,
        "cleaned_dataset.csv",
        "text/csv"
    )
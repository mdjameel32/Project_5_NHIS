import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="TellCo User Analytics", layout="wide")
st.title("📱 TellCo Telecommunication User Analytics Dashboard")
st.markdown("### Investor Evaluation Platform — Republic of Pefkakia")


# Data load karein
@st.cache_data
def load_data():
    return pd.read_csv("user_satisfaction_scores.csv")


try:
    df = load_data()

    # Sidebar Filters
    st.sidebar.header("Filter Options")
    top_n = st.sidebar.slider("Top Satisfied Users", 5, 50, 10)

    # 1. KPI Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Unique Users", f"{len(df):,}")
    col2.metric("Avg Satisfaction Score", f"{df['Satisfaction_Score'].mean():.2f}")
    col3.metric("Avg Engagement Score", f"{df['Engagement_Score'].mean():.2f}")

    # 2. Top Customers Table
    st.subheader(f"🏆 Top {top_n} Most Satisfied Customers")
    top_users = df.sort_values(by="Satisfaction_Score", ascending=False).head(
        top_n
    )
    st.dataframe(top_users)

    # 3. Visualizations
    st.subheader("📊 Engagement vs Experience Distribution")
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.scatterplot(
        data=df.sample(min(1000, len(df))),
        x="Engagement_Score",
        y="Experience_Score",
        hue="Satisfaction_Score",
        palette="viridis",
        ax=ax,
    )
    st.pyplot(fig)

    
except FileNotFoundError:
    st.error(
        "Error: 'user_satisfaction_scores.csv' file nahi mili. Pehle apna analytics code chalayein!"
    )

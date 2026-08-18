import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.title("📊 Dashboard Capteurs")

DATABASE_URL = st.secrets["DATABASE_URL"]
engine = create_engine(DATABASE_URL)

df = pd.read_sql(
    "SELECT * FROM donnees_capteurs ORDER BY timestamp DESC LIMIT 50;",
    engine
)

if not df.empty:
    st.metric("Température", f"{df.iloc[0]['temperature']} °C")
    st.line_chart(df, x="timestamp", y=["temperature", "humidite"])

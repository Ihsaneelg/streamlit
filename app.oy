import streamlit as st
import pandas as pd

st.title("📊 Dashboard Capteurs")

# Connexion à la base de données
conn = st.connection("mysql", type="sql")

# Charger les données
df = conn.query("SELECT * FROM donnees_capteurs ORDER BY timestamp DESC LIMIT 50;", ttl=5)

if not df.empty:
    st.metric("Température", f"{df.iloc[0]['temperature']} °C")
    st.line_chart(df, x="timestamp", y=["temperature", "humidite"])

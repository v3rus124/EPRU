import streamlit as st
import pandas as pd
import xgboost as xgb
import joblib

# Načtení trénovaného modelu
model = joblib.load("best_model.json")

st.title("Predikce potřebného tepla podle venkovní teploty")

# Uživatelský vstup
teplota = st.number_input("Venkovní teplota (°C)", min_value=-20.0, max_value=40.0, step=0.1)
hodina = st.slider("Hodina dne", 0, 23)
den_v_tydnu = st.selectbox("Den v týdnu", ["Pondělí", "Úterý", "Středa", "Čtvrtek", "Pátek", "Sobota", "Neděle"])

# Převod dne v týdnu na číselnou hodnotu (0 = Pondělí, 6 = Neděle)
den_v_tydnu_num = ["Pondělí", "Úterý", "Středa", "Čtvrtek", "Pátek", "Sobota", "Neděle"].index(den_v_tydnu)

# Příprava vstupu pro model
data = pd.DataFrame({"outdoor_temperature": [teplota], "hour": [hodina], "day_of_week": [den_v_tydnu_num]})

# Predikce
predikce = model.predict(data)[0]

# Zobrazení výsledku
st.write(f"### Predikované množství tepla: {predikce:.2f} MW")
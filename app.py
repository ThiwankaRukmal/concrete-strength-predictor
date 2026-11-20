import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import numpy as np

@st.cache_resource
def train_model():
    df = pd.read_csv('Concrete Compressive Strength.csv').dropna()
    X = df.iloc[:, :8]
    y = df.iloc[:, 8]
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

model = train_model()

st.title("🧱 Concrete Compressive Strength Predictor")
st.write("අමුද්‍රව්‍ය අනුපාත ඇතුළත් කර කොන්ක්‍රීට් මිශ්‍රණයේ සම්පීඩන ශක්තිය (MPa) කලින් අනුමාන කරන්න.")

st.sidebar.header("අමුද්‍රව්‍ය ප්‍රමාණයන් (kg/m³)")

cement = st.sidebar.slider("Cement (සිමෙන්ති)", 100.0, 550.0, 300.0)
slag = st.sidebar.slider("Blast Furnace Slag", 0.0, 360.0, 0.0)
fly_ash = st.sidebar.slider("Fly Ash (අළු)", 0.0, 200.0, 0.0)
water = st.sidebar.slider("Water (ජලය)", 120.0, 250.0, 180.0)
superplasticizer = st.sidebar.slider("Superplasticizer", 0.0, 35.0, 5.0)
coarse_agg = st.sidebar.slider("Coarse Aggregate (ගල්)", 800.0, 1150.0, 950.0)
fine_agg = st.sidebar.slider("Fine Aggregate (වැලි)", 590.0, 1000.0, 750.0)
age = st.sidebar.slider("Curing Age (පදම් වන දින ගණන)", 1, 365, 28)

input_data = np.array([[cement, slag, fly_ash, water, superplasticizer, coarse_agg, fine_agg, age]])
prediction = model.predict(input_data)[0]

st.subheader("පුරෝකථනය කළ සම්පීඩන ශක්තිය (Predicted Strength):")
st.success(f"👉 {prediction:.2f} MPa")

wc_ratio = water / cement
st.info(f"**Water-to-Cement (W/C) අනුපාතය:** {wc_ratio:.2f}")

if wc_ratio > 0.55:
    st.warning("⚠️ අවවාදයයි: ජල-සිමෙන්ති අනුපාතය ඉහළ බැවින් කොන්ක්‍රීට් තුළ සිදුරු (Porosity) ඇති වී ශක්තිය අඩු විය හැක.")
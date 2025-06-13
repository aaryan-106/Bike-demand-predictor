import streamlit as st
import joblib
import numpy as np

model = joblib.load("bike_demand_model.pkl")

weather_map = {
    "Clear": 1,
    "Mist": 2,
    "Light Snow": 3,
    "Heavy Rain": 4
}

st.title("🚲 Real-Time Bike Sharing Demand Predictor")

temp = st.slider("Temperature (°C)", 0.0, 40.0, 20.0)
humidity = st.slider("Humidity (%)", 0, 100, 50)
windspeed = st.slider("Wind Speed (km/h)", 0.0, 50.0, 10.0)
hour = st.slider("Hour of Day", 0, 23, 8)
weather = st.selectbox("Weather", list(weather_map.keys()))
holiday = st.selectbox("Is it a holiday?", ["No", "Yes"])

weather_idx = weather_map[weather]
holiday_flag = 1 if holiday == "Yes" else 0

input_data = np.array([[temp, humidity, windspeed, hour, weather_idx, holiday_flag]])

if st.button("Predict Demand"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Bike Rentals: {int(prediction[0])}")

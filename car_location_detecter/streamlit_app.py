# streamlit_app.py

import streamlit as st
import pandas as pd
import joblib
from math import radians, cos, sin, asin, sqrt

# Load trained model
model = joblib.load("model.pkl")

# Haversine distance function
def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    return R * 2 * asin(sqrt(a))

st.title("🚗 Vehicle ETA Prediction")

# User input form
with st.form("eta_form"):
    st.subheader("Enter trip details")
    
    col1, col2 = st.columns(2)
    with col1:
        current_lat = st.number_input("Current Latitude", value=12.9716)
        current_lon = st.number_input("Current Longitude", value=77.5946)
        speed = st.number_input("Speed (km/h)", value=40.0)
    
    with col2:
        dest_lat = st.number_input("Destination Latitude", value=13.0358)
        dest_lon = st.number_input("Destination Longitude", value=77.5970)
        traffic_level = st.selectbox("Traffic Level", ["Low", "Medium", "High"])
    
    hour = st.slider("Hour (24h)", 0, 23, 10)
    minute = st.slider("Minute", 0, 59, 30)
    
    submitted = st.form_submit_button("Predict ETA")

# Process and predict
if submitted:
    traffic_map = {"Low": 0, "Medium": 1, "High": 2}
    traffic_val = traffic_map[traffic_level]
    
    distance = haversine(current_lat, current_lon, dest_lat, dest_lon)
    
    input_df = pd.DataFrame([{
        "distance_km": distance,
        "speed_kmph": speed,
        "hour": hour,
        "minute": minute,
        "traffic_level": traffic_val
    }])
    
    eta = model.predict(input_df)[0]
    st.success(f"⏱️ Predicted ETA: {round(eta)} minutes")

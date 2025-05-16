from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from math import radians, cos, sin, asin, sqrt

app = FastAPI()

# Load trained model
model = joblib.load("model.pkl")

# Input schema
class LocationInput(BaseModel):
    current_lat: float
    current_lon: float
    dest_lat: float
    dest_lon: float
    speed_kmph: float
    hour: int
    minute: int
    traffic_level: int  # 0 = Low, 1 = Medium, 2 = High

# Haversine distance
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in KM
    dlat = radians(lat2 - lat1)
    dlon = radians(dest_lon - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(dest_lat)) * sin(dlon/2)**2
    return R * 2 * asin(sqrt(a))

# Prediction route
@app.post("/predict-eta")
def predict_eta(data: LocationInput):
    distance = haversine(data.current_lat, data.current_lon, data.dest_lat, data.dest_lon)
    
    input_df = pd.DataFrame([{
        "distance_km": distance,
        "speed_kmph": data.speed_kmph,
        "hour": data.hour,
        "minute": data.minute,
        "traffic_level": data.traffic_level
    }])
    
    prediction = model.predict(input_df)[0]
    return {"predicted_eta_minutes": round(prediction)}

import pandas as pd
import joblib
from xgboost import XGBRegressor
from datetime import datetime
from math import radians, cos, sin, asin, sqrt

# Load data
df = pd.read_csv("C:/Users/ragha/py_file/car_location_detecter/vehicle_eta_data.csv")


# Feature engineering
df['hour'] = pd.to_datetime(df['time_of_day'], format='%H:%M').dt.hour
df['minute'] = pd.to_datetime(df['time_of_day'], format='%H:%M').dt.minute
df['traffic_level'] = df['traffic_level'].map({'Low': 0, 'Medium': 1, 'High': 2})

# Haversine distance
def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    return R * c

df['distance_km'] = df.apply(lambda row: haversine(row['current_lat'], row['current_lon'], row['dest_lat'], row['dest_lon']), axis=1)

features = ['distance_km', 'speed_kmph', 'hour', 'minute', 'traffic_level']
X = df[features]
y = df['eta_minutes']

# Train model
model = XGBRegressor()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

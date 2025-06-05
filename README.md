# Car Location Detector

This module is part of the [Vehicle ETA Prediction](https://github.com/Raghav077/vehicle_ETA_prediction) project. The purpose of this component is to detect and extract the current location of a vehicle, which is a critical input for accurately predicting estimated time of arrival (ETA).

## 📌 Overview

The `car_location_detecter` module is designed to:
- Extract the current GPS coordinates of a car
- Save the current location into a CSV file
- Act as a data source for the ETA prediction model

## 🗂️ Project Structure

```
car_location_detecter/
│
├── car_current_location.csv     # Stores the latest car location data
├── current_location.py          # Python script to get and save location data
└── __pycache__/                 # Bytecode cache (auto-generated)
```

## 🚀 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/Raghav077/vehicle_ETA_prediction.git
cd vehicle_ETA_prediction/car_location_detecter
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

This module may rely on external libraries like `geocoder` or `geopy`. Install any required packages:

```bash
pip install -r ../requirements.txt
```

### 4. Run the Script

To fetch the current location and save it:

```bash
python current_location.py
```

The output will be saved in a CSV file named `car_current_location.csv`.

## 📝 Output

The output CSV will contain:
- Latitude
- Longitude
- Timestamp

Example:
```csv
latitude,longitude,timestamp
28.7041,77.1025,2025-06-05 13:22:45
```

## 🔧 Configuration

- The script currently uses a placeholder/mock GPS system. You may update `current_location.py` to pull real-time GPS data from a device or API.

## 📌 Future Enhancements

- Live GPS tracking via mobile app/device
- Integration with Google Maps API for geocoding
- Real-time push to ETA prediction pipeline

## 📄 License

This project is open-source and available under the MIT License.

---

*Maintained as part of the Vehicle ETA Prediction system by [Raghav077](https://github.com/Raghav077).*
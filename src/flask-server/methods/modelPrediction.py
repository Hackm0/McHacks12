import pandas as pd
import joblib

model = joblib.load("methods/model/asbestos_model.pkl")

# Function to predict confidence for asbestos presence
def predict_asbestos(lon, lat, year_of_construction):
    """
    Predict the confidence of asbestos presence for a given location.

    Args:
    lon (float): Longitude of the location.
    lat (float): Latitude of the location.
    year_of_construction (int or float): Average construction year of the location.

    Returns:
    float: Confidence score for asbestos presence (0 to 1).
    """
    input_data = pd.DataFrame({'year_of_construction': [year_of_construction], 'lat': [lat], 'lon': [lon]})
    probability = model.predict_proba(input_data)[:, 1][0]
    return probability
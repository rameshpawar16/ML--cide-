import joblib
import pandas as pd

def predict(input_data):
    model = joblib.load("models/model.pkl")
    return model.predict(pd.DataFrame(input_data))
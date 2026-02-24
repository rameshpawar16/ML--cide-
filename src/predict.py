import joblib
import pandas as pd

def predict(input_data):
    model = joblib.load("models/model.pkl")
    if isinstance(input_data, list):
        input_data = [input_data]

    df = pd.DataFrame(input_data)
    return model.predict(pd.DataFrame(input_data))
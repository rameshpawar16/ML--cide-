import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

def train():
    df = pd.read_csv("data/processed.csv")

    X = df.drop("variety", axis=1)
    y = df["variety"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=500)
    model.fit(X_train, y_train)

    joblib.dump(model, "models/model.pkl")

if __name__ == "__main__":
    train()
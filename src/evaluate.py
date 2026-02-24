import pandas as pd
import joblib
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import sys

THRESHOLD = 0.80

def evaluate():
    df = pd.read_csv("data/processed.csv")
    X = df.drop("variety", axis=1)
    y = df["variety"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = joblib.load("models/model.pkl")
    predictions = model.predict(X_test)

    acc = accuracy_score(y_test, predictions)
    print(f"Accuracy: {acc}")

    if acc < THRESHOLD:
        print("Accuracy below threshold!")
        sys.exit(1)

if __name__ == "__main__":
    evaluate()
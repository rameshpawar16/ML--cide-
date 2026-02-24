import pandas as pd

def preprocess(input_path="data/raw.csv", output_path="data/processed.csv"):
    df = pd.read_csv(input_path)

    # Example cleaning
    df = df.dropna()
    df = df.sample(frac=1, random_state=42)

    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    preprocess()
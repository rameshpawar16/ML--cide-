from src.preprocess import preprocess
import os

def test_preprocess():
    preprocess()
    assert os.path.exists("data/processed.csv")
from src.predict import predict

def test_predict():
    sample = [[1, 2, 3, 4]]
    result = predict(sample)
    assert len(result) == 1
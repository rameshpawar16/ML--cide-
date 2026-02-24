from src.predict import predict

def test_predict():
    sample = [5.1,3.5,1.4,.2]
    result = predict(sample)
    assert len(result) == "Setosa"
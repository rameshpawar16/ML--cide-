from flask import Flask, request, jsonify
from src.predict import predict

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def prediction():
    data = request.json["data"]
    result = predict(data)
    return jsonify({"prediction": result.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
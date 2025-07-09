# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib

app = Flask(__name__)
CORS(app)

# Load your trained model
model = joblib.load("energy_model.pkl")  # make sure to save it first

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    df = pd.read_csv(file)
    
    # Adjust this part based on your model's expected input
    features = df.drop(columns=['Target'])  # or whatever column is the target
    
    predictions = model.predict(features).tolist()
    return jsonify({"predictions": predictions})

if __name__ == "__main__":
    app.run(debug=True)

# app.py

from flask import Flask, request, jsonify
from pycaret.classification import load_model, predict_model
import pandas as pd

app = Flask(__name__)

# Załaduj zapisany model
model = load_model('best_model')

@app.route('/predict', methods=['POST'])
def predict():
    # Pobierz dane z żądania
    data = request.get_json(force=True)

    # Konwertuj dane wejściowe do DataFrame
    input_data = pd.DataFrame([data['input']])

    # Wykonaj predykcję
    predictions = predict_model(model, data=input_data)
    output = {'prediction': int(predictions['Label'][0])}

    # Zwróć wynik jako JSON
    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

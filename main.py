from flask import Flask, request, jsonify
from pycaret.classification import load_model, predict_model
import pandas as pd
import traceback

app = Flask(__name__)

# Load the saved model
try:
    model = load_model('best_model')
except Exception as e:
    print("Error loading model:", e)
    traceback.print_exc()
    model = None

@app.route('/predict', methods=['POST'])
def predict():
    # Check if the model is loaded
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500

    # Check if the request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    # If the user does not select a file
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Read the CSV file into a pandas DataFrame
        input_data = pd.read_csv(file)
    except Exception as e:
        return jsonify({'error': f'Error reading CSV file: {str(e)}'}), 400

    try:
        # Perform predictions
        predictions = predict_model(model, data=input_data)
    except Exception as e:
        return jsonify({'error': f'Error making predictions: {str(e)}'}), 500

    # Convert predictions to JSON format
    output = predictions.to_dict(orient='records')

    # Return the predictions as JSON
    return jsonify({'predictions': output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

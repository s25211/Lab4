from flask import Flask, request, jsonify
from pycaret.classification import load_model, predict_model
import pandas as pd

app = Flask(__name__)

# Load the saved model
model = load_model('best_model')

@app.route('/predict', methods=['POST'])
def predict():
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
        return jsonify({'error': str(e)}), 400

    # Perform predictions
    predictions = predict_model(model, data=input_data)
    
    # Convert predictions to JSON format
    output = predictions.to_json(orient='records')

    # Return the predictions as JSON
    return jsonify({'predictions': output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

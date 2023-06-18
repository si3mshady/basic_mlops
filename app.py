from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('price_prediction_model.pkl', 'rb') as file:
    model = pickle.load(file)['model']

@app.route('/health', methods=['GET'])
def health():
    return jsonify(status='healthy')

@app.route('/predict_price', methods=['POST'])
def predict_price():
    # Retrieve feature values from the request
    features = request.get_json()

    # Perform price prediction
    test_values = np.array([list(features.values())]).astype(float)
    price_result = model.predict(test_values)
    # Return the predicted price
    return jsonify(predicted_price=float(price_result[0]))

if __name__ == '__main__':
    app.run(debug=True)



# curl -X POST -H "Content-Type: application/json" -d '{
#   "qty": 43,
#   "unit_price": 188,
#   "comp_1": 193,
#   "product_score": 4,
#   "comp_price_diff": 33
# }' http://localhost:5000/predict_price

# {
#   "predicted_price": 6287.2
# }

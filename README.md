To use this Flask app, make sure you have the trained model file (price_prediction_model.pkl) in the same directory as the app file. You can run the Flask app by executing the script, and it will start the server. The app will be accessible at http://localhost:5000.

The /health endpoint is a GET request that returns a JSON response indicating the health status of the application.

The /predict_price endpoint is a POST request that expects a JSON payload containing the feature values for the prediction. The app retrieves the features, performs the price prediction using the loaded model, and returns the predicted price as a JSON response.

You can test the /health endpoint by making a GET request to http://localhost:5000/health. To make a price prediction, send a POST request to http://localhost:5000/predict_price with a JSON payload containing the feature values. For example:# basic_mlops
# basic_mlops

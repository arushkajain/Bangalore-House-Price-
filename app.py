import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the trained machine learning model from the pickle file
with open("banglore_home_prices_model.pickle", "rb") as file:
    model = pickle.load(file)

@app.route("/predict_price", methods=["POST"])
def predict_price():
    data = request.get_json()
    area = data["area"]
    bhk = data["bhk"]
    bathrooms = data["bathrooms"]
    location = data["location"]

    # Preprocess the input data (e.g., convert location to a numerical value, perform feature scaling, etc.)
    # ...

    # Make the prediction using the loaded model
    price = model.predict([[area, bhk, bathrooms, location]])[0]

    # Return the predicted price as a JSON response
    return jsonify({"price": price})

if __name__ == "__main__":
    app.run(debug=True)

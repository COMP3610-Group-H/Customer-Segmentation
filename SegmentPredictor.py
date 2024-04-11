
from flask import Flask, request, jsonify
from joblib import load
import json

app = Flask(__name__)

# Load the saved logistic regression model
model = load('Model.joblib')

def parseJSON(formData):
    # data = json.loads(formData)
    jsonArray = list(formData.values())
    
    education_level = formData.get("Education")
    marital_status = formData.get("Marital_Status")

    print(education_level)  
    print(marital_status)

    




    return jsonArray


@app.route('/predict', methods=['POST'])
def predict():
    # Extract input features from the POST request
    data = request.get_json()

    features = parseJSON(data)
    # features = data['features']
    print(features)

    # Make a prediction
    # prediction = model.predict([features])
    prediction = []
    prediction.append(0)

    # Send back the prediction
    return jsonify({'prediction': int(prediction[0])})


if __name__ == '__main__':
    app.run(debug=True)

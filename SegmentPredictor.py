
from flask import Flask, request, jsonify
from joblib import load
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Load the saved logistic regression model
model = load('Model.joblib')


def encodeEducation(education):
    encode = []

    if(education == "Graduation"):
        # encode.append([1, 0, 0])
        encode = [1, 0, 0]
        # print(education)
    elif (education == "PhD"):
        # encode.append([0, 0, 1])
        encode = [0, 0, 1]

        # print(education)
    elif(education == "Master"): 
        # encode.append([0, 1, 0])
        encode = [0, 1, 0]
        # print(education)  
    elif(education == "Foundational"):
        # encode.append([0, 0 , 0])
        encode = [0, 0 , 0]
        # print(education)
    return encode

def encodeMaritalStatus(marriage):
    if(marriage == "Relationship"):
        return 0
    elif(marriage == "Single"):
        return 1



def parseJSON(formData):
    # data = json.loads(formData)
    jsonArray = list(formData.values())
    
    education_level = formData.get("Education")
    marital_status = formData.get("Marital_Status")

    print(education_level)  
    print(marital_status)

    
    del jsonArray[0]

    del jsonArray[1:3]
    # del jsonArray[2]


    print(encodeEducation(education_level))
    jsonArray.extend(encodeEducation(education_level))
    jsonArray.append(encodeMaritalStatus(marital_status))

    return jsonArray


@app.route('/predict', methods=['POST'])
def predict():
    # Extract input features from the POST request
    data = request.get_json()

    features = parseJSON(data)
    # features = data['features']
    print(features)

    # Make a prediction
    prediction = model.predict([features])
    # prediction = []
    # prediction.append(0)

    # Send back the prediction
    return jsonify({'prediction': int(prediction[0])})


if __name__ == '__main__':
    app.run(debug=True)

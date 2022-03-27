from flask import Flask, request
import pickle

import numpy as np


classifier = pickle.load(open('classifier1.pickle', 'rb'))
scaler = pickle.load(open('sc1.pickle', 'rb'))

app = Flask(__name__)

@app.route('/model', methods=['POST'])
def hello_world():
    request_data = request.get_json(force=True)
    
    age = request_data['age']
    salary = request_data['salary']
    
    prediction = classifier.predict(scaler.transform(np.array([[age,salary]])))[:,1]
    
    
    return "The prediction is  {} model".format(prediction)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
    
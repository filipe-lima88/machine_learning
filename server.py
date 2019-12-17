import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask('MachineLearningFlaskServer')
model = pickle.load(open('modelo.pkl','rb'))

@app.route('/api', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([[np.array(data['anosDeExperiencia'])]])
    output = prediction[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
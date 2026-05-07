from flask import Flask, request, jsonify
from flask_cors import CORS
from catboost import CatBoostClassifier
import pandas as pd

app = Flask(__name__)
CORS(app)

model = CatBoostClassifier()
model.load_model("heart_model.cbm")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

    return jsonify({
        "prediction": "Heart Disease Detected" if prediction == 1 else "No Heart Disease"
    })

if __name__ == "__main__":
=======
from flask import Flask, request, jsonify
from flask_cors import CORS
from catboost import CatBoostClassifier
import pandas as pd

app = Flask(__name__)
CORS(app)

model = CatBoostClassifier()
model.load_model("heart_model.cbm")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

    return jsonify({
        "prediction": "Heart Disease Detected" if prediction == 1 else "No Heart Disease"
    })

if __name__ == "__main__":
    app.run(debug=True)
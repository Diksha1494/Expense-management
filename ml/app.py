from flask import Flask, request, jsonify
import pickle

# Load model
with open("expense_model.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    desc = data.get("description", "")
    if not desc:
        return jsonify({"error": "No description provided"}), 400

    X = vectorizer.transform([desc])
    pred = model.predict(X)[0]

    return jsonify({"category": pred})

if __name__ == "__main__":
    app.run(port=5000, debug=True)

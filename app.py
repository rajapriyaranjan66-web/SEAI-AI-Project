from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Health AI API Running"

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data
        data = request.get_json()

        # Validate input
        if not data or "input" not in data:
            return jsonify({"error": "Invalid input format"}), 400

        values = data["input"]

        # Check if list
        if not isinstance(values, list):
            return jsonify({"error": "Input must be a list"}), 400

        # Simple model logic (dummy AI)
        result = sum(values)

        if result > 5:
            prediction = "High Risk"
        else:
            prediction = "Low Risk"

        # Return response
        return jsonify({
            "input": values,
            "sum": result,
            "prediction": prediction
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run server
if __name__ == '__main__':
    app.run(debug=True)

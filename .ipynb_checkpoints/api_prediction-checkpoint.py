from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1.0/predict')
def predict():
    try:
        num1 = float(request.args.get("num1"))
        num2 = float(request.args.get("num2"))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input type"})
    
    sum_values = num1 + num2
    if sum_values > 5.8:
        result = 1
    else:
        result = 0

    return jsonify({"prediction": result, "features": {"num1": num1, "num2": num2}})

if __name__ == '__main__':
    app.run(port=5000)

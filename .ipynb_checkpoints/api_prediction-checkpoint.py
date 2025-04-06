###

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1.0/predict')
def predict():
    try:
        x1 = float(request.args.get("x1"))
        x2 = float(request.args.get("x2"))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input type"})
        
    sum_values = x1 + x2
    if sum_values > 5.8:
        result = 1
    else: 
        result = 0
     return jsonify({"prediction": result, "features": {"num1": x1, "num2": x2}})
            
if __name__ == ('__main__'):
    app.run(port = 5003)
###

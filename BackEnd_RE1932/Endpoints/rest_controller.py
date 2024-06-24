import os

from flask_cors import CORS
from flask import Flask, jsonify

from scripts.trulia_exp import get_trulia_data

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/properties', methods=['GET'])
def get_properties():
    print("Got Request")
    data = get_trulia_data()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host=os.getenv('FLASK_RUN_HOST', '0.0.0.0'), port=int(os.getenv('FLASK_RUN_PORT', 5001)))
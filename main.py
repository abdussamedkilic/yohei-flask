from flask import Flask, request, jsonify, abort
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Opening JSON file
f = open('data.json',)
data = json.load(f)

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.route('/<name>')
def getUserByName(name):
    users = data["users"]
    if users is None:
        abort(404, description="JSON error")
    try:
        return jsonify(data["users"][name])
    except:
        abort(404, description="User not found")

if __name__ == '__main__':
    app.run()
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    response = {"status": "on"}
    return jsonify(**response)

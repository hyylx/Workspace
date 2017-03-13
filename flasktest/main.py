from flask import Flask, jsonify
from gw_quppa import QuppaAPI
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api")
def api():
    return jsonify({'test' : 23})


if __name__ == "__main__":
    app.run(debug=True , host='0.0.0.0')


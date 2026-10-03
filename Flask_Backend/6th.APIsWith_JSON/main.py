from flask import Flask, jsonify

APIs = Flask(__name__)

@APIs.route("/")
def apiJSON():
    data = {
        "message" : "Namaste! Welcome student."
    }
    return jsonify(data), 200

if __name__ == "__main__":
    APIs.run(debug=True)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

@app.route("/s")
def hello2():
    return "hello saumya"

# app.run()
app.run(debug=True)
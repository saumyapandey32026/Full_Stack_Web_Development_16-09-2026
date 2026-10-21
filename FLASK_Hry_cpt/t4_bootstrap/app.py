from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")
@app.route("/b")
def helloB():
    return render_template("bootstrap.html")

app.run(debug=True)
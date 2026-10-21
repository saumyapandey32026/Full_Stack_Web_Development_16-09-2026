from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/about")
def hello2():
    name = "ram"
    return render_template("about.html", naam = name)

app.run(debug=True)
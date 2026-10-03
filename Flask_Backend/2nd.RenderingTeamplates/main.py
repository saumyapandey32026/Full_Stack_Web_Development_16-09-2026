from flask import Flask, render_template

site = Flask(__name__)

@site.route("/")
def my_website():
    return render_template("index.html")

@site.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    site.run(debug=True)
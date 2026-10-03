from flask import Flask, render_template

temp = Flask(__name__)

@temp.route("/")
def templ():
    return render_template("index.html")
@temp.route("/contact")
def cont():
    return render_template("contact.html")
if __name__ == "__main__":
    temp.run(debug=True)








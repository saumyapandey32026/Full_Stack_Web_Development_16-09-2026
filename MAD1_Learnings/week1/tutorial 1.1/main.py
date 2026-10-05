from flask import Flask, render_template

MAD1 = Flask(__name__)

@MAD1.route("/")
def mad1():
    return render_template("index.html")

if __name__ == "__main__":
    MAD1.run(debug=True)

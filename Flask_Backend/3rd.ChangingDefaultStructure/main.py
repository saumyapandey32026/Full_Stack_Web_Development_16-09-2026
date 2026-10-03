from flask import Flask, render_template, url_for  

custom = Flask(__name__, static_folder="assets", static_url_path="/assets")

@custom.route("/")
def defaultChg():
    # print("/assets")
    print(url_for("static",filename="style.css"))
    return render_template("index.html")

if __name__ == "__main__":
    custom.run(debug=True)
from flask import Flask, render_template, request

jinjaT = Flask(__name__)

@jinjaT.route("/", methods=["GET","POST"])
def jin():
    if request.method == "POST":
        name = request.form["Cname"]
        psw = request.form["Cpass"]

        friends = ["ram", "radha", "siya", "kanha", "kitab"]
        header = "<h1>WELCOME PAGE</h1>"
        return render_template("welcome.html", name = name, password = psw , frds = friends, header = header)
    else:
        return render_template("login.html")
if __name__ == "__main__":
    jinjaT.run(debug=True)

















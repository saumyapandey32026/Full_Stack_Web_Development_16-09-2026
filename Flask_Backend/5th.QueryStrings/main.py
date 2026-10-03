from flask import Flask, render_template, request

QS = Flask(__name__)

@QS.route("/", methods=["GET","POST"])
def qsLearn():
    if request.method == "POST":
        name = request.form["user"]
        return f"<h2>welcome {name}! </h2>"
    else:
    # 2nd.
        nameCl = request.args.get("name", default="ASHUTOSH")
        subP = request.args.get("subject")
        print(nameCl)
        return render_template("index.html", nameJ = nameCl, sub = subP)

    # 1st.
        # query = request.args.get("qu")
        # print(query)
        # return render_template("index.html", query=query)
if __name__ == "__main__":
    QS.run(debug=True)
from flask import Flask, render_template, url_for, request

final = Flask(__name__)

@final.route("/")
def deployFinal():
    return render_template("index.html")

@final.route("/ask", methods=["POST"])
def ask():
    return ""
    # question = request.form.get("question")
    # l1 = ["hi", "hello","name","how"]
    # return render_template("answer.html", lst1=l1, q = question)

@final.route("/summarize", methods=["POST"])
def summarize():
    return ""
    # email = request.form.get("email")
    # l2 = ["good", "bad", "sad", "happy", "angry"]
    # return render_template("summary.html", lst2 = l2, e = email)


if __name__ == "__main__":
    final.run(debug=True)


































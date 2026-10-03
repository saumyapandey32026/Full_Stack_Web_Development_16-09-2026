from flask import Flask, render_template, flash, redirect, url_for, request

msgF = Flask(__name__)
msgF.secret_key = "any message or key"

@msgF.route("/", methods=["GET", "POST"])
def msgFlash():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # .strip() यह चेक करता है कि यूजर ने सिर्फ 'Space' तो नहीं दबा दिया
        if username and password and username.strip() and password.strip():
            flash(f"Welcome {username}! You are successfully logged in!", "login_success")
            return render_template("index.html")
        else:
            flash("Please enter both username and password!")
            return redirect(url_for("login"))
    else:
        return redirect(url_for("login"))

@msgF.route("/login")
def login():
    return render_template("login.html")
    # return "<h1>login page</h1>"

@msgF.route("/contact")
def msgFlash2():
    flash("contact timing is 10-2",  "contact_info")
    return render_template("contact.html")

if __name__ == "__main__":
    msgF.run(debug=True)
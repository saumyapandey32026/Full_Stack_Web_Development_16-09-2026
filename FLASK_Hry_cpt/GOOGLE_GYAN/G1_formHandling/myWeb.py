from flask import Flask, render_template, request

the_flask_app = Flask(__name__)

# 🌟 STEP 1: Pehle page ka route (Yahan user sirf form dekhega)
@the_flask_app.route("/")
def show_empty_form():
    # Chupchap form wala HTML page load kar do
    return render_template("form_page.html")


# 🌟 STEP 2: Dusre page ka route (Yahan form submit hone ke baad data aayega)
# Kyunki yahan data submit hokar AA RAHA HAI, isliye methods=["POST"] likhna zaroori hai
@the_flask_app.route("/dashboard", methods=["POST"])
def display_user_details():
    
    # HTML form se teeno fields ka data unke 'name' attribute se uthaya  => "html_name_field", "html_email_field" ,"html_password_field"
    captured_name = request.form.get("html_name_field")
    captured_email = request.form.get("html_email_field")
    captured_password = request.form.get("html_password_field") # Iska use aap verification ke liye kar sakti hain
    
    # Saare data ko lekar ek naya HTML page render kiya aur variables ko wahan bhej diya
    return render_template(
        "welcome_page.html",
        user_name_to_display = captured_name,
        user_email_to_display = captured_email
    )

if __name__ == "__main__":
    the_flask_app.run(debug=True)

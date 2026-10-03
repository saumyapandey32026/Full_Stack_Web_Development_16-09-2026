from flask import Flask, render_template, url_for, request

forms = Flask(__name__)

# @forms.route("/form")
# def form():
#     return render_template("index.html")

# @forms.route("/handle_login", methods=["GET", "POST"])
# def login():
#     # 1st method
#     # return render_template("login.html")
#     # 2nd method
#     # if request.method == "POST":
#     #     print("post req")
#     # if request.method == "GET":
#     #     print("get req")
#     # return "<h3>Login Completed</h3>"                  # without return error aayega  
#     # return render_template("login.html")
#     # 3rd method. to access form data 
#     if request.method == "POST":
#         print(request.form)
#         client = request.form["username"]
#         clientPassword = request.form["password"]
#         return f"<p>welcome {client}! your password is {clientPassword}, btw SORRY maine aapka password bhi print kar diya...</p>"
    
    # return "<p>completed</p>"

## 💙💙💙💙💙💙💙💙💙💙💙💙💙💙💙💙💙💙  both routes ko merge karna ya dono ka kaam ek hi route me karna 

@forms.route("/form", methods=["GET","POST"])
def form():
    if request.method == "POST":
        client = request.form["username"]
        clientPassword = request.form["password"]
        return f"<p>welcome {client}! your password is {clientPassword}, btw SORRY maine aapka password bhi print kar diya...</p>"
    else:
        return render_template("index.html")

if __name__ == "__main__":
    forms.run(debug=True)
# from flask import Flask

# app = Flask(__name__)

# # URL => endpoint /
# @app.route("/")
# def hello_world():
#     return "<p>Hello World!</p>"

# app.run(debug=True)
# app.run(debug=True, port=5500)
# app.run(debug=True, host='0.0.0.0', port=8080)


# from flask import Flask

# app = Flask(__name__)

# # URL => endpoint /
# @app.route("/")
# def hello_world():
#     return "<p>Hello World!</p>"
# @app.route("/cya")
# def hello_Cya():
#     return "<p>Hello Catalytic Dhairya Family! Even if in Future, no problem at all.</p>"

# app.run(debug=True, port= 5500)

from flask import Flask

app = Flask(__name__)

# URL => endpoint /
@app.route("/")
def hello_world():
    return "<h1>Hello World!</h1>"
@app.route("/cya")
def hello_Cya():
    return "<h1>Hello Catalytic Dhairya Family! Even if in Future, no problem at all.</h1>"

if __name__ == "__main__":
    app.run(debug=True)
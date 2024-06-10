from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "<h1>Welcome to Home Page!</h1>"


@app.route("/about")
def about():
    return "<h1>Welcome to About Page</h1>"


@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>Hi {name}, you are welcome to this page!</h1>"


@app.route("/addition/<int:num>")
def addition(num):
    return f"<h1> Input is {num}, output is {num + 10} </h1>"


if __name__ == "__main__":
    app.run(debug=True)

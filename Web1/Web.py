from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")

@app.route("/users/<username>")
def user(username):
    return "Hello my name is " + username + ", welcome to my page <3"

@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    a = int(a)
    b = int(b)
    return "{0}+{1} = {2}".format(a, b, a+b)

if __name__ == '__main__':
    app.run()

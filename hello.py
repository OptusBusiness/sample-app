from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"


@app.route("/devops")
def devops():
    f = open("devops.html", "r")
    return f.read()


if __name__ == "__main__":
    app.run()

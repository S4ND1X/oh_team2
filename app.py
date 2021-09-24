from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>This is the homepage for Team 2 Portfolio</h1>"


@app.route("/jorge")
def jorge():
    return render_template("jorge.html")
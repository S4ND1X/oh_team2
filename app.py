from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>This is the homepage for Team 2 Portfolio</h1>"
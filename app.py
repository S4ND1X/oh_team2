from flask import Flask, render_template

app = Flask(__name__)


# This is the route that will display the landing page.
@app.route("/")
def index():
    return render_template("landing_page.html")


# This is the route that will display jorge portfolio.
@app.route("/jorge")
def jorge():
    return render_template("jorge.html")
    

# This is the route that will display Onyemowo portfolio.
@app.route("/onyemowo")
def onyemowo():
    return render_template("onyemowo.html")


# This is the route that will display Long portfolio.
@app.route("/long")
def long():
    return render_template("long_phan.html")
    
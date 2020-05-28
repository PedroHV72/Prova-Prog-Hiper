from application import app
from flask import render_template


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/categoria")
def home():
    return render_template("categorias.html")

@app.route("/pre")
def prefire():
    return render_template("pre.html")

@app.route("/triple")
def triplekill():
    return render_template("triple.html")

@app.route("/headshot")
def hs():
    return render_template("headshot.html")
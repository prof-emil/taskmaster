from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods={"GET", "POST"})
def login():
    return render_template("login.html")

@app.route("/usuario")
def usuario():
    return "Usuário"

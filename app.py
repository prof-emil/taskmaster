from flask import Flask, render_template, request, flash, redirect
import re

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods={"GET", "POST"})
def login():
    if(request.method == "POST"):
        username = request.form["username"]
        password = request.form["pwd"]
        if not login_validation(username, password):
#            flash("Credênciais Invalidas")
            return redirect("/login") 
    return render_template("login.html")

@app.route("/usuario")
def usuario():
    return "Usuário"


def login_validation(username, password):
    print(f"{username}, {password}")
    valida_apenasAlphanumericos = r"^[a-zA-Z0-9]+$"
    if not re.search(valida_apenasAlphanumericos, username):
        return False

    valida_maiusculas = r"[A-Z]"
    valida_caracteresEspeciais = r"[!@#$%^&*()_+-=]"

    if not re.search(valida_maiusculas, password):
        return False

    if not re.search(valida_caracteresEspeciais, password):
        return False

    return True



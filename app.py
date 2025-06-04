from config import *
from model import *

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/listagem")
def listagem():
    return render_template("listagem.html")

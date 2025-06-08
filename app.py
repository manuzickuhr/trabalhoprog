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
    with db_session:
        pokemons = Pokemon.select()
        return render_template('cadastro.html', pokemons=pokemons)
    

@app.route("/listagem")
def listagem():
    with db_session:
        pokemons = Pokemon.select() 
        return render_template("listagem.html", pokemons=pokemons)     

@app.route("/adicionar_pokemon")
def adicionar_pokemon():
    nome = request.args.get("nome")
    idpokedex = request.args.get("idpokedex")
    tipo_primario = request.args.get("tipo_primario")
    tipo_secundario = request.args.get("tipo_secundario")
    geracao = request.args.get("geracao")
    regiao = request.args.get("regiao")
    genero = request.args.get("genero")
    tem_evolucao = request.args.get("tem_evolucao")
    evolui_de = request.args.get("evolui_de")
    imagem = request.args.get("imagem")
    
    with db_session:
        p = Pokemon(
            nome=nome,
            idpokedex=int(idpokedex) if idpokedex else None,
            tipo_primario=tipo_primario,
            tipo_secundario=tipo_secundario,
            geracao=int(geracao) if geracao else None,
            regiao=regiao,
            genero=genero,
            tem_evolucao=tem_evolucao,
            evolui_de=int(evolui_de) if evolui_de else None,
            imagem=imagem
        )



        commit()
    return redirect("listagem")
from flask import Flask, render_template, request, redirect, url_for, abort
from config import db, db_session
from model import Pokemon
from pony.orm import commit, select

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/cadastro")
def cadastro():
    with db_session:
        pokemons = list(Pokemon.select())
        return render_template('cadastro.html', pokemons=pokemons)

@app.route("/listagem")
def listagem():
    with db_session:
        pokemons = Pokemon.select()
        return render_template("listagem.html", pokemons=pokemons)

# Alteração importante: usar POST para adicionar Pokémon
@app.route("/adicionar_pokemon", methods=["GET", "POST"])
def adicionar_pokemon():
    if request.method == "POST":
        nome = request.form.get("nome")
        idpokedex = request.form.get("idpokedex")
        tipo_primario = request.form.get("tipo_primario")
        tipo_secundario = request.form.get("tipo_secundario")
        geracao = request.form.get("geracao")
        regiao = request.form.get("regiao")
        genero = request.form.get("genero")
        tem_evolucao = request.form.get("tem_evolucao")
        evolui_de = request.form.get("evolui_de")
        imagem = request.form.get("imagem")

        with db_session:
            Pokemon(
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

        return redirect(url_for("listagem"))

    # Se for GET, exibe o formulário (ou redireciona para cadastro)
    return redirect(url_for("cadastro"))

@app.route("/editar/<int:id>")
def editar_pokemon(id):
    with db_session:
        pokemon = Pokemon.get(id=id)
        if not pokemon:
            return "Pokémon não encontrado", 404
        pokemons = Pokemon.select()
        return render_template("editar.html", pokemon=pokemon, pokemons=pokemons)

@app.route("/atualizar", methods=["POST"])
def atualizar_pokemon():
    id = int(request.form["id"])
    
    with db_session:
        pokemon = Pokemon.get(id=id)
        if not pokemon:
            return "Pokémon não encontrado", 404

        pokemon.nome = request.form["nome"]
        pokemon.idpokedex = int(request.form["idpokedex"]) if request.form["idpokedex"] else None
        pokemon.tipo_primario = request.form["tipo_primario"]
        pokemon.tipo_secundario = request.form["tipo_secundario"]
        pokemon.geracao = int(request.form["geracao"]) if request.form["geracao"] else None
        pokemon.regiao = request.form["regiao"]
        pokemon.genero = request.form["genero"]
        pokemon.tem_evolucao = request.form["tem_evolucao"]
        #pokemon.evolui_de = int(request.form["evolui_de"]) if request.form["evolui_de"] else None
        # Tentativa de conversão para int, se falhar, define como None, antes ele tentava converter o none para int que dava erro
        try:
            pokemon.evolui_de = int(request.form["evolui_de"])
        except (ValueError, TypeError):
            pokemon.evolui_de = None
        
        pokemon.imagem = request.form["imagem"]

        commit()

    return redirect(url_for("listagem"))

@app.route('/excluir/<int:id>')
def excluir_pokemon(id):
    with db_session:
        pokemon = Pokemon.get(id=id)  # busca o pokemon pelo id
        if not pokemon:
            abort(404)  # não achou, retorna erro 404
        pokemon.delete()  # exclui o registro
    return redirect(url_for('listagem'))


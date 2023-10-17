from flask import Flask, render_template
from requests import request
from models.pokemon import Pokemon
from flask import request
import requests
import json

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/buscar", methods = ["GET","post"])
def buscar():
    pokemon = Pokemon(request.form["nome"].lower(), "")
    try:
        response = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.nome}").text)    
        result = response["sprites"]
        result = result["front_default"]        
        pokemon.foto = result
    except:
        return "Pokemon não encontrado!"

    return render_template("index.html",
    nome = pokemon.nome,
    foto = pokemon.foto    
    )

if __name__ == "__main__":
    app.run(debug=True)
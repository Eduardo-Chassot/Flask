from flask import Flask #Importando Flask

app = Flask(__name__)

@app.route("/") #Le a URL do site#
def hello_world(): #Define oque será feito em tal URL#
    return "<p>Bom Dia, professor! Tente adicionar um 'nota10' ao final da url</p>"

@app.route("/nota10") #Le a URL do site#
def nota10(): #Define oque será feito em tal URL#
    return "<h1>É bem facil fazer isso com flask</h1>"
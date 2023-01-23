#importando bibliotecas
from flask import Flask, render_template, request, flash, redirect, jsonify
import math
#definindo local do arquivo html para renderização da APi 
app = Flask(__name__, template_folder='templates')
#definindo rotas e metodos e iniciando app.
@app.route("/", methods=['GET', "POST"])
#função para renderização de documento html
def index():
    return render_template("index.html")
#criando rota
@app.route("/calcular", methods=['GET', "POST"])
#função para calcular o valor da hipotenusa
def calcula():
#requisitando valor inserido no forms no campo "cateto adjacente"
    ca = request.args.get('ca', default= 0.0, type=float)
   #requisitando valor do campo "cateto oposto no forms"
    co = request.args.get('co', default= 0.0, type=float)
    #inicio de calculo 
    potoop=math.pow(co,2)
    potadj=math.pow(ca, 2)
    soma=potadj+potoop
    h = soma **(1/2)
    print(ca, co, h)
    #adicionando variaveis para uso web
    response = {"Cateto Adjacente":ca, "Cateto Oposto": co, "hipotenusa":h}
    return jsonify(response)
if __name__ == "__main__":


#debugando o codigo
    app.run(debug=True)
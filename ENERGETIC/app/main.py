from flask import Flask, render_template, request

app = Flask(__name__, template_folder="../templates")

def calcular_excedente_deficit(injecao_diaria, consumo_diario):
    if injecao_diaria > consumo_diario:
        excedente = injecao_diaria - consumo_diario
        deficit = 0
    else:
        deficit = consumo_diario - injecao_diaria
        excedente = 0
    return excedente, deficit

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/calcular", methods=["POST"])
def calcular():
    injecao_diaria = float(request.form['injecao_diaria'])
    injetado_total = float(request.form['injetado_total'])
    consumo_total_hoje = float(request.form['consumo_total_hoje'])
    consumo_total_ontem = float(request.form['consumo_total_ontem'])

    consumo_diario = consumo_total_hoje - consumo_total_ontem
    excedente, deficit = calcular_excedente_deficit(injecao_diaria, consumo_diario)

    return render_template('result.html', excedente=excedente, deficit=deficit)

if __name__ == '__main__':
    app.run()

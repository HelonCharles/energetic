from flask import Flask, render_template, request
from utils import calcular_excedente_deficit, salvar_dados_csv
import os
from datetime import datetime

app = Flask(__name__, template_folder="../templates")
csv_filepath = os.path.join(os.path.dirname(__file__), '../data/registros.csv')

@app.route("/", methods=["GET", "POST"])
def home():
    resultado = None
    erro = None
    consumo_diario = None
    if request.method == "POST":
        try:
            injecao_diaria = float(request.form['injecao_diaria'])
            injetado_total = float(request.form['injetado_total'])
            consumo_total_hoje = float(request.form['consumo_total_hoje'])
            consumo_total_ontem = float(request.form['consumo_total_ontem'])
            geracao_diaria_placas = float(request.form['geracao_diaria_placas'])  # Novo campo
            hora_registro_placas = request.form['hora_registro_placas']  # Novo campo

            # Data e hora inseridas pelo usuário
            data_registro_usuario = request.form['data_registro_usuario']
            hora_registro_usuario = request.form['hora_registro_usuario']

            # Calcular o consumo diário
            consumo_diario = consumo_total_hoje - consumo_total_ontem

            excedente, deficit = calcular_excedente_deficit(injecao_diaria, consumo_diario)

            resultado = {'excedente': excedente, 'deficit': deficit}

            # Data e hora do registro pelo sistema para consistência
            data_registro_sistema = datetime.now().strftime("%Y-%m-%d")
            hora_registro_sistema = datetime.now().strftime("%H:%M:%S")

            # Dados a serem salvos no CSV
            dados_csv = [
                injecao_diaria, consumo_diario, 
                injetado_total, consumo_total_hoje,
                hora_registro_usuario, geracao_diaria_placas,  # Atualizado para usar o campo inserido pelo usuário
                data_registro_usuario, hora_registro_placas  # Atualizado para usar o campo inserido pelo usuário
            ]
            salvar_dados_csv(csv_filepath, dados_csv)
        except ValueError as e:
            erro = f"Erro de entrada: {str(e)}. Certifique-se de inserir números válidos."
    
    return render_template('home.html', resultado=resultado, erro=erro, consumo_diario=consumo_diario)

if __name__ == '__main__':
    app.run(debug=True)

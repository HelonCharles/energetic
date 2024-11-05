import csv
from datetime import datetime

def calcular_excedente_deficit(injecao_diaria, consumo_diario):
    if injecao_diaria > consumo_diario:
        excedente = injecao_diaria - consumo_diario
        deficit = 0
    else:
        deficit = consumo_diario - injecao_diaria
        excedente = 0
    return excedente, deficit

def salvar_dados_csv(filepath, dados):
    # Verificar se o arquivo CSV já existe
    try:
        with open(filepath, 'r', newline='') as csvfile:
            pass
    except FileNotFoundError:
        # Se o arquivo não existe, criar e adicionar cabeçalho
        with open(filepath, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                'COD-24(INJETADO DIÁRIA)-MEDIDOR', 'COD-124(CONSUMO DIÁRIO)-MEDIDOR',
                'COD-103(INJETADO TOTAL)-MEDIDOR', 'COD-03(CONSUMO TOTAL)-MEDIDOR',
                'HORA DO REGISTRO-MEDIDOR', 'GERAÇÃO DIÁRIA(PLACAS)', 
                'DATA', 'HORA DO REGISTRO-APP PLACAS'
            ])
    # Salvar os dados no arquivo CSV
    with open(filepath, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(dados)

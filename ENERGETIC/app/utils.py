import csv
import os
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
    cabeçalho = [
        'COD-24(INJETADO DIÁRIA)-MEDIDOR', 'COD-124(CONSUMO DIÁRIO)-MEDIDOR',
        'COD-103(INJETADO TOTAL)-MEDIDOR', 'COD-03(CONSUMO TOTAL)-MEDIDOR',
        'HORA DO REGISTRO-MEDIDOR', 'GERAÇÃO DIÁRIA(PLACAS)', 
        'DATA', 'HORA DO REGISTRO-APP PLACAS'
    ]
    file_exists = os.path.isfile(filepath)
    
    with open(filepath, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(cabeçalho)
        writer.writerow(dados)

def limpar_csv(filepath):
    cabeçalho = [
        'COD-24(INJETADO DIÁRIA)-MEDIDOR', 'COD-124(CONSUMO DIÁRIO)-MEDIDOR',
        'COD-103(INJETADO TOTAL)-MEDIDOR', 'COD-03(CONSUMO TOTAL)-MEDIDOR',
        'HORA DO REGISTRO-MEDIDOR', 'GERAÇÃO DIÁRIA(PLACAS)', 
        'DATA', 'HORA DO REGISTRO-APP PLACAS'
    ]
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(cabeçalho)

def ler_dados_csv(filepath):
    with open(filepath, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Pular cabeçalho
        return [row for row in reader]

def atualizar_registro_csv(filepath, index, novos_dados):
    registros = ler_dados_csv(filepath)
    registros[index] = novos_dados

    cabeçalho = [
        'COD-24(INJETADO DIÁRIA)-MEDIDOR', 'COD-124(CONSUMO DIÁRIO)-MEDIDOR',
        'COD-103(INJETADO TOTAL)-MEDIDOR', 'COD-03(CONSUMO TOTAL)-MEDIDOR',
        'HORA DO REGISTRO-MEDIDOR', 'GERAÇÃO DIÁRIA(PLACAS)', 
        'DATA', 'HORA DO REGISTRO-APP PLACAS'
    ]
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(cabeçalho)
        writer.writerows(registros)

def excluir_registro_csv(filepath, index):
    registros = ler_dados_csv(filepath)
    registros.pop(index)

    cabeçalho = [
        'COD-24(INJETADO DIÁRIA)-MEDIDOR', 'COD-124(CONSUMO DIÁRIO)-MEDIDOR',
        'COD-103(INJETADO TOTAL)-MEDIDOR', 'COD-03(CONSUMO TOTAL)-MEDIDOR',
        'HORA DO REGISTRO-MEDIDOR', 'GERAÇÃO DIÁRIA(PLACAS)', 
        'DATA', 'HORA DO REGISTRO-APP PLACAS'
    ]
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(cabeçalho)
        writer.writerows(registros)

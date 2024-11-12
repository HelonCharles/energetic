#arquivo utils.py
import csv
import os

def calcular_excedente_deficit(geracao_diaria_placas, consumo_diario):
    injecao_diaria = round(geracao_diaria_placas - consumo_diario, 2)
    if geracao_diaria_placas > consumo_diario:
        excedente = injecao_diaria
        deficit = 0
    else:
        excedente = 0
        deficit = injecao_diaria
    return round(excedente, 2), round(deficit, 2), round(injecao_diaria, 2)

def salvar_dados_csv(filepath, dados):
    cabeçalho = [
        'INJETADO DIÁRIA-MEDIDOR', 'COD-103(INJETADO TOTAL)-MEDIDOR',
        'CONSUMO DIÁRIO-MEDIDOR', 'COD-03(CONSUMO TOTAL)-MEDIDOR',
        'HORA DO REGISTRO-MEDIDOR', 'GERAÇÃO DIÁRIA-PLACAS',
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
        'INJETADO DIÁRIA-MEDIDOR', 'COD-103(INJETADO TOTAL)-MEDIDOR',
        'CONSUMO DIÁRIO-MEDIDOR', 'COD-03(CONSUMO TOTAL)-MEDIDOR',
        'HORA DO REGISTRO-MEDIDOR', 'GERAÇÃO DIÁRIA-PLACAS',
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
        'INJETADO DIÁRIA-MEDIDOR', 'COD-103(INJETADO TOTAL)-MEDIDOR',
        'CONSUMO DIÁRIO-MEDIDOR', 'COD-03(CONSUMO TOTAL)-MEDIDOR',
        'HORA DO REGISTRO-MEDIDOR', 'GERAÇÃO DIÁRIA-PLACAS',
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
        'INJETADO DIÁRIA-MEDIDOR', 'COD-103(INJETADO TOTAL)-MEDIDOR',
        'CONSUMO DIÁRIO-MEDIDOR', 'COD-03(CONSUMO TOTAL)-MEDIDOR',
        'HORA DO REGISTRO-MEDIDOR', 'GERAÇÃO DIÁRIA-PLACAS',
        'DATA', 'HORA DO REGISTRO-APP PLACAS'
    ]
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(cabeçalho)
        writer.writerows(registros)

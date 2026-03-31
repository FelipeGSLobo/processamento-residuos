import json
import csv
import math
from numbers import Number

def getCsvData(path):
    csv_data = []
    with open(path, "r", newline="", encoding="utf-8") as f:
        leitor = csv.DictReader(f, fieldnames=["residuo", "peso"])
        for linha in leitor:
            valor_valido = getValidData(linha["peso"])
            if valor_valido is None:
                continue
            data = {"residuo": linha["residuo"], "peso": valor_valido}
            csv_data.append(data)
    return csv_data

def getValidData(value):
    try:
        if isinstance(value, str):
            value = value.strip().replace(',', '.')
        valid_value = float(value)
        if math.isnan(valid_value):
            print(f"Valor de peso inválido (NaN): '{value}'")
            return None
    except (ValueError, TypeError, AttributeError):
        print(f"Valor de peso inválido (Erro de conversão): '{value}'")
        return None
    if valid_value <= 0:
        print(f"Valor de peso inválido (Menor ou igual a 0): '{value}'")
        return None
    return valid_value

print(getCsvData("./residuos2.csv"))

def exportar_dados(dados, resumo, nome_arquivo="exportacao"):
    with open(f"{nome_arquivo}.json", "w", encoding="utf-8") as f_json:
        json.dump(resumo, f_json, ensure_ascii=False, indent=4)
        
    with open(f"{nome_arquivo}.csv", "w", newline="", encoding="utf-8") as f_csv:
        cabecalho = dados.keys()

        escritor = csv.DictWriter(f_csv, fieldnames=cabecalho)
        
        escritor.writeheader()
        escritor.writerow(dados)
import json
import csv
import math

MATERIALS_COST = {
    "Papel": 2,
    "Plástico": 2,
    "Metal": 5,
    "Químico": 15, 
}

def getCsvData(path):
    print(f"Obtendo dados do arquivo: {path}")
    try:
        csv_data = []
        with open(path, "r", newline="", encoding="utf-8") as f:
            leitor = csv.DictReader(f, fieldnames=["residuo", "peso"])
            for linha in leitor:
                peso_valido = getValidWeight(linha["peso"])
                material_valido = getValidMaterial(linha["residuo"])
                if peso_valido is None or material_valido is None:
                    continue
                data = {"residuo": material_valido, "peso": peso_valido}
                csv_data.append(data)
        return csv_data
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {path}")
        return []

def getValidWeight(value):
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

def getValidMaterial(value):
    if not isinstance(value, str) or not value.strip():
        print(f"Valor de resíduo inválido: '{value}'")
        return None
    if value.strip() not in MATERIALS_COST:
        print(f"Material desconhecido: '{value}'")
        return None
    return value.strip()

print(getCsvData("residuos2.csv"))

def exportar_dados(dados, resumo, nome_arquivo="exportacao"):
    with open(f"{nome_arquivo}.json", "w", encoding="utf-8") as f_json:
        json.dump(resumo, f_json, ensure_ascii=False, indent=4)
        
    with open(f"{nome_arquivo}.csv", "w", newline="", encoding="utf-8") as f_csv:
        cabecalho = dados.keys()

        escritor = csv.DictWriter(f_csv, fieldnames=cabecalho)
        
        escritor.writeheader()
        escritor.writerow(dados)
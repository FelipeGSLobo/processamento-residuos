import csv

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
    valid_value = value
    try:
        valid_value = float(value)
    except ValueError:
        print(f"Valor de peso inválido: {value}")
        return None;
    if valid_value <= 0:
        print(f"Valor de peso inválido: {value}")
        return None
    return valid_value
print(getCsvData("./residuos2.csv"))
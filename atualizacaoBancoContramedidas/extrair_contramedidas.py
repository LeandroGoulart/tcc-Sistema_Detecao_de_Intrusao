# extrair_contramedidas.py

import json

def extrair_contramedidas(arquivo_json):
    """
    Extrai informações específicas sobre contramedidas de segurança de um arquivo JSON.

    Args:
        arquivo_json (str): Caminho para o arquivo JSON.

    Returns:
        dict: Dados extraídos contendo ameaças e contramedidas.
    """
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)
    
    contramedidas = {}
    for item in dados.get('threats', []):
        nome_ameaca = item.get('name')
        contramedida = item.get('countermeasure')
        if nome_ameaca and contramedida:
            contramedidas[nome_ameaca] = contramedida
    
    return contramedidas

# Exemplo de uso
if __name__ == "__main__":
    arquivo_json = "dados.json"
    contramedidas = extrair_contramedidas(arquivo_json)
    print(contramedidas)
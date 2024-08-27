import requests
import json
from cryptography.fernet import Fernet

# Função para baixar dados de uma URL
def baixar_dados(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao baixar dados de {url}, código de status: {response.status_code}")

# Função para processar os dados baixados (por exemplo, extraindo informações relevantes)
def processar_dados(dados):
    # Exemplo: Extraindo apenas as contramedidas
    contramedidas = []
    for item in dados.get('objects', []):
        if item.get('type') == 'course-of-action':
            contramedidas.append({
                'id': item.get('id'),
                'name': item.get('name'),
                'description': item.get('description')
            })
    return contramedidas

# Função para armazenar os dados processados em um arquivo JSON
def armazenar_dados(dados, caminho_arquivo):
    with open(caminho_arquivo, 'w') as arquivo_json:
        json.dump(dados, arquivo_json, indent=4)

# Função para carregar a chave de criptografia
def carregar_chave():
    with open("chave.key", "rb") as chave_file:
        chave = chave_file.read()
    return chave

# Função para criptografar dados
def criptografar_dados(dados, chave):
    fernet = Fernet(chave)
    return fernet.encrypt(dados.encode())

# Função para descriptografar dados
def descriptografar_dados(dados_encriptados, chave):
    fernet = Fernet(chave)
    return fernet.decrypt(dados_encriptados).decode()

if __name__ == "__main__":
    # Exemplo de uso das funções
    url = "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-1.0.json"
    dados = baixar_dados(url)
    dados_processados = processar_dados(dados)
    armazenar_dados(dados_processados, "dados_treinamento/dados_v1.0.json")

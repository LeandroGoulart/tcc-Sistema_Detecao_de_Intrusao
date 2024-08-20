import os
import requests
import json

def baixar_dados(url):
    """
    Baixa os dados da URL especificada.
    
    Args:
        url (str): URL de onde os dados serão baixados.
    
    Returns:
        str: Dados baixados.
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def salvar_dados(caminho_arquivo, dados):
    """
    Salva os dados em um arquivo JSON.
    
    Args:
        caminho_arquivo (str): Caminho do arquivo onde os dados serão salvos.
        dados (str): Dados a serem salvos.
    """
    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.write(dados)

def processar_dados(dados):
    """
    Processa os dados de malware para extrair informações úteis para a IA.
    
    Args:
        dados (str): Dados de malware em formato JSON.
    
    Returns:
        list: Lista de objetos de malware processados.
    """
    dados_json = json.loads(dados)
    malware_processado = []
    
    for item in dados_json.get("objects", []):
        if item.get("type") == "malware":
            malware_info = {
                "id": item.get("id"),
                "name": item.get("name"),
                "description": item.get("description"),
                "aliases": item.get("x_mitre_aliases", []),
                "domains": item.get("x_mitre_domains", []),
                "version": item.get("x_mitre_version")
            }
            malware_processado.append(malware_info)
    
    return malware_processado
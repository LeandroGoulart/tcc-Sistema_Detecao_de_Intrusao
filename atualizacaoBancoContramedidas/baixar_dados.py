import requests

def baixar_dados(url):
    """
    Baixa os dados do URL fornecido.
    
    Args:
        url (str): URL do arquivo JSON.
    
    Returns:
        str: Dados JSON como string.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar os dados: {e}")
        return None

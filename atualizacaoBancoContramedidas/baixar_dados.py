# baixar_dados.py

import requests

def baixar_dados(url, caminho_arquivo):
    """
    Realiza o download dos arquivos JSON das URLs fornecidas.

    Args:
        url (str): URL do arquivo JSON.
        caminho_arquivo (str): Caminho onde o arquivo será salvo.

    Returns:
        bool: True se o download foi bem-sucedido, False caso contrário.
    """
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        with open(caminho_arquivo, 'wb') as file:
            file.write(resposta.content)
        return True
    except requests.RequestException as e:
        print(f"Erro ao baixar dados: {e}")
        return False

# Exemplo de uso
if __name__ == "__main__":
    url = "https://exemplo.com/dados.json"
    caminho_arquivo = "dados.json"
    sucesso = baixar_dados(url, caminho_arquivo)
    print("Download bem-sucedido" if sucesso else "Falha no download")
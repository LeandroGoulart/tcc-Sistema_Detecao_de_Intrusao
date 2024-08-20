import sys
import os

# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from security import criptografar_dados

def armazenar_dados(dados, caminho_arquivo):
    """
    Armazena os dados criptografados no arquivo especificado.

    Args:
        dados (str): Dados a serem armazenados.
        caminho_arquivo (str): Caminho do arquivo onde os dados serão armazenados.
    """
    try:
        dados_criptografados = criptografar_dados(dados)
        with open(caminho_arquivo, 'w') as arquivo:
            arquivo.write(dados_criptografados)
        print(f"Dados armazenados com sucesso em {caminho_arquivo}.")
    except Exception as e:
        print(f"Erro ao armazenar dados: {e}")

# Exemplo de uso
if __name__ == "__main__":
    dados = "Exemplo de dados a serem criptografados e armazenados."
    caminho_arquivo = "dados_criptografados.txt"
    armazenar_dados(dados, caminho_arquivo)
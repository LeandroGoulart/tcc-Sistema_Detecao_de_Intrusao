import os
import psutil
from cryptography.fernet import Fernet

def gerar_chave():
    """
    Gera uma chave de criptografia e a salva em um arquivo 'chave.key'.
    """
    chave = Fernet.generate_key()
    with open("D:/OneDrive/Github/tcc-Sistema_Detecao_de_Intrusao/chave.key", "wb") as chave_arquivo:
        chave_arquivo.write(chave)

def carregar_chave():
    """
    Carrega a chave de criptografia a partir do arquivo 'chave.key'.
    Se o arquivo não existir, gera uma nova chave.
    """
    caminho_chave = "D:/OneDrive/Github/tcc-Sistema_Detecao_de_Intrusao/chave.key"
    if not os.path.exists(caminho_chave):
        gerar_chave()
    return open(caminho_chave, "rb").read()

def criptografar_dados(dados):
    """
    Criptografa os dados usando a chave carregada.
    """
    chave = carregar_chave()
    fernet = Fernet(chave)
    dados_criptografados = fernet.encrypt(dados.encode())
    return dados_criptografados.decode()

def verificar_vulnerabilidades(dados_processados):
    """
    Verifica vulnerabilidades nos programas abertos.
    """
    # Obter a lista de programas abertos
    programas_abertos = [proc.name() for proc in psutil.process_iter(['name'])]

    # Verificar vulnerabilidades
    programas_vulneraveis = []
    for programa in programas_abertos:
        if programa in dados_processados.get('vulnerabilidades', []):
            programas_vulneraveis.append(programa)

    # Gerar alertas ou tomar ações
    if programas_vulneraveis:
        print("Programas vulneráveis encontrados:")
        for programa in programas_vulneraveis:
            print(f"- {programa}")
        # Aqui você pode adicionar lógica para tomar ações específicas, como encerrar o programa ou notificar o usuário
    else:
        print("Nenhum programa vulnerável encontrado.")

# Gera a chave se não existir ao importar o módulo
if __name__ == "__main__":
    gerar_chave()
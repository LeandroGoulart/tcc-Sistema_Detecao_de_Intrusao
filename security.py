import os
import json
from cryptography.fernet import Fernet, InvalidToken

CHAVE_ARQUIVO = "chave.key"
PROGRAMAS_ARQUIVO = "dados_treinamento/programs_data_v1.0.enc"


def gerar_chave():
    chave = Fernet.generate_key()
    with open(CHAVE_ARQUIVO, "wb") as chave_arquivo:
        chave_arquivo.write(chave)


def carregar_chave():
    if not os.path.exists(CHAVE_ARQUIVO):
        raise FileNotFoundError(f"Arquivo de chave não encontrado: {CHAVE_ARQUIVO}")
    return open(CHAVE_ARQUIVO, "rb").read()


def criptografar_dados(dados, chave):
    fernet = Fernet(chave)
    dados_criptografados = fernet.encrypt(dados.encode())
    with open(PROGRAMAS_ARQUIVO, "wb") as arquivo:
        arquivo.write(dados_criptografados)


def descriptografar_dados(chave):
    if not os.path.exists(PROGRAMAS_ARQUIVO):
        raise FileNotFoundError(f"Arquivo não encontrado: {PROGRAMAS_ARQUIVO}")
    try:
        fernet = Fernet(chave)
        with open(PROGRAMAS_ARQUIVO, "rb") as arquivo:
            dados_criptografados = arquivo.read()

        dados = fernet.decrypt(dados_criptografados).decode()
        return json.loads(dados)
    except InvalidToken:
        raise ValueError("Falha na descriptografia: chave inválida ou dados corrompidos.")


def verificar_vulnerabilidades(dados):
    pass

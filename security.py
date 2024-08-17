# security.py

from cryptography.fernet import Fernet

def gerar_chave():
    """Gera e salva uma chave de criptografia em um arquivo."""
    chave = Fernet.generate_key()
    with open("secret.key", "wb") as chave_file:
        chave_file.write(chave)

def carregar_chave():
    """Carrega a chave de criptografia do arquivo."""
    return open("secret.key", "rb").read()

def criptografar_arquivo(file_name):
    """Criptografa um arquivo usando a chave gerada."""
    chave = carregar_chave()
    fernet = Fernet(chave)

    with open(file_name, "rb") as file:
        arquivo_dados = file.read()

    arquivo_criptografado = fernet.encrypt(arquivo_dados)

    with open(file_name + ".enc", "wb") as file_enc:
        file_enc.write(arquivo_criptografado)

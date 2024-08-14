import os
import time
from cryptography.fernet import Fernet
from security import encrypt_data, decrypt_data, generate_key

# Caminho do arquivo criptografado onde os dados serão salvos
DATA_FILE = "programs_data.enc"
KEY_FILE = "secret.key"

def listar_programas_abertos():
    """Lista os programas abertos no sistema."""
    processos = os.popen('tasklist').read()
    return processos

def salvar_programas_abertos(processos, key):
    """Salva os programas abertos em um arquivo criptografado."""
    encrypted_data = encrypt_data(processos, key)
    with open(DATA_FILE, 'wb') as file:
        file.write(encrypted_data)

def monitorar_programas():
    """Monitora os programas abertos continuamente e salva os dados."""
    # Gerar ou carregar a chave de criptografia
    if not os.path.exists(KEY_FILE):
        key = generate_key(KEY_FILE)
    else:
        with open(KEY_FILE, 'rb') as file:
            key = file.read()

    while True:
        processos = listar_programas_abertos()
        salvar_programas_abertos(processos, key)
        time.sleep(60)  # Pausa por 60 segundos

if __name__ == "__main__":
    monitorar_programas()

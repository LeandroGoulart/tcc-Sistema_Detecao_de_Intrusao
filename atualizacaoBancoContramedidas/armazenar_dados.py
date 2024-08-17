from cryptography.fernet import Fernet

def armazenar_dados(contramedidas, versao):
    """
    Armazena os dados das contramedidas em um arquivo criptografado.
    
    Args:
        contramedidas (list): Lista de contramedidas a serem armazenadas.
        versao (float): Versão dos dados sendo armazenados.
    """
    key = Fernet.generate_key()
    cipher = Fernet(key)
    
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)
    
    dados = f"Versão: {versao}\n" + "\n".join([f"{nome}: {desc}" for nome, desc in contramedidas])
    encrypted_data = cipher.encrypt(dados.encode())
    
    with open(f'programs_data_v{versao}.enc', 'wb') as file:
        file.write(encrypted_data)

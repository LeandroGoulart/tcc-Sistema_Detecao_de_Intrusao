from cryptography.fernet import Fernet
import os

def generate_key(key_file):
    """Gera uma nova chave de criptografia e salva em um arquivo."""
    key = Fernet.generate_key()
    with open(key_file, 'wb') as file:
        file.write(key)
    return key

def encrypt_data(data, key):
    """Criptografa os dados usando a chave fornecida."""
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data, key):
    """Descriptografa os dados usando a chave fornecida."""
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

def detectar_intrusao():
    """Função de exemplo para detectar intrusões."""
    # Simulação: Detecta se há alguma atividade suspeita no sistema
    return False  # Exemplo, retorna False se não há intrusão

if __name__ == "__main__":
    # Exemplo de uso das funções de segurança
    key = generate_key("secret.key")
    data = "Exemplo de dados sensíveis"
    encrypted = encrypt_data(data, key)
    print("Dados criptografados:", encrypted)
    decrypted = decrypt_data(encrypted, key)
    print("Dados descriptografados:", decrypted)

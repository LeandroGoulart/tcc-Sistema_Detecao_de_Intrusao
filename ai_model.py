import os
import time
import json
import requests
import psutil
from cryptography.fernet import Fernet
from win10toast import ToastNotifier

# Função para carregar a chave de criptografia
def carregar_chave():
    """Carrega a chave de criptografia do arquivo 'chave.key'."""
    with open("chave.key", "rb") as chave_file:
        chave = chave_file.read()
    return chave

# Função para criptografar dados
def criptografar_dados(dados, chave):
    """Criptografa os dados usando a chave fornecida."""
    fernet = Fernet(chave)
    return fernet.encrypt(dados.encode())

# Função para descriptografar dados
def descriptografar_dados(dados_encriptados, chave):
    """Descriptografa os dados usando a chave fornecida."""
    fernet = Fernet(chave)
    return fernet.decrypt(dados_encriptados).decode()

# Função para monitorar processos em execução
def monitorar_processos():
    """Obtém uma lista dos processos atualmente em execução."""
    processos = {}
    for processo in psutil.process_iter(attrs=['pid', 'name']):
        processos[processo.info['pid']] = processo.info['name']
    return processos

# Função para detectar comportamentos suspeitos
def detectar_intrusao(processos_monitorados, processos_atuais):
    """Detecta processos novos ou modificados que não estavam no conjunto monitorado."""
    intrusoes = []
    for pid, nome in processos_atuais.items():
        if pid not in processos_monitorados:
            intrusoes.append(nome)
    return intrusoes

# Função para buscar contramedidas online
def buscar_contramedida(nome_intrusao):
    """Busca contramedidas online para um processo suspeito."""
    try:
        response = requests.get(f"https://api.contramedidas.com/search/{nome_intrusao}")
        if response.status_code == 200:
            return response.json().get('contramedida', "Contramedida nao encontrada.")
        else:
            return "Erro ao buscar contramedida."
    except Exception as e:
        return f"Erro de conexao: {str(e)}"

# Função para salvar programas comuns em um arquivo criptografado
def salvar_programas_comuns(programas):
    """Salva a lista de programas monitorados em um arquivo criptografado."""
    chave = carregar_chave()
    dados_criptografados = criptografar_dados(json.dumps(programas), chave)
    with open("dados_treinamento/programs_data_v1.0.enc", "wb") as file:
        file.write(dados_criptografados)

# Função para mostrar alertas no Windows
def mostrar_alerta(titulo, mensagem):
    """Mostra um popup de alerta no Windows."""
    toaster = ToastNotifier()
    toaster.show_toast(titulo, mensagem, duration=10)

# Função principal do bot de protecao e seguranca
def bot_protecao():
    """Funcao principal para monitorar o sistema e responder a intrusoes."""
    processos_monitorados = monitorar_processos()
    salvar_programas_comuns(processos_monitorados)

    while True:
        time.sleep(60 * 60)  # Verificacao a cada 1 hora
        processos_atuais = monitorar_processos()
        intrusoes_detectadas = detectar_intrusao(processos_monitorados, processos_atuais)
        
        if intrusoes_detectadas:
            for intrusao in intrusoes_detectadas:
                print(f"Alerta: Intrusao detectada - {intrusao}")
                contramedida = buscar_contramedida(intrusao)
                print(f"Contramedida recomendada: {contramedida}")
                
                # Mostra um popup de alerta
                mostrar_alerta("Alerta de Intrusao", f"Intrusao detectada: {intrusao}\nContramedida: {contramedida}")
            
            # Atualiza os processos monitorados apos alerta
            processos_monitorados = processos_atuais
            salvar_programas_comuns(processos_monitorados)

if __name__ == "__main__":
    bot_protecao()

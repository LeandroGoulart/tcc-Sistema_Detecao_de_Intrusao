import os
import json
import requests
import time
from datetime import datetime
from cryptography.fernet import Fernet
from atualizacaoBancoContramedidas.atualizacaoBancoContramedidas import baixar_dados, salvar_dados, processar_dados
from ai_model import treinar_modelo, detectar_anomalias
from atualizacaoBancoContramedidas.atualizar_arquivo import atualizar_informacoes  # Importar a função atualizar_informacoes
from security import verificar_vulnerabilidades  # Importar a função verificar_vulnerabilidades

VERSAO_DATA_ARQUIVO = "versao_data.txt"
DADOS_ARQUIVO = "dados_malware_processados.json"
PROGRAMAS_ARQUIVO = "programas_utilizados.txt"
CHAVE_ARQUIVO = "chave.key"

def gerar_chave():
    chave = Fernet.generate_key()
    with open(CHAVE_ARQUIVO, 'wb') as chave_arquivo:
        chave_arquivo.write(chave)

def carregar_chave():
    return open(CHAVE_ARQUIVO, 'rb').read()

def criptografar_dados(dados, chave):
    fernet = Fernet(chave)
    return fernet.encrypt(dados.encode())

def descriptografar_dados(dados, chave):
    fernet = Fernet(chave)
    return fernet.decrypt(dados).decode()

def salvar_programas_utilizados(programas):
    if not os.path.exists(CHAVE_ARQUIVO):
        gerar_chave()
    chave = carregar_chave()
    dados_criptografados = criptografar_dados(json.dumps(programas), chave)
    with open(PROGRAMAS_ARQUIVO, 'wb') as arquivo:
        arquivo.write(dados_criptografados)

def ler_programas_utilizados():
    if not os.path.exists(PROGRAMAS_ARQUIVO):
        return []
    chave = carregar_chave()
    with open(PROGRAMAS_ARQUIVO, 'rb') as arquivo:
        dados_criptografados = arquivo.read()
    return json.loads(descriptografar_dados(dados_criptografados, chave))

def monitorar_programas_abertos(dados_processados):
    programas_utilizados = ler_programas_utilizados()
    while True:
        # Verificar vulnerabilidades nos programas abertos
        verificar_vulnerabilidades(dados_processados)
        
        # Simulação de programas abertos (substituir pela lógica real)
        programas_abertos = ["programa1.exe", "programa2.exe"]
        programas_utilizados.extend(programas_abertos)
        
        # Salvar programas utilizados
        salvar_programas_utilizados(programas_utilizados)
        
        time.sleep(10)  # Esperar 10 segundos antes de verificar novamente

def ler_versao_data():
    if os.path.exists(VERSAO_DATA_ARQUIVO):
        with open(VERSAO_DATA_ARQUIVO, 'r') as arquivo:
            linha = arquivo.read().strip()
            versao, data_atualizacao = linha.split(',')
            return float(versao), data_atualizacao
    return 0.0, None

def salvar_versao_data(versao, data_atualizacao):
    with open(VERSAO_DATA_ARQUIVO, 'w') as arquivo:
        arquivo.write(f"{versao},{data_atualizacao}")

def comparar_dados(dados_novos, dados_existentes):
    return dados_novos != dados_existentes

def atualizar_dados():
    versao_atual, _ = ler_versao_data()
    nova_versao = versao_atual + 1.0
    dados_processados = None  # Inicializar com valor padrão
    
    while True:
        url = f"https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-{nova_versao}.json"
        caminho_arquivo = f"dados_v{nova_versao}.json"
        
        try:
            dados = baixar_dados(url)
            salvar_dados(caminho_arquivo, dados)
            print(f"Dados da versão {nova_versao} baixados com sucesso.")
            
            # Carregar dados existentes
            if os.path.exists(DADOS_ARQUIVO):
                with open(DADOS_ARQUIVO, 'r') as arquivo:
                    dados_existentes = json.load(arquivo)
            else:
                dados_existentes = None
            
            # Processar os dados e comparar
            dados_processados = processar_dados(dados)
            if comparar_dados(dados_processados, dados_existentes):
                salvar_dados(DADOS_ARQUIVO, json.dumps(dados_processados, indent=4))
                salvar_versao_data(nova_versao, datetime.now().strftime("%Y-%m-%d"))
                print(f"Dados da versão {nova_versao} processados e salvos com sucesso.")
            
            # Treinar o modelo com os novos dados
            treinar_modelo(dados_processados)
            
            # Verificar vulnerabilidades
            verificar_vulnerabilidades(dados_processados)
            
            nova_versao += 1.0
        except requests.exceptions.RequestException as e:
            if e.response.status_code == 404:
                print(f"Erro ao baixar dados da versão {nova_versao}: {e}")
                break
            else:
                print(f"Erro ao baixar dados da versão {nova_versao}: {e}")
                nova_versao += 1.0
        except ValueError as e:
            print(f"Erro ao processar dados: {e}")
            break
    
    return dados_processados

def iniciar_ia():
    data_atual = datetime.now().strftime("%Y-%m-%d")
    versao_atual, ultima_atualizacao = ler_versao_data()
    
    if ultima_atualizacao != data_atual:
        dados_processados = atualizar_dados()
        salvar_versao_data(versao_atual, data_atual)
    else:
        print("Atualização já realizada hoje.")
        # Carregar dados processados existentes
        if os.path.exists(DADOS_ARQUIVO):
            with open(DADOS_ARQUIVO, 'r') as arquivo:
                dados_processados = json.load(arquivo)
        else:
            dados_processados = None
    
    # Continuar monitorando programas abertos e verificando vulnerabilidades
    if dados_processados is not None:
        monitorar_programas_abertos(dados_processados)
    else:
        print("Nenhum dado processado disponível para monitoramento.")

if __name__ == "__main__":
    # Chamar a função atualizar_informacoes
    atualizar_informacoes('versao.txt', 'versao_data.txt', 'versao_completa.txt')
    iniciar_ia()
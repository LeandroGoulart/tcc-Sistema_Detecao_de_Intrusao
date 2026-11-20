import os
import time
import psutil
from ai_model import detectar_anomalias, carregar_dados_treinamento, treinar_modelo
from security import verificar_vulnerabilidades, carregar_chave, descriptografar_dados

DADOS_ARQUIVO = "dados_treinamento/dados_malware_processados.json"


def monitorar_sistema():
    try:
        chave = carregar_chave()
        dados_descriptografados = descriptografar_dados(chave)
    except (FileNotFoundError, ValueError) as e:
        print(e)
        return

    while True:

        verificar_vulnerabilidades(dados_descriptografados)

        processos = [proc.name() for proc in psutil.process_iter(['name'])]
        print(f"Processos em execução: {processos}")


        modelo = treinar_modelo(dados_descriptografados)
        anomalias = detectar_anomalias(modelo, processos)
        if any(anomalias):
            print("Anomalias detectadas!")


        time.sleep(60)


if __name__ == "__main__":
    if os.path.exists(DADOS_ARQUIVO):
        monitorar_sistema()
    else:
        print(f"Arquivo de dados de treinamento não encontrado: {DADOS_ARQUIVO}")

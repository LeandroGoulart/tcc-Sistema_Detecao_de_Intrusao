import os
from gerenciar_dados import baixar_dados, processar_dados, armazenar_dados

def atualizar_contramedidas():
    base_url = "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-"
    versao = 1.0

    while True:
        try:
            url = f"{base_url}{versao}.json"
            print(f"Baixando dados da versão {versao:.1f}...")
            dados = baixar_dados(url)
            dados_processados = processar_dados(dados)
            armazenar_dados(dados_processados, f"dados_treinamento/dados_v{versao:.1f}.json")
            
            # Atualizar a versão para a próxima
            versao += 1.0

        except Exception as e:
            if "404" in str(e):
                print(f"Sistema atualizado. Nenhuma versão nova encontrada para a versão {versao:.1f}. Continuando processos!")
            else:
                print(f"Erro ao processar a versão {versao:.1f}: {str(e)}")
            break  # Sai do loop se a versão não for encontrada ou ocorrer outro erro

if __name__ == "__main__":
    atualizar_contramedidas()

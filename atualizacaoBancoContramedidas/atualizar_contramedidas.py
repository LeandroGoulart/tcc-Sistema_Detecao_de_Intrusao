from extrair_contramedidas import extrair_contramedidas
from baixar_dados import baixar_dados
from armazenar_dados import armazenar_dados

def atualizar_contramedidas():
    """
    Atualiza o banco de contramedidas diariamente, iterando sobre as versões disponíveis.
    """
    versao = 1.0
    while True:
        url = f"https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-{versao}.json"
        dados = baixar_dados(url)
        
        if not dados:
            print("Todas as versões disponíveis foram processadas.")
            break
        
        contramedidas = extrair_contramedidas(dados)
        armazenar_dados(contramedidas, versao)
        
        versao += 1.0

import json

def extrair_contramedidas(json_data):
    """
    Extrai as contramedidas do arquivo JSON.
    
    Args:
        json_data (str): String contendo os dados JSON.
    
    Returns:
        list: Lista de tuplas com nome do ataque e contramedida.
    """
    dados = json.loads(json_data)
    contramedidas = []
    
    for item in dados['objects']:
        if item['type'] == 'intrusion-set':
            nome_ataque = item.get('name', 'N/A')
            descricao = item.get('description', 'N/A')
            contramedidas.append((nome_ataque, descricao))
    
    return contramedidas

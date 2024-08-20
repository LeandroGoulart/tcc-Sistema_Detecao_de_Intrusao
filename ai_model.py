from sklearn.ensemble import IsolationForest
import numpy as np
import logging

def detectar_anomalias(dados, params):
    """
    Detecta anomalias nos dados fornecidos usando o modelo IsolationForest.

    Args:
        dados (list of dict): Lista de dicionários contendo os dados.
        params (dict): Parâmetros para o modelo IsolationForest.

    Returns:
        list: Lista de anomalias detectadas.
    """
    try:
        # Inicializa o modelo com os parâmetros fornecidos
        modelo = IsolationForest(**params)

        # Verifica se todos os itens em 'dados' são dicionários
        if not all(isinstance(item, dict) for item in dados):
            raise ValueError("Todos os itens em 'dados' devem ser dicionários.")

        # Verifica se todos os itens têm o mesmo número de características
        keys = list(dados[0].keys())
        if not all(len(item) == len(keys) for item in dados):
            raise ValueError("Todos os itens em 'dados' devem ter o mesmo número de características.")

        # Converte os valores dos dicionários em uma matriz NumPy
        X = np.array([list(item.values()) for item in dados])

        # Ajusta o modelo e prevê anomalias
        modelo.fit(X)
        anomalias = modelo.predict(X)

        return anomalias

    except Exception as e:
        logging.error(f"Erro ao detectar anomalias: {e}")
        raise
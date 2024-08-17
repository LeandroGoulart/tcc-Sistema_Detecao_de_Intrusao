# monitor.py

import psutil
from alert import alertar_suspeita

def monitorar_programas():
    """Monitora os programas em execução e detecta comportamentos suspeitos."""
    for proc in psutil.process_iter(['pid', 'name']):
        if detectar_comportamento_suspeito(proc.info['name']):
            alertar_suspeita(proc.info['name'])

def detectar_comportamento_suspeito(nome_programa):
    """Detecta comportamentos suspeitos baseados no nome do programa."""
    # Lógica para detectar comportamentos suspeitos
    return False  # Implementar lógica de detecção

monitorar_programas()

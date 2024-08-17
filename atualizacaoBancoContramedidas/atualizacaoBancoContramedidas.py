import time
from atualizar_contramedidas import atualizar_contramedidas

def atualizar_banco_diariamente():
    """
    Configura o processo de atualização para ser executado uma vez ao dia.
    """
    while True:
        atualizar_contramedidas()
        time.sleep(86400)  # 86400 segundos = 24 horas

if __name__ == "__main__":
    atualizar_banco_diariamente()

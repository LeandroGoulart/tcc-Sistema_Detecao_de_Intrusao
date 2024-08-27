import time
from ai_model import bot_protecao
from atualizacao_contramedidas.atualizar_contramedidas import atualizar_contramedidas
from gerenciar_dados import baixar_dados, processar_dados, armazenar_dados

def main():
    # Intervalo de tempo para atualizacoes (em segundos)
    intervalo_atualizacao = 24 * 60 * 60  # 1 vez ao dia

    while True:
        # Atualizar contramedidas diariamente
        atualizar_contramedidas()

        # Iniciar o bot de protecao e seguranca
        bot_protecao()

        # Esperar até a próxima atualizacao
        time.sleep(intervalo_atualizacao)

if __name__ == "__main__":
    main()

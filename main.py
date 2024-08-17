from atualizacaoBancoContramedidas import atualizar_contramedidas
import schedule
import time

def main():
    """
    Inicia o sistema de monitoramento e atualização.
    """
    schedule.every().day.at("00:00").do(atualizar_contramedidas)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

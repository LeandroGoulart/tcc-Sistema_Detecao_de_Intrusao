from monitor import monitorar_programas
from security import detectar_intrusao
from alert import exibir_alerta, sugerir_contramedida
from ai_model import treinar_modelo, carregar_dados

def main():
    # Inicia o monitoramento de programas
    monitorar_programas()

    # Verifica por intrusões
    if detectar_intrusao():
        exibir_alerta("Atenção: Uma intrusão foi detectada no sistema!")
        contramedida = sugerir_contramedida()
        exibir_alerta(contramedida)

    # Treina o modelo de IA (simulação)
    data = carregar_dados("dados.csv")
    modelo = treinar_modelo(data)

if __name__ == "__main__":
    main()

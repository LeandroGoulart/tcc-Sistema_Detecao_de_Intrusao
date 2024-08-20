import psutil
import os

def monitorar_sistema():
    """
    Monitora o comportamento do sistema e dos aplicativos em execução.
    """
    uso_cpu = psutil.cpu_percent(interval=1)
    uso_memoria = psutil.virtual_memory().percent
    print(f"Uso de CPU: {uso_cpu}%")
    print(f"Uso de Memória: {uso_memoria}%")

    # Limites predefinidos
    limite_cpu = 80  # Limite de uso de CPU em porcentagem
    limite_memoria = 80  # Limite de uso de memória em porcentagem

    # Verificar se os limites foram excedidos
    if uso_cpu > limite_cpu:
        print("Alerta: Uso de CPU excedeu o limite!")
        # Sugerir contramedida
        print("Sugestão: Fechar programas que consomem muita CPU.")
    
    if uso_memoria > limite_memoria:
        print("Alerta: Uso de Memória excedeu o limite!")
        # Sugerir contramedida
        print("Sugestão: Fechar programas que consomem muita memória.")

def listar_processos():
    """
    Lista os processos em execução no sistema.
    """
    print("\nProcessos em execução:")
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            info = proc.info
            print(f"PID: {info['pid']}, Nome: {info['name']}, Uso de CPU: {info['cpu_percent']}%, Uso de Memória: {info['memory_percent']}%")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

if __name__ == "__main__":
    monitorar_sistema()
    listar_processos()
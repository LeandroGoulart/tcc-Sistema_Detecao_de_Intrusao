import tkinter as tk
from tkinter import messagebox

def exibir_alerta(mensagem):
    """Exibe um alerta de segurança."""
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    messagebox.showwarning("Alerta de Segurança", mensagem)
    root.destroy()

def sugerir_contramedida():
    """Sugere uma contramedida para a ameaça detectada."""
    return "Sugerimos que você atualize seu antivírus e revise as permissões de firewall."

if __name__ == "__main__":
    exibir_alerta("Atenção: Uma intrusão foi detectada no sistema!")


def alertar_suspeita(nome_programa):
    """Gera um alerta caso um programa suspeito seja detectado."""
    print(f"ALERTA: Programa suspeito detectado: {nome_programa}")
    # Pode incluir mais lógica aqui, como envio de email, notificação, etc.

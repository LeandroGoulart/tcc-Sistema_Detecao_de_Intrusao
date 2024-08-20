# alert.py

import smtplib
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox

def enviar_alerta(mensagem, contramedida, tentativa_ataque):
    """
    Envia alertas de segurança e exibe um popup com a contramedida e a tentativa de ataque.

    Args:
        mensagem (str): Mensagem do alerta.
        contramedida (str): Contramedida necessária.
        tentativa_ataque (str): Tentativa de ataque detectada.
    """
    remetente = "seu_email@example.com"
    destinatario = "destinatario@example.com"
    msg = MIMEText(mensagem)
    msg['Subject'] = "Alerta de Segurança"
    msg['From'] = remetente
    msg['To'] = destinatario

    try:
        with smtplib.SMTP('smtp.example.com') as server:
            server.login("seu_email@example.com", "sua_senha")
            server.sendmail(remetente, destinatario, msg.as_string())
        print("Alerta enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar alerta: {e}")

    # Exibir popup com a contramedida e a tentativa de ataque
    root = tk.Tk()
    root.withdraw()  # Esconder a janela principal
    messagebox.showinfo("Alerta de Segurança", f"Tentativa de Ataque: {tentativa_ataque}\nContramedida: {contramedida}")

if __name__ == "__main__":
    mensagem = "Atividade suspeita detectada."
    contramedida = "Isolar o sistema afetado e iniciar análise forense."
    tentativa_ataque = "Tentativa de acesso não autorizado detectada."
    enviar_alerta(mensagem, contramedida, tentativa_ataque)
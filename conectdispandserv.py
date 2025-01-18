import os
import platform
import subprocess
import time
from tabulate import tabulate

def ping(host):
    """
    Realiza o comando ping no sistema operacional atual.
    Retorna True se o ping foi bem-sucedido, False caso contrário.
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    try:
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    print("Bem-vindo ao Network Status Checker!")
    print("Verifique rapidamente o status de conexão de dispositivos na rede.\n")

    # Lista de hosts para monitorar
    hosts = [
        {"Nome": "Google", "Endereço": "google.com"},
        {"Nome": "Cloudflare", "Endereço": "1.1.1.1"},
        {"Nome": "OpenAI", "Endereço": "openai.com"},
        {"Nome": "Servidor Local", "Endereço": "192.168.1.1"},
    ]

    while True:
        status_list = []
        for host in hosts:
            status = "Online" if ping(host["Endereço"]) else "Offline"
            status_list.append([host["Nome"], host["Endereço"], status])
        
        # Exibir a tabela com os resultados
        print(tabulate(status_list, headers=["Dispositivo", "Endereço", "Status"], tablefmt="fancy_grid"))

        # Atualizar a cada 10 segundos
        print("\nAtualizando em 10 segundos...\n")
        time.sleep(10)

if __name__ == "__main__":
    main()

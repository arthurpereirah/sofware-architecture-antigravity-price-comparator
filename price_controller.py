import time
import subprocess
import datetime
import os

def run_price_controller(interval_minutes=60):
    print("=======================================================")
    print(" 🤖 CONTROLADOR DE PREÇOS (DAEMON PLAYWRIGHT ATIVADO)")
    print("=======================================================")
    print(f"📡 Monitoramento Contínuo: Iniciando ciclo de {interval_minutes} minutos.")
    
    while True:
        agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n[⏳ {agora}] 🚀 Disparando novo rastreamento de ofertas da Amazon...")
        
        try:
            # Chama o motor principal que integra nosso CSV -> Playwright -> SQLite History
            subprocess.run(["python", "main.py"], check=True)
            print(f"[✅ {datetime.datetime.now().strftime('%H:%M:%S')}] Escaneamento completo. Banco de Dados atualizado.")
        except Exception as e:
            print(f"[❌] Erro crítico no ciclo de raspagem: {e}")
            
        print(f"\n💤 Piloto automático ativado. Dormindo por {interval_minutes} minutos até a próxima rodada...")
        time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    # Pode reduzir esse número de minutos para testes
    run_price_controller(interval_minutes=60)

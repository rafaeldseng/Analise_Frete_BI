import pandas as pd
import json
import requests
import json
from etapa2_calculos import calcular_metricas
import os

# --- 1 Leitura dos dados ---
clientes = pd.read_csv("data/Clientes.csv")
entregas = pd.read_csv("data/Entregas.csv")
motoristas = pd.read_csv("data/Motoristas.csv")

resultado = calcular_metricas()

if resultado:
    # --- 2️ Define o endpoint da API ---
    url = "https://httpbin.org/post" # "https://api.empresa.com.br/fretes"  # endpoint fictício substituído para simulação

    # --- 3️ Converte o dicionário Python em JSON ---
    # payload = json.dumps(resultado, ensure_ascii=False)
    json_data = json.dumps(resultado)

    # --- 4️ Define os headers (como um conteúdo JSON real) ---
    headers = {
        "Content-Type": "application/json"
    }

    # --- 5️ Envia a requisição POST ---
try:
    response = requests.post(url, data=json_data, headers=headers)

    if response.status_code == 200:
        print("\n✅ Dados enviados com sucesso!")
        response_json = response.json()

        # --- 5️ Garante que a pasta output exista ---
        os.makedirs("output", exist_ok=True)

        # --- 6️ Salva a resposta da API ---
        with open("output/response.json", "w", encoding="utf-8") as f:
            json.dump(response_json, f, indent=4, ensure_ascii=False)

        print("📁 Resposta salva em: output/response.json")

    else:
        print(f"\n⚠️ Falha ao enviar dados. Código de status: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"\n❌ Erro ao enviar requisição: {e}")
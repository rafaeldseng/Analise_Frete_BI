import pandas as pd
import json
import requests

# --- 1 Leitura dos dados ---
clientes = pd.read_csv("data/Clientes.csv")
entregas = pd.read_csv("data/Entregas.csv")
motoristas = pd.read_csv("data/Motoristas.csv")


# src/etapa1_leitura_csv.py

import pandas as pd

# Caminhos dos arquivos CSV
clientes = pd.read_csv("C:/Users/Usuário/Documents/Projetos/Etapa de Testes - Ventana Serra do Brasil/Analise_Frete_BI/data/Clientes.csv")
entregas = pd.read_csv("C:/Users/Usuário/Documents/Projetos/Etapa de Testes - Ventana Serra do Brasil/Analise_Frete_BI/data/Entregas.csv")
motoristas = pd.read_csv("C:/Users/Usuário/Documents/Projetos/Etapa de Testes - Ventana Serra do Brasil/Analise_Frete_BI/data/Motoristas.csv")

# --- Preview dos dados ---
print("=== Clientes ===")
print(clientes.head(), "\n")

print("=== Entregas ===")
print(entregas.head(), "\n")

print("=== Motoristas ===")
print(motoristas.head(), "\n")

# --- Informações adicionais ---
print("Shapes:")
print("Clientes:", clientes.shape)
print("Entregas:", entregas.shape)
print("Motoristas:", motoristas.shape)

print("\nTipos de dados (Entregas):")
print(entregas.dtypes)

print("\nValores nulos (Entregas):")
print(entregas.isnull().sum())

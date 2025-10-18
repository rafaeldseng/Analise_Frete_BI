import pandas as pd

# --- 1 Leitura dos dados ---
clientes = pd.read_csv("data/Clientes.csv")
entregas = pd.read_csv("data/Entregas.csv")
motoristas = pd.read_csv("data/Motoristas.csv")

# --- 2️ Criação das colunas calculadas ---
# Garante que as datas estão no formato datetime
entregas["DataEntregaPrevista"] = pd.to_datetime(entregas["DataEntregaPrevista"])
entregas["DataEntregaReal"] = pd.to_datetime(entregas["DataEntregaReal"])

# Calcula dias de atraso
entregas["DiasAtraso"] = (entregas["DataEntregaReal"] - entregas["DataEntregaPrevista"]).dt.days

# Cria status da entrega
entregas["StatusEntrega"] = entregas["DiasAtraso"].apply(lambda x: "Atrasado" if x > 0 else "No prazo")

# --- 3️ Cálculos principais ---
# Frete médio
frete_medio = entregas["ValorFrete"].mean()

# Percentual de entregas atrasadas
percentual_atrasadas = (entregas[entregas["StatusEntrega"] == "Atrasado"].shape[0] / entregas.shape[0]) * 100

# --- 4️ Exibição dos resultados ---
print("=== Resultados da Etapa 2 ===")
print(f"Frete médio: R$ {frete_medio:.2f}")
print(f"% Entregas atrasadas: {percentual_atrasadas:.2f}%")

# --- 5️ Prepara os dados para exportar na próxima etapa ---
resultado = {
    "frete_medio": round(frete_medio, 2),
    "percentual_atrasadas": round(percentual_atrasadas, 2)
}

print("\nDicionário pronto para converter em JSON:")
print(resultado)

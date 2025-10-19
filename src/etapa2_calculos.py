import pandas as pd

def calcular_metricas():
    # --- 1️ Leitura dos dados ---
    clientes = pd.read_csv("data/Clientes.csv")
    entregas = pd.read_csv("data/Entregas.csv")
    motoristas = pd.read_csv("data/Motoristas.csv")

    # --- 2️ Criação das colunas calculadas ---
    entregas["DataEntregaPrevista"] = pd.to_datetime(entregas["DataEntregaPrevista"])
    entregas["DataEntregaReal"] = pd.to_datetime(entregas["DataEntregaReal"])

    # Calcula dias de atraso
    entregas["DiasAtraso"] = (entregas["DataEntregaReal"] - entregas["DataEntregaPrevista"]).dt.days

    # Cria status da entrega
    entregas["StatusEntrega"] = entregas["DiasAtraso"].apply(lambda x: "Atrasado" if x > 0 else "No prazo")

    # --- 3️ Cálculos principais ---
    frete_medio = entregas["ValorFrete"].mean()
    percentual_atrasadas = (entregas[entregas["StatusEntrega"] == "Atrasado"].shape[0] / entregas.shape[0]) * 100

    # --- 4️ Retorna o resultado como dicionário ---
    resultado = {
        "frete_medio": round(frete_medio, 2),
        "percentual_atrasadas": round(percentual_atrasadas, 2)
    }

    return resultado

if __name__ == "__main__":
    resultado = calcular_metricas()
    print("=== Resultados da Etapa 2 ===")
    print(f"Frete médio: R$ {resultado['frete_medio']:.2f}")
    print(f"% Entregas atrasadas: {resultado['percentual_atrasadas']:.2f}%")
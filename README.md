# Analise_Frete_BI
Análise operacional de uma empresa fictícia de logística

Este projeto foi desenvolvido para estudo e avaliação técnica de análise de dados e BI com foco em logística e transporte.  
O objetivo é demonstrar conhecimentos em SQL, Power BI, Python, análise e modelagem de dados.

---

## Estrutura do Projeto

Analise_Frete_BI/
│
├── data/
│ ├── Clientes.csv
│ ├── Entregas.csv
│ └── Motoristas.csv
│
├── src/
│ ├── etapa1_leitura_csv.py # Leitura e exploração inicial dos dados
│ ├── etapa2_calculos.py    # Cálculos de indicadores (frete médio, % atrasos)
│ └── etapa3_post_api.py    # Conversão em JSON e envio via POST
│
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação

---


---

## Tecnologias Utilizadas

| Categoria | Ferramenta |
|------------|-------------|
| Linguagem | Python 3.10+ |
| Bibliotecas | `pandas`, `requests` |
| BI e Visualização | Power BI |
| Versionamento | Git + GitHub |

---

## Etapas do Projeto

**Etapa 1 — Leitura e Exploração dos Dados**
Arquivo: `src/etapa1_leitura_csv.py`

- Leitura dos arquivos CSV (`Clientes`, `Entregas`, `Motoristas`)
- Inspeção inicial: colunas, tipos de dados, valores nulos
- Estruturação dos dados para análise posterior

**Etapa 2 — Cálculos e Indicadores**
Arquivo: `src/etapa2_calculos.py`

- Cálculo do **frete médio**
- Cálculo do **percentual de entregas atrasadas**
- Criação de colunas derivadas (`DiasAtraso`, `StatusEntrega`)

**Etapa 3 — Envio via API**
Arquivo: `src/etapa3_post_api.py`

- Conversão dos resultados em **JSON**
- Envio via **POST** para o endpoint fictício: https://api.empresa.com.br/fretes

---

## Indicadores Calculados

**Frete Médio (R$)** Média dos valores de frete registrados
**% Entregas Atrasadas** Proporção de entregas com `StatusEntrega = "Atrasado"`
**Ticket Médio por Cliente** Valor médio de frete por cliente distinto
**Peso Total Transportado** Soma do peso total das entregas
**Valor Total de Frete** Soma de todos os fretes realizados

---

##  Modelagem de Dados (Power BI)

**Relacionamentos principais:**
- `Clientes[IDCliente]` - `Entregas[IDCliente]`
- `Entregas[Motorista]` - `Motoristas[Motorista]`

**Colunas criadas:**

- ` DiasAtraso = Duration.Days( [DataEntregaReal] - [DataEntregaPrevista] )`

- ` StatusEntrega = if Duration.Days([DataEntregaReal] - [DataEntregaPrevista]) <= 0 then "No prazo" else "Atrasado"`


**Medidas DAX:**
```DAX
FreteMédio = AVERAGEA(Entregas[ValorFrete])

EntregasAtrasadas% = DIVIDE(
    CALCULATE(COUNTROWS(Entregas), 
    Entregas[StatusEntrega] = "Atrasado"), 
    COUNTROWS(Entregas), 
    0)

PesoTotalTransportado = SUM(Entregas[Peso])

ValorTotalFrete = SUM(Entregas[ValorFrete])

TicketMédioCliente = DIVIDE([ValorTotalFrete], DISTINCTCOUNT(Entregas[IDCliente]), 0)

TopClientesFrete = 
IF([RankFreteCliente]<=[Valor Parâmetro],
CALCULATE(
    [TotalFrete_DAX],
    TOPN(
        [Valor Parâmetro],
        VALUES(Clientes),
        [TotalFrete_DAX]
    )
))

```

---

## Visualizações:

- Mapa de calor por UF destino
- Top 5 clientes por valor de frete
- Gráfico de frete médio por motorista
- KPI Cards: % atrasos, ticket médio, peso total

---

## Estrutura do Projeto

Este projeto demonstrou a análise de dados de uma operação logística fictícia, transformando informações brutas em indicadores estratégicos.
Com Python e Power BI, foi possível calcular métricas relevantes, modelar dados e criar visualizações interativas que auxiliam na tomada de decisão.
O repositório serve como referência para estudos em análise de dados, criação de indicadores, BI e boas práticas de organização de projetos e versionamento Git. 

💡 Análise de dados de logística podem ser transformados em insights estratégicos!

Rafael Evangelista




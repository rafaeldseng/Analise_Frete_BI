import subprocess

# Lista de scripts a serem executados
scripts = [
    "src/etapa1_leitura_csv.py",
    "src/etapa2_calculos.py",
    "src/etapa3_post_api.py"
]

# Executa cada script na ordem
for script in scripts:
    print(f"\n🚀 Executando {script} ...")
    subprocess.run(["python", script], check=True)

# Inicia o servidor web
print("\n🌐 Iniciando servidor web na porta 8000...")
subprocess.run(["python", "-m", "http.server", "8000"])

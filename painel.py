import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt

conn = sqlite3.connect("patrimonio.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patrimonio (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT,
    total REAL
)
""")

def inserir_valor(total):
    data = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO patrimonio (data, total) VALUES (?, ?)", (data, total))
    conn.commit()

def buscar_dados():
    cursor.execute("SELECT data, total FROM patrimonio ORDER BY data")
    return cursor.fetchall()

def gerar_grafico():
    dados = buscar_dados()

    if len(dados) == 0:
        print("Sem dados ainda.")
        return

    datas = [d[0] for d in dados]
    valores = [d[1] for d in dados]

    plt.plot(datas, valores, marker='o')
    plt.title("Evolução do Patrimônio")
    plt.xlabel("Data")
    plt.ylabel("R$")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

while True:
    print("\n1 - Adicionar patrimônio")
    print("2 - Ver gráfico")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        valor = float(input("Digite o patrimônio total: "))
        inserir_valor(valor)
        print("Salvo!")

    elif opcao == "2":
        gerar_grafico()

    elif opcao == "3":
        break

conn.close()
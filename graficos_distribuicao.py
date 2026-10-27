# 1 - Importar as ferramentas
import os
import pandas as pd
import matplotlib.pyplot as plt

# 2 - Criar a pasta
os.makedirs("graficos", exist_ok=True)

# 3 - Ler o CSV
df = pd.read_csv("dados/dados_distribuicao.csv")

# 4 - Criar a tela
plt.figure(figsize=(10, 6))

# 5 - Desenhar o histograma
plt.hist(df["idade"], bins=15, color="steelblue", edgecolor="black")

# 6 - Enfeitar
plt.title("Distribuição de Idade dos Clientes")
plt.xlabel("Idade")
plt.ylabel("Quantidade de Clientes")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

# 7 - Salvar e mostrar
plt.savefig("graficos/distribuicao.png")
plt.show()
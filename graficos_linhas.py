# 1 - Importar as ferramentas
import os
import pandas as pd
import matplotlib.pyplot as plt

# 2 - Criar a pasta
os.makedirs("graficos", exist_ok=True)

# 3 - Ler o CSV
df = pd.read_csv("dados/dados_linhas.csv")

# 4 - Transformar o texto da data em data de verdade
df["data"] = pd.to_datetime(df["data"])

# 5 - Criar a tela
plt.figure(figsize=(12, 6))

# 6 - Desenhar uma linha para cada loja
for loja, grupo in df.groupby("loja"):
    plt.plot(grupo["data"], grupo["vendas"], marker="o", markersize=3, label=loja)

# 7 - Enfeitar
plt.title("Evolução das Vendas (Jan a Mar 2026)")
plt.xlabel("Data")
plt.ylabel("Vendas")
plt.legend(title="Loja")
plt.grid(alpha=0.3)
plt.tight_layout()

# 8 - Salvar e mostrar
plt.savefig("graficos/linhas.png")
plt.show()
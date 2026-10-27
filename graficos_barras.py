# 1 - Importar as ferramentas
import os
import pandas as pd
import matplotlib.pyplot as plt

# 2 - Criar a pasta onde a imagem vai ser salva
os.makedirs("graficos", exist_ok=True)

# 3 - Ler o arquivo CSV
df = pd.read_csv("dados/dados_barras.csv")

# 4 - Reorganizar a tabela
tabela = df.pivot(index="categoria", columns="regiao", values="vendas_medias")

# 5 - Desenhar o gráfico
tabela.plot(kind="bar", figsize=(10, 6))

# 6 - Enfeitar
plt.title("Vendas Médias por Categoria e Região")
plt.xlabel("Categoria")
plt.ylabel("Vendas Médias")
plt.xticks(rotation=0)
plt.legend(title="Região")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

# 7 - Salvar e mostrar
plt.savefig("graficos/barras.png")
plt.show()
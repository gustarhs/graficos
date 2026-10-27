# 1 - Importar as ferramentas
import os
import pandas as pd
import matplotlib.pyplot as plt

# 2 - Criar a pasta
os.makedirs("graficos", exist_ok=True)

# 3 - Ler o CSV
df = pd.read_csv("dados/dados_frequencia.csv")

# 4 - Contar quantas vezes cada tipo aparece
contagem = df["tipo_atendimento"].value_counts()

# 5 - Criar a tela e desenhar
plt.figure(figsize=(10, 6))
contagem.plot(kind="bar", color="coral", edgecolor="black")

# 6 - Enfeitar
plt.title("Frequência por Tipo de Atendimento")
plt.xlabel("Tipo de Atendimento")
plt.ylabel("Quantidade de Chamados")
plt.xticks(rotation=0)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

# 7 - Salvar e mostrar
plt.savefig("graficos/frequencia.png")
plt.show()
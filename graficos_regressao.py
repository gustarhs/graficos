# 1 - Importar as ferramentas
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 2 - Criar a pasta
os.makedirs("graficos", exist_ok=True)

# 3 - Ler o CSV
df = pd.read_csv("dados/dados_regressao.csv")

# 4 - Separar as colunas
x = df["renda_mensal"]
y = df["gasto_mensal"]

# 5 - Calcular a reta de regressão (y = a*x + b)
a, b = np.polyfit(x, y, 1)

# 6 - Criar a tela e desenhar os pontos
plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.6, label="Dados")

# 7 - Desenhar a reta
x_ordenado = np.sort(x)
plt.plot(x_ordenado, a * x_ordenado + b, color="red", linewidth=2,
         label=f"Regressão: y = {a:.2f}x + {b:.2f}")

# 8 - Enfeitar
plt.title("Regressão Linear: Renda Mensal x Gasto Mensal")
plt.xlabel("Renda Mensal (R$)")
plt.ylabel("Gasto Mensal (R$)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

# 9 - Salvar e mostrar
plt.savefig("graficos/regressao.png")
plt.show()
# 1 - Importar as ferramentas
import os
import pandas as pd
import matplotlib.pyplot as plt

# 2 - Criar a pasta
os.makedirs("graficos", exist_ok=True)

# 3 - Ler o CSV
df = pd.read_csv("dados/dados_boxplot.csv")

# 4 - Desenhar o gráfico
df.boxplot(column="salario", by="departamento", figsize=(10, 6))

# 5 - Enfeitar
plt.suptitle("")
plt.title("Distribuição de Salários por Departamento")
plt.xlabel("Departamento")
plt.ylabel("Salário (R$)")
plt.tight_layout()

# 6 - Salvar e mostrar
plt.savefig("graficos/boxplot.png")
plt.show()
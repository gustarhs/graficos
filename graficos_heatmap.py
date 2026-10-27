# 1 - Importar as ferramentas
import os
import pandas as pd
import matplotlib.pyplot as plt # matplotlib.pyplot - ferramenta para desenhar gráficos.
import seaborn as sns

# 2 - Criar a pasta
os.makedirs("graficos", exist_ok=True)

# 3 - Ler o CSV
df = pd.read_csv("dados/dados_heatmap.csv")

# 4 - Reorganizar a tabela (dias x horários)
tabela = df.pivot(index="dia_semana", columns="horario", values="movimento_clientes")

# 5 - Colocar os dias na ordem certa
ordem = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
tabela = tabela.reindex(ordem)

# 6 - Criar a tela e desenhar
plt.figure(figsize=(10, 6))
sns.heatmap(tabela, annot=True, fmt="d", cmap="YlOrRd")

# 7 - Enfeitar
plt.title("Movimento de Clientes por Dia e Horário")
plt.xlabel("Horário")
plt.ylabel("Dia da Semana")
plt.tight_layout()

# 8 - Salvar e mostrar
plt.savefig("graficos/heatmap.png")
plt.show()
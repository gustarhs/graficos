# 1 - Importar as ferramentas
import os
import pandas as pd
import matplotlib.pyplot as plt

# 2 - Criar a pasta
os.makedirs("graficos", exist_ok=True)

# 3 - Ler o CSV
df = pd.read_csv("dados/dados_dispersao.csv")

# 4 - Criar a tela
plt.figure(figsize=(10, 6))

# 5 - Desenhar um grupo de pontos para cada sexo
for sexo, grupo in df.groupby("sexo"):
    plt.scatter(grupo["altura_cm"], grupo["peso_kg"], label=sexo, alpha=0.7)

# 6 - Enfeitar
plt.title("Relação entre Altura e Peso")
plt.xlabel("Altura (cm)")
plt.ylabel("Peso (kg)")
plt.legend(title="Sexo")
plt.grid(alpha=0.3)
plt.tight_layout()

# 7 - Salvar e mostrar
plt.savefig("graficos/dispersao.png")
plt.show()
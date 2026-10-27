import os 
import pandas as pd 
import matplotlib.pyplot as plt # matplot.pyplo - ferramenta para desenhar gráficos.

os.makedirs("graficos" , exist_ok=True)

df = pd.read_csv("dados/dados_pizza.csv")

plt.figure(figsize=(8,8)) # crie uma tela tamanho 8x8 , quadrada , porque a pizza é redonda

plt.pie(df["faturamento"] , labels =df["canal_venda"], autopct="%1.1f%%" , startangle=90)

plt.title("Faturamento por Canal de Venda")
plt.axis("equal")
plt.tight_layout()

#salvar e mostrar
plt.savefig("graficos/pizza.png")
plt.show()
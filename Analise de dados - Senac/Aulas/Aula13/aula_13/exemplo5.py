import pandas as pd
import numpy as np

df = pd.read_excel('./aula_2/vendas_roupas.xlsx')

# print(df.head(10))
# print(df.describe())

categoria = df['Categoria']
quantidade_vendida = df['Unidades Vendidas']

media = np.mean(quantidade_vendida)
mediana = np.median(quantidade_vendida)
print("")
print(f'Média: {media:.2f}')
print("")
print(f'Mediana: {mediana:.2f}')

quantidade_organizada = df.sort_values(by='Unidades Vendidas', ascending=True)

print(quantidade_vendida.values)

satisfação = df[df['Satisfação'] == "Baixo"]
print(satisfação)


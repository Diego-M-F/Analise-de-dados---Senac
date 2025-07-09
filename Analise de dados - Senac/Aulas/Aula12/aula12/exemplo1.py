import pandas as pd

produtos = ['Notebook', 'Smathphone', 'Tablet', 'Smartchwatch', 'Câmera']
quantidade_estoque = [15, 30, 20, 10, 25]


estoque = pd.Series(quantidade_estoque, index=produtos)

# print("Séries Estoque de Produtos:")
# print(estoque)
# print(estoque['Notebook'])  # Mostra apenas os valores
# print(estoque[['Notebook',  'Smathphone']].values)  # Mostra apenas os valores com mais de 1
# print(estoque[['Notebook',  'Smathphone']])  # Mostra o Nome e o Valor

# print("Produtos com estoque abaixo de 20:")
# print(estoque[estoque < 20])
# Adicionando 5 unidades em todos os estoques
# print(estoque + 5)
# print(estoque - 5)
# print(estoque / 2)
# print(estoque * 10)

estoque.loc['Headphone'] = None
# print(estoque)

precos = pd.Series([3500, 2500, 1200, 900, 1500], index=produtos)

print(precos * estoque)

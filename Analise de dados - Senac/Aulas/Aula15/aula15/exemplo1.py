from sqlalchemy import create_engine
import pandas as pd
import numpy as np 


host = ''
user = ''
password = ''
database = ''


engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')


df_estoque = pd.read_sql('tb_produtos', engine)

# print(df)

df_estoque['TotalEstoque'] = df_estoque['preco'] * df_estoque['qtd']

# print(df_estoque[['produto', 'TotalEstoque']])

# print(f'Total geral de produtos: {df_estoque["TotalEstoque"].sum()}')
array_estoque = np.array(df_estoque['TotalEstoque'])

media = np.mean(array_estoque)
mediana = np.median(array_estoque)
distancia = abs(media - mediana) / mediana

print(distancia)
print(f'{media:.2f}')
print(f'{mediana:.2f}')

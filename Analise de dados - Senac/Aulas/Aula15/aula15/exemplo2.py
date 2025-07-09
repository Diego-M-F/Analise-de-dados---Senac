from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os
import numpy as np

load_dotenv()


host = os.getenv('DB_host')
user = os.getenv('DB_user')
password = os.getenv('DB_password')
database = os.getenv('DB_database')

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')


df_estoque = pd.read_sql('tb_vendas', engine)

df = pd.DataFrame(df_estoque)

df_estoque['Vendas'] = df_estoque['preco'] * df_estoque['qtd']


array_estoque = np.array(df_estoque['Vendas'])

media = np.mean(array_estoque)
mediana = np.median(array_estoque)
distancia = (media - mediana) / mediana

print(f' Vendas totais {df_estoque["Vendas"]}')
print(f'A distância entre media e mediana é: {distancia:.2f}')
print(f"Alternativa que reflete melhor é a mediana: {mediana:.2f}")

from datetime import datetime
import pandas as pd
import polars as pl 

try:
    ENDERECO_DADOS = r'../dados/'

    hora_inicio = datetime.now()

    print('Carregando...')

    df_bolsa_janeiro = pl.read_csv(ENDERECO_DADOS + '202501_NovoBolsaFamilia.csv', separator=";", encoding='iso-8859-1')

    print(df_bolsa_janeiro.head)
    hora_final = datetime.now()

    print(f'tempo de execução: {hora_final - hora_inicio}')
except Exception as a:
    print(f'Erro: {a}')

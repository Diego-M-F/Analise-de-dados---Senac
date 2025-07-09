from datetime import datetime
import pandas as pd
import polars as pl 

try:
    ENDERECO_DADOS = r'../dados/'

    hora_inicio = datetime.now()
    lista_jan_fev = ['202501_NovoBolsaFamilia.csv', '202502_NovoBolsaFamilia.csv', '202503_NovoBolsaFamilia.csv', '202504_NovoBolsaFamilia.csv']

    df_bolsa_familia = None

    for arquivo in lista_jan_fev:
        print(f"Processando arquivo {arquivo}.")
        
        df_temp = pl.read_csv(ENDERECO_DADOS + arquivo, separator=";", encoding='iso-8859-1')

        if df_bolsa_familia is None:
            df_bolsa_familia = df_temp
        else:
            df_bolsa_familia = pl.concat([df_bolsa_familia, df_temp])

        print(df_temp)
        print(df_temp.shape)

        del df_temp
    
    print(df_bolsa_familia.head)
    print(df_bolsa_familia.shape)
    hora_final = datetime.now()

    print(f'tempo de execução: {hora_final - hora_inicio}')
except Exception as a:
    print(f'Erro: {a}')

#pd 3m 35
import pandas as pd
import numpy as np
from utils import limpar_nome_municipio

try: 
    print('Obtendo dados...')
    Endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    df_ocorrencia = pd.read_csv(Endereco_dados, sep=";", encoding='iso-8859-1')
    # print(df_ocorrencia.head())
    for i in range(2):
        df_ocorrencia['munic'] = df_ocorrencia['munic'].apply(limpar_nome_municipio)

    df_ocorrencia = df_ocorrencia[['munic', 'roubo_veiculo']]

    df_roubo_veiculo = df_ocorrencia.groupby('munic').sum('roubo_veiculo').reset_index()
    # print(df_roubo_veiculo.to_string())


except Exception as e:
    print(f'Erro: {e}')
    exit()
try:
    print("Obtendo informações sobre padrão de roubos de veiculos...")
    array_roubo_carros = np.array(df_roubo_veiculo['roubo_veiculo'])

    mediana = np.median(array_roubo_carros)
    media = np.mean(array_roubo_carros)
    distancia = abs((media - mediana) / mediana)
    # print('media:', media)
    # print('mediana:', mediana)
    # print(f'Distancia: {distancia:.3f}')

    q1 = np.quantile(array_roubo_carros, 0.25, method='weibull')
    q2 = np.quantile(array_roubo_carros, 0.50, method='weibull')
    q3 = np.quantile(array_roubo_carros, 0.75, method='weibull')

    # print(f'Q1: {q1}, Q2: {q2}, Q3: {q3},')

    df_roubo_veículo_menores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < q1]
    df_roubo_veículo_maiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > q3]
    # print(df_roubo_veículo_menores.sort_values(by='roubo_veiculo', ascending=True))
    # print("")
    # print(100*"-")
    # print("")
    # print(df_roubo_veículo_maiores.sort_values(by='roubo_veiculo', ascending=False ))

    iqr = q3 - q1 
    limite_superior = q3 + (1.5*iqr)
    limite_inferior = q1 - (1.5*iqr)
    
    # print('\nLimites - Medidasde posição')
    # print(f'Limite inferior: {limite_inferior}')
    # print(f'Limite superior: {limite_superior	}')

    df_roubo_veiculo_outliers_superiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > limite_superior]
    df_roubo_veiculo_outliers_inferior = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < limite_inferior]
    print("limite inferior")
    if len(df_roubo_veiculo_outliers_inferior) == 0:
        print("Não tem outliers inferiores")
    else:
        print(df_roubo_veiculo_outliers_inferior.sort_values(by='roubo_veiculo', ascending=True))

    
    print("\limite inferior")
    if len(df_roubo_veiculo_outliers_superiores) == 0:
        print("Não tem outliers superiores")
    else:
        print(df_roubo_veiculo_outliers_superiores.sort_values(by='roubo_veiculo', ascending=False))



except Exception as a:
    print(f'Erro {a}')

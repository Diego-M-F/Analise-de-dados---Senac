import pandas as pd
import numpy as np 

try:
    print('Searching for data...')
    # Faz a conexão e pega a base diretamente do site
    data_address = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    # Ler o conteudo da base, separando por ; e lendo o tipo de cryptografia
    df_rjpolicedata = pd.read_csv(data_address, sep=";", encoding='iso-8859-1')
    # seleciona as colunos que interessam
    df_rjpolicedata = df_rjpolicedata[['munic', 'estelionato']]
    # agrupa por munucipio, soma a quantidade de estelionato por municipio e...
    # adicionao index. 
    df_fraud = df_rjpolicedata.groupby('munic').sum('estelionato').reset_index()
  
except Exception as a:
    print(f"Error: {a}")

try:
    print("Searching for data related with fraud...")
    array_fraud_data = np.array(df_fraud['estelionato'])
    # mediana, media e distancia entre as duas
    median = np.median(array_fraud_data)
    medium = np.mean(array_fraud_data)
    distancy = abs((medium - median) / median)
    # mediana = 1347.5
    # media = 11315.188....
    # distância = 7.3971....
    # De acordo com os quartis a media e mediana não refletem bem a curva. 

    q1 = np.quantile(array_fraud_data, 0.25, method='weibull')
    q2 = np.quantile(array_fraud_data, 0.50, method='weibull')
    q3 = np.quantile(array_fraud_data, 0.75, method='weibull')
    # 25% dos municipios ficaram em uma media de 596,25 
    # 50% dos municipios ficaram em uma media de 1347,5
    # 75% dos municipios ficaram em uma media de 6946,0

    df_fraud_smaller = df_fraud[df_fraud['estelionato'] < q1]
    df_fraud_higher = df_fraud[df_fraud['estelionato'] > q3]

    # print(df_fraud_higher.sort_values(by='estelionato',ascending=False))
    # print(100*'*')
    # print(df_fraud_smaller.sort_values(by='estelionato',ascending=True))

    iqr = q3 - q1 
    limit_superior = q3 + (1.5*iqr)
    limit_inferior = q1 - (1.5*iqr)

    df_fraud_highest_outliers = df_fraud[df_fraud['estelionato'] > limit_superior]
    df_fraud_smallest_outliers = df_fraud[df_fraud['estelionato'] < limit_inferior]

    print(f"{'Inferior limit':^75}")
    if len(df_fraud_smallest_outliers) == 0:
        print('There is no inferior outlier.')
    else:
        print(df_fraud_smallest_outliers.sort_values(by='estelionato', ascending=True).head())

    print(100*'*')

    print(f"{'Superior limit':^75}")
    if len(df_fraud_highest_outliers) == 0:
        print('There is no superior outlier.')
    else:
        print(df_fraud_highest_outliers.sort_values(by='estelionato', ascending=False).head())
    
    print(100*'*')

    max_cases = df_fraud['estelionato'].max()
    highest_city = df_fraud[df_fraud['estelionato'] == max_cases]
    print(f"The city with the highest cases of fraud is: {highest_city.iloc[0]['munic']} with {highest_city.iloc[0]['estelionato']} cases.")
    


except Exception as e:
    print(f"Error: {e}")
    

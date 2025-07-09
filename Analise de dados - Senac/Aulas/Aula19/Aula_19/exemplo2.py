import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

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
    mini = np.min(array_fraud_data)
    maxi = np.max(array_fraud_data)
    full_range = maxi - mini


    iqr = q3 - q1 
    limit_superior = q3 + (1.5*iqr)
    limit_inferior = q1 - (1.5*iqr)

    df_fraud_highest_outliers = df_fraud[df_fraud['estelionato'] > limit_superior]
    df_fraud_smallest_outliers = df_fraud[df_fraud['estelionato'] < limit_inferior]

    variancy = np.var(array_fraud_data)
    variacy_distancy = variancy / (medium ** 2)

    pattern_detour = np.std(array_fraud_data)
    print(pattern_detour)
    coef_variation = pattern_detour / medium

except Exception as e:
    print(f"Error: {e}")

try:
    # import matplotlib.pyplot as plt
    # fig, ax = plt.subplots(figsize=(10, 6))
    # ax.boxplot(array_estelionato, vert=False, showmeans=True)
    
    plt.subplots(2, 2, figsize=(16, 10))
    plt.suptitle('Análise de roubo de veículos no RJ') 

    # POSIÇÃO 01
    # BOXPLOT
    plt.subplot(2, 2, 1)  
    plt.boxplot(array_fraud_data, vert=False, showmeans=True)
    plt.title("Boxplot dos Dados")

    # POSIÇÃO 02
    # MEDIDAS
    # Exibição de informações estatísticas
    plt.subplot(2, 2, 2)
    plt.title('Medidas Estatísticas')
    plt.text(0.1, 0.9, f'Limite inferior: {limit_inferior}', fontsize=10)
    plt.text(0.1, 0.8, f'Menor valor: {mini}', fontsize=10) 
    plt.text(0.1, 0.7, f'Q1: {q1}', fontsize=10)
    plt.text(0.1, 0.6, f'Mediana: {median}', fontsize=10)
    plt.text(0.1, 0.5, f'Q3: {q3}', fontsize=10)
    plt.text(0.1, 0.4, f'Média: {medium:.3f}', fontsize=10)
    plt.text(0.1, 0.3, f'Maior valor: {maxi}', fontsize=10)
    plt.text(0.1, 0.2, f'Limite superior: {limit_superior}', fontsize=10)

    plt.text(0.5, 0.9, f'Distância Média e Mediana: {distancy:.4f}', fontsize=10)
    plt.text(0.5, 0.8, f'IQR: {iqr}', fontsize=10)
    plt.text(0.5, 0.7, f'Amplitude Total: {full_range}', fontsize=10)
    plt.text(0.5, 0.6, f'Desvio padrão: {pattern_detour:.3f}', fontsize=10)
    plt.text(0.5, 0.5, f'Coeficiente de Variação: {coef_variation:.3f}', fontsize=10)
    
    # POSIÇÃO 03
    # OUTLIERS INFERIORES
    plt.subplot(2, 2, 3)
    plt.title('Outliers Inferiores')
    # Se o DataFrame do outliers não estiver vazio
    if not df_fraud_smallest_outliers.empty:
        dados_inferiores = df_fraud_smallest_outliers.sort_values(by='estelionato', ascending=True) #crescente
        # Gráfico de Barras
        plt.barh(dados_inferiores['munic'], dados_inferiores['estelionato'])
    else:
        # Se não houver outliers
        plt.text(0.5, 0.5, 'Sem Outliers Inferiores', ha='center', va='center', fontsize=12)
        plt.title('Outilers Inferiores')
        plt.xticks([])
        plt.yticks([])
    
    # POSIÇÃO 04
    # OUTLIERS SUPERIORES
    plt.subplot(2, 2, 4)
    plt.title('Outliers Superiores')
    if not df_fraud_highest_outliers.empty:
        dados_superiores = df_fraud_highest_outliers.sort_values(by='estelionato', ascending=True)

        # Cria o gráfico e guarda as barras
        barras = plt.barh(dados_superiores['munic'], dados_superiores['estelionato'], color='black')
        # Adiciona rótulos nas barras
        plt.bar_label(barras, fmt='%.0f', label_type='edge', fontsize=8, padding=2)

        # Diminui o tamanho da fonte dos eixos
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)

        plt.title('Outliers Superiores')
        plt.xlabel('Total Roubos de Veículos')    
    else:
        # Se não houver outliers superiores, exibe uma mensagem no lugar.
        plt.text(0.5, 0.5, 'Sem outliers superiores', ha='center', va='center', fontsize=12)
        plt.title('Outliers Superiores')
        plt.xticks([])
        plt.yticks([])

    # Ajusta os espaços do layout para que os gráficos não fiquem espremidos
    plt.tight_layout()
    # Mostra a figura com os dois gráficos
    plt.show()
  
    
    plt.tight_layout()
    plt.show()
except Exception as z:
    print(f'erro: {z}')
    exit

    

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


try: 
    print('Obtendo dados...')
    Endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    df_ocorrencia = pd.read_csv(Endereco_dados, sep=";", encoding='iso-8859-1')
    # print(df_ocorrencia.head())

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


    # Medidas de dispersão
    print('/nMedidas de Dispersão')
    
    maximo = np.max(array_roubo_carros)
    minimo = np.min(array_roubo_carros)
    amplitude_total = maximo - minimo
    

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
    

    print('\nLimites - Medidasde posição')
    print(f'Limite Inferior: {limite_inferior}')
    print(f'Minimo: {minimo}')
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q3: {q3}')
    print(f'IQR: {iqr}')
    print(f'Máximo: {maximo}')
    print(f'Limite Superior: {limite_superior}')
    print(f'Media: {media:.2f}')
    print(f'Mediana: {mediana:.2f}')
    print(F'distância media e mediana: {distancia}')

    # Medidas de dispersão:
    variancia = np.var(array_roubo_carros)
    print('\nLimites - Medidasde de dispersão')
    distancia_var_media = variancia / (media ** 2)

    # Desvio padrão
    desvio_padrao = np.std(array_roubo_carros)
    coef_variacao = desvio_padrao / media



    print(f'Variancia: {variancia:.2f}')
    print(f'Distancia: {distancia_var_media:.2f}')
    print(f'Desvio Padrão: {desvio_padrao:.2f}')
    print(f'Coeficiente: {coef_variacao:.2f}')


    df_roubo_veiculo_outliers_superiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > limite_superior]
    df_roubo_veiculo_outliers_inferior = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < limite_inferior]
    
    print("\nlimite inferior")
    if len(df_roubo_veiculo_outliers_inferior) == 0:
        print("Não tem outliers inferiores")
    else:
        print(df_roubo_veiculo_outliers_inferior.sort_values(by='roubo_veiculo', ascending=True))

    
    print("\nlimite Superior")
    if len(df_roubo_veiculo_outliers_superiores) == 0:
        print("Não tem outliers superiores")
    else:
        print(df_roubo_veiculo_outliers_superiores.sort_values(by='roubo_veiculo', ascending=False))



except Exception as a:
    print(f'Erro {a}')

#pip install matplotlib
try:
    # import matplotlib.pyplot as plt
    # fig, ax = plt.subplots(figsize=(10, 6))
    # ax.boxplot(array_roubo_veiculo, vert=False, showmeans=True)
    
    plt.subplots(2, 2, figsize=(16, 10))
    plt.suptitle('Análise de roubo de veículos no RJ') 

    # POSIÇÃO 01
    # BOXPLOT
    plt.subplot(2, 2, 1)  
    plt.boxplot(array_roubo_carros, vert=False, showmeans=True)
    plt.title("Boxplot dos Dados")

    # POSIÇÃO 02
    # MEDIDAS
    # Exibição de informações estatísticas
    plt.subplot(2, 2, 2)
    plt.title('Medidas Estatísticas')
    plt.text(0.1, 0.9, f'Limite inferior: {limite_inferior}', fontsize=10)
    plt.text(0.1, 0.8, f'Menor valor: {minimo}', fontsize=10) 
    plt.text(0.1, 0.7, f'Q1: {q1}', fontsize=10)
    plt.text(0.1, 0.6, f'Mediana: {mediana}', fontsize=10)
    plt.text(0.1, 0.5, f'Q3: {q3}', fontsize=10)
    plt.text(0.1, 0.4, f'Média: {media:.3f}', fontsize=10)
    plt.text(0.1, 0.3, f'Maior valor: {maximo}', fontsize=10)
    plt.text(0.1, 0.2, f'Limite superior: {limite_superior}', fontsize=10)

    plt.text(0.5, 0.9, f'Distância Média e Mediana: {distancia:.4f}', fontsize=10)
    plt.text(0.5, 0.8, f'IQR: {iqr}', fontsize=10)
    plt.text(0.5, 0.7, f'Amplitude Total: {amplitude_total}', fontsize=10)
    
    # POSIÇÃO 03
    # OUTLIERS INFERIORES
    plt.subplot(2, 2, 3)
    plt.title('Outliers Inferiores')
    # Se o DataFrame do outliers não estiver vazio
    if not df_roubo_veiculo_outliers_inferior.empty:
        dados_inferiores = df_roubo_veiculo_outliers_inferior.sort_values(by='roubo_veiculo', ascending=True) #crescente
        # Gráfico de Barras
        plt.barh(dados_inferiores['munic'], dados_inferiores['roubo_veiculo'])
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
    if not df_roubo_veiculo_outliers_superiores.empty:
        dados_superiores = df_roubo_veiculo_outliers_superiores.sort_values(by='roubo_veiculo', ascending=True)

        # Cria o gráfico e guarda as barras
        barras = plt.barh(dados_superiores['munic'], dados_superiores['roubo_veiculo'], color='black')
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

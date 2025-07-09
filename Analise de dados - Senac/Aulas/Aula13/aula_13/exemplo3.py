import numpy as np

dados_salario = [2000, 2500, 3000, 3500, 4000, 30000]

# calculando a media e a mediana
media = np.mean(dados_salario)
media_ponderada = np.median(dados_salario)
print("Média", media)
print("Média", media_ponderada)
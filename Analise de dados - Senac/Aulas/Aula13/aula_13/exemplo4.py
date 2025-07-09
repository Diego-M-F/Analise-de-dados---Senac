import numpy as np 

idade = np.array([35, 25, 38, 31, 45, 22, 36, 29, 40, 32])

q1 = np.quantile(idade, 0.25)
q2 = np.quantile(idade, 0.50)
q3 = np.quantile(idade, 0.75)

print('q1: ', q1)
print('q2: ', q2)
print('q3: ', q3)
print("")
media = np.mean(idade)
mediana = np.median(idade)
print(media)
print(mediana)

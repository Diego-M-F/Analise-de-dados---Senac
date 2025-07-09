import numpy as np

casas_valor = np.array([150000, 180000, 200000, 220000, 250000, 280000, 300000, 320000, 400000, 15000000])

mediana_casas = np.median(casas_valor)
media_casas = np.mean(casas_valor)

print(f'Media: R${media_casas:.2f}')
print(f'Mediana: R${mediana_casas:.2f}')

# Resposta: Mediana reflete melhor o valor das casas porque traz o valor
# central e isola o valor que é desproporcional aos outros
l
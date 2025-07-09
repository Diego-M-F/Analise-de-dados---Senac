import pandas as pd
data = {
    'Nome': ['Ana', 'João', 'Maria'],
    'Idade': [23, 25, 29],
    'Gênero': ['F', 'M', 'F'],
    'Altura': [1.70, 1.80, 1.75]
}

df_dados = pd.DataFrame(data)
print(df_dados)
print("")
print("Quantitativo:")
print(df_dados['Idade'])
print("")
print(df_dados['Altura'])
print("")
print("Qualitativo:")
print(df_dados['Nome'])
print("")
print(df_dados['Gênero'])
# print(df_dados[['Nome', 'Gênero']])
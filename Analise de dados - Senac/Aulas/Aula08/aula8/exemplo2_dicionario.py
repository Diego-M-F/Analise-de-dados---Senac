aluno = {
    'Nome': 'Maria',
    'Idade': 29,
    'Curso': 'Análise de Dados'
}

aluno['Nome'] = "Diego"


aluno['Email'] = 'aluno@gmail.com'

print(aluno)

print(aluno['Email'])


# print(aluno)
# print(aluno['Nome'])

for chave, valor in aluno.items():
    print(chave, valor)
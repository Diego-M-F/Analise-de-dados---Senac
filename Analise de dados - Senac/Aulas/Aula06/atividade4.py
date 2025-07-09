notas = [7.5, 8.0, 6.5, 9.0, 7.0, 8.5, 6.0, 9.5, 4.5, 10.0 ]
aprovados = []
reprovados = []
recuperacao = []

for n in notas:
    if n >= 7.0:
        aprovados.append(n)
    elif n < 5.0:
        reprovados.append(n)
    else:
        recuperacao.append(n)

print(f'Quantidade de alunos aprovados {len(aprovados)}.')
print(f'Quantidade de alunos reprovados {len(reprovados)}.')
print(f'Quantidade de alunos em recuperação {len(recuperacao)}.')


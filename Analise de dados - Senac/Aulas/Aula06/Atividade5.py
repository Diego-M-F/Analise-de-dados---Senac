notas = []
nomes = []
aprovado = []
reprovado = []
quantidade = int(input("Informe a quantidade de alunos:"))

for n in range(quantidade):
    nome = input("informe o nome do aluno: ") 
    nomes.append(nome)
    teste = float(input("Informe a nota do teste: "))
    prova = float(input("Informe a nota da prova: "))
    media = (teste + prova) / 2
    notas.append(media)
    print("")

for i in range(len(nomes)):
    if notas[i] > 7:
        aprovado.append([nomes[i],notas[i]])
    else:
        reprovado.append([nomes[i],notas[i]])

print(f'Lista e nota dos alunos aprovados{aprovado}')
print(f'Lista e notas dos alunos reprovados {reprovado}')
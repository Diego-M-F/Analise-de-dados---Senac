# # Explicando for e while
# for

# list_valores = []

# for i in range(5):
#     num = int(input("Informe o número: "))
#     list_valores.append(num)

# print(f'Os números são: {list_valores}')

# While
# list_nomes = []
# resposta = ''

# while resposta != 'n':
#     nome = input("Informe o nome: ").capitalize()
#     list_nomes.append(nome)
#     resposta = input('Gostaria de continuar? [s] para continuar e [n] para sair. ')[0].lower() para pegar apenas a primeira e transformar em minuscula
#     print()

# print(f'Nomes: {list_nomes}')

# list nomes = [ ]
# contador = 0

# while resposta < 5:
#     nome = input("Informe o nome: ").capitalize()
#     list_nomes.append(nome)
#     contador += 1 
#     print()

# print(f'Nomes: {list_nomes}')

# While True
list_nomes2 = []
while True: 
    nome = input("Informe o nome: ").capitalize
    list_nomes2.append(nome)
    resposta = input("Quer continuar? [s/n] ")
    if resposta == "n":
        break

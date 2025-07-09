

def cadastro_pessoa(num):
    for i in range(num):
        nome = input('Informe o nome do vendedor: ')
        valor = input('Informe o valor da venda: ')

        pessoa = {
            'Nome': nome,
            'Valor': valor
        }

        lista_cadastro.append(pessoa)


# Prinipal
lista_cadastro = []
quant = int(input("Quantas Pessoas: "))
cadastro_pessoa(quant)
print(lista_cadastro)
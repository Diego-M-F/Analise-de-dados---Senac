
# cadastra
def cadastro_pessoa(num):
  
    for i in range(num):
        nome = input('Informe o nome do vendedor: ')
        valor = float(input('Informe o valor da venda: '))

        pessoa = {
            'Nome': nome,
            'Valor': valor
        }

        lista_cadastro.append(pessoa)
    

# Media e Total


def calcula_total_media():
    tot = 0
    for pessoa in lista_cadastro:
        tot += pessoa['Valor']

    media = tot / len(lista_cadastro)
    return tot, media


# Maior Venda e Vendedor
def buscar_maior():
    maior = 0
    vendedor = ''
    for i in lista_cadastro:
        if i['Valor'] > maior:
            maior = i['Valor']
            vendedor = i['Nome']
        
    return maior, vendedor

# Procurar Vendedor


def proc_vendedor(nome):
    resposta = ''
    vl = 0
    for cadastro in lista_cadastro:
        if cadastro['Nome'] == nome:
            # resposta = cadastro['Nome']
            # vl = cadastro['Valor']
            return cadastro
    return resposta, vl
            



# Prinipal
lista_cadastro = []
quant = int(input("Quantas Pessoas: "))
cadastro_pessoa(quant)
print(lista_cadastro)

# Exemplo 2 Total e Media


total, media = calcula_total_media()
print(f'total: R${total:.2f}, media: R${media:.2f}')

# Exemplo 3 - Maior Valor e Vendedor.

maior_venda, maior_vendedor = buscar_maior()

print(f'Maior venda: R${maior_venda:.2f}, vendedor: {maior_vendedor}.')

# Exemplo 4 - Buscar Vendedor 
pergunta = input("informe nome do vendedor: ")
# nome_vendedor, valor20 = proc_vendedor(pergunta)
cadastro = proc_vendedor(pergunta)
if cadastro:
    print(f"{cadastro['Nome']}, {cadastro['Valor']:.2f}")
else:
    print(f"{pergunta} não encontrado")
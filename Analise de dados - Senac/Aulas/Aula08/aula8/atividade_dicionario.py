produtos = {
    'Nome': 'Notebook',
    'preco': 3500,
    'estoque': 15
}

produtos.pop('estoque')
produtos['preco'] = 4000
print(f'{produtos["Nome"]}, R$ {produtos["preco"]:.2f}')

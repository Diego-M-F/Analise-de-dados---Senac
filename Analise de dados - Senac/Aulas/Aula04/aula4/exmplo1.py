valor_compra = float(input("Insira o valor da compra: "))
valor_desconto = float(0.16)
LIMITE = 250 #iLetra maiscula é utilizada para constante ou seja valores que não mudam 
if valor_compra > LIMITE:
    valor_compra = valor_compra - (valor_compra * valor_desconto)
    print(f'O valor será de R${valor_compra:.2f}')
else:
    print(f"O valor será de R${valor_compra:.2f}")

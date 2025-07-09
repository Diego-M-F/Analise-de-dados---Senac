
def dobro_num(x):
    dobro = x * 2
    triplo = x * 3
    quadrado = x ** 2
    return dobro, triplo, quadrado


numero = float(input("Informe o Valor: "))
n1, n2, n3 = dobro_num(numero)
print(f'dobro: {n1}, triplo: {n2}, quadrado: {n3}.')

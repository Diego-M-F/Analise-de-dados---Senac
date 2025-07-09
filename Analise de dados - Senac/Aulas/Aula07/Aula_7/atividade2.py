
limite = 100
multa = 4


def multa_dia(n):
    calculo = (n - limite) * multa
    return calculo


peso_dia = float(input("Informe a quantidade de quilos pescada hoje: "))

if peso_dia > limite:
    valor_multa = multa_dia(peso_dia)
    print(f'A multa a ser paga é de R${valor_multa:.2f}.')
else:
    print('Não excedeu o limite de quilos.')

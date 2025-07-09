import random
import os
os.system('cls')


def adicionar(n1, n2): 
    resultado = n1 + n2
    return resultado


def subtrair(n1, n2):
    resultado = n1 - n2
    return resultado


def dividir(n1, n2):
    resultado = n1 / n2
    return resultado


def multiplicar(n1, n2):
    resultado = n1 * n2
    return resultado


numero1 = random.randint(1, 100)
numero2 = random.randint(1, 100)
print('multiplicar [*], adição [+], divisão [/], subtração [-]')
operacao = input("Qual operação: ")
print(f'Os numeros gerados foram {numero1} e {numero2}')


match operacao:
    case "+":
        soma = adicionar(numero1, numero2)
        print(f'O resultado da soma é {soma}.')
    case "-":
        sub = subtrair(numero1, numero2)
        print(f'O resultado da subtação é {sub}.')
    case "/":
        div = dividir(numero1, numero2)
        print(f'O resultado da divisão é {div}.')
    case "*":
        mult = multiplicar(numero1, numero2)
        print(f'O resultado da multiplicação é {mult}.')
    case _:
        print("Operador inválido")

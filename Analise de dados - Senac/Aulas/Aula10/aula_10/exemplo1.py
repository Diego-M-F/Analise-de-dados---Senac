# biblioteca para números aleatórios 
import random
import os
os.system('cls')
# m = random.randint(1, 2)
# n = random.randint(10, 20)

# print(m, n)
# os.system('cls')
# lista_numeros = [random.randint(1, 10) for i in range(5)]
# print(lista_numeros)

# Exemplo 2


def gerar_numeros(i, f, q):
    lst_num = [random.randint(i, f) for num in range(q)]
    return lst_num


ini = int(input("Informe inicio o primeiro número do intervalo: "))
fin = int(input("Informe inicio o segundo número do intervalo: "))
qtd = int(input("Quantos números: "))

lst_numeros = gerar_numeros(ini, fin, qtd)
print(lst_numeros)

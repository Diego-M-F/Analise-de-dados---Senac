# Funções em python inicia com a palavra
# reservada "def".
# Funções são rotinas em seu conceito
# São blocos de códigos que só serão executados se forem chamados.

# def saudação():
#     print('Olá mundo!')


# saudação()

# def linha():
#     print(30*"-")  # Trinta vezes oque está dentro das aspas.


# linha()
# print('Módulo 01')
# linha()
# print('Algorintimos')
# linha()
# print('Análise de dados')
# linha()


# def saudação(texto):
#     print(f'Olá! {texto}.')


# nome = input("informe o nome: ")
# saudação(nome)

# def somar(a, b):
#     s = a + b
#     # print(soma)
#     return s


# soma = somar(4, 5)
# print(f'O valor da variável soma é {soma}')
def somar_numeros(x, y):
    s = x + y
    return s


for i in range(3):
    print(" ")
    n1 = int(input("Informe um número:"))
    n2 = int(input("Informe um número:"))
    
    soma = somar_numeros(n1, n2)
    print(soma)

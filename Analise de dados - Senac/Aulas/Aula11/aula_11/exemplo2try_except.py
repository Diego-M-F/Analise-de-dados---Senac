# try:
#     n1 = float(input("Número: "))
#     n2 = float(input("Número: "))
#     n3 = n1/n2
#     print(n3)
# except ZeroDivisionError as a:
#     print(f"Erro não pode dividir por zero {a}")

# try:
#     n1 = float(input("Número: "))
#     n2 = float(input("Número: "))
#     n3 = n1/n2
#     print(n3)
# except ZeroDivisionError as a:
#     print(f"Não é possível dividir por zero, {a}.")

# except ValueError as a:
#     print(f"Não digite por extenso, {a}.")

# try:
#     n1 = float(input("Número: "))
#     n2 = float(input("Número: "))
#     resultado = n1/n2

# except ZeroDivisionError as a:
#     print(f"Não é possível dividir por zero, {a}.")

# else:
#     print(f'resultado é: {resultado}')

# finally:
#     print("Fim da operação!")
try:
    n1 = float(input("Número: "))
    n2 = float(input("Número: "))
    resultado = n1/n2

except Exception as a:
    print(f"Não é possível dividir por zero, {a}.")

else:
    print(f'resultado é: {resultado}')

finally:
    print("Fim da operação!")

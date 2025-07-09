
try:
    nota1 = float(input("Informe a 1° nota: "))
    nota2 = float(input("Informe a 2° nota: "))
except ValueError as e:
    print(f"Não digite por estenso {e}.")
else:
    if nota1 in range(0, 10) and nota2 in range(0, 10):
        media = (nota1 + nota2) / 2
        print(f"Média: {media}")
        if media > 6:
            print("Aprovado")
        else:
            print("Reprovado")
    else:
        print("Valor da nota está fora dos limites.")
finally:
    print("Desligando")

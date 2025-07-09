nota = float(input("Informe a nota: "))

if nota >= 0:
    if nota >= 7:
        print("Aprovado")
    elif nota >= 5:
        print("Recuperação")
    else:
        print("Reprovado")
else:
    print("Numero Inválido")

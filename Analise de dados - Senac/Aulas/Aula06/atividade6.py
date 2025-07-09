
notas = []

while True:
    pergunta = input("Gostaria de continuar 'S' ou 'N': ")
    if pergunta == 'N':
        break
    elif pergunta == 'S':
        nota = float(input("Informe a nota: "))
        notas.append(nota) 
    else:
        print("Resposta inválida")
        break
    print ("")
if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f'Media é {media}')

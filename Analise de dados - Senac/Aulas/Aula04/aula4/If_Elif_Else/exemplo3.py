tempo_beneficio = 3
quant_beneficio = 5000
tempo_usuario = int(input("Informe o tempo na empresa: "))
quant_usuario = float(input("Informe a quantidade movimentada no periodo: "))

if tempo_usuario >= tempo_beneficio or quant_usuario >= quant_beneficio:
    print("Tem acesso aos beneficios.")
else:
    print("Não tem acesso aos beneficios.")

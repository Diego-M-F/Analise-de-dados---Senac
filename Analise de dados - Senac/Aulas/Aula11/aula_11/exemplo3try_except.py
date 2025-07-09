print('=== Caixa ELETRÔNICO ===')

try:
    saldo = 1000
    saque = float(input('Informe o valor de saque: '))

except ValueError as e:
    print(f'ERRO digite apenas numeros, {e}')
else:
    if saldo >= saque and saque > 0:
        saldo -= saque
    elif saque > saldo:
        print("Saldo insuficiente.")
    else:
        print("O valor do saque precisa ser maior que 0.")

finally:
    print(f'Saldo: {saldo}')
    print('Desligando')

quant_estoque = int(input("Informe quantidade em estoque: "))
quant_pedido = int(input("Informe quantidade do pedido: "))
peso = float(input("Informe o peso do pedido: "))
limite_peso = 50

if quant_estoque >= quant_pedido and peso < limite_peso:
    print("Pedido liberado.")
else:
    print("Não Liberado.")

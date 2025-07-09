#No exercicio o valor do desconto é de 13%.
#valor final da camisa é de R$ 72,21 e o desconto é de R$ 10,79.
desconto_hoje = int(input("Qual a porcentagem do desconto?"))
#comentário para o github
valor_camisa = 83
desconto_porcentagem = desconto_hoje / 100
valor_desconto = valor_camisa * desconto_porcentagem
novo_valor = valor_camisa - valor_desconto

print(f"Valor do desconto é de R${valor_desconto:.2f} Valor final da camisa é de: R${novo_valor}")
print("Valor do desconto é de R$", round(valor_desconto,2), "Valor final da camisa é de R$", novo_valor)
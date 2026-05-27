valor_produto = float(input("Informe o valor do produto: "))
if valor_produto > 100:
    desconto = valor_produto * 0.10
    print("O valor do com desconto é: ", valor_produto - desconto)
else:
    print("O valor do produto não tem desconto e é: ", valor_produto)
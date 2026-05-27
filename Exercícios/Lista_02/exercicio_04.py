# 4. Maior entre Três Números: Peça três números e exiba o maior.

num_1 = int(input("Digite o primeiro nº para comparar: "))
num_2 = int(input("Digite o segundo nº para comparar: "))
num_3 = int(input("Digite o terceiro n º para comparar: "))

if num_1 > num_2 and num_1 > num_3:
	print(f"O primeiro nº {num_1} é maior que o segundo nº {num_2} e o terceiro nº {num_3}")
elif num_2 > num_1 and num_2 > num_3:
	print(f"O segundo nº {num_2} é maior que o primeiro nº {num_1} e o terceiro  nº {num_3}")
elif num_3 > num_1 and num_3 > num_2:
	print(f"O terceiro nº {num_3} é maior que o primeiro nº {num_1} e o segundo nº {num_2}")
else:
	print(f"os números são iguais!")
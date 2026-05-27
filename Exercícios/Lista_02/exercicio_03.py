# 3 peça dois nº e diga qual o maior entre elees

num_1 = int(input("Digite o primeiro nº para comparar: "))
num_2 = int(input("Digite o segundo nº para comparar: "))

if num_1 > num_2:
	print(f"O nº {num_1} é maior que o nº {num_2}")
elif num_1 < num_2:
	print(f"O nº {num_2} é maior que o nº {num_1}")
else:
	print(f"O nº {num_1} é igual ao nº {num_2}")
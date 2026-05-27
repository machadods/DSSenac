# 5. Verificação de Igualdade: Leia dois números e informe se eles são iguais ou diferentes. 

num_1 = float(input("Digite o primeiro nº para comparar: "))
num_2 = float(input("Digite o segundo nº para comparar: "))

if num_1 == num_2:
	print(f"Os nº {num_1} e {num_2} são iguais")
elif num_1 != num_2:
	print(f"Os nº {num_1} e {num_2} são diferentes")
else:
	print(f"Os nº inseridos são invalidos, digite um nº inteiro")
# 8. Classificação de Peso: Leia o peso de uma pessoa e informe se está abaixo do peso (< 18,5), peso ideal (18,5 a 24,9) ou sobrepeso (≥ 25,0).

print("=== Classificação de Peso com IMC ===")
altura = float(input("Digite sua altura: "))
peso  = float(input("Digite seu peso: "))

imc = peso / (altura * altura)

if 18.5 > peso:
	print(f"Devido ao seu IMC {imc} você se encontra abaixo do peso")
elif 18.5 <= peso and peso <= 24.9:
	print(f"Conforme seu IMC {imc} você esta com o peso ideal")
elif 24.9 < peso:
	print(f"Porra nem precisa de calcúlo para seu IMC {imc} é só se olhar no espelho balofo!")
else:
	print(f"valores invalidos!")
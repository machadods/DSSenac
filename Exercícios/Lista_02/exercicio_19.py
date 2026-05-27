num_1 = int(input("Digite o primeiro nº: "))
num_2 = int(input("Digite o segundo nº: "))

operacao = int(input("Digite 1 = soma, 2 = subtração, 3 = multiplicação, 4 = divisão: "))
if operacao == 1:
    resultado = num_1 + num_2
    print(f"A soma entre {num_1} e {num_2} é {resultado}")
elif operacao == 2:
    resultado = num_1 - num_2
    print(f"A subtração entre {num_1} e {num_2} é {resultado}")
elif operacao == 3:
    resultado = num_1 * num_2
    print(f"A multiplicação entre {num_1} e {num_2} é {resultado}")
elif operacao == 4:
    resultado = num_2 / num_1
    print(f"A divisão entre {num_1} e {num_2} é {resultado}")
else:
    print("Operação inválida")
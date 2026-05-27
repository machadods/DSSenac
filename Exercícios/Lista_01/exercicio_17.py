# num = int(input("Digite um nº de dois digitos: "))
# dezena = num // 10
# print(f"dezena: {dezena}")
# unidade = num % 10
# print(f"unidade: {unidade}")

# print(f"A inversão dos digitos de {num} é: {unidade}{dezena}")


# num = int(input("Digite um  nº de dois digitos para inverter: "))
# dezena = num // 10

# num_str = input("Digite um nº de dois digitos para inverter: ")
# inversao = num_str[::-1]

# print(f"A inversão dos digitos de {num_str} é: {inversao}")

num_str = input("digite um nº de dois digitos para inverter: ")
if len(num_str) != 2:
    print("Informe somente dois digitos")
else:
    dezena = num_str[0]
    unidade = num_str[1]
    print(f"A inversão dos digitos de {num_str} é: {unidade}{dezena}")

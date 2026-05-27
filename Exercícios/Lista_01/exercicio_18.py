num = int(input("digite o nº de dois digitos: "))
dezena = num // 10
unidade = num % 10

num_invertido = (unidade * 10) + dezena

subtracao = num - num_invertido

print("o numero invertido é: ", num_invertido)
print("A subtração entre o numero original e o inverso é: ", subtracao)

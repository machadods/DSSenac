real_dolar = 5.25
real_euro = 5.50
real_libra = 6.20

moeda = int(input("Escolha a moeda: 1 - Dolar, 2 - Euro, 3 - Libra: "))
valor = float(input("Digite o valor: "))
if moeda == 1:
    valor_real = valor * real_dolar
    print("O valor em reais é: ", valor_real)
elif moeda == 2:
    valor_real = valor * real_euro
    print("O Valor em reais é: ", valor_real)
elif moeda == 3:
    valor_real = valor * real_libra
    print("O valor em reais é: ", valor_real)
else:
    print("Valor invalido, escolha uma moeda entre 1 e 3")
    
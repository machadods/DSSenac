num = int(input("Digite um numero: "))

if 0 <= num <= 9:
    print("O nº tem um digito")
elif 10 <= num <= 99:
    print("O nº tem dois digitos")
elif 100 <= num <= 999:
    print("O nº tem três digitos")
else:
    print("O nº é negativo ou tem mais de três digitos")
    
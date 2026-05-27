# Número Positivo ou Negativo: Peça um número e informe 
# se ele é positivo, negativo ou zero.     

# numero = int(input("informe um número: "))

# if numero > 0 :
#     print(f"{numero} é maior que 0")
# elif numero == 0:
#     print(f"numero é igual a 0")
# else:
#     print(f"{numero} é menor que 0")

#1 Nº positivo ou Negativo: Peça um nº e informe se ele é positivo negativo ou zero


num_texto = input(" Digite um nº para verificar se é positivo ou negativo: ")

try:
    num_limpo = num_texto.replace(",", ".")
    num = float(num_limpo)

    if num > 0:
        print(f"O nº {num:.0f} é um número positivo!")
    elif num < 0:
        print(f"O nº {num} é um número negativo!")
    else:
        print(f"O nº {num:.0f} é um nº neutro!")
except ValueError:
    print("Valor inválido, digite um nº e não: ", num_texto)

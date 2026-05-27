#10. Faça um algoritmo que receba dois números e exiba a soma de seus quadrados (a² + b²)
           
# a= int(input("Digite o primeiro nº: "))
# b= int(input("Digite o segundo nº: "))

# print(f"A soma dos quadrados de {a} e {b} é: {(a**2) + (b**2)}")

a = int(input("Digite o primeiro nº: "))
a_quadrado = a ** 2
print(a_quadrado)

b = int(input("Digite o segundo nº: "))
b_quadrado = b ** 2
print(b_quadrado)

soma_quadrados = a_quadrado + b_quadrado
print(f"A soma dos quadrados de {a} e {b} é {soma_quadrados}")
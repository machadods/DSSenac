# 2. Faça um algoritmo que receba dois números e:
# a. Realize a subtração do primeiro pelo segundo e exiba o resultado na
# tela.
# b. Realize a subtração do segundo pelo primeiro, e exiba o resultado na
# tela.
termo_1 = int(input("Informe o primeiro termo: "))
termo_2 = int(input("Informe o segundo termo: "))

sub1 = termo_1-termo_2
sub2 = termo_2-termo_1
print(sub1)
print(sub2)
#errado
# print("A subtração entre "+termo_1+" e "+termo_2+" é " +sub1)
print("A subtração entre "+str(termo_1)+" e "+str(termo_2)+" é " +str(sub1))
print(f"A subtração entre {termo_1} e {termo_2} é {sub1}")
print("A subtração entre {} e {} é {}".format(termo_2,termo_1,(termo_2-termo_1)))


numero_1 = int(input("Digite o 1º nº: "))
numero_2 = int(input("Digite o 2º nº: "))

subtracao_1 = numero_1 - numero_2
subtracao_2 = numero_2 - numero_1

print(subtracao_1) # Errado pois não informa nada apenas o resultado 0
print(subtracao_2)


# Forma correta póis explica o que é o resultado
print(f"A subtrção entre {numero_1} e {numero_2} é igual a {subtracao_1}")
print(f"A subtração entre {numero_2} e {numero_1} é igual a {subtracao_2}")

      

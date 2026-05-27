# O laço while repere um bloco enquanto uma condição for verdadeira. É ideal quando não sabemos antecipadamente quantas interções serão necessárias.

# Exercicio 1: Leia um númro inteiro positivo N e exiba todos os nº de 1 até N um por linha


n = int(input("Digite o número para exibir a lista até ele: "))

contador = 1 # para iniciar

# Loop principal

while contador <= n:
    print(contador)
    contador += 1 # para add 1 a cada contagem



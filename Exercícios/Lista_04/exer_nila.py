# Configuração de decimal importar Decimal e getcontext para forçar o Python a 22 casas decimais pq o terminal tem preguiça de mostrar mais do que isso, por isso getcontext().prec = 22
from decimal import Decimal, getcontext
getcontext().prec = 22

# Variaveis para calculo, mudança de sinal e iterações
pi = Decimal('3')
n = Decimal('2')
sinal = Decimal('1')
iteracoes = 1

#Loop simples enquanto for verdade que o valor de pi seja diferente do valor real, ele continua calculando
while True:
    pi = pi + sinal * (Decimal('4')/ (n * (n + Decimal('1')) * (n + Decimal('2')))) # formula de Nilakantha: pi = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - ... adaptada para o codigo

    sinal = sinal * Decimal('-1') # metodo de mudar o sinal, multiplicando por -1 ele alterna entre positivo e negativo
    n = n + Decimal('2') # metodo de aumentar o valor para sequencia real
    iteracoes = iteracoes + 1 # metodo para contar iteraçoes

# comparação com o valor objetivo, se for igual da break e interrompe o loop
    if pi == Decimal('3.14159265358979323846'):
        break

print (f"Para conseguir o valor de pi = {pi:.20f} foram necessárias {iteracoes} iterações confirmando a operação correta do código a chegar em 20 casas decimais para o valor de pi")

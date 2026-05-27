# Configuração de decimal importar Decimal e getcontext para forçar o Python a 21 casas decimais pq o terminal tem preguiça de mostrar mais do que isso, por isso getcontext().prec = 21
from decimal import Decimal, getcontext
getcontext().prec = 21

# O valor de Pi real para comparação
pi_real = Decimal("3.14159265358979323846")

# Variáveis para o cálculo
pi = Decimal("3.0")
sinal = Decimal("1")
n = Decimal("2")
iteracoes = 0

# O loop usa round(pi,20) != round(pi_real, 20) para forçar a comparaçã e enquanto estiver diferente ele continua calculando

while round(pi, 20) != round(pi_real, 20):
    denominador = n * (n + 1) * (n + 2)
    
    # Formula de Nilakantha: pi = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - ...
    pi += sinal * (Decimal("4.0") / denominador)
    
    sinal *= -1 # Alterna o sinal para a próxima iteração
    n += 2 # Incrementa n para a próxima iteração e soma 2 para seguir a sequência 2, 4, 6, 8...
    iteracoes += 1 #

print(f"Número de iterações: {iteracoes}")
print(f"Pi Real:       {pi:.20f}")
print(f"Pi Calculado:  {pi:.20f}")

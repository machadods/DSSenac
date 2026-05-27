
# 6. Classificação de Idade: Peça a idade de uma pessoa e diga se ela é criança (0 12), adolescente (13-17) ou adulta (18+).

# idade = int(input("Digite sua idade para classificação: "))
# if 0 <= idade <= 12:
# 	print(f"Você é uma criança por ter {idade} anos de idade!")
# elif 13 <= idade <= 17:
# 	print(f"Você é um aborrecente por ter {idade} anos de idade!")
# elif idade >= 18:
# 	print(f"Você já pode ser preso por ter {idade} anos de idade e ser um adulto!")
# else:
# 	print(f"Você digitou um valor inválido!")

try:
    idade = int(input("Digite sua idade para classificação: "))

    if idade < 0:
        print(f"Você digitou um valor invalido")
    elif 0 <= idade <= 12:
        print(f"Você é uma criança por ter {idade} anos de idade!")
    elif 13 <= idade <= 17:
        print(f"Você é um aborrecente por ter {idade} anos de idade!")
    elif idade >= 18:
        print(f"Você já pode ser preso por ter {idade} anos de idade e ser um adulto!")
except ValueError:
    print("Erro: digite apenas número inteiro para idade!")
    
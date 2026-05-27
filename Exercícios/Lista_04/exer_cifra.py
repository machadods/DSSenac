# 1. Entradas simples do usuário
chave = int(input("Digite a chave (1 a 25): "))
msg_original = input("Digite a mensagem: ")

# Alfabeto completo com letras minúsculas e maiúsculas
alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Criando os dicionários vazios
dic_cifrar = {}
dic_decifrar = {}

# 2. Criando as tabelas de conversão letra por letra
for letra in alfabeto:
    # Encontra a posição atual da letra (de 0 a 51)
    posicao_atual = alfabeto.index(letra)
    
    # Soma a chave para descobrir a nova posição
    nova_posicao = posicao_atual + chave
    
    # AJUSTE PARA MINÚSCULAS: Se passar do 'z' (posição 25), volta para o 'a' (0)
    if letra.islower() and nova_posicao > 25:
        nova_posicao = nova_posicao - 26
        
    # AJUSTE PARA MAIÚSCULAS: Se passar do 'Z' (posição 51), volta para o 'A' (26)
    if letra.isupper() and nova_posicao > 51:
        nova_posicao = nova_posicao - 26
        
    letra_cifrada = alfabeto[nova_posicao]
    
    # Salva nos dicionários de ida e volta
    dic_cifrar[letra] = letra_cifrada
    dic_decifrar[letra_cifrada] = letra

# 3. Cifrando a mensagem
msg_cifrada = ""
for letra in msg_original:
    if letra in dic_cifrar:
        msg_cifrada = msg_cifrada + dic_cifrar[letra]
    else:
        msg_cifrada = msg_cifrada + letra # Mantém espaços e pontos

# 4. Decifrando a mensagem de volta
msg_decifrada = ""
for letra in msg_cifrada:
    if letra in dic_decifrar:
        msg_decifrada = msg_decifrada + dic_decifrar[letra]
    else:
        msg_decifrada = msg_decifrada + letra # Mantém espaços e pontos

# 5. Mostrando tudo na tela
print("\n--- RESULTADOS ---")
print("Chave:", chave)
print("Dicionario Cifrar:", dic_cifrar)
print("Dicionario Decifrar:", dic_decifrar)
print("Original:", msg_original)
print("Cifrada:", msg_cifrada)
print("Decifrada:", msg_decifrada)

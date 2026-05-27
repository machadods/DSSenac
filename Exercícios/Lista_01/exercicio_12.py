#12. Faça um algoritmo que receba o raio de um círculo e exiba sua área (A = π ×
#r²) e o seu volume (V = (4/3) × π × r³). Considere π = 3.14159.

pi = 3.14159
raio = int(input("Digite o raio escolhido: "))

area = pi * (raio ** 2)
volume = (4/3) * pi * (raio ** 3)

print(f"A área do círculo é {area:.2f} cm²")
print(f"O volume do círculo é {volume:.2f} cm³")

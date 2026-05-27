# 7. Nota do Aluno: Leia a nota de um aluno e informe se ele está aprovado (nota ≥ 7,0) ou reprovado.

nota = float(input("Digite a nota do aluno para descobrir sua condição: "))
if 7.0 <= nota:
	print(f"Aluno aprovado com a nota {nota}")
else:
	print(f"Aluno reprovado com a nota {nota}")
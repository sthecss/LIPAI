""" 
Exercício 2 - Controle de Fluxo 
Solicite notas no formato n1, n2... e apresente média e situação.
"""

print('The scores must be in the format: "n1, n2, n3, n4..."')
scores_input = input("Enter the scores: ")

# Tratamento da string
scores_str = scores_input.split(", ")

# Conversão usando List Comprehension (mais legível que map+lambda)
scores = [float(x) for x in scores_str]

# Cálculo
average = sum(scores) / len(scores)
print(f"Average: {average:.2f}")

# Verificação da Situação
# Aprovado > 6.0 | Recuperação 4.0 <= média <= 6.0 | Reprovado < 4.0
if average > 6:
    print("Approved")
elif 4.0 <= average <= 6.0:
    print("Retake Exam")
else:
    print("Reproved")

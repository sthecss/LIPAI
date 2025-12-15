""" 
Exercício 1 - Controle de Fluxo 
Solicite ao usuário 3 notas e apresente o resultado da média aritmética.
"""

soma = 0

# Entrada e Processamento
for i in range(1, 4):
    # Acumulamos o valor na variável 'soma'
    nota = int(input(f"Enter the {i} score: "))
    soma += nota

# Cálculo final
media = soma / 3

# Saída
print(f"Average: {media:.2f}")

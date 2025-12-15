""" 
Exercício 1 - Tipos de Dados: Listas e Funções Built-in

Objetivo:
- Solicitar 3 números.
- Armazenar em uma lista.
- Apresentar o maior e o menor valor.
"""

numbers = []

# Coleta de dados
# Usamos range(1, 4) para exibir 1, 2, 3 no print (melhor para o usuário)
for i in range(1, 4):
    num = int(input(f"Enter the {i}º number: "))
    numbers.append(num)

# Processamento e Saída
# max() e min() são funções nativas do Python para listas
highest = max(numbers)
lowest = min(numbers)

print("-------------------")
print(f"Highest Number: {highest}")
print(f"Lowest Number: {lowest}")

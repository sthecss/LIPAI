""" Aula 03 - Estrutura de Repetição (Loop For) """

# Usos principais:
# 1. Iteração em coleção de elementos (listas, strings, etc)
# 2. Repetir uma instrução determinado número de vezes

linguagens = ["C", "Python", "Java"]

# Acesso manual (pouco prático):
print(linguagens[0])

# --- Iteração direta (Item a Item) ---
print("--- Lista de Linguagens ---")
for linguagem in linguagens:
    print(linguagem.upper())

# --- Cálculo de Média com For ---
notas = [10.0, 5.5, 8.3, 2.5]
soma = 0.0

for nota in notas:
    soma += nota  # Operador de incremento

media = soma / len(notas)
print(f"A média é: {media:.2f}")

# --- Função range() ---
# range(inicio, fim, passo)
# O 'fim' é exclusivo (não entra na contagem)

# print(list(range(10)))      # 0 a 9
# print(list(range(5, 10)))   # 5 a 9

print("--- Contagem Regressiva ---")
valores = range(9, -1, -1)
for valor in valores:
    print(valor)

# --- Iteração por Índice ---
# Útil quando precisamos alterar o valor na lista original
print("--- Acessando por índice ---")
for i in range(len(linguagens)):
    print(f"Índice {i}: {linguagens[i]}")

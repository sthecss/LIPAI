""" Aula 03 - Tipos de Dados: Sets (Conjuntos) """

# Características dos Sets:
# - Não ordenados (a ordem de print pode variar)
# - Mutáveis (podemos adicionar/remover)
# - Não indexáveis (não existe set[0])
# - Não aceitam elementos duplicados

# Criar um set
numeros = {1, 12, 5, 7, 4, 3, 3, 1}
# Note que os repetidos (3 e 1) serão ignorados
print(numeros, type(numeros))

# Iteração
for numero in numeros:
    print(numero)

# Verificação de existência (in)
print(3 in numeros)
print(50 in numeros)

# --- Adicionar itens ---
print(numeros)
numeros.add(8)
print(numeros)

# --- Unir Sets (Update) ---
print("-------")
print(numeros)

numeros2 = {1, 5, 4, 4, 3, 9}
print(numeros2)

# Adiciona elementos de numeros2 em numeros (sem duplicar)
numeros.update(numeros2)
print(numeros, type(numeros))

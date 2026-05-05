""" Aula 01 - Tipos de Dados: Listas (Lists) """

# Características das Listas:
# - Ordenadas
# - Mutáveis (podemos alterar)
# - Indexáveis (acessíveis por índice)

nomes = ['Maria', 'Pedro', 'João', 1, True]
print(nomes, type(nomes))

# --- Acessando Elementos ---
print(nomes[0])
print(nomes[0:2])
print(nomes[:2])
print(nomes[1:])

# --- Modificando Elementos ---
nomes[0] = 'Maria da Silva'
nomes[1:] = ['Pedro da Silva', 'João Santos']  # Fatiamento (Slicing)
print(nomes)

# --- Tamanho da Lista ---
tamanho = len(nomes)
print(f"Tamanho da lista: {tamanho}")

# --- Adicionar Elementos ---

# 1. Método append (adiciona ao final)
nomes.append('Marta Gomes')
print(nomes)

# 2. Método insert (adiciona em posição específica)
nomes.insert(0, 'Guilherme Tavares')
print(nomes)

nomes.insert(2, 'Ana Lúcia')
print(nomes)

# 3. Método extend (juntar listas)
nomes2 = ['Kaio Silva', 'Carlos Gomes']
print(len(nomes))

nomes.extend(nomes2)
print(len(nomes))
print(nomes)

# --- Remover Elementos ---

# 1. remove (pelo valor)
nomes.remove('Maria da Silva')
print(nomes)

# 2. del (pelo índice)
del nomes[0]
print(nomes)

# 3. del (deletar objeto da memória)
# del nomes
# print(nomes) # Isso causaria erro pois a variável deixaria de existir

# 4. clear (limpar conteúdo)
# nomes.clear()
print(nomes)

# --- Iteração (Loops) ---

# For Each (Para cada item)
print("--- Loop por item ---")
for nome in nomes:
    print(nome)

# For Range (Por índice)
print("--- Loop por índice ---")
for i in range(len(nomes)):
    print(nomes[i])

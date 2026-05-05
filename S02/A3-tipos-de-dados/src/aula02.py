""" Aula 02 - Tipos de Dados: Tuplas (Tuples) """

# Características das Tuplas:
# - Ordenadas
# - Imutáveis (NÃO podemos alterar)
# - Indexáveis

nomes = ('Maria', 'Pedro', 'João')
print(nomes, type(nomes))

# --- Acessando Elementos ---
print(nomes[0])
print(nomes[0:2])
print(nomes[:2])
print(nomes[1:])

# --- Imutabilidade ---
# Tentar alterar gera erro (TypeError):
# nomes[0] = 'Maria da Silva'

# --- Iteração ---
for nome in nomes:
    print(nome)

for i in range(len(nomes)):
    print(nomes[i])

print("-----")

# --- Criação sem parênteses e Unpacking ---
nomes2 = 'Ana', 'Amélia', 'Marcos'
print(nomes2, type(nomes2))

# Unpack (Desempacotamento manual)
nome1 = nomes2[0]
nome2 = nomes2[1]
nome3 = nomes2[2]

# Unpack (Desempacotamento automático)
nome1, nome2, nome3 = nomes2
print(nome1, nome2, nome3)

# --- Concatenação ---
todos_nomes = nomes + nomes2
print(todos_nomes, type(todos_nomes))

""" Aula 05 - LIPAI - Tipos de Dados em Python """

# --- Numéricos ---
# int (inteiro), float (ponto flutuante)

idade = 20
peso = 70.5

print(idade, type(idade))
print(peso, type(peso))

# --- Strings ---
nome = "Pedro"  # Corrigido de 'Predro'
sobrenome = 'dos Santos'

# Concatenação antiga:
nome_completo = nome + ' ' + sobrenome
print(nome_completo)

# F-strings (Recomendado):
produto = 'Coca-Cola'
print(f"O cliente {nome_completo} comprou o produto {produto}")

# Indexação e Métodos:
print(nome[0], nome[-1])  # Primeiro e último caractere
print(nome.lower())
print(nome.upper())

# Separador no print:
print(1, 3, 7, 10, 'Final', sep=' - ')

# --- Booleanos ---
ligado = True
print(ligado, type(ligado))

resultado = 10 < 3      # False
resultado2 = 10 == 10   # True
print(resultado, type(resultado))
print(resultado2, type(resultado2))

# --- Coleções ---

# 1. Listas (Mutáveis, ordenadas)
frutas = ['maçã', 'banana', 'laranja']
print(frutas, type(frutas))
print(frutas[0])  # Acesso por índice

# Modificando a lista:
frutas[0] = 'Maçã Argentina'
frutas.append('abacaxi')

print(frutas)
print(f"Total de frutas: {len(frutas)}")

# Iteração:
for fruta in frutas:
    print(fruta.upper())

# 2. Tuplas (Imutáveis)
codigos = ('SP01', 'SP02', 'SP03')
print(codigos[0])

# codigos[0] = 'SP10'  # TypeError: Tuplas não podem ser alteradas!
print(len(codigos))

# 3. Conjuntos (Sets - não ordenados, sem duplicatas)
resultado_sorteio = {10, 4, 3, 55, 9}
print(resultado_sorteio)

resultado_sorteio.add(18)
print(resultado_sorteio)

# 4. Dicionários (Chave: Valor)
funcionarios = {
    'codigo': 123,
    'nome': 'Ana Silva',
    'salario': 4500.00
}

print(funcionarios)
print(funcionarios['nome'])
print(funcionarios.keys())
print(funcionarios.values())

# Atualizando valor:
funcionarios['salario'] = 9000.00
print(funcionarios)

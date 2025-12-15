""" Aula 02.01 - Operadores em Python """

# --- 1. Operadores Aritméticos ---
n1 = 10.2
n2 = 3.5
resultado = n1 + n2 + 8.5

# Exibindo resultados e tipos:
print('1 + 1 =', 1 + 1, type(1 + 1))
print('1.2 + 1.3 =', 1.2 + 1.3, type(1.2 + 1.3))
print('Resultado:', resultado, type(resultado))

print(3 - 1)
print(3 * 2, type(3 * 2))
print(3 / 2, type(3 / 2))       # Divisão normal (float)
print(3 % 2, type(3 % 2))       # Módulo (resto da divisão)
print(10 // 3)                  # Divisão inteira
print(10 ** 2)                  # Potenciação

# --- 2. Operador de Atribuição ---
x = 10
print(f"Valor de x: {x}")

# --- 3. Operadores de Comparação ---
resultado_comp = x > 10
print(resultado_comp, type(resultado_comp))

print('10 == 10', 10 == 10)  # Igual
print('10 != 10', 10 != 10)  # Diferente
print('10 > 10', 10 > 10)   # Maior
print('10 >= 10', 10 >= 10)  # Maior ou igual
print('10 < 10', 10 < 10)   # Menor
print('10 <= 10', 10 <= 10)  # Menor ou igual

# --- 4. Operadores Lógicos ---
# Tabela verdade básica
print('True and True:', True and True)
print('True and False:', True and False)
print('False or True:', False or True)
print('False or False:', False or False)

condicao = True
print('not condicao:', not condicao)  # Negação

# --- 5. Operadores Especiais ---

# IS vs ==
# == verifica VALOR
# is verifica REFERÊNCIA DE MEMÓRIA (Identidade)

a = 10
b = 10.0
c = b

print(f"a == b: {a == b}")  # True (valores equivalentes)
# False (int vs float são objetos diferentes na memória)
print(f"a is b: {a is b}")
print(f"b is c: {b is c}")  # True (apontam para o mesmo objeto)

# IN (Pertencimento)
frase = 'Você é um palavrão'

print('palavrão' in frase)  # True
print('Palavrão' in frase)  # False (Case sensitive)

# In em Coleções
numeros = {1, 5, 2, 6}
print(10 in numeros)

pessoa = {
    'nome': 'Maria',
    'idade': 22,
    'email': 'maria@gmail.com'
}

# IMPORTANTE: Em dicionários, o 'in' busca pelas CHAVES, não pelos valores.
print('nome' in pessoa)  # True
print(22 in pessoa)      # False (22 é valor, não chave)

""" Aula 02 -Keyboards e identificadores"""

# Palavras reservadas: True, False, None, and, import, lambda

# Identificadores:
# Nome de variáveis , funções, classes
# Case sensitive
# Devem iniciar com uma letra ou _
# Não pode ter espaços em branco
# Convenção é em snake, não é comum o cammel
# Não pode usar caracteres especiais: !, @, #, $

nome = 'Maria'
idade = 30

Nome = 'João'

c = 10
contador = 10
s = 10 + 20
soma = 10 + 20

# Constantes:
PI = 3.14
idade = 18

if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')

# Boa prática:
MAIORIDADE = 18
if idade >= MAIORIDADE:
    print('Maior de idade')
else:
    print('Menor de idade')

""" Aula 06 - LIPAI - Conversão de Tipos (Casting) """

# 1. Conversão Implícita (Automática)
# O Python converte int para float automaticamente quando necessário.
leitura = 5.53
peso = 3
total = leitura * peso
print(total, type(total))

# 2. Conversão Explícita (Manual)
# Quando precisamos forçar o tipo (ex: somar string numérica com float).
soma = 13.4 + float('3.5')
print(soma)

idade = int('32')
print(idade, type(idade))

# 3. Conversão em Strings
nome = 'Maria'
altura = 1.70

# Forma antiga (Trabalhosa - precisa converter tudo para str):
# mensagem = nome + ' tem ' + str(altura) + ' de altura.'

# Forma Pythonica (f-string - conversão automática na visualização):
mensagem = f"{nome} tem {altura} de altura."
print(mensagem)

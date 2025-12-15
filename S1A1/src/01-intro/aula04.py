""" Aula 04 -  Variaveis, Constantes e Literais """

# Variavel container para guardar dados
# inferencia de tipo

numero = 10
print(numero)
print(type(numero))

# E taambém pode:
print(numero, type(numero))

# Alterar o valor de uma variavel:
numero = 20
print(numero)

# Multipllas atribuicoes:
nome, idade, endereco = 'Maria', 20, 'Rua das...'

# E apesar de poder, é de bom tom:
nome = 'Maria'
idade = 20
endereco = 'Rua das...'
print(nome, idade, endereco)

# E podemoos atribuir o mesmo valor para varias variaveis:
nome1 = nome2 = nome3 = 'Joao'
print(nome1, nome2, nome3)

# Perceba que não tem problema, é apontamento de valor, não encadeamento:
nome2 = 'Pedro'
print(nome1, nome2, nome3)

# Variaveis:
# snake_case
id_funcionario = 209

salario_atual = 5000

print(id_funcionario, salario_atual)

# Ex: quero renomar salariooAtual paara salario_atual
# selecione a palavra, F2, renomeie
# Pronto, toda ocorrencia será renomeada também

# Recomendação:
# skae_case : variavell funcao
# PascalCase : nome de classe


# Constantes:
# Upper case

PI = 3.14
MAIORIDADE_CIVIL = 21
MAIORIDADE_PENAL = 18

print(PI, MAIORIDADE_CIVIL, MAIORIDADE_PENAL)

# Literais:
idade = 27
print(idade)
print(27)  # <- literall

# Numericos:
print(10, type(10))
print(10, type(-10))
print(10.5, type(10.5))

# String:
print('Maria', type('Maria'))
print("Maria", type("Maria"))
# Quando usar cada uma:
# Você escolhe :D, e mantenha o padrão para consistencia

# Mas há uma dica!! se houver apostrofe na string, use aspas
# se há aspas, use apostrofe
print('O filme estava ¨excelente¨')
print("John's house")

# Booleano
print(True, type(True))
print(False, type(False))

# None
print(None, type(None))

# Coleções:

# Lista (list)
numeros = [1, 3, 5]
print(numeros, type(numeros))

# Tupla (tuple)
emails = ('joao@gmaail.com', 'maria@email.com')
print(emails, type(emails))

# Conjunto (set)
nomes = {'maria', 'joao', 'pedro', 'maria'}
print(nomes, type(nomes))

# Dicionario (dictionary)
aluno = {
    'prontuario': 21345, 
    'nome': 'Maria da Silva',
    'idade':34 
}

print(aluno, type(aluno))
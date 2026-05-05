""" Aula 02 - Argumentos: Posicional, Keyword e Default """


def somar(n1, n2):
    return n1 + n2


def dividir(dividendo, divisor):
    return dividendo / divisor


# --- 1. Argumentos Posicionais ---
# A ordem importa!
print(f"Soma posicional: {somar(10.0, 3.5)}")
print(f"Divisão posicional: {dividir(10.0, 2.0)}")  # 10 / 2 = 5


# --- 2. Unpacking (Desempacotamento) ---
# Usando * para listas/tuplas e ** para dicionários

# Lista/Tupla -> Argumentos Posicionais
numeros_lista = [10.0, 5.5]

# Manual:
print(somar(numeros_lista[0], numeros_lista[1]))

# Com Unpacking (*):
print(f"Soma com unpacking de lista: {somar(*numeros_lista)}")


# Dicionário -> Argumentos Nomeados
numeros_dict = {
    "n1": 10.2,
    "n2": 5.3
}
# Com Unpacking (**):
print(f"Soma com unpacking de dict: {somar(**numeros_dict)}")


# --- 3. Argumentos Nomeados (Keyword Arguments) ---
# A ordem não importa, pois especificamos o nome.
print(somar(n1=3.0, n2=6.2))
print(somar(n2=5.0, n1=7.8))

# Muito útil para clareza:
print(dividir(divisor=3.0, dividendo=10.0))  # 10 / 3 = 3.33...


# --- 4. Valores Padrão (Default Values) ---
# Parâmetros opcionais devem vir SEMPRE por último.

def saudacoes(nome, saudacao='Oi'):
    return f'{saudacao}, {nome}!'


# Uso padrão (assume 'Oi')
print(saudacoes('João'))

# Sobrescrevendo o padrão
print(saudacoes('Maria', 'Bom dia'))

# Misturando nomeados e padrão
print(saudacoes(saudacao='Olá', nome='Marcio'))

""" Aula 04 - Tipos de Dados: Dicionários (Dicts) """

# Características dos Dicionários:
# - Coleção de chave-valor (key-value)
# - Chave (key): deve ser única
# - Mutáveis

# Criar um dicionário
carro = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}

# --- Acessar Valores ---
print(carro, type(carro))
print(carro["marca"])      # Acesso direto
print(carro.get("marca"))  # Acesso via método (seguro)

# --- Métodos de Visualização ---
print(carro.keys())   # Apenas chaves
print(carro.values())  # Apenas valores
print(carro.items())  # Pares (tuplas)

# --- Verificação (in) ---
print("marca" in carro)  # True
print("cor" in carro)   # False

# --- Adicionar/Alterar ---
# Adicionar chave/valor de forma dinâmica
carro["cor"] = "Azul"

print("cor" in carro)
print(carro, type(carro))

# --- Remover ---
# Remove a chave e retorna o valor removido
marca = carro.pop("marca")
print(marca)
print(carro)

# --- Iteração (Loops) ---

# Loop padrão (pelas chaves)
print("--- Loop Keys ---")
for key in carro:
    print(key, carro[key], type(key))

# Loop apenas valores
print("--- Loop Values ---")
for value in carro.values():
    print(value)

# Loop apenas chaves (explícito)
for key in carro.keys():
    print(key)

# Loop itens (Chave e Valor juntos)
print(carro.items())

print("--- Loop Items (Unpacking) ---")
for key, value in carro.items():
    print(f"{key}: {value}")

# --- Estruturas Complexas (Lista de Dicionários) ---
aluno1 = {
    "nome": "João",
    "email": "joão@email.com",
    "notas": [10.0, 5.3, 7.0]
}

aluno2 = {
    "nome": "Maria",
    "email": "maria@email.com",
    "notas": [10.0, 2.3, 10.0]
}

alunos = [aluno1, aluno2]

print("--- Iterando Lista de Alunos ---")
for aluno in alunos:
    print(aluno['nome'], aluno['email'])
    for nota in aluno['notas']:
        print(f"Nota: {nota}")

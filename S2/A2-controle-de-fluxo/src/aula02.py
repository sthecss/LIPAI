""" Aula 02.02 - Instrução if (Condicionais) """

# Estrutura básica:
# if condicao:
#     instrucao

# --- Exemplo 1: Flags Booleanas ---
codigo_cliente = 32
valor_desconto = 30.0

# É comum criar variáveis booleanas explicativas (boas práticas)
tem_desconto_especial = valor_desconto >= 20.0

if tem_desconto_especial:
    print("Desconto Especial aplicado!")
    print(f"Cliente: {codigo_cliente}")
else:
    print("Sem desconto especial")

# --- Exemplo 2: Validação de String ---
nome = "Lois"
print(f"Tamanho do nome: {len(nome)}")

# Verificação negativa
nome_invalido = len(nome) < 3

if nome_invalido:
    print("Erro: Nome deve ter pelo menos 3 caracteres.")
else:
    print("Nome válido.")

# --- Exemplo 3: Acumulando Erros (Validação Robusta) ---
nome_input = "Lo"
idade_input = 17
lista_erros = []

if len(nome_input) < 3:
    lista_erros.append("Nome deve ter pelo menos 3 caracteres.")

if idade_input < 18:
    lista_erros.append("Idade deve ser maior ou igual a 18.")

# Truthy e Falsy Values em Python:
# Considerados False: False, None, 0, 0.0, '', [], (), {}
# Considerados True: Todo o resto

if lista_erros:  # Se a lista não estiver vazia (True)
    print("Foram encontrados erros:", lista_erros)
else:
    print("Dados válidos.")

# --- Exemplo 4: if / elif / else ---
numero = -4

if numero > 0:
    print("Maior que zero")
elif numero == 0:
    print("Zero")
else:
    print("Menor que zero")

# --- Exemplo 5: Lógica aninhada vs Lógica limpa ---
n1 = 5.6
n2 = 10.0

# Validação Pythonica (Encadeamento de comparadores)
nota1_valida = 0 <= n1 <= 10
nota2_valida = 0 <= n2 <= 10

if nota1_valida and nota2_valida:
    media = (n1 + n2) / 2

    if media >= 6:
        print(f"Média {media}: Aprovado")
    elif media >= 4:
        print(f"Média {media}: Recuperação")
    else:
        print(f"Média {media}: Reprovado")
else:
    print("Notas inválidas inseridas.")

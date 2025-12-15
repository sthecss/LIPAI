"""
Exercício 4 - Controle de Fluxo 
Validação de identificador com relatório de erros.
"""

id_user = input("Enter the id: ")
errors = []

# Validações independentes
if len(id_user) != 7:
    errors.append("The identifier does not have 7 characters.")

if not id_user.startswith("BR"):
    errors.append("The identifier does not start with the sequence BR.")

if not id_user.endswith("X"):
    errors.append("The identifier does not end with the character X.")

# Validação Numérica
# Verifica se os caracteres do meio são dígitos antes de converter
middle_part = id_user[2:-1]

if middle_part.isdigit():
    num = int(middle_part)
    # Se NÃO estiver entre 1 e 9999, é erro
    if not (1 <= num <= 9999):
        errors.append("The number is not between 0001 and 9999.")
else:
    errors.append("The middle section must be numeric.")


# Saída de Dados
if len(errors) == 0:
    print("Valid identification")
else:
    print("Invalid identification")
    print("Errors found:")
    for error in errors:
        print("-", error)

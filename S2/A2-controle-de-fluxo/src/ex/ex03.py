""" 
Exercício 3 - Controle de Fluxo 
Validação de identificador (BR + 4 dígitos + X).
"""

id_user = input("Enter the id: ")
correctness = 0

# 1. Verifica tamanho (7 caracteres)
if len(id_user) == 7:
    print("Correct length")
    correctness += 1

# 2. Verifica início (BR)
if id_user.startswith("BR"):
    print("Starts with BR...")
    correctness += 1

# 3. Verifica fim (X)
if id_user.endswith("X"):
    print("Ends with X...")
    correctness += 1

# 4. Verifica meio (Numérico entre 0001 e 9999)
# Primeiro verificamos se o miolo É um número para não quebrar o programa
middle_part = id_user[2:-1]

if middle_part.isdigit():
    num = int(middle_part)
    if 1 <= num <= 9999:
        print(f"{num} is a Correct Middle Number")
        correctness += 1
else:
    print("Middle part is not a number")

# Resultado Final
if correctness == 4:
    print("Valid identification")
else:
    print("Invalid identification")

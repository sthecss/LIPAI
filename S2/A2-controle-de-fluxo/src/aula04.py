""" Aula 02.04 - Estrutura de Repetição (Loop While) """

# while condicao:
#     instrução
#     instrução

# Cuidado: O While requer atenção para não criar loops infinitos.
# A condição de parada deve ser garantida dentro do bloco.

contador = 0

print("--- Iniciando contagem ---")
while contador <= 10:
    print(f"Contador: {contador}")
    contador += 1  # Incremento essencial

print('--- Fim do programa ---')

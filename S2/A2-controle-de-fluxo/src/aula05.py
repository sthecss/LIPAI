""" Aula 02.05 - Comandos de Controle (Break e Continue) """

# Break: Interrompe o loop imediatamente

print("--- Exemplo Break simples ---")
for i in range(10):
    if i == 4:
        print("Encontrei o 4, parando...")
        break
    print(i)

# --- Algoritmo de Busca Linear ---
# Objetivo: Encontrar a posição de um número na lista.
# Se não encontrar, posição será -1.

busca = 5
numeros = [1, 4, 9, 7, 5, 3, 2, 1, 7]
posicao = -1

# Método 1: Contador manual
contador = 0
for numero in numeros:
    # print(f"Verificando índice {contador}...")
    if numero == busca:
        posicao = contador
        break  # Encontrou? Para de procurar! (Otimização)
    contador += 1

print(f"Número {busca} encontrado no índice: {posicao}")

# Método 2: Usando range e len (Mais comum em C/Java)
posicao = -1
for i in range(len(numeros)):
    if numeros[i] == busca:
        posicao = i
        break

# Dica buoa: Existe a função enumerate() que dá o índice e o valor juntos
# for i, numero in enumerate(numeros): ...

# --- Continue ---
# Pula a iteração atual e vai para a próxima
print("\n--- Exemplo Continue (Pulando o 3) ---")
for numero in numeros:
    if numero == 3:
        continue
    print(numero)

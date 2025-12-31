"""
Exercício 3 - Funções com Coleções (Tuplas)
Objetivo: Receber uma tupla e retornar a soma de seus elementos.
"""

breakpoint()
def somar_tupla(numeros: tuple) -> float:
    # Utilizando sum() tornamos a função flexível para qualquer tamanho de tupla
    return sum(numeros)


resultado = somar_tupla((5, 6, 10))
print(f"Soma da tupla: {resultado}")

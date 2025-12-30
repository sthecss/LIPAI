"""
Exercício 1 - Funções: Retorno Void (Print)
Objetivo: Receber parâmetros e imprimir diretamente (sem retorno).
"""


def imprimir_soma(n1: float, n2: float, n3: float) -> None:
    """Imprime a soma de três números."""
    print(f"A soma é: {n1 + n2 + n3}")


# Chamada
imprimir_soma(3, 4, 5)

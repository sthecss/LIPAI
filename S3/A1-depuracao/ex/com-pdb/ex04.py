"""
Exercício 4 - Funções com Argumentos Variáveis (*args)
Objetivo: Receber N argumentos e retornar a soma.
"""


def somar_args(*args):
    # args é tratado internamente como uma tupla
    return sum(args)


breakpoint()
resultado = somar_args(5, 6, 7, 8)
print(f"Soma dos args: {resultado}")

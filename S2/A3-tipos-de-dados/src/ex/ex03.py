""" 
Exercício 3 - Tipos de Dados: Dicionários (Map)

Objetivo:
- Receber número do mês.
- Retornar nome usando Dicionário (chave: valor).
"""

meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

try:
    numero_do_mes = int(input("Digite o número do mês desejado: "))

    # O método .get() é mais seguro que colchetes [], pois não trava se a chave não existir.
    # Sintaxe: dicionario.get(chave, valor_padrao_se_falhar)

    nome_mes = meses.get(numero_do_mes, "Mês inválido")

    print(f"Resultado: {nome_mes}")

except ValueError:
    print("Erro: Entrada deve ser um número inteiro.")

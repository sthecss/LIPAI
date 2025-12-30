""" 
Exercício 2 - Tipos de Dados: Tuplas (Lookup)

Objetivo:
- Receber número do mês (1-12).
- Retornar nome do mês usando Tupla.
"""

# Tuplas são ideais para listas estáticas (que não mudam), como os meses.
nomes_dos_meses = (
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
)

try:
    numero_do_mes = int(input("Digite o número do mês desejado (1-12): "))

    # Validamos se está no intervalo correto
    if 1 <= numero_do_mes <= 12:
        # Ajuste de índice: O mês 1 está no índice 0 da tupla
        mes_selecionado = nomes_dos_meses[numero_do_mes - 1]
        print(f"Mês escolhido: {mes_selecionado}")
    else:
        print("Erro: Mês inválido. Digite um número entre 1 e 12.")

except ValueError:
    print("Erro: Por favor, digite apenas números inteiros.")

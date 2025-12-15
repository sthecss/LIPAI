"""
Exercício 6 - Dimensionamento de Aquário
Objetivo: Calcular volume, potência de termostato e filtragem.
"""


def calcular_volume(aquario: dict) -> float:
    """Retorna volume em Litros. Fórmula: (c * a * l) / 1000"""
    return (aquario["comprimento"] * aquario["altura"] * aquario["largura"]) / 1000


def calcular_potencia_termostato(aquario: dict) -> float:
    """Retorna potência em Watts."""
    vol = calcular_volume(aquario)
    delta_temp = aquario["temp_desejada"] - aquario["temp_ambiente"]
    return vol * 0.05 * delta_temp


def calcular_filtragem(aquario: dict) -> tuple:
    """Retorna uma tupla com (minima, maxima) de litros por hora."""
    volume = calcular_volume(aquario)
    return (volume * 2, volume * 3)


# --- Entrada de Dados ---
print("=== Configurador de Aquário ===")
dados_aquario = {}

try:
    dados_aquario["comprimento"] = float(input("Comprimento (cm): "))
    dados_aquario["altura"] = float(input("Altura (cm): "))
    dados_aquario["largura"] = float(input("Largura (cm): "))
    dados_aquario["temp_desejada"] = float(input("Temp. Desejada (°C): "))
    dados_aquario["temp_ambiente"] = float(input("Temp. Ambiente (°C): "))

    # --- Processamento ---
    vol = calcular_volume(dados_aquario)
    pot = calcular_potencia_termostato(dados_aquario)
    filtro_min, filtro_max = calcular_filtragem(dados_aquario)

    # --- Relatório Final ---
    print("\n" + "="*40)
    print(f"{'RELATÓRIO TÉCNICO':^40}")
    print("="*40)
    print(f"Volume Total:          {vol:.2f} L")
    print(f"Termostato Necessário: {pot:.2f} W")
    print(f"Filtragem Recomendada: {filtro_min:.0f} a {filtro_max:.0f} L/h")
    print("="*40)

except ValueError:
    print("\nErro: Por favor, insira apenas números válidos.")

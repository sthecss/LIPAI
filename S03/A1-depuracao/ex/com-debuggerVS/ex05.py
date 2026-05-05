"""
Exercício 5 - Calculadora de IMC (Diretrizes OMS)
"""


def calcular_imc(individuo: dict) -> float:
    """Calcula o IMC baseado em peso e altura."""
    return individuo["peso"] / (individuo["altura"] ** 2)


def obter_classificacao(imc: float) -> str:
    """Retorna a classificação da OMS baseada no IMC."""
    if imc >= 40:
        return "Obesidade de Classe 3"
    elif imc >= 35:
        return "Obesidade de Classe 2"
    elif imc >= 30:
        return "Obesidade de Classe 1"
    elif imc >= 25:
        return "Excesso de peso"
    elif imc >= 18.5:
        return "Peso Normal"
    else:
        return "Baixo peso"


def obter_situacao(imc: float) -> str:
    """Define a ação recomendada baseada no IMC."""
    if imc < 18.5:
        return "Ganhar Peso"
    elif 18.5 <= imc <= 25:
        return "Manter (Normal)"
    else:
        return "Perder Peso"


# --- Execução ---
paciente = {
    'altura': 1.79,
    'peso': 78.5
}

imc_calculado = calcular_imc(paciente)
classificacao = obter_classificacao(imc_calculado)
situacao = obter_situacao(imc_calculado)

print(f"IMC: {imc_calculado:.2f}")
print(f"Classificação: {classificacao}")
print(f"Recomendação: {situacao}")

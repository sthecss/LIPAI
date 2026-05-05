""" Aula 01 - Introdução a Funções """

# Definição: Bloco de código que realiza tarefa específica.
# Vantagens: Modularização (dividir problemas) e Reutilização (evitar repetição).

# --- 1. Funções Built-in (Biblioteca Padrão) ---
# Exemplos: print(), len(), type(), input()

print("Olá", 123, True)

nomes = ['João', 'Maria']
tamanho_lista = len(nomes)
print(f"Lista: {nomes} | Tamanho: {tamanho_lista}")


# --- 2. Funções Definidas pelo Usuário (UDF) ---

# Caso A: Função sem parâmetros e sem retorno (Procedimento)
def saudacoes():
    print("Olá! (Função simples)")


saudacoes()
saudacoes()


# Caso B: Função com parâmetros (Argumentos)
def saudacoes_personalizada(nome):
    print(f"Olá, {nome}")


# Chamando com argumentos
saudacoes_personalizada('Maria')
saudacoes_personalizada('Pedro')

nome_usuario = 'Carlos'
saudacoes_personalizada(nome_usuario)


# Caso C: Função sem retorno explícito (imprime direto)
# Problema: O dado morre dentro da função.
def calcular_media_imprimir(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    print(f"Média calculada (print): {media:.2f}")


calcular_media_imprimir(10.0, 3.0, 6.0)


# Caso D: Função com RETORNO (Return)
# Vantagem: O dado volta para o programa principal para ser usado depois.
def calcular_media_retornar(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media


# Capturando o retorno em uma variável
media_final = calcular_media_retornar(10.0, 8.4, 3.2)
print(f"Valor retornado: {media_final:.2f}")

# Exemplo de uso do retorno:
# if media_final >= 6: ...
# salvar_banco(media_final)
# enviar_email(media_final)

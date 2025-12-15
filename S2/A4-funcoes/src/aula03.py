""" Aula 03 - Leitura do Artigo e Prática (*args e **kwargs) """

def exemplo_args(*args):
    """
    *args: Permite passar um número variável de argumentos posicionais.
    Internamente, o Python os converte em uma TUPLA.
    """
    print(f"\n--- Testando *args ---")
    print(f"Tipo de args: {type(args)}")
    print(f"Conteúdo de args: {args}")

    # Exemplo prático: Somar todos os números passados
    soma = sum(args)
    print(f"Soma dos valores passados: {soma}")


def exemplo_kwargs(**kwargs):
    """
    **kwargs: Permite passar um número variável de argumentos nomeados (keyword arguments).
    Internamente, o Python os converte em um DICIONÁRIO.
    """
    print(f"\n--- Testando **kwargs ---")
    print(f"Tipo de kwargs: {type(kwargs)}")
    print(f"Conteúdo de kwargs: {kwargs}")

    # Exemplo prático: Iterar sobre as chaves e valores
    for chave, valor in kwargs.items():
        print(f"Campo: {chave} -> Valor: {valor}")


def exemplo_misturado(obrigatorio, *args, **kwargs):
    """
    A ordem dos parâmetros SEMPRE deve ser:
    1. Argumentos posicionais (obrigatórios)
    2. *args
    3. **kwargs
    """
    print(f"\n--- Testando Mistura (Args + Kwargs) ---")
    print(f"Argumento obrigatório: {obrigatorio}")
    print(f"Args (Tupla): {args}")
    print(f"Kwargs (Dicionário): {kwargs}")


if __name__ == "__main__":
    # 1. Testando *args com números inteiros
    # Imagine que não sabemos quantos números vamos somar
    exemplo_args(10, 20, 30, 5)

    # 2. Testando **kwargs com dados de usuário
    # Útil para configurações ou passar dados para construção de objetos/queries
    exemplo_kwargs(nome="João", idade=25, cidade="Uberlândia", status="Ativo")

    # 3. Testando a ordem correta e mistura de tipos
    exemplo_misturado(
        "Título do Relatório",  # Argumento posicional obrigatório
        1, 2, 3,               # Vão para *args
        autor="Maria",         # Vão para **kwargs
        data="14/12/2025"
    )

    # 4. Bônus: Desempacotamento (Unpacking)
    # Usando * e ** para passar listas e dicionários existentes para as funções
    print("\n--- Bônus: Desempacotamento ---")
    lista_numeros = [100, 200, 300]
    # O * explode a lista em argumentos individuais
    exemplo_args(*lista_numeros)

    dict_config = {"cor": "azul", "resolucao": "1080p"}
    # O ** explode o dicionário em argumentos nomeados
    exemplo_kwargs(**dict_config)

"""
Exercício 2 - Arquivos:  Carregar dados de projetos

"""


with open("S3/A2-arquivos/ex/txt/dados_projetos.txt", "r", encoding="utf-8") as dados_projetos:
    def carregar_dados_projetos(dados_projetos):
        """Retorna uma tupla de dicionários com
        dados de projetos."""
        tupla_dicionario = ()
        for dado in dados_projetos:
            dado_tratado = dado.strip().split(sep=',')
            codigo, titulo, responsavel = dado_tratado
            info_projeto = {
                'codigo': int(codigo),
                'titulo': titulo,
                'responsavel': responsavel
            }
            tupla_dicionario += (info_projeto,)
        return tupla_dicionario

    tupla_dados_projetos = carregar_dados_projetos(dados_projetos)
    for projeto in tupla_dados_projetos:
        print('{')
        for key, value in projeto.items():
            print(f'    {key}: {value}')
        print('}')

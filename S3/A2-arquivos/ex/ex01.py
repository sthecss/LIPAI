"""
Exercício 1 - Arquivos:  Carregar dados de alunos

"""


with open("S3/A2-arquivos/ex/txt/dados_alunos.txt", "r", encoding="utf-8") as dados_alunos:

    def carregar_dados_alunos(dados_alunos):
        """Retorna uma tupla de dicionários
            com dados de alunos."""
        tupla_dicionario = ()
        for dado in dados_alunos:
            dado_tratado = dado.strip().split(sep=',')
            prontuario, nome, email = dado_tratado
            info_aluno = {
                'prontuario': prontuario,
                'nome': nome,
                'email': email
            }
            tupla_dicionario += (info_aluno,)
        return tupla_dicionario

    tupla_dados_alunos = carregar_dados_alunos(dados_alunos)
    for aluno in tupla_dados_alunos:
        print('{')
        for key, value in aluno.items():
            print(f'    {key}: {value}')
        print('}')

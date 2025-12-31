"""
Exercício 2 - Arquivos:  Convertendo uma linha em dicionário genérico

"""


def linha_para_dict(linha_arquivo, lista_chaves):
    valores = linha_arquivo.strip().split(",")
    chaves = lista_chaves.strip().split(",")

    dicionario = {}
    for i in range(len(chaves)):
        dicionario[chaves[i]] = valores[i]

    return dicionario


def carregar_dados_arquivos(arquivo):
    linhas = []

    for linha in arquivo:
        linha = linha.strip()
        if linha:
            linhas.append(linha)

    return linhas


with open("S3/A2-arquivos/ex/txt/dados_dic-gen.txt", "r", encoding="utf-8") as dados_arquivos:
    linhas = carregar_dados_arquivos(dados_arquivos)

    for i in range(0, len(linhas), 2):
        valores = linhas[i]
        chaves = linhas[i + 1]

        dicionario = linha_para_dict(valores, chaves)

        print("{")
        for chave, valor in dicionario.items():
            print(f"    '{chave}': '{valor}',")
        print("}")
        print()

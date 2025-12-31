# """ Aula 01 -  Curso de Python para iniciantes 
#             12 – Manipulando Arquivos

# https://www.youtube.com/watch?v =G-kUBX0U8IQ

# """

# open("caminho",¨modo")

# # Modos podem ser:

# # r     = Leitura
# # a     = Append (incrementar)
# # w     = Escrita
# # x     = Criar Arquivo
# # r+    = Leitura + Escrita

# # Dica: Sempre que for lidar com arquivos, instancie o open e o close

# # Analide de leitura:

# arquivoR = open("S3/A2-arquivos/src/test01.py", "r")
# podeSerLido = arquivoR.readable()  # para saber se pode ser lido ou não
# print("Arquivo em modo R  : ", podeSerLido)
# arquivoR.close()

# arquivoA = open("S3/A2-arquivos/src/test01.py", "a")
# podeSerLido = arquivoA.readable()  # para saber se pode ser lido ou não
# print("Arquivo em modo A  : ", podeSerLido)
# arquivoA.close()

# arquivoW = open("S3/A2-arquivos/src/test01.py", "w")
# podeSerLido = arquivoW.readable()  # para saber se pode ser lido ou não
# print("Arquivo em modo W  : ", podeSerLido)
# arquivoW.close()

# arquivoRPlus = open("S3/A2-arquivos/src/test01.py", "r+")
# podeSerLido = arquivoRPlus.readable()  # para saber se pode ser lido ou não
# print("Arquivo em modo R+ : ", podeSerLido)
# arquivoRPlus.close()

# # -----------------------------------------------

# arquivo = open("S3/A2-arquivos/src/test01.txt", "r")

# print(arquivo.readable())
# print(arquivo.read())


# # ========================= Ler linha a linha, iterando:
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())


# # ========================= Colocar numa lista: 
# lista = arquivo.readlines()

# print(lista)        # imprimir toda a lista

# print(lista[3])     # num indice especifico

# # -----------------------------------------------
# # Inserindo textos num arquivo:
# arquivo = open("S3/A2-arquivos/src/test01.txt", "a")

# arquivo.write("C\n")
# arquivo.write("C++\n")
# arquivo.write("Terraform\n")

# arquivo.close()

# # -----------------------------------------------
# # Subscrevendo texto num arquivo:
# arquivo = open("S3/A2-arquivos/src/test01.txt", "w")

# arquivo.write("C\n")
# arquivo.write("C++\n")
# arquivo.write("Terraform\n")

# arquivo.close()

# # -----------------------------------------------

# # Diferenca entra "a" e "w":
# # > a : vai acrescentando, mantendo o anterior
# # > w : escreve, subescrevendo o antigo

# # -----------------------------------------------
# # Criando com modo w:

# arquivo = open("S3/A2-arquivos/src/test02.txt", "w")

# arquivo.write("C\n")
# arquivo.write("C++\n")
# arquivo.write("Terraform\n")

# arquivo.close()

# # -----------------------------------------------
# # Criando com modo x:

# # Também podemos usar o mod "x" para criar arquivos

# # arquivo = open("S3/A2-arquivos/src/aula01/test03.txt", "x")

# # arquivo.write("Python\n")

# # arquivo.close()

# # -----------------------------------------------

# """
# Se o arquivo não existir, ambos criam arquivos sem problema

# A diferença está no caso dele existie.

# Mooo "w" : Subscreve o anterior
# Modo "x" : Gera um erro (FileExistsError) e não sobrescreve. 

# É de bom usar o "w" quando a subrescrita é intencional, já se queremoss unicidade de arquivo o "x" é melhor.
# """

# # -----------------------------------------------

# # E para remover:

# import os

# # Arquivos:
# arquivo = open("S3/A2-arquivos/src/aula01/arquivoParaExcluir.txt", "x")
# arquivo.write("Python\n")
# arquivo.close()

# breakpoint()

# if os.path.exists("S3/A2-arquivos/src/aula01/arquivoParaExcluir.txt"):
#     os.remove("S3/A2-arquivos/src/aula01/arquivoParaExcluir.txt")
#     print("Removido")
# else:
#     print("Arquivo não existe")

# # Pasta:

# # Obs: comando os.rmdir só exclui pastas vazias
# os.makedirs("S3/A2-arquivos/src/aula01/pastaExcluir")

# breakpoint() # controar vizualização

# os.rmdir("S3/A2-arquivos/src/aula01/pastaExcluir")

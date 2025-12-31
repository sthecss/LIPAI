# """ Aula 02 -  MANIPULANDO ARQUIVOS COM PYTHON

# https://www.youtube.com/watch?v=5uJNQiBFxUc

# """

# # -----------------------------------------------

# arq = open('S3/A2-arquivos/src/aula02/arquivo.txt', 'w')

# string = 'Olá Teté, tudo bem?\n'           # uso de: arq.write()
# lista = ['Olá', 'Teté', 'Tudo', 'Bem']   # uso de: arq.writelines()

# # Para string:
# # arq.write(string)   # aparece toda a string
# # arq.write('Opa!')   # passa a ser só essa astring, pq o modo é 'w'
# # arq.write(lista)    # erro, pq iteracação é writelines

# # Para iterados:
# # for nome in lista:
# #     arq.write(nome + '\n')

# # Ou se for uma lista previamente ajustada:
# # lista = ['Olá\n', 'Teté\n', 'Tudo\n', 'Bem\n']
# # arq.write(lista)


# print(arq)

# arq.close()

# # -----------------------------------------------
# """
# Forma mais elegante de lidar com arquivos: Exe Manager
# desse modo, ao sair do escopo o with, o arquivo é automaticamente4 fechado
# """

# # MODO W : Criacao e subscrita:
# with open('S3/A2-arquivos/src/aula02/arquivo.txt','w') as arq:
#     arq.write('teste\n')


# # MODO A: Iterante/adicionado:
# with open('S3/A2-arquivos/src/aula02/arquivo.txt', 'a') as arq:
#     arq.write('append\n')


# # MODO R: Iterante/adicionado:
# with open('S3/A2-arquivos/src/aula02/arquivo.txt', 'r') as arq:
#     x = arq.read()
#     print('Printando read()\t:', x, '\n')
#     print('Printando type(read())\t:', type(x), '\n')

#     x = arq.readlines()
#     print('Printando readlines(): ', x, '\n')
#     print('Printando type(readlines()): ', type(x), '\n')

# # MODO RB: Iterante/adicionado:
# with open('S3/A2-arquivos/src/aula02/arquivo.txt', 'rb') as arq:
#     x = arq.read()
#     print('Printando read()\t:', x, '\n')
#     print('Printando type(read())\t:', type(x), '\n')

#     interessante quando é pertinente em envios via software

#     E se quisermos decodificar basta:
#     x = arq.read()
#     print('Printando read()\t:', x.decode(), '\n')
#     print('Printando type(read())\t:', type(x.decode()), '\n')


""" Aula 07 - LIPAI - Entrada e Saída (I/O) """

# --- Saída Padrão (sys.stdout) ---
print("Olá, Mundo!", "Maria")

# Parâmetros sep e end:
print("Olá Mundo!", "Maria", 1, True, sep=' -> ', end=" || Final\n")

# --- Manipulação de Arquivos (Escrita) ---
# 'w' = write (sobrescreve o arquivo se existir)
arquivo = open('nomes.txt', 'w', encoding='utf-8')
print("Ana", "Bruno", "Carlos", file=arquivo, sep=', ')
arquivo.close()  # Sempre fechar o recurso!

# --- Entrada Padrão (sys.stdin) ---
nome = input("Digite seu nome: ")
print(nome.upper())

# O input sempre retorna string, necessário converter se for número:
idade = int(input("Digite sua idade: "))
print(type(nome), type(idade))

if idade >= 18:
    print(f"{nome}, você é maior de idade.")
else:
    print(f"{nome}, você é menor de idade.")

# --- Manipulação de Arquivos (Leitura) ---
# Nota: É necessário que o arquivo 'notas.txt' exista e tenha dados separados por ';'
# Exemplo de conteúdo no arquivo: 8.5;9.0;7.5

try:
    arquivo_notas = open('notas.txt', 'r', encoding='utf-8')
    conteudo = arquivo_notas.read()

    # Processamento dos dados
    notas_str = conteudo.split(sep=';')  # Quebra a string onde tem ';'
    print(f"Dados crus: {notas_str}")

    # List Comprehension para converter tudo para float
    notas = [float(nota) for nota in notas_str]
    print(f"Notas convertidas: {notas}")

    # Usando sum() fica mais dinâmico que somar índices fixos
    media = sum(notas) / len(notas)
    print(f"Média das notas: {media:.2f}")

    arquivo_notas.close()
except FileNotFoundError:
    print("Erro: O arquivo 'notas.txt' não foi encontrado.")

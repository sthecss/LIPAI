# Reflexão sobre Manipulação de Arquivos


Pergunta: Qual a vantagem de transformar cada linha do arquivo em dicionários em vez de trabalhar apenas com strings?

Resposta: Trabalhar apenas com strings acaba sendo pouco prático quando o arquivo representa dados estruturados. Ao transformar cada linha em um dicionário, os campos passam a ter significado explícito, o que facilita o acesso e a manipulação das informações. Em vez de depender da posição dos dados na string, como é comum em C com vetores ou em Java com arrays, o uso de chaves deixa o código mais legível e menos propenso a erros, além de se integrar melhor com outras estruturas do Python.


---

Pergunta: Em que situações pode ser útil retornar uma tupla de registros (como nos exercícios ex01 e ex02) em vez de apenas uma lista de linhas?

Resposta: A tupla é útil quando os dados lidos do arquivo representam um conjunto que não deve ser modificado ao longo do programa. Diferente de listas, as tuplas são imutáveis, o que ajuda a evitar alterações acidentais após a leitura. Além disso, retornar uma tupla de dicionários já processados permite que o restante do código trabalhe em um nível mais alto de abstração, semelhante ao uso de objetos ou structs em Java e C, em vez de lidar diretamente com linhas de texto.


---

Pergunta: O que você achou mais desafiador: ler o arquivo ou transformar as linhas em estruturas de dados (dicionários)?

Resposta: A leitura do arquivo em si não foi a parte mais difícil, pois o uso de with open torna esse processo bastante direto em Python. O maior desafio foi transformar corretamente as linhas em dicionários, garantindo que os campos fossem separados de forma consistente e associados às chaves corretas. Esse passo exige mais atenção à formatação dos dados e à lógica do programa, especialmente para evitar erros como índices fora do intervalo ou inconsistências entre valores e chaves.

\vspace{0.5cm}
\textbf{Pergunta:}
\textbf{Resposta:}
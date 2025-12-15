# Reflexão sobre Funções e Modularização



## 1. Flexibilidade: Imprimir (Void) vs Retornar (Return)

Pergunta: Qual função é mais flexível em relação ao uso: a do ex01 (que imprime) ou a do ex02 (que retorna o valor)? Por quê?

Resposta: A função que retorna valor (ex02) ganha de lavada. O motivo principal é arquitetural: misturar cálculo com output viola o princípio da responsabilidade única. Quando eu uso `return`, ganho três superpoderes que o `print` mata:

    1.  Controle total: Posso pegar esse dado e salvar num banco, mandar pra uma API ou jogar num gráfico. O `print` só joga na tela e o dado se perde.
    2.  Testabilidade: Testar o retorno de uma função é trivial (`assert soma(2,2) == 4`). Testar um `print` exige capturar o stdout, o que é uma gambiarra desnecessária.
    3.  Composição: Posso usar o resultado dessa função como entrada de outra.



---



## 2. Flexibilidade: Parâmetros Fixos vs Variáveis

Pergunta: Qual abordagem é mais flexível: a do ex02 (3 parâmetros fixos) ou a do ex03/ex04 (que permitem número variável de argumentos)?

Resposta: Sem dúvida a abordagem dinâmica (ex03/ex04).

No mundo real, requisitos são voláteis. Hoje o cliente quer a média de 3 notas, amanhã quer de 5, depois quer importar uma planilha inteira. Se eu travar a assinatura da função em `(n1, n2, n3)`, eu crio um código rígido que quebra na primeira mudança de escopo. Usar listas ou `args` torna a função agnóstica à quantidade de dados: ela processa o que vier, seja 2 itens ou 2 milhões, sem que eu precise refatorar a lógica interna.



---



## 3. Tuplas vs args

Pergunta: As funções do ex03 e ex04 permitem enviar um número variável de parâmetros (tupla ou args). Em que situações você prefere cada forma? Justifique.

Resposta: Aqui é uma questão de Origem do Dado vs. Experiência do Desenvolvedor (DX).

Eu uso Tuplas/Listas (Coleção Única) quando o dado já existe estruturado no meu sistema.
    > Cenário: O dado veio de uma query SQL ou de um arquivo CSV. Não faz sentido eu desempacotar uma lista de 100 itens só para passar para a função. Passo a lista inteira e pronto. É mais performático.

Eu uso `args` (Espelhamento) quando estou criando bibliotecas ou utilitários.
    > Cenário: Quero oferecer uma sintaxe limpa para quem vai usar meu código. É muito mais intuitivo escrever `somar(10, 20, 30)` do que obrigar o desenvolvedor a criar uma lista auxiliar `somar([10, 20, 30])` só para satisfazer a função. O `args` deixa a chamada mais elegante e "Pythonica".
# Introdução a Aprendizagem de Máquina

## Objetivos

Este relatório documenta a realização das tarefas que cobrem os fundamentos de Machine Learning, com base no Capítulo 1 do livro [Fundamentals of Machine Learning](https://www.taylorfrancis.com/chapters/oa-mono/10.1201/9781003486817-1/fundamentals-machine-learning-ally-nyamawe-mohamedi-mjahidi-noe-nnko-salim-diwani-godbless-minja-kulwa-malyango?context=ubx&refId=6096b041-c49e-4b8f-8629-6481a2cc483c).

Os principais pontos abordados foram:

- Compreensão do conceito de Machine Learning e sua relação com IA e Data Science;
- Diferenciação entre os principais tipos de aprendizado (supervisionado, não supervisionado e por reforço);
- Estudo de terminologias como Generative AI e NLP;
- Identificação das habilidades técnicas e interpessoais necessárias para atuar na área;
- Reconhecimento de aplicações reais de ML em diferentes setores.

---

## Respostas dos Exercícios

### Questão 05 — Descreva: Generative AI e NLP

#### a) Generative AI

IA Generativa é um subcampo do Deep Learning que vai além da simples classificação ou análise de dados — seu foco é **criar conteúdo novo**: textos, imagens, músicas, cenários realistas. É o que está por trás de ferramentas como o ChatGPT e o Midjourney.

Três avanços foram centrais para que isso se tornasse possível:

- **Transformers**: revolucionaram o NLP ao permitir que modelos entendam contexto e relações entre palavras de forma muito mais sofisticada do que antes;
- **GANs (Redes Adversariais Generativas)**: duas redes neurais competem — uma tenta gerar dados falsos convincentes, a outra tenta detectar a fraude. Essa dinâmica força melhoria contínua na qualidade do que é gerado;
- **Modelos de Difusão**: aprendem a criar dados novos revertendo, passo a passo, um processo de adição de ruído. São especialmente eficazes para geração de imagens em alta resolução.

#### b) NLP — Processamento de Linguagem Natural

NLP é a área do ML que lida com linguagem humana — texto e fala. O objetivo é fazer com que máquinas consigam extrair significado de dados não estruturados como artigos, avaliações de produtos ou transcrições de áudio.

Algumas aplicações práticas:

- **Saúde**: análise de registros médicos e prontuários clínicos;
- **Educação**: correção automática de redações e tutores inteligentes;
- **Comunicação**: Google Translate, autocomplete de texto;
- **Negócios**: análise de sentimentos em redes sociais, chatbots de suporte;
- **Entretenimento**: recomendações de conteúdo e assistentes de voz.

---

### Questão 08 — Habilidades essenciais para profissionais de ML

As habilidades necessárias para trabalhar com Machine Learning estão no cruzamento entre engenharia de software, ciência de dados e comunicação. O livro as divide em técnicas e interpessoais.

#### Habilidades Técnicas

- **Engenharia de Software**: saber programar, entender algoritmos e estruturas de dados, e ter noção de arquitetura de sistemas;
- **Estatística e Matemática**: dominar probabilidade, álgebra linear, modelagem estatística e saber avaliar modelos preditivos de forma criteriosa.

#### Habilidades Interpessoais

São justamente as *soft skills* que separam profissionais eficazes dos ineficazes — não adianta saber o conteúdo técnico se a entrega do projeto falha por problemas de comunicação ou gestão:

- **Comunicação**: explicar resultados técnicos para diferentes públicos sem perder a precisão;
- **Resolução de problemas**: pensar analiticamente diante de desafios sem resposta imediata;
- **Gestão de tempo**: projetos de ML costumam envolver muitas iterações — saber priorizar é essencial;
- **Trabalho em equipe**: a área é intrinsecamente multidisciplinar — cientistas de dados, engenheiros, especialistas de domínio e gestores precisam trabalhar juntos;
- **Sede de aprendizado**: o campo muda rápido demais para quem não se mantém atualizado.

---

### Questão 09 — Cinco aplicações reais de Machine Learning

#### 1. Reconhecimento de Imagem

Modelos treinados com grandes volumes de imagens rotuladas conseguem identificar e classificar objetos visuais com precisão elevada.

- Classificação de imagens de raio-X como cancerosas ou não — suporte direto ao diagnóstico médico;
- Reconhecimento facial em redes sociais, como o sistema de *tagging* automático do Facebook.

#### 2. Diagnóstico Médico

Modelos que analisam dados fisiológicos, genéticos e ambientais para auxiliar médicos em diagnósticos mais precoces e precisos.

- *Ada Health*: plataforma que sugere hipóteses diagnósticas com base nos sintomas informados pelo paciente;
- *CareAI*: focado no monitoramento contínuo de pacientes internados.

#### 3. Automóveis Autônomos

Integração de múltiplos modelos de ML para percepção do ambiente, interpretação de sinais e tomada de decisão em tempo real.

- Tesla: usa redes neurais profundas para processar dados de câmeras e sensores e guiar o veículo;
- Waymo (Google): pioneira no desenvolvimento de frotas de veículos sem motorista.

#### 4. Sistemas de Recomendação

Modelos que aprendem preferências dos usuários a partir do histórico de interações para sugerir conteúdo personalizado.

- Netflix: recomenda filmes e séries com base no comportamento de visualização de cada usuário;
- Facebook: analisa interações na plataforma para personalizar o feed de notícias.

#### 5. Cibersegurança

Modelos que aprendem o comportamento normal de sistemas e redes para identificar desvios que possam indicar ataques ou fraudes.

- Detecção de intrusão: identifica acessos anômalos a redes corporativas em tempo real;
- Detecção de malware: classifica arquivos como maliciosos com base em padrões de comportamento aprendidos.
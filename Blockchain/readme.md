# Introdução

A tecnologia de *blockchain* está sendo cada vez mais aplicada aos negócios, não apenas na parte de transações mas também na logística para acompanhar os produtos ao longo da cadeia de suprimentos. Tendo isso em vista comecei a estudar e entender melhor como funciona essa tecnologia para buscar aplicá-la em projetos futuros.

Nesse repositório tem um funcionamento básico de uma *blockchain*, onde usei a linguagem *python* aplicada a alguns conhecimentos de Programação Orientada a Objeto (POO) e montei alguns *endpoints* com *fastAPI*.

# Conhecimentos

- Nesse projeto, pude aplicar POO (Programação Orientada a Objetos) na prática, o que me ajudou a fixar alguns conceitos.
- Reforcei meu conhecimento em criptografia utilizando o algoritmo SHA-256 da biblioteca *hashlib*.
- Conheci a *FastAPI* do Python e aprendi a trabalhar com ela.
- Pesquisei sobre estrutura de dados, pois a arquitetura *blockchain* usa bastante desse conceito.
- Também estudei sobre APIs e como lidar com elas usando o CURL.
- Testei diferentes maneiras de montar a *blockchain*, até chegar nesta versão final (funcionamento um pouco diferente das que eu vi por aí).
- Vi diversos exemplos de uso da *blockchain* para solucionar problemas de negócio, como, por exemplo, usá-la como ferramenta logística.


# Indice

1. Entendendo a estrutura da Blockchain
2. Estrutura dos blocos
3. Mineração de um novo bloco


# Estrutura da Blockchain

A blockchain é um conjunto de blocos que guardam informações dentro deles. A informação armazenada em um bloco selado não pode ser alterada, o que garante a integridade de tudo que está armazenado neles.

Para garantir essa integridade, os blocos são ligados uns aos outros utilizando um algoritmo chamado proof of work (prova de trabalho), que aplica criptografia para gerar uma chave do bloco chamada de *Hash*. Abaixo segue uma ilustração da estrutura de uma blockchain.

![Blockchain](https://github.com/MateusNaza/Estudos-Engenharia-de-Dados/blob/main/Blockchain/assets/Blockchain.png)

> Bloco Gênesis é o nome dado ao primeiro bloco, ele não trás nenhuma informação na parte do seu corpo e é usado somente para dar início a cadeia de blocos (*Blockchain*).
> 


# Estrutura dos Blocos

Dentro de cada bloco temos 3 estruturas principais:

![Corpo do bloco.png](https://github.com/MateusNaza/Estudos-Engenharia-de-Dados/blob/main/Blockchain/assets/Corpo_do_bloco.png)


# Mineração de um novo bloco

Após o bloco Gênesis, todos os blocos são criados através da mineração. Abaixo detalho cada uma das etapas:

1. O Bloco antigo já selado deverá ser transformado em um *Hash*.
2. A função *Hash()* trabalha dentro de uma outra função maior chamada *proof_of_work()*. Dentro da *proof_of_work* o bloco antigo é concatenado com o *Nonce* (Número que começa em 0 e vai aumentando até gerar o *Hash* Válido). A cada novo *nonce* a função *Hash* é chamada e é verificado se o *Hash* gerado corresponde a regra estabelecida (nesse caso deve começar com ‘7777’), esse processo se repete até que o *Hash* correto é encontrado.
3. Quando a função encontra o *Hash* válido ela retorna o *Hash* e o *Nonce.*
4. É criado e selado um novo bloco com todas as transações que estavam esperando o novo bloco, na parte de ‘Prova de Trabalho’ desse novo bloco é colocado o resultado da função anterior (*Hash* e *Nonce*).

![Processo de Mineraçãoi.png](https://github.com/MateusNaza/Estudos-Engenharia-de-Dados/blob/main/Blockchain/assets/Processo_de_Mineraoi.png)

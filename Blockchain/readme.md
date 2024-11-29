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

1. [Entendendo a estrutura da Blockchain](https://github.com/MateusNaza/Estudos-Engenharia-de-Dados/edit/main/Blockchain/readme.md#estrutura-da-blockchain)
2. [Estrutura dos blocos](https://github.com/MateusNaza/Estudos-Engenharia-de-Dados/edit/main/Blockchain/readme.md#estrutura-dos-blocos)
3. [Mineração de um novo bloco](https://github.com/MateusNaza/Estudos-Engenharia-de-Dados/edit/main/Blockchain/readme.md#minera%C3%A7%C3%A3o-de-um-novo-bloco)
4. [Lista de Transações](https://github.com/MateusNaza/Estudos-Engenharia-de-Dados/edit/main/Blockchain/readme.md#lista-de-transa%C3%A7%C3%B5es)
5. [Funcionamento na prática com fastAPI](https://github.com/MateusNaza/Estudos-Engenharia-de-Dados/edit/main/Blockchain/readme.md#blockchain-em-funcionamento-com-fastapi)
    1. [/mine_block/](https://github.com/MateusNaza/Estudos-Engenharia-de-Dados/edit/main/Blockchain/readme.md#mine-block)
    2. [/new_transactions/](https://github.com/MateusNaza/Estudos-Engenharia-de-Dados/edit/main/Blockchain/readme.md#new-transactions)
    3. [/chain/](https://github.com/MateusNaza/Estudos-Engenharia-de-Dados/edit/main/Blockchain/readme.md#chain)
    4. [/current_transactions/](https://github.com/MateusNaza/Estudos-Engenharia-de-Dados/edit/main/Blockchain/readme.md#current-transactions)


# Estrutura da Blockchain

A blockchain é um conjunto de blocos que guardam informações dentro deles. A informação armazenada em um bloco selado não pode ser alterada, o que garante a integridade de tudo que está armazenado neles.

Para garantir essa integridade, os blocos são ligados uns aos outros utilizando um algoritmo chamado proof of work (prova de trabalho), que aplica criptografia para gerar uma chave do bloco chamada de *Hash*. Abaixo segue uma ilustração da estrutura de uma blockchain.

![Blockchain.png](https://github.com/MateusNaza/Estudos-Engenharia-de-Dados/blob/main/Blockchain/assets/Blockchain.png)

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


# Lista de transações

Todas as transações realizadas vão primeiro para uma lista chamada ‘*current_transactions*’ onde ficam até que um bloco seja minerado, nesse momento elas passam para o bloco novo e a ‘*current_transactions*’ é zerada para armazenar novas transações.

1. Cada transação carrega três informações.
2. A nova transação criada vai para a lista de transações atuais ‘*current_transactions*’
3. Ao ser minerado um bloco, todas as transações da ‘*current_transactions*’ passa para dentro desse novo bloco e a lista é zerada para armazenar novas transações.

![image.png](https://github.com/MateusNaza/Estudos-Engenharia-de-Dados/blob/main/Blockchain/assets/image.png)


# Blockchain em funcionamento com fastAPI

No código temos um arquivo chamado [main.py](http://main.py) que é onde está toda a parte de *endpoints* da API. Para iniciar o ambiente digitei o seguinte código no terminal:

```bash
uvicorn main:app --reload
```

E precisei acrescentar ao final da URL /docs. Com isso, abre essa janela com todos os *endpoints*.

![image.png](https://github.com/MateusNaza/Estudos-Engenharia-de-Dados/blob/main/Blockchain/assets/image%201.png)


# Mine Block

Esse endpoint faz o processo de minerar novos blocos, quando ele termina de minerar o novo bloco ele mostra o conteúdo do bloco minerado.

![image.png](https://github.com/MateusNaza/Estudos-Engenharia-de-Dados/blob/main/Blockchain/assets/image%202.png)

# New Transactions

Aqui é onde criamos as transações, deve-se preencher todos os campos e executar o *endpoit*. Esse *endpoint* retorna o bloco onde a transação futuramente ficará armazenada.

![image.png](https://github.com/MateusNaza/Estudos-Engenharia-de-Dados/blob/main/Blockchain/assets/image%203.png)


# Chain

Esse *endpoint* serve para mostrar a *blockchain* completa, como todos os seus blocos e conteúdos dos blocos. A Imagem abaixo contêm os 2 primeiros blocos.

![image.png](https://github.com/MateusNaza/Estudos-Engenharia-de-Dados/blob/main/Blockchain/assets/image%204.png)


# Current Transactions

Esse *endpoint* retorna a lista das transações que estão aguardando para serem armazenadas quando um novo bloco for minerado.

![image.png](https://github.com/MateusNaza/Estudos-Engenharia-de-Dados/blob/main/Blockchain/assets/image%205.png)

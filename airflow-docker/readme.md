# Airflow Step by Step

# Instalação

```bash
# Install
curl -LfO 'https://airflow.apache.org/docs/\
apache-airflow/stable/docker-compose.yaml'

# Permissions
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

# Create directors
mkdir ./dags ./plugins ./logs

# Init
docker-compose up airflow-init

# run
docker-compose up
```

> Após os passos acima, se abrir um terminal novo e fazer o ‘docker ps’ é possível ver todos os containers rodando.
>
> 


<img src="https://github.com/MateusNaza/Estudos-Engenharia-de-Dados/blob/main/airflow-docker/assets/image.png" alt="Texto Alternativo" width="900">


# Primeira DAG

<img src="https://github.com/MateusNaza/Estudos-Engenharia-de-Dados/blob/main/airflow-docker/assets/image%201.png" alt="Texto Alternativo" width="900">

> Essa acima é minha primeira DAG, ela inicia rodando em paralelo 3 funções python que retornam um número simbolizando a acurácia de um modelo de Machine Learning. Em seguida ela efetua uma outra função python que verifica qual dos três modelos obteve uma maior pontuação e por fim chama outras duas funções, dessa vez de bash, para informar se o modelo ficou dentro da acurácia desejada ou não.
>

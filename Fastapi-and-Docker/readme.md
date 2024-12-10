# Postgres & FastAPI


## Iniciando ambiente postgres

```bash
# Baixando a imagem Postgres
docker pull postgres:alpine

# Iniciando container Postgres
Docker run --name fastapi-postgres -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres:alpine

# Acessando container
docker exec -it fastapi-postgres bash

# Acessando o psql para entrar no Postgres
psql -U postgres
```


## Primeiros comandos dentro do Postgres

```sql
# Criando *Database*
create database fastapi_db;

# Criando Usuário
create user mateusnaza with encrypted password 'password';

# Permissionando usuário para acesso ao *Database*criado
grant all privileges on database fastapi_db to mateusnaza;

# Conectando ao *Database*
\c fastapi_db
```


## Comandos auxiliares que testei

```sql
# Listar Databases
\list

# Listar Usuários
\du

# Verificar o Database que estamos dentro atualmente
SELECT current_database();

# Jogando o database para o postgres que está rodando na porta 5432
psql -h localhost -p 5432 postgres

# Comando para verificar tabelas do banco de dados 
\dt
```


## Iniciando um novo ambiente

Abri um novo terminal e acessei a pasta que criei para esse projeto (Fastapi & Docker)

```bash
# Inicando ambiente venv
python3 -m venv venv

# Instalando dependências
pip install "fastapi[all]" SQLAlchemy psycopg2-binary sqlalchemy-utils
```


![Estrutura de arquivos.png](https://github.com/MateusNaza/Estudos-Engenharia-de-Dados/blob/main/Fastapi-and-Docker/assets/image.png)

> Estrutura de pastas
> 

## Rodando no ambiente venv

Após escrever meu código agora vamos rodar no ambiente venv.

```bash
# Primeiro iniciamos o python no ambiente
python

# Depois importamos o código que queremos rodar
import services

# Ai podemos chamar a função que está dentro do código
services._add_table
```


## Possíveis erros

Criei essa função para testar se a conexão deu certinho com o banco de dados, pois enfrentei um erro terrível e ela me ajudou a ver que o erro não estava na conexão.

![codigo_python.png](https://github.com/MateusNaza/Estudos-Engenharia-de-Dados/blob/main/Fastapi-and-Docker/assets/image%201.png)

O erro em questão foi uma questão de permissão, o usuário que estou usando tinha permissão para acessar o *Database* porém não tinha permissão no *schema public*, que é onde eu estava tentando criar uma tabela.

Para resolver tive que criar as permissões necessárias para o *schema.*

```sql
# Permissionando para o schema public
GRANT ALL PRIVILEGES ON SCHEMA public TO mateusnaza;

# Verificando se os privilégios foram aplicados
SELECT nspname, 
       pg_catalog.has_schema_privilege('mateusnaza', n.oid, 'USAGE') AS has_usage,
       pg_catalog.has_schema_privilege('mateusnaza', n.oid, 'CREATE') AS has_create
FROM pg_catalog.pg_namespace n
WHERE n.nspname = 'public';

```

> É recomendável manter o terminal aberto conectado ao container do postgres e abrir outro terminal para executar os códigos python
> 


## FastAPI & Endpoints

Os comandos de FastAPI estão em um arquivo chamado [main.py](http://main.py) e para acessá-los basta executar o seguinte comando no bash.

```bash
uvicorn main:app --reload
```

Temos os seguintes *endpoints*:

1. Criar um novo contato (POST)
2. Obter a lista completa de contatos (GET)
3. Obter um contato específico através de seu ID (GET)
4. Modificar/atualizar um contato através de seu ID (PUT)
5. Deletar um contato através de seu ID (DELETE)

![fastapi.png](https://github.com/MateusNaza/Estudos-Engenharia-de-Dados/blob/main/Fastapi-and-Docker/assets/image%202.png)

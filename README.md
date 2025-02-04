# Processamento_1_Bilhao_Linhas

## Overview

Esse projeto consiste em um desafio de processar 1 bilhão de linhas, inicialmente acompanhei uma video aula sobre o desafio porém fiz a minha versão, armazenando o arquivo em um Amazon S3 e acessando localmente.    
    
Minha versão utiliza as seguintes ferramentas:    
    
- Amazon S3: Para armazenar o arquivo (particionado e em formato .parquet)    
- DuckDB: Como processamento de dados, utilizando SQL para a consulta    
- Python: Como linguagem, criação de ambiente virtual e bibliotecas para conexão com AWS e manipulação de arquivos.      
    
## Criando o arquivo

Para criar o arquivo utilizei o script 'create_csv.py'. Ele acessa um bucket S3 com auxilio do script 'aws_utils.py', lê o arquivo de amostra que contêm dentro do bucket, cria um novo arquivo contendo os 1 Bilhão de linhas e armazena dentro do mesmo Bucket na camada 'output'.

## Processando os dados
    
Os dados são valores de temperaturas registrados em diversos locais ao redor do mundo. O objetivo é pegar a temperatura mínima e maxima e a média de temperatura de cada um dos locais.

O processamento é feito pela engine do DuckDB, e ocorre no script 'main.py'. Esse script acessa o Bucket contendo vários arquivos .parquet particionados, une todos esses arquivos em uma query SQL que trás o resultado da consulta.

import pandas as pd 
import sqlite3 as sql 
from datetime import datetime 

# Setando pandas para mostrar todas as colunas
pd.options.display.max_columns = None

# Leitura de dados
df = pd.read_json('../../data/bronze/data.jsonl', lines=True)

# Criação de colunas
df['_source'] = 'https://lista.mercadolivre.com.br/tenis-corrida-masculino#D[A:tenis%20corrida%20masculino]'
df['_datetime'] = datetime.now()

# Tratando nulos e tipos de dados
df['old_price_temp'] = df['old_price'].fillna(0).astype('float64')
df['old_cents'] = df['old_cents'].fillna(0).astype('float64')
df['new_price_temp'] = df['new_price'].fillna(0).astype('float64')
df['new_cents'] = df['new_cents'].fillna(0).astype('float64')

# Tratando coluna 'total_reviews'
df['total_reviews'] = df['total_reviews'].replace('[\(\)]', '', regex=True)
df['total_reviews'] = df['total_reviews'].fillna(0).astype('int64')

# Unindo colunas de preço com respectivos centavos
df['old_price'] = df['old_price_temp'] + df['old_cents'] / 100
df['new_price'] = df['new_price_temp'] + df['new_cents'] / 100

# Removendo colunas desnecessárias
df = df.drop(columns=['old_price_temp', 'new_price_temp', 'old_cents', 'new_cents'])

# Conexão com banco de dados
conn = sql.connect('../../data/silver/quotes.db')

# Salvando no banco de dados
df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)

# Encerrando conexão do banco de dados
conn.close()

print('\nDados transformados e armazenados com sucesso para a pasta "data/silver"\n')


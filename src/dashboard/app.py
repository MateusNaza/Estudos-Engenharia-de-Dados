import streamlit as st
import pandas as pd
import sqlite3 as sql

# Gera conexão de banco de dados
conn = sql.connect('../../data/silver/quotes.db')

# Lê o arquivo onde está a tabela do banco de dados
df = pd.read_sql_query('SELECT * FROM mercadolivre_items', conn)

# Encerra conexão com banco de dados
conn.close()


# --- Criação do Dash ---

st.title('Pesquisa de Mercado - Tênis Esportivo')

# --- Filtros ---
promotional_products = st.checkbox('Apenas produtos em promoção', value=False)

if promotional_products:
    df_filter = df[df['old_price'] > 0]
else:
    df_filter = df

col1, col2, col3 = st.columns(3)


# KPI 1 - Total de itens
total_itens = df_filter.shape[0]
col1.metric(label='Total de itens', value=total_itens)

# KPI 2 - Marcas analisadas
unique_brands = df_filter['brand'].nunique()
col2.metric(label='Total de Marcas', value=unique_brands)

# KPI 3 - Preço médio atual
current_price_avg = df_filter['new_price'].mean().round(2)
col3.metric(label='Preço médio atual (R$)', value=current_price_avg)

st.subheader('Marcas mais encontradas')

col1, col2 = st.columns([4,2])

# Marcas mais encontradas na pesquisa
top_brands = df_filter['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_brands)
col2.write(top_brands)

# Melhores custo benefícios (Preço X Avaliação)


selected_brand = st.selectbox('Selecione a Marca', df_filter['brand'].unique())
df_filter_selected = df_filter[df_filter['brand'] == selected_brand]
st.write(df_filter_selected)

st.write(df_filter)


import os
import random
import time
import pyarrow as pa
import pyarrow.parquet as pq
from io import BytesIO

import aws_utils as util

 
def construir_lista_estacoes_meteorologicas(bucket_name, s3_key_input):
    """
    Obtém os nomes das estações meteorológicas a partir de um arquivo e remove duplicatas.
    """
    df = util.process_csv_from_s3(bucket_name, s3_key_input)

    return df['City'].unique()


def converter_bytes(num):
    """
    Converte bytes para um formato legível (ex: KB, MB, GB).
    """
    for unidade in ['B', 'KB', 'MB', 'GB']:
        if num < 1024:
            return f"{num:.1f} {unidade}"
        num /= 1024


def formatar_tempo_decorrido(segundos):
    """
    Formata o tempo decorrido de forma simplificada.
    """
    minutos, segundos = divmod(segundos, 60)
    return f"{int(minutos)}m {int(segundos)}s" if minutos else f"{segundos:.2f}s"

def gerar_dados_teste(num_registros, bucket_name, s3_key):
    """
    Gera e salva um arquivo Parquet com medições sintéticas de temperatura diretamente no S3.
    """
    inicio_tempo = time.time()
    nomes_estacoes = construir_lista_estacoes_meteorologicas(bucket_name, s3_key_input)
    estacoes_10k_max = random.choices(nomes_estacoes, k=10_000)
    tamanho_lote = 10_000  # Processamento em lotes
    lote_dados = []

    print(f"Criando dados e enviando para o bucket '{bucket_name}'...")

    try:
        for _ in range(num_registros // tamanho_lote):
            lote = random.choices(estacoes_10k_max, k=tamanho_lote)
            lote_dados.extend([(estacao, round(random.uniform(-99.9, 99.9), 1)) for estacao in lote])

            # Salvar em lotes para evitar consumo excessivo de memória
            if len(lote_dados) >= 1_000_000:
                util.save_parquet(lote_dados, bucket_name, f"{s3_key}/medicoes_{num_registros}_{time.time()}.parquet")
                lote_dados = []  # Limpa a lista para o próximo lote

        # Salvar qualquer dado restante
        if lote_dados:
            util.save_parquet(lote_dados, bucket_name, f"{s3_key}/medicoes_{num_registros}.parquet")

        print(f"Dados enviados para o bucket '{bucket_name}' com a chave '{s3_key}/medicoes_{num_registros}.parquet'.")
        print(f"Tempo decorrido: {formatar_tempo_decorrido(time.time() - inicio_tempo)}")
    
    except Exception as e:
        print('Erro ao criar o arquivo Parquet:', e)

num_registros = 1_000_000_000
bucket_name = 'processando-1bilhao-linhas'
s3_key_input = 'sample/amostra_44k.csv'
s3_key = 'output'

gerar_dados_teste(num_registros, bucket_name, s3_key)

# if __name__ == "__main__":
#     num_registros = 1_000_000_000  # Número de registros parametrizado
#     gerar_dados_teste(num_registros)
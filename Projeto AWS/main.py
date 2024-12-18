import logging as _log
from web_scraper import scraping
from categories import categories
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

current_date = datetime.now().strftime('%Y-%m-%d')

# Configuração do logging para salvar em um arquivo
_log.basicConfig(
    level=_log.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        _log.FileHandler(f'extract/logs/{current_date}_scraping.log'),  # Salva os logs no arquivo scraping.log
        _log.StreamHandler()  # Exibe os logs no console
    ]
)


def run_scraping(category, url):
    _log.info(f'Iniciando scraping para a categoria {category}')
    scraping(url, category)


with ThreadPoolExecutor(max_workers=2) as executor:
    futures = [executor.submit(run_scraping, category, url) for category, url in categories.items()]

for future in futures:
    future.result()


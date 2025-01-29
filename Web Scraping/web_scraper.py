from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time as _time
import logging as _log
from bs4 import BeautifulSoup
import pandas as _pd
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

# Variáveis importantes
button_xpath = '/html/body/app-root/app-layout/app-layout-default/div/app-produtos-page/div/div[2]/div[2]/app-produtos/div/div[2]/div[2]/button'
products_df = _pd.DataFrame(columns=[
                        'Categoria',
                        'Descrição',
                        'Preço Antigo',
                        'Preço Promocional',
                        'Origem',
                        'Mercado'])

def scraping(url, category):
    # Configuração do WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    wait = WebDriverWait(driver, 4)
    i = 0

    while i < 100:
        try:
            load_more_button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
            driver.execute_script("arguments[0].click();", load_more_button)
            _log.info(f'Clicando no botão "carregar mais" a {i + 1}ª vez | Categoria: {category}')
            _time.sleep(3)
        except Exception as e:
            _log.error(f"Erro ao clicar no botão: {e}")
            break
        i += 1

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    driver.quit()

    product_container = soup.find('div', {'id': 'all-product-grid'})
    if product_container:
        products = product_container.find_all('app-produtos-produto')
        num_products = len(products)

        for product in products:
            try:
                description = product.find('span', {'class': 'produto-descricao'}).get_text(strip=True)
                old_price_element = product.find('span', {'class': 'produto-preco-de ng-star-inserted'})
                old_price = old_price_element.get_text(strip=True) if old_price_element else "Preço não disponível"
                current_price = product.find('span', {'class': 'produto-preco-por'}).get_text(strip=True)

                new_row = _pd.DataFrame({
                    'Categoria': [category],
                    'Descrição': [description],
                    'Preço Antigo': [old_price],
                    'Preço Promocional': [current_price],
                    'Origem': ['Web Scraping'],
                    'Mercado': ['Rena']
                })

                global products_df
                products_df = _pd.concat([products_df, new_row], ignore_index=True)
            except Exception as e:
                _log.error(f"Erro ao extrair dados do produto: {e}")

        products_df.to_csv(f'extract/{category}.csv', encoding='utf-8', index=False)
        _log.info(f'Foram gravados {num_products} produtos no arquivo {category}!')
    else:
        _log.warning("Contêiner de produtos não encontrado.")

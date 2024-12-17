from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.renaemcasa.com.br/p"
button_xpath = "/html/body/app-root/app-layout/app-layout-default/div/app-produtos-page/div/div[2]/div[2]/app-produtos/div/div[2]/div[2]/button"
products_df = pd.DataFrame(columns=['Descrição', 'Preço Antigo', 'Preço Promocional', 'Origem', 'Mercado'])

# Configurar o WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)
driver.get(url)

# Esperar até que o botão esteja presente e clicável
wait = WebDriverWait(driver, 10)

i = 0

while i < 10:
    try:
        load_more_button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
        driver.execute_script("arguments[0].click();", load_more_button)
        print(f'Clicando no botão "carregar mais" a {i + 1}ª vez')
        time.sleep(3)  # Ajuste o tempo de espera conforme necessário
    except Exception as e:
        print(f"Erro ao clicar no botão: {e}")
        break  # Sai do loop quando não há mais botão para clicar
    i += 1

# Obter o HTML da página carregada
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Fechar o WebDriver
driver.quit()

# Encontrar o contêiner principal dos produtos
product_container = soup.find('div', {'id': 'all-product-grid'})

# Aqui eu encontro a quantidade de produtos que foram extraídos
products = product_container.find_all('span', class_='produto-descricao')
num_products = len(products)

if product_container:
    # Iterar sobre cada produto dentro do contêiner
    for product in product_container.find_all('app-produtos-produto'):
        # Extrair a descrição do produto
        description = product.find('span', {'class': 'produto-descricao'}).get_text(strip=True)

        # Extração do preço antes da promoção (Se o produto estiver em promoção)
        old_price_element = product.find('span', {'class': 'produto-preco-de ng-star-inserted'})
        if old_price_element:
            old_price = old_price_element.get_text(strip=True)
        else:
            old_price = "Preço não disponível"

        # Extrair o preço atual do produto
        current_price = product.find('span', {'class': 'produto-preco-por'}).get_text(strip=True)

        # Criar um DataFrame temporário com a nova linha
        new_row = pd.DataFrame({
            'Descrição': [description],
            'Preço Antigo': [old_price],
            'Preço Promocional': [current_price],
            'Origem': ['Web Scraping'],
            'Mercado': ['Rena']})

        # Concatenar o DataFrame temporário com o DataFrame principal
        products_df = pd.concat([products_df, new_row], ignore_index=True)

else:
    print("Contêiner de produtos não encontrado.")

products_df.to_csv('extract/produtos.csv', encoding='utf-8', index=False)
print(f'Foram gravados {num_products} produtos no arquivo!')


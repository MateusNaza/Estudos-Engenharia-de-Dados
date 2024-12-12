from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

url = "https://www.renaemcasa.com.br/p"
button_xpath = "/html/body/app-root/app-layout/app-layout-default/div/app-produtos-page/div/div[2]/div[2]/app-produtos/div/div[2]/div[2]/button"

# Configurar o WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)
driver.get(url)

# Esperar até que o botão esteja presente e clicável
wait = WebDriverWait(driver, 10)

while True:
    try:
        load_more_button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
        driver.execute_script("arguments[0].click();", load_more_button)
        time.sleep(3)  # Ajuste o tempo de espera conforme necessário
    except Exception as e:
        print(f"Erro ao clicar no botão: {e}")
        break  # Sai do loop quando não há mais botão para clicar

# Obter o HTML da página carregada
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Fechar o WebDriver
driver.quit()

# Encontrar o contêiner principal dos produtos
product_container = soup.find('div', {'id': 'all-product-grid'})

if product_container:
    # Iterar sobre cada produto dentro do contêiner
    for product in product_container.find_all('app-produtos-produto'):
        # Extrair a descrição do produto
        description = product.find('span', {'class': 'produto-descricao'}).get_text(strip=True)

        # Extrair o preço do produto
        price = product.find('span', {'class': 'produto-preco-por'}).get_text(strip=True)

        # Extrair a URL da imagem do produto
        image_url = product.find('img', {'class': 'produto-imagem'})['src']

        # Imprimir os dados extraídos
        print(f'Descrição: {description}')
        print(f'Preço: {price}')
        print(f'Imagem: {image_url}')
        print('-' * 40)
else:
    print("Contêiner de produtos não encontrado.")

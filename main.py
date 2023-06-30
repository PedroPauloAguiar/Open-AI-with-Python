import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Substitua pelo caminho do seu ChromeDriver
CHROME_DRIVER_PATH = "caminho/para/o/chromedriver"

url = "https://www.amazon.com/dp/1789346347/ref=cm_sw_r_as_gl_api_gl_i_HFYB8PHAX05B8ERE4TC6?linkCode=ml1&tag=meucamdesan-20"

# Inicialize o webdriver
driver = webdriver.Chrome(CHROME_DRIVER_PATH)

# Abra a URL
driver.get(url)

# Aguarde 5 segundos
time.sleep(5)

# Localize o elemento com a classe 'a-text-price'
price_element = driver.find_element(By.CSS_SELECTOR, "span.a-text-price")

# Extraia o texto do elemento e remova o símbolo de dólar
price_text = price_element.text.replace("$", "")

# Converta o texto do preço para float
price = float(price_text)
print(price)
# Verifique se o preço é menor que 40
if price < 40:
    print("Comprar o livro")
else:
    print("O preço do livro é maior ou igual a $40")

# Feche o navegador
driver.quit()

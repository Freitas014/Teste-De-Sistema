from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

# Configuração do WebDriver (nesse exemplo, estamos usando o Chrome)
driver = webdriver.Chrome()

# Acessa a página de cadastro usando o caminho absoluto com protocolo file://
# Certifique-se de que o caminho está apontando para um arquivo HTML específico

driver.get("file:///C:/Users/luis_f_de-freitas/Documents/GitHub/Teste-De-Sistema/atividade/produto.html")

# Preenche o campo id
id_input = driver.find_element(By.ID, "id")
id_input.send_keys("15")
time.sleep(1)
# Preenche o campo descrição
desc_input = driver.find_element(By.ID, "desc")
desc_input.send_keys("Coxinha Grande")
time.sleep(1)
# Preenche o campo marca
marca_input = driver.find_element(By.ID, "marca")
marca_input.send_keys("Panificadora Mokele y Mbembe")
time.sleep(1)
# Preenche o campo qtde
qtde_input = driver.find_element(By.ID, "qtde")
qtde_input.send_keys("3")
time.sleep(1)
# Preenche o campo preco
preco_input = driver.find_element(By.ID, "preco")
preco_input.send_keys("6")
time.sleep(1)
# Clica no botão de Cadastrar
submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_button.click()

# TEMPORIZADOR --Aguarda um momento para visualizar o resultado (em uma aplicação real, você verificaria a resposta))
time.sleep(10)
#fecha o navegador
driver.quit()
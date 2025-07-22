from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

# Configuração do WebDriver (nesse exemplo, estamos usando o Chrome)
driver = webdriver.Chrome()

# Acessa a página de cadastro usando o caminho absoluto com protocolo file://
# Certifique-se de que o caminho está apontando para um arquivo HTML específico

driver.get("file:///C:/Users/luis_f_de-freitas/Documents/GitHub/Teste-De-Sistema/index.html")

# Preenche o campo Nome
nome_input = driver.find_element(By.ID, "name")
nome_input.send_keys("Luisito")
time.sleep(1)
# Preenche o campo CPF
cpf_input = driver.find_element(By.ID, "cpf")
cpf_input.send_keys("12312312312")
time.sleep(1)
# Preenche o campo Endereço
endereco_input = driver.find_element(By.ID, "address")
endereco_input.send_keys("Ponta Grossa, 06")
time.sleep(1)
# Preenche o campo Telefone
telefone_input = driver.find_element(By.ID, "phone")
telefone_input.send_keys("47 999254175")
time.sleep(1)
# Clica no botão de Cadastrar
submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_button.click()

# TEMPORIZADOR --Aguarda um momento para visualizar o resultado (em uma aplicação real, você verificaria a resposta))
time.sleep(10)
#fecha o navegador
driver.quit()
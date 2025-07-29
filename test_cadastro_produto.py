from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#configuração do webdriver (nesse exemplo, estamos usando o chrome)
driver = webdriver.Chrome()

#acessa a página de cadastro usando o caminho absoluto com o protocolo file://
#certifique-se de que o caminho está apontando para um arquivo HTML específico

driver.get("file:///C:/Users/eduardo_b_reinert/Documents/GitHub/teste_eduardoreinert/ATIV_produto/produto.html")

#preenche o campo Nome
nome_input = driver.find_element(By.ID, "name")
nome_input.send_keys("Capinha celular")

#preenche o campo ID
id_input = driver.find_element(By.ID, "id_produto")
id_input.send_keys("123")

#preenche o campo descrição
descricao_input = driver.find_element(By.ID, "descricao")
descricao_input.send_keys("Capinha de celular, Azul-marinho")

#preenche o campo marca
marca_input = driver.find_element(By.ID, "marca")
marca_input.send_keys("Empresa genérica")

#preenche o campo quantidade
quantidade_input = driver.find_element(By.ID, "quantidade")
quantidade_input.send_keys("1")

#preenche o campo preço
preco_input = driver.find_element(By.ID, "preco")
preco_input.send_keys("R$15,00")

#clica no botão de cadastrar
submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_button.click()

# aguarda um momento para visualizar o resultado (em uma aplicação real, você verificaria a resposta)
time.sleep(80)

#fecha o navegador
driver.quit()
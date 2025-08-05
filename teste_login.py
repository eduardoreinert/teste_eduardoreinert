from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

# driver.get("http://localhost:8080/teste_eduardoreinert/login.html")

driver.get("file:///C:/Users/eduardo_b_reinert/Documents/GitHub/teste_eduardoreinert/login.html")

time.sleep(1)

#preenche o campo de usuário
usuario_input=driver.find_element(By.ID, "username")
usuario_input.send_keys("admin")
time.sleep(1)

#preenche o campo de senha
senha_input=driver.find_element(By.ID, "password")
senha_input.send_keys("123456")

#clica no botão de login
botao_login=driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
botao_login.click()

time.sleep(8)
if "Cadastro de Cliente" in driver.page_source:
    print("Login realizado com sucesso e redirecionado para index.html!")
else:
    print("Falha no login ou redirecionamento.")

print("Título atual da página: ", driver.title)

#encerra o navegador
#driver.quit()
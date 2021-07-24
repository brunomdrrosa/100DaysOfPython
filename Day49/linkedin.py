from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import os

chrome_driver_path = "C:/Users/bruno/OneDrive/Documentos/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

PASSWORD = os.getenv("PASSWORD")

# Página de candidatura de vagas do LinkedIn
driver.maximize_window()
driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&f_WRA=true&geoId=92000000&keywords=python%20developer&location=Mundialmente&sortBy=R')
time.sleep(3)

# Logar com a conta do LinkedIn
login = driver.find_element_by_xpath("/html/body/div[3]/a[1]")
login.click()
time.sleep(3)

email = driver.find_element_by_id("username")
email.send_keys("brunomdr46@gmail.com")

senha = driver.find_element_by_id("password")
senha.send_keys(PASSWORD)

botao = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
botao.click()
time.sleep(3)

vagas = driver.find_elements_by_css_selector(".job-card-container--clickable")

for vaga in vagas:
    print("Chamado")
    vaga.click()
    time.sleep(2)

    # Localiza o botão de salvar a vaga, se já estiver salvo ele pula para a próxima vaga.
    try:
        botao_salvar = driver.find_element_by_css_selector(".jobs-save-button")
        botao_salvar.click()
        time.sleep(3)
    
    except NoSuchElementException:
        print("Não foi encontrado o botão de salvar, pulando para próxima vaga.")
        continue

time.sleep(5)
driver.quit()
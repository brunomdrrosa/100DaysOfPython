from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

chrome_driver_path = "C:/Users/bruno/OneDrive/Documentos/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Entrar na página do Tinder
driver.maximize_window()
driver.get('https://tinder.com/')
time.sleep(5)

# Logar com a conta do Facebook
login = driver.find_element_by_xpath(
    '//*[@id="c2094796203"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()
time.sleep(3)

facebook = driver.find_element_by_xpath(
    '//*[@id="c366415127"]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook.click()
time.sleep(5)

# Trocar para a guia de login do Facebook
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email_face = driver.find_element_by_id('email')
email_face.send_keys(EMAIL)

senha_face = driver.find_element_by_id('pass')
senha_face.send_keys(PASSWORD)
senha_face.send_keys(Keys.ENTER)

# Voltar para a página do Tinder
driver.switch_to.window(base_window)
print(driver.title)
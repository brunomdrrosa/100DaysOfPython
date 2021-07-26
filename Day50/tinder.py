import selenium
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

google = driver.find_element_by_xpath(
    '//*[@id="c366415127"]/div/div/div[1]/div/div[3]/span/div[1]/div/button')
google.click()
time.sleep(5)

# Trocar para a guia de login do Google
base_window = driver.window_handles[0]
google_window = driver.window_handles[1]
driver.switch_to.window(google_window)
print(driver.title)
time.sleep(5)

# Logar na conta do Google
email_google = driver.find_element_by_xpath('//*[@id="identifierId"]')
email_google.send_keys(EMAIL)
email_google.send_keys(Keys.ENTER)
time.sleep(3)

senha_google = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
time.sleep(3)
senha_google.send_keys(PASSWORD)
senha_google.send_keys(Keys.ENTER)

# Voltar para a página do Tinder
driver.switch_to.window(base_window)
print(driver.title)
time.sleep(5)

# Permitir localização
allow_location_button = driver.find_element_by_xpath('//*[@id="c366415127"]/div/div/div/div/div[3]/button[1]/span')
allow_location_button.click()

# Desativar notificações
notifications_button = driver.find_element_by_xpath('//*[@id="c366415127"]/div/div/div/div/div[3]/button[2]/span')
notifications_button.click()

# Permitir cookies
cookies = driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[2]/div/div/div[1]/button/span')
cookies.click()
time.sleep(10)

dislike = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')

# Loop para dar deslike
while True:
    time.sleep(2)
    try:
        dislike.click()
    except selenium.common.exceptions.ElementClickInterceptedException:
        time.sleep(1)
        continue

# Loop para dar curtidas
# for n in range(100):

    # time.sleep(1)
    # try:
    #     print("called")
    #     like_button = driver.find_element_by_xpath(
    #         '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
    #     like_button.click()

    # Caso o botão de "Match" fique na frente do botão de like
#     except ElementClickInterceptedException:
#         try:
#             match_popup = driver.find_element_by_css_selector(".itsAMatch a")
#             match_popup.click()

#         except NoSuchElementException:
#             time.sleep(2)

# driver.quit()
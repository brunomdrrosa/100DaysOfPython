from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

# Limitei em 90Mbps de download por conta do meu computador não chegar aos 100Mpbs por causa da placa de rede.
DOWNLOAD_PROMETIDO = 90.0
UPLOAD_PROMETIDO = 10.0
CHROME_DRIVER_PATH = "C:/Users/bruno/OneDrive/Documentos/chromedriver.exe"
TWITTER_EMAIL = os.getenv("EMAIL")
TWITTER_PASSWORD = os.getenv("PASSWORD")

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.maximize_window()
        self.driver.get("https://www.speedtest.net/")
        sleep(5)
        botao_iniciar = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        botao_iniciar.click()
        sleep(45)
        self.down = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text.strip().replace(",","."))
        self.up = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text.strip().replace(",","."))
        print(f"A internet está com {self.down}Mbps de Download e {self.up}Mbps de Upload")
        if self.down < DOWNLOAD_PROMETIDO or self.up < UPLOAD_PROMETIDO:
            bot.tweet_at_provider()

    def tweet_at_provider(self):
        # Trocar para a guia de login do Google
        self.driver.get("https://twitter.com/")
        sleep(5)

        # Entrar no Twitter
        entrar = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[3]/span/span')
        entrar.click()
        sleep(2)
        logar = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a/div/span/span')
        logar.click()

        # Logar na conta do Twitter
        email_twitter = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        email_twitter.send_keys(TWITTER_EMAIL)

        senha_twitter = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        senha_twitter.send_keys(TWITTER_PASSWORD)
        senha_twitter.send_keys(Keys.ENTER)
        sleep(5)

        # Realizar o tweet     
        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet.click()
        tweet.send_keys(f"Olá, provedor de internet!\nPor que minha internet está com {self.down}Mbps de download e {self.up}Mbps de upload se eu pago 120Mbps de download e 10Mbps de upload?")
        botao_tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
        botao_tweet.click()
        sleep(5)

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
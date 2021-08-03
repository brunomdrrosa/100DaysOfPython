from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep
import os

CHROME_DRIVER_PATH = "C:/Users/bruno/OneDrive/Documentos/chromedriver.exe"
ACCOUNT_TO_FOLLOW = "oficialoplano"
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(5)
        email_instagram = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input')
        email_instagram.send_keys(EMAIL)
        senha_instagram = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input')
        senha_instagram.send_keys(PASSWORD)
        senha_instagram.send_keys(Keys.ENTER)
        sleep(5)        

    def find_followers(self):
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{ACCOUNT_TO_FOLLOW}")

        sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
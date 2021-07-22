from bs4 import BeautifulSoup
import smtplib
import requests
import os

SMTP_ADDRESS = "smtp.gmail.com"
FIRST_EMAIL = os.getenv("FIRST_EMAIL")
SECOND_EMAIL = os.getenv("SECOND_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

# Scraping Amazon
url = "https://www.amazon.com.br/Echo-Dot-3%C2%AA-Gera%C3%A7%C3%A3o-Cor-Preta/dp/B07PDHSJ1H/ref=zg_bs_electronics_home_3?_encoding=UTF8&psc=1&refRID=9366HW8AYAPE7KHFSDA2"
resposta = requests.get(f"https://www.amazon.com.br/Echo-Dot-3%C2%AA-Gera%C3%A7%C3%A3o-Cor-Preta/dp/B07PDHSJ1H/ref=zg_bs_electronics_home_3?_encoding=UTF8&psc=1&refRID=9366HW8AYAPE7KHFSDA2", headers={
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36", "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"})

soup = BeautifulSoup(resposta.content, "lxml")

price = soup.find(
    class_="a-size-medium a-color-price priceBlockSavingsString").getText()

price_string = price.split("R$")[1]
prices = price_string.split(",")
total_price = ""
for price in prices:
    total_price += price

price_float = float(total_price) / 100

# Enviando e-mail
title = soup.find(id="productTitle").get_text().strip()

BUY_PRICE = 200

if price_float < BUY_PRICE:
    message = f"{title} está custando R$ {price_float}"
    message.encode('utf-8')

with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
    connection.starttls()
    result = connection.login(FIRST_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=FIRST_EMAIL,
        to_addrs=SECOND_EMAIL,
        msg=f"Subject:Amazon | Alerta de preço baixo!\n\n{message}\n{url}".encode(
            'utf-8')
    )

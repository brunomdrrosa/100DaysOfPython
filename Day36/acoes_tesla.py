import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_ALPHAVANTAGE = "" # Sua API do Alpha Vantage
API_NEWSAPI = "" # Sua API do News API
TWILIO_SID = "" # Sua ACCOUNT SID do Twilio
TWILIO_AUTH_TOKEN = "" # Seu AUTH TOKEN do Twilio

API_CONVERTER_DOLAR_PARA_REAL = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
resposta_brl = requests.get(API_CONVERTER_DOLAR_PARA_REAL)
valor_brl = float(resposta_brl.json()["USDBRL"]["bid"])

# Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
parametros = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_ALPHAVANTAGE,
}

resposta = requests.get(STOCK_ENDPOINT, params=parametros)
dados = resposta.json()["Time Series (Daily)"]
lista_dados = [value for (key, value) in dados.items()]
dados_ontem = lista_dados[0]
preco_ontem_usd = float(dados_ontem["4. close"])
preco_ontem_brl = preco_ontem_usd * valor_brl

# Get the day before yesterday's closing stock price
dados_anteontem = lista_dados[1]
preco_anteontem_usd= float(dados_anteontem["4. close"])
preco_anteontem_brl = preco_anteontem_usd * valor_brl

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diferenca = preco_ontem_brl - preco_anteontem_brl
emoji = None
if diferenca > 0:
    emoji = "🔺"
else:
    emoji = "🔻"

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentual_diferenca = round((diferenca / preco_ontem_brl) * 100)

# If TODO4 percentage is greater than 5 then print("Get News").
# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if abs(percentual_diferenca) > 0.5:
    parametros_noticias = {
        "apiKey": API_NEWSAPI,
        "qInTitle": COMPANY_NAME,
    }

    resposta_noticias = requests.get(NEWS_ENDPOINT, params=parametros_noticias)
    artigos = resposta_noticias.json()["articles"]

# Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
tres_artigos = artigos[:3]

# Create a new list of the first 3 article's headline and description using list comprehension.
artigos_formatados = [f"{STOCK_NAME}: {emoji}{percentual_diferenca}%\nTítulo: {artigo['title']}.\nResumo: {artigo['content']}" for artigo in tres_artigos]

# Send each article as a separate message via Twilio. 
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

for artigo in artigos_formatados:
    message = client.messages.create(
        body=artigo,
        from_="+", # O número do trial do Twilio
        to="+" # Seu número de celular
    )
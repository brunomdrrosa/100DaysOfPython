import requests
from twilio.rest import Client

openWeather = "https://api.openweathermap.org/data/2.5/onecall"

minha_api = "" # Sua API do OpenWeatherMap
account_sid = "" # Sua ACCOUNT SID do Twilio
auth_token = "" # Seu AUTH TOKEN do Twilio

# Latitude e longitude de Cachoeirinha/RS
parameters = {
    "lat": -29.947670,
    "lon": -51.092419,
    "appid": minha_api,
    "exclude": "current,minutely,daily"
}

vai_chover = False

# Site para ver JSON online = http://jsonviewer.stack.hu/
resposta = requests.get(openWeather, params=parameters)
resposta.raise_for_status()
dados_clima = resposta.json()
clima_dividido = dados_clima["hourly"][:12]
for hora in clima_dividido:
    codigo_condicao = hora["weather"][0]["id"]
    if int(codigo_condicao) < 700:
        vai_chover = True

if vai_chover:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Vai chover, pegue um guarda-chuva 🌧️☂️", # Mensagem que será enviada no SMS
        from_="+", # O número do trial do Twilio
        to="+" # Seu número de telefone
    )
    print(message.status)
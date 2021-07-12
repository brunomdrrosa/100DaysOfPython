import requests
from datetime import datetime

USERNAME = "brunomdr"
TOKEN = "bruno123"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

parametros_usuario = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

GRAFICO_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
ID_GRAFICO = "grafico"

configuracoes_grafico = {
    "id": ID_GRAFICO,
    "name": "Leitura",
    "unit": "páginas",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}


# Criar um pixel no gráfico
CRIAR_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID_GRAFICO}"
hoje = datetime.now()
print(hoje.strftime("%Y%m%d"))
dados_pixel = {
    "date": hoje.strftime("%Y%m%d"),
    "quantity": "0",
}
# resposta = requests.post(url=CRIAR_PIXEL_ENDPOINT, json=dados_pixel, headers=headers)
# print(resposta.text)


# Atualizar os pixels do gráfico
UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID_GRAFICO}/20210712"
atualizar_pixel = {
    "quantity": "0",
}
# resposta = requests.post(url=UPDATE_ENDPOINT, json=atualizar_pixel, headers=headers)
# print(resposta.text)


# Deletar os pixels do gráfico
DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID_GRAFICO}/20200712"
# resposta = requests.delete(url=DELETE_ENDPOINT, headers=headers)
# print(resposta.text)
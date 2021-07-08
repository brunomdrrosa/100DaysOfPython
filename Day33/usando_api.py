import requests

resposta = requests.get(url="http://api.open-notify.org/iss-now.json")
resposta.raise_for_status()

longitude = resposta.json()["iss_position"]["longitude"]
latitude = resposta.json()["iss_position"]["latitude"]

posicao_iss = (longitude, latitude)
print(posicao_iss)

# Site para descobrir o local baseado na longitude e latitude
# https://www.latlong.net/Show-Latitude-Longitude.html
from bs4 import BeautifulSoup
import requests

resposta = requests.get("https://news.ycombinator.com/")
web_page = resposta.text

soup = BeautifulSoup(web_page, "html.parser")
artigos = soup.find_all(name="a", class_="storylink")
lista_textos = []
lista_links = []

for artigo in artigos:
    text = artigo.getText()
    lista_textos.append(text)
    link = artigo.get("href")
    lista_links.append(link)

votos_artigo = [int(vote.getText().split()[0]) for vote in soup.find_all(name="span", class_="score")]

maior_numero = max(votos_artigo)
posicao_maior = votos_artigo.index(maior_numero)

print(lista_textos[posicao_maior])
print(lista_links[posicao_maior])

# print(lista_textos)
# print(lista_links)
# print(votos_artigo)

# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup.prettify)
# print(soup.title.string)

# todas_tags_a = soup.find_all(name="a")

# for tag in todas_tags_a:
#     print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# name = soup.select_one("#name")
# print(name)
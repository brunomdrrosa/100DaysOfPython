from selenium import webdriver
from time import sleep
from logo import logo

chrome_driver_path = "C:/Users/bruno/OneDrive/Documentos/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Página da Steam Database
driver.maximize_window()
driver.get('https://steamdb.info/')
sleep(3)

lista_jogos = []
lista_players = []
numero_jogos = 2
numero_players = 2
numero_estatistica = 0

# Checar os 5 jogos sendo mais jogados no momento
jogos = range(5)
for jogo in jogos:
    jogo_steam = driver.find_element_by_xpath(f'/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/table/tbody/tr[{numero_jogos}]/td[2]/a').text
    numero_jogos += 1
    lista_jogos.append(jogo_steam)

# Checar a quantidade de players atual em cada jogo 
for player in jogos:
    players_jogando = driver.find_element_by_xpath(f'/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/table/tbody/tr[{numero_players}]/td[3]').text
    numero_players += 1
    lista_players.append(players_jogando)

print(logo)
print("Esse são os jogos que estão sendo mais jogos no momento na Steam\n")

for estatistica in jogos:
    print(f"O jogo {lista_jogos[numero_estatistica]} tem {lista_players[numero_estatistica]} jogadores jogando agora.")
    numero_estatistica += 1
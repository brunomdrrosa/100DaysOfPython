import detectlanguage
import pandas as pd
from logo import logo

data = pd.read_csv('languages.csv')  
detectlanguage.configuration.api_key = "03e1e4f1320ec177f1e08a1d9051edeb"

print(logo)
mensagem = input("Digite uma mensagem para o programa descobrir o idioma em que ela foi escrito:\n")
sigla_idioma = detectlanguage.simple_detect(mensagem)

linha = 0
coluna = 0
programa = True

while programa:
    sigla = data.iloc[linha, coluna]
    linha += 1
    if sigla == sigla_idioma:
        programa = False
        coluna += 1
        linha -= 1
        sigla = data.iloc[linha, coluna]

print(f"A sua mensagem foi escrito no idioma: {sigla}")
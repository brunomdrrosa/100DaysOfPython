from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

# Início do programa
print(logo)
print("Bem vindo ao Leilão às Cegas")

# Dicionário com nomes e lances
lista_leilao = {}
lance_finalizado = False

# Achar o valor mais alto
def valor_mais_alto(lance_recorde):
  lance_mais_alto = 0
  ganhador = ""
  for apostador in lance_recorde:
    quantia_lances = lance_recorde[apostador]
    if quantia_lances > lance_mais_alto:
      lance_mais_alto = quantia_lances
      ganhador = apostador
  print(f"O ganhador é {ganhador} com um lance de R${lance_mais_alto}")

# Perguntas
while not lance_finalizado:
  nome = input("Qual o seu nome? ")
  lance = int(input("Qual o seu lance? R$ "))
  lista_leilao[nome] = lance
  apostadores = input("Tem mais alguém para realizar um lance? Digite 'S' ou 'N'.\n").lower()
  if apostadores == "s":
    clear()
  elif apostadores == "n":
    lance_finalizado = True
    valor_mais_alto(lista_leilao)
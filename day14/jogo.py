# Importar a logo, dados, módulo clear e random
import random
import os
from arte import logo, vs
from dados import dados

# Perfil aleatório
def perfil_aleatorio():
  return random.choice(dados)

# Função para formatar os dados
def formatar_dados(pessoa):
  nome = pessoa["name"]
  descricao = pessoa["description"]
  return f"{nome}, {descricao}"

# Checar se a resposta do usuário está certa
def check_answer(palpite, seguidores_a, seguidores_b):
  if seguidores_a > seguidores_b:
    return palpite == "a"
  else:
    return palpite == "b"  

# Função para limpar o console
def limpar():
    clear = lambda: os.system('cls')
    clear()

def jogar():
  print(logo)
  pontuacao = 0
  gameover = False
  conta_a = perfil_aleatorio()
  conta_b = perfil_aleatorio()

  while not gameover:
    conta_a = conta_b
    conta_b = perfil_aleatorio()

    while conta_a == conta_b:
      conta_b = perfil_aleatorio()

    print(f"Comparar A: {formatar_dados(conta_a)}.")
    print(vs)
    print(f"Contra B: {formatar_dados(conta_b)}.")
    
    palpite = input("Quem tem mais seguidores? Digite 'A' or 'B': ").lower()
    quantidade_seguidor_a = conta_a["follower_count"]
    quantidade_seguidor_b = conta_b["follower_count"]
    correto = check_answer(palpite, quantidade_seguidor_a, quantidade_seguidor_b)

    clear = lambda: os.system('cls')
    clear()
    print(logo)
    if correto:
      pontuacao += 1
      print(f"Você acertou! Pontuação atual: {pontuacao}.")
    else:
      gameover = True
      print(f"Você errou. Pontuação final: {pontuacao}")

jogar()
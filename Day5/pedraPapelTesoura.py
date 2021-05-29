import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
escolha = input("O que você quer escolher? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura.\n")

if escolha == "0":
    print(pedra)
elif escolha == "1":
    print(papel)
elif escolha == "2":
    print(tesoura)

computador = [pedra, papel, tesoura]
escolhaPC = random.choice(computador)
print("O computador escolheu:")
print(escolhaPC)

# Computador escolheu pedra.
if escolha == "0" and escolhaPC == pedra:
    print("Deu empate!")
elif escolha == "1" and escolhaPC == pedra:
    print("Você ganhou!")
elif escolha == "2" and escolhaPC == pedra:
    print("Você perdeu!")

# Computador escolheu papel.
if escolha == "0" and escolhaPC == papel:
    print("Você perdeu!")
elif escolha == "1" and escolhaPC == papel:
    print("Deu empate!")
elif escolha == "2" and escolhaPC == papel:
    print("Você ganhou!")

# Computador escolheu tesoura.
if escolha == "0" and escolhaPC == tesoura:
    print("Você ganhou!")
elif escolha == "1" and escolhaPC == tesoura:
    print("Você perdeu!")
elif escolha == "2" and escolhaPC == tesoura:
    print("Deu empate!")
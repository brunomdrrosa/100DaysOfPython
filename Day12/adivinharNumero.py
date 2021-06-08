#Number Guessing Game Objectives:

# Include an ASCII art logo.
from arte import logo
import random

# Criar um número aleatório de 1 a 100
numero = random.randint(1,100)

# Mensagens de início do jogo
def jogar():
    print(logo)
    print("Bem-vindo ao jogo 'Adivinhe o número'")
    print("Eu estou pensando num número entre 1 e 100.")
    dificuldade = input("Escolha uma dificuldade. Digite 'fácil' ou 'difícil': ").lower()
    
# Dificuldade fácil
    if dificuldade == "facil" or "fácil":
        tentativas = 10
        print(f"Você tem {tentativas} tentativas para adivinhar o número")
        palpite = int(input("Faça um palpite: "))
        if palpite == numero:
            print(f"Você conseguiu! O número era {numero}")
        while palpite > numero:
            tentativas -= 1
            print("Número muito alto.")
            print("Faça um palpite novamente.")
            print(f"Você tem {tentativas} tentativas restantes para adivinhar o número.")
            palpite = int(input("Faça um palpite: "))
            if palpite == numero:
                print(f"Você conseguiu! O número era {numero}")
            if tentativas == 1:
                print("Você gastou todas suas tentativas, você perdeu.")
                exit()
        while palpite < numero:
            tentativas -= 1
            print("Número muito baixo.")
            print("Faça um palpite novamente.")
            print(f"Você tem {tentativas} tentativas restantes para adivinhar o número.")
            palpite = int(input("Faça um palpite: "))
            if palpite == numero:
                print(f"Você conseguiu! O número era {numero}")
            if tentativas == 1:
                print("Você gastou todas suas tentativas, você perdeu.")

# Dificuldade difícil
    elif dificuldade == "dificil" or "difícil":
        print("DIFICULDADE DIFICIL")
        tentativas = 5
        print(f"Você tem {tentativas} tentativas para adivinhar o número")
        palpite = int(input("Faça um palpite: "))
        if palpite == numero:
            print(f"Você conseguiu! O número era {numero}")
        while palpite > numero:
            tentativas -= 1
            print("Número muito alto.")
            print("Faça um palpite novamente.")
            print(f"Você tem {tentativas} tentativas restantes para adivinhar o número.")
            palpite = int(input("Faça um palpite: "))
            if palpite == numero:
                print(f"Você conseguiu! O número era {numero}")
            if tentativas == 1:
                print("Você gastou todas suas tentativas, você perdeu.")
                exit()
        while palpite < numero:
            tentativas -= 1
            print("Número muito baixo.")
            print("Faça um palpite novamente.")
            print(f"Você tem {tentativas} tentativas restantes para adivinhar o número.")
            palpite = int(input("Faça um palpite: "))
            if palpite == numero:
                print(f"Você conseguiu! O número era {numero}")
            if tentativas == 1:
                print("Você gastou todas suas tentativas, você perdeu.")

jogar()

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
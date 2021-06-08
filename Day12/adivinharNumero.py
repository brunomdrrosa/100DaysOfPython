# Importar a logo, módulo aleatório e opção de limpar o console
from arte import logo
import random
import os

# Criar um número aleatório de 1 a 100
numero = random.randint(1,100)

# Reiniciar o jogo
def reiniciar():
    restart = input("Você deseja jogar novamente? Digite 'S' ou 'N': ").lower()
    if restart == 's':
        cls = lambda: os.system('cls')
        cls()
        jogar()
    elif restart == 'n':
        exit()

# Dificuldade fácil
def facil():
    tentativas = 10
    print(f"Você tem {tentativas} tentativas para adivinhar o número")
    if tentativas != 0:
        palpite = int(input("Faça um palpite: "))
    if palpite == numero:
        print(f"A chance era de 1% e você conseguiu! O número era {numero}")
        print()
        reiniciar()

    while tentativas != 0:
        if palpite > numero:
            tentativas -= 1
            if tentativas == 0:
                print()
                print(f"Você perdeu, o numero era {numero}.")
                reiniciar()
            print("Número muito alto.")
            print(f"Você tem {tentativas} tentativas restantes para adivinhar o número.")
            print()
            palpite = int(input("Faça um palpite: "))
            if palpite == numero:
                print(f"Você conseguiu! O número era {numero}")
                print()
                reiniciar()
            if tentativas == 0:
                reiniciar()

        elif palpite < numero:
            tentativas -= 1
            if tentativas == 0:
                print()
                print(f"Você perdeu, o numero era {numero}.")
                reiniciar()
            print("Número muito baixo.")
            print(f"Você tem {tentativas} tentativas restantes para adivinhar o número.")
            print()
            palpite = int(input("Faça um palpite: "))
            if palpite == numero:
                print(f"Você conseguiu! O número era {numero}")
                print()
                reiniciar()
            if tentativas == 0:
                reiniciar()

# Dificuldade difícil
def dificil():
    tentativas = 5
    print(f"Você tem {tentativas} tentativas para adivinhar o número")
    if tentativas != 0:
        palpite = int(input("Faça um palpite: "))
    if palpite == numero:
        print(f"A chance era de 1% e você conseguiu! O número era {numero}")
        print()
        reiniciar()

    while tentativas != 0:
        if palpite > numero:
            tentativas -= 1
            if tentativas == 0:
                print()
                print(f"Você perdeu, o numero era {numero}.")
                reiniciar()
            print("Número muito alto.")
            print(f"Você tem {tentativas} tentativas restantes para adivinhar o número.")
            print()
            palpite = int(input("Faça um palpite: "))
            if palpite == numero:
                print(f"Você conseguiu! O número era {numero}")
                print()
                reiniciar()
            if tentativas == 0:
                reiniciar()

        elif palpite < numero:
            tentativas -= 1
            if tentativas == 0:
                print()
                print(f"Você perdeu, o numero era {numero}.")
                reiniciar()
            print("Número muito baixo.")
            print(f"Você tem {tentativas} tentativas restantes para adivinhar o número.")
            print()
            palpite = int(input("Faça um palpite: "))
            if palpite == numero:
                print(f"Você conseguiu! O número era {numero}")
                print()
                reiniciar()
            if tentativas == 0:
                reiniciar()

def jogar():
    print(logo)
    print("Bem-vindo ao jogo 'Adivinhe o número'")
    print("Eu estou pensando num número entre 1 e 100.")
    dificuldade = input("Escolha uma dificuldade. Digite 'fácil' ou 'difícil': ").lower()
    if dificuldade == "facil" or dificuldade == "fácil":
        facil()
    elif dificuldade == "dificil" or dificuldade == "difícil":
        dificil()

jogar()

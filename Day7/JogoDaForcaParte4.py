#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lista_palavras = ["bruno", "gaucho", "gremio", "cachoeirinha", "agosto"]
palavra_escolhida = random.choice(lista_palavras)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
vidas = 6

#Testing code
print(f'Ei, a palavra é {palavra_escolhida}.')

#Create blanks
campos = []
for _ in range(len(palavra_escolhida)):
    campos += "_"

palavra_escolhida_lista = list(palavra_escolhida)

while campos != palavra_escolhida_lista:
    palpite = input("Digite uma letra para adivinhar a palavra escolhida: ").lower()

    #Check guessed letter
    for posicao in range(len(palavra_escolhida)):
        letra = palavra_escolhida[posicao]

        if letra == palpite:
            campos[posicao] = letra       

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
   
    if palpite not in palavra_escolhida:
        vidas -= 1
        if vidas == 0:
            campos != palavra_escolhida_lista
            print("Você perdeu.")    


    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(campos)}")    

    #Check if user has got all letters.
    if campos == palavra_escolhida_lista:
        print("Parabéns, você ganhou!")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[vidas])
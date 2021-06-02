#Step 5

import random
from asciiArtes import stages, logo
from palavras import lista_palavras

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
palavra_escolhida = random.choice(lista_palavras)

vidas = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

#Testing code
print("Bem-vindo ao Jogo da Forca do Brasileirão 2021")

#Create blanks
campos = []
for _ in range(len(palavra_escolhida)):
    campos += "_"

palavra_escolhida_lista = list(palavra_escolhida)

while campos != palavra_escolhida_lista:
    palpite = input("Digite uma letra para adivinhar o time escolhido: ").lower()
    palpites_lista = list(palpite)

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if palpite in campos:
        print(f"Você já escolheu a letra {palpite}")

    #Check guessed letter
    for posicao in range(len(palavra_escolhida)):
        letra = palavra_escolhida[posicao]

        if letra == palpite:
            campos[posicao] = letra       

#Check if user is wrong.
    if palpite not in palavra_escolhida:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        vidas -= 1
        print(f"Você escolheu a letra {palpite}, porém ela não está na palavra. Você perdeu uma vida! ")
        if vidas == 0:
            campos != palavra_escolhida_lista
            print("Você perdeu.")    


    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(campos)}")    

    #Check if user has got all letters.
    if campos == palavra_escolhida_lista:
        print("Parabéns, você ganhou!")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[vidas])
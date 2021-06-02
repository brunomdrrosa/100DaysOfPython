import random

#Step 1 

lista_palavras = ["bruno", "gaucho", "gremio", "cachoeirinha"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

palavra_escolhida = random.choice(lista_palavras)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

palpite = input("Digite uma letra para adivinhar a palavra escolhida: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letra in palavra_escolhida:
  if palpite == letra:
    print("Certo")
  else:
    print("Errado")

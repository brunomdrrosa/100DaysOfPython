#Step 3

import random
lista_palavras = ["bruno", "gaucho", "gremio", "cachoeirinha", "agosto"]
palavra_escolhida = random.choice(lista_palavras)

#Testing code
print(f'Ei, a palavra é {palavra_escolhida}.')

#Create blanks
campos = []
for _ in range(len(palavra_escolhida)):
    campos += "_"
print(campos)

palavra_escolhida_lista = list(palavra_escolhida)

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
while campos != palavra_escolhida_lista:
    palpite = input("Digite uma letra para adivinhar a palavra escolhida: ").lower()
    
    for posicao in range(len(palavra_escolhida)):
        letra = palavra_escolhida[posicao]
        if letra == palpite:
            campos[posicao] = letra
            print(campos)

if campos == palavra_escolhida_lista:
    print("Parabéns, você ganhou!")
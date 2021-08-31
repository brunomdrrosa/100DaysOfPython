from logo import logo

MORSE = {' ': '_',
         "'": '.----.',
         '(': '-.--.-',
         ')': '-.--.-',
         ',': '--..--',
         '-': '-....-',
         '.': '.-.-.-',
         '/': '-..-.',
         '0': '-----',
         '1': '.----',
         '2': '..---',
         '3': '...--',
         '4': '....-',
         '5': '.....',
         '6': '-....',
         '7': '--...',
         '8': '---..',
         '9': '----.',
         ':': '---...',
         ';': '-.-.-.',
         '?': '..--..',
         'A': '.-',
         'B': '-...',
         'C': '-.-.',
         'D': '-..',
         'E': '.',
         'F': '..-.',
         'G': '--.',
         'H': '....',
         'I': '..',
         'J': '.---',
         'K': '-.-',
         'L': '.-..',
         'M': '--',
         'N': '-.',
         'O': '---',
         'P': '.--.',
         'Q': '--.-',
         'R': '.-.',
         'S': '...',
         'T': '-',
         'U': '..-',
         'V': '...-',
         'W': '.--',
         'X': '-..-',
         'Y': '-.--',
         'Z': '--..',
         '_': '..--.-'}


def convertToMorseCode(sentence):
    sentence = sentence.upper()
    encodedSentence = ""
    for character in sentence:
        encodedSentence += MORSE[character] + " "
    return encodedSentence


def menu():
    print(logo)
    print("Bem-vindo ao convertor de texto para código morse")
    frase = input("Digite uma frase para converter em código morse:\n")
    fraseMorse = convertToMorseCode(frase)
    print(fraseMorse)
    pergunta = input("Você quer rodar o programa de novo? S ou N\n").lower()
    if pergunta == "s":
        menu()
    elif pergunta == "n":
        exit()

menu()

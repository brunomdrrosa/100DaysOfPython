# 🚨 Don't change the code below 👇
print("Bem-vindo a Calculadora do Amor")
nome1 = input("Qual o seu nome? \n")
nome2 = input("Qual o nome dele ou dela? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Contador de letras do primeiro nome (TRUE LOVE)
nome1Minusculo = nome1.lower()

# Contador de letras do segundo nome (TRUE LOVE)
nome2Minusculo = nome2.lower()

# Soma das letras de ambos nomes
words_true = nome1Minusculo.count("t") + nome2Minusculo.count("t") + nome1Minusculo.count("r") + nome2Minusculo.count("r") + nome1Minusculo.count("u") + nome2Minusculo.count("u") + nome1Minusculo.count("e") + nome2Minusculo.count("e")
words_love = nome1Minusculo.count("l") + nome2Minusculo.count("l") + nome1Minusculo.count("o") + nome2Minusculo.count("o") + nome1Minusculo.count("v") + nome2Minusculo.count("v") + nome1Minusculo.count("e") + nome2Minusculo.count("e")

# Convertendo a pontuação para um valor númerico
score = str(words_true) + str(words_love)
score_int = int(score)

# Estruturas condicionais para dizer o valor ao usuário
if score_int < 10 or score_int > 90:
    print(f"Sua pontuação é {score_int}, vocês combinam como Coca-Cola e Mentos.")
elif score_int >= 40 and score_int <= 50:
    print(f"Sua pontuação é {score_int}, vocês estão bem juntos.")
else:
    print(f"Sua pontuação é {score_int}.")
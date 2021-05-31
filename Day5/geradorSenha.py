import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem-vindo ao Gerador PySenha!")
nmr_letras = int(input("Quantas letras você gostaria que tivesse na sua senha?\n")) 
nmr_simbolos = int(input(f"Quantos símbolos você gostaria?\n"))
nmr_numeros = int(input(f"Quantos números você gostaria?\n"))

#Easy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# senha = ""

# for char in range(1, nmr_letras + 1):
#   senha += random.choice(letras)

# for char in range(1, nmr_simbolos + 1):
#   senha += random.choice(simbolos)

# for char in range(1, nmr_numeros + 1):
#   senha += random.choice(numeros)

# print(senha)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

lista_senha = []

for char in range(1, nmr_letras + 1):
  lista_senha.append(random.choice(letras))

for char in range(1, nmr_simbolos + 1):
  lista_senha += random.choice(simbolos)

for char in range(1, nmr_numeros + 1):
  lista_senha += random.choice(numeros)

random.shuffle(lista_senha)

senha = ""
for x in lista_senha:
  senha += x

print(f"Sua senha é: {senha}")
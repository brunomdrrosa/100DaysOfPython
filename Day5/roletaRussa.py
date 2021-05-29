# Split string method.
nomes_string = input("Me dê o nome de todos, separado por vírgula. ")
nomes = nomes_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

total_pessoas = len(nomes)
escolha = random.randint(0, total_pessoas - 1)
pessoa = nomes[escolha]
print(pessoa + " irá pagar a refeição hoje!")
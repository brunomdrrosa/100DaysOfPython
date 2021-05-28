# 🚨 Don't change the code below 👇
print("Bem-vindo ao Entregas Pizza Python!")
tamanho = input("Que tamanho de pizza você quer? P, M, ou G\n")
pepperoni = input("Você quer pepperoni? S ou N\n")
queijo_extra = input("Você quer queijo extra? S ou N\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Pizza pequena
if tamanho == "P":
    total = 30
    if pepperoni == "S":
        total += 2
    if queijo_extra == "S":
        total += 1
    print(f"Sua pizza custará: R${total}.")

# Pizza média
if tamanho == "M":
    total = 45
    if pepperoni == "S":
        total += 3
    if queijo_extra == "S":
        total += 1
    print(f"Sua pizza custará: R${total}.")

# Pizza grande
if tamanho == "G":
    total = 55
    if pepperoni == "S":
        total += 3
    if queijo_extra == "S":
        total += 1
    print(f"Sua pizza custará: R${total}.")
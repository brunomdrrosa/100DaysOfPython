# 🚨 Don't change the code below. 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
mapa = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
posicao = input("Onde você quer colocar o tesouro? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal = int(posicao[0])
vertical = int(posicao[1])

linha = mapa[vertical - 1]
linha[horizontal - 1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
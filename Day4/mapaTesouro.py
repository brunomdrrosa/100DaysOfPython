# ð¨ Don't change the code below. ð
row1 = ["â¬ï¸","â¬ï¸","â¬ï¸"]
row2 = ["â¬ï¸","â¬ï¸","â¬ï¸"]
row3 = ["â¬ï¸","â¬ï¸","â¬ï¸"]
mapa = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
posicao = input("Onde vocÃª quer colocar o tesouro? ")
# ð¨ Don't change the code above ð

#Write your code below this row ð
horizontal = int(posicao[0])
vertical = int(posicao[1])

linha = mapa[vertical - 1]
linha[horizontal - 1] = "X"

#Write your code above this row ð

# ð¨ Don't change the code below ð
print(f"{row1}\n{row2}\n{row3}")
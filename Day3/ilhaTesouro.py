print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem-vindo a Ilha do Tesouro.")
print("Sua missão é encontrar o tesouro.")

lado = input("Você deseja ir para a direita ou para a esquerda? D ou E \n")
if lado == "E":
  print("Você escolheu o lado certo!")
  acao = input("Você deseja nadar ou esperar? N ou E \n")
  if acao == "E":
    print("Você escolheu a ação certa!")
    porta = input("Você deseja abrir a porta vermelha, amarela ou azul? V, AM ou AZ \n")
    if porta == "AM":
      print("Parabéns, você acertou a porta e ganhou o tesouro!")
    elif porta == "V":
      print("Você errou a porta e morreu queimado. Game Over!")
    elif porta == "AZ":
      print("Você errou a porta e foi devorado por um animal. Game Over!")
    else:
      print("Essa porta não existe. Game Over!")
  else:
    print("Você foi atacado por um tubarão. Game Over!")
else:
  print("Você caiu num buraco. Game Over!")
# 🚨 Don't change the code below 👇
ano = int(input("Qual ano você quer checar? "))
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests
if ano % 4 == 0:
  if ano % 100 == 0:
    if ano % 400 == 0:
      print("É um ano bissexto.")
    else:
      print("Não é um ano bissexto.")
  else:
    print("É um ano bissexto.")
else:
  print("Não é um ano bissexto.")


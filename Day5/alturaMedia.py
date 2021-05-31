# 🚨 Don't change the code below 👇
altura_alunos = input("Insira a lista da altura dos estudantes: ").split()
for n in range(0, len(altura_alunos)):
  altura_alunos[n] = int(altura_alunos[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
alturaTotal = 0
for altura in altura_alunos:
  alturaTotal += altura

alunoQuantia = 0
for aluno in altura_alunos:
  alunoQuantia += 1

media = alturaTotal / alunoQuantia
print(round(media))
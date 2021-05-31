# 🚨 Don't change the code below 👇
notas_aluno = input("Digite a lista das notas dos estudantes: ").split()
for n in range(0, len(notas_aluno)):
  notas_aluno[n] = int(notas_aluno[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
maior_nota = 0
for nota in notas_aluno:
  if nota > maior_nota:
    maior_nota = nota
    
print(f"A maior nota da turma foi: {maior_nota}")
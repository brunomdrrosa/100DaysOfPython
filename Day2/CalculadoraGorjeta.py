#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Bem-vindo a calculadora de gorjeta")
conta = float(input("Qual foi o total da conta? R$"))
gorjeta = int(input("Qual percentual de gorjeta você quer dar? 10, 12, or 15? "))
pessoas = int(input("Quantas pessoas para dividar a conta? "))

gorjeta_percentual = gorjeta / 100
total_gorjeta = conta * gorjeta_percentual
total_conta = conta + total_gorjeta
conta_por_pessoa = total_conta / pessoas
quantia_final = round(conta_por_pessoa, 2)

#FAQ: How to round to 2 decimal places?
#https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048

print(f"Cada pessoa deve pagar: R${quantia_final}")
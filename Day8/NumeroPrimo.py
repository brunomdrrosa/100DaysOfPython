#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

def prime_checker(number):
    primo = True
    for i in range(2, number):
        if number % i == 0:
            primo = False
    if primo:
        print("É um número primo.")
    else:
        print("Não é um número primo.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Checar esse número: "))
prime_checker(number=n)
for numeros in range(1, 101):
    if numeros % 3 == 0 and numeros % 5 == 0:
        numeros = "FizzBuzz"
    elif numeros % 3 == 0:
        numeros = "Fizz"
    elif numeros % 5 == 0:
        numeros = "Buzz"
       
    print(numeros)
def somar(*args):
    soma = 0
    for numero in args:
        soma += numero
    return soma

print(somar(3, 5, 6, 4, 8))
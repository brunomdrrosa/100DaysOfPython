# Exception Handling

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error that I made up.")

# Exemplo do IMC

altura = float(input("Altura: "))
peso = int(input("Peso: "))

if altura > 3:
    raise ValueError("Um humano não tem mais de 3 metros de altura.")

imc = peso / altura ** 2
print(imc)
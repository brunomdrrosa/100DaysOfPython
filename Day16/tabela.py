from prettytable import PrettyTable

tabela = PrettyTable()
tabela.add_column("Nome do Pokémon", ["Pikachu","Squirtle","Charmander"])
tabela.add_column("Tipo", ["Elétrico","Água","Fogo"])
print(tabela)
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas
import os
os.chdir(r'C:/Users/bruno/OneDrive/Área de Trabalho/100DaysOfPython/Day26')
data = pandas.read_csv("alfabeto_otan.csv")

#TODO 1. Create a dictionary in this format:
alfabeto_dict = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
palavra = input("Insira uma palavra: ").upper()
lista = [alfabeto_dict[letra] for letra in palavra]
print(lista)
import os
os.chdir(r'C:/Users/bruno/OneDrive/Área de Trabalho/100DaysOfPython/Day26')
result = [int(num) for num in open("file1.txt") if num in open("file2.txt")]

# Write your code above 👆
print(result)

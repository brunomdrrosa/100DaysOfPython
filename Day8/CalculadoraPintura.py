#Write your code below this line 👇
import math

def paint_calc(height, width, cover):
    cans = (test_h * test_w) / coverage
    numberCans = math.ceil(cans)
    print(f"Você precisará de {numberCans} latas de tinta.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Altura da parede: "))
test_w = int(input("Largura da parede: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
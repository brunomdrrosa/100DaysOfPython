from turtle import Turtle, Screen
import random

corrida = True
screen = Screen()
screen.setup(width=500, height=400)
escolha = screen.textinput(title="Faça a sua aposta", prompt="Qual tartaruga irá ganhar a corrida?\nRED, ORANGE, YELLOW, GREEN, BLUE, PURPLE\nInsira uma cor: ")
cores = ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "PURPLE"]
y_tartaruga = [-70, -40, -10, 20, 50, 80]
todas_tartarugas = []

for turtle_index in range(0, 6):
    nova_tartaruga = Turtle(shape="turtle")
    nova_tartaruga.color(cores[turtle_index])
    nova_tartaruga.penup()
    nova_tartaruga.goto(x=-230, y=y_tartaruga[turtle_index])
    todas_tartarugas.append(nova_tartaruga)

if escolha:
    corrida = True

while corrida:
    for turtle in todas_tartarugas:
        if turtle.xcor() > 230:
            corrida = False
            vencedora = turtle.pencolor()
            if vencedora == escolha:
                print(f"Você ganhou! A tartaruga vencedora foi a  {vencedora}")
            else:
                print(f"Você perdeu! A tartaruga vencedora foi a {vencedora}")

        distancia = random.randint(0, 10)
        turtle.forward(distancia)

screen.exitonclick()
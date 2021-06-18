from turtle import Turtle, Screen, shape

tartaruga = Turtle()
tartaruga.shape("turtle")
tartaruga.color("blue")

for _ in range(4):
    tartaruga.forward(100)
    tartaruga.right(90)

screen = Screen()
screen.exitonclick()
from turtle import Turtle, Screen, shape

tartaruga = Turtle()
tartaruga.shape("turtle")
tartaruga.color("blue")

for _ in range(15):
    tartaruga.forward(10)
    tartaruga.penup()
    tartaruga.forward(10)
    tartaruga.pendown()
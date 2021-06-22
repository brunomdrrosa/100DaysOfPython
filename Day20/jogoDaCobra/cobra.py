from turtle import Turtle

POSICOES = [(0, 0), (-20, 0), (-40, 0)]
DISTANCIA = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segmentos = []
        self.create_snake()
        self.head = self.segmentos[0]
    
    def create_snake(self):
        for posicao in POSICOES:
            novo_segmento = Turtle(shape="square")
            novo_segmento.color("white")
            novo_segmento.penup()
            novo_segmento.goto(posicao)
            self.segmentos.append(novo_segmento)
    
    def move(self):
            for seg_num in range(len(self.segmentos) - 1, 0, -1):
                novo_x = self.segmentos[seg_num - 1].xcor()
                novo_y = self.segmentos[seg_num - 1].ycor()
                self.segmentos[seg_num].goto(novo_x, novo_y)
            self.head.forward(DISTANCIA)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
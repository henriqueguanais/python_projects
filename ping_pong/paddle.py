from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, pos_x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5)
        self.setheading(90)
        self.penup()
        self.goto(pos_x, 0)
        

    def up(self):
        self.forward(20)

    
    def down(self):
        self.backward(20)
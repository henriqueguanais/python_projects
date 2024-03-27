from turtle import Turtle
import random
NUMBERS = list(range(-10, 0)) + list(range(1, 11))

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_direction = random.choice(NUMBERS)
        self.x_direction = 10
        self.ball_speed = 0.1


    def move_ball(self):
        new_x = (self.xcor() + self.x_direction)
        new_y = (self.ycor() + self.y_direction)
        self.goto(new_x, new_y) 

    
    def bounce_y(self):
        self.y_direction *= -1

    
    def bounce_x(self):
        self.x_direction *= -1
        self.ball_speed *= 0.9
    

    def ball_restart(self):
        self.goto(0, 0)
        self.y_direction = random.choice(NUMBERS)
        self.ball_speed = 0.1
        self.x_direction *= -1

    


from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

class Player(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    
    def up(self):
        self.forward(MOVE_DISTANCE)


    def player_restart(self):
        self.goto(STARTING_POSITION)
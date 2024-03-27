from turtle import Turtle

STRING = "| \n"*30
class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.board()
        
    
    def board(self):
        self.clear()
        self.goto(0, -400)
        self.write(STRING, align="center", font=("Courier", 20, "normal"))
        self.goto(-100, 210)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 210)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))


    def increase_score(self, direction_score):
        if direction_score == "left":
            self.l_score += 1
        elif direction_score == "right":
            self.r_score += 1
        self.board()
        
    

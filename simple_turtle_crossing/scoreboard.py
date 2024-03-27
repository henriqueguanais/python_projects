from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.score = 1
        self.board()
    

    def board(self):
        self.clear()
        self.goto(-210, 265)
        self.write(f"Level: {self.score}", align="center", font=FONT)
    

    def increase_score(self):
        self.score += 1
        self.board()
    

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

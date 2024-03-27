from turtle import Turtle
import os

os.chdir("C:\\Users\\henri\\Desktop\\estudas\\projects_100days\\project20")

FONT = ("Courier", 20, "bold")
ALIGNMENT = "center"

class ScoreBoard:

    def __init__(self) -> None:
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())

    def score_board(self):
        self.board = Turtle()
        self.board.goto(x=0, y=268)
        self.board.hideturtle()
        self.board.color("White")
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()


    def update_score(self):
        self.board.clear()
        self.board.write(f"Pontuação: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def score_plus(self):
        self.score += 1
        self.update_score()
        
        


import pandas as pd
import turtle
import os 

os.chdir("C:\\Users\\henri\\Desktop\\estudas\\projects_100days\\project25\\game")
DATA = pd.read_csv("name_states.csv")
FONT = ("Courier", 10, "normal")

class Manager:

    def __init__(self) -> None:
        self.answer_score = 0
        self.correct_list = []

    def check_answer(self, user_answer):
        self.answer = user_answer.lower()
        DATA['data lower'] = DATA['state'].str.lower()

        if (not self.answer in self.correct_list) and (self.answer in DATA['data lower'].values):
            self.correct_list.append(self.answer)
            self.write_state()
            self.increase_score()
            print("Correto")
        else:
            print("Incorreto")
    
    def write_state(self):
        actual_state = DATA[DATA['data lower'] == self.answer]
        pos_x = actual_state.x.iloc[0]
        pos_y = actual_state.y.iloc[0]

        text = turtle.Turtle()
        text.hideturtle()
        text.color("black")
        text.penup()
        text.goto(pos_x, pos_y)
        text.write(f"{actual_state.state.iloc[0]}", align="center", font=FONT)
    
    def increase_score(self):
        self.answer_score += 1

    def create_csv_missing(self):
        states_remaing = [state for state in DATA["data lower"] if not state in self.correct_list]
        
        new_data = pd.DataFrame(states_remaing)
        new_data.to_csv("states_to_learn.csv")







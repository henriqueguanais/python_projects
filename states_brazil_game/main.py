import os
import turtle
from manager import Manager
import time

os.chdir("C:\\Users\\henri\\Desktop\\estudas\\projects_100days\\project25\\game")

screen = turtle.Screen()
screen.title("Estados do Brasil Game")
screen.setup(width=600, height=600)
image = "brasil.gif"
turtle.addshape(image)
turtle.shape(image)

manager = Manager()

is_game_on = True
start_time = time.time()
while is_game_on:

    answer_state = screen.textinput(title=f"{manager.answer_score}/27 estados corretos", prompt="Qual o nome de outro estado?")
    if answer_state == "exit":
        manager.create_csv_missing()
        print("Que pena! Um arquivo foi criado com a lista dos estados que faltam!")
        break
    manager.check_answer(answer_state)
    
    if len(manager.correct_list) == 27:
        end_time = time.time()
        elapsed_time = (end_time - start_time)/60
        minutes_elapsed = int(elapsed_time)
        seconds_elapsed = int((elapsed_time - minutes_elapsed)*60)
        print(f"Parabéns, você acertou os 27 estados! Em {minutes_elapsed} minutos e {seconds_elapsed} segundos")
        is_game_on = False


screen.exitonclick()

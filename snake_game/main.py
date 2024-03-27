#Snake Game
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()
score.score_board()

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    #Colisão com comida
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_plus()
    
    #Colisão com a parede
    if snake.head.xcor() < -300 or snake.head.xcor() > 280 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score.reset()
        snake.reset()
    
    #Colisão com a calda
    for segment in snake.all_segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
            

screen.exitonclick()
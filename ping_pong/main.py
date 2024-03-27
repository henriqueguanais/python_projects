from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

paddle_r = Paddle(350)
paddle_l = Paddle(-350)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(paddle_r.up, "Up")
screen.onkeypress(paddle_r.down, "Down")
screen.onkeypress(paddle_l.up, "w")
screen.onkeypress(paddle_l.down, "s")


game_is_on = True
while game_is_on:

    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()

    #Colisao com a parede
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #Colisao com raquete 
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    #Ponto para a esquerda 
    if ball.xcor() > 380:
        ball.ball_restart()
        scoreboard.increase_score("left")
    
    #Ponto para a direita
    if ball.xcor() < -380:
        ball.ball_restart()
        scoreboard.increase_score("right")
   
screen.exitonclick()
from turtle import Turtle,Screen
import time
import random
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
screen = Screen()

screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong Game")

screen.tracer(0)
l_paddle = Paddle(-350,0)
r_paddle = Paddle(350,0)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(l_paddle.move_up, "u")
screen.onkey(l_paddle.move_down, "d")
screen.onkey(r_paddle.move_up, "w")
screen.onkey(r_paddle.move_down, "s")
game_on = True
while game_on:
    scoreboard.scoreboard()
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) <50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.xcor() < -320 and ball.distance(l_paddle) <50:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_score_inc()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_score_inc()
screen.exitonclick()


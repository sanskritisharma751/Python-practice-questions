from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from scoreboard import *
screen = Screen()
tim = Turtle()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")
food = Food()
snake = Snake()
score=Scoreboard()
screen.listen()
screen.onkey(snake.up,"u")
screen.onkey(snake.down,"d")
screen.onkey(snake.left,"l")
screen.onkey(snake.right,"r")
Game_on = True
while Game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()

    if snake.head.xcor() >280 or snake.head.ycor() >280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        score.highest_score()
        snake.reset_segments()


    for segment in snake.segments[1:]:
      if snake.head.distance(segment) < 10:
          score.highest_score()
          snake.reset_segments()



screen.exitonclick()
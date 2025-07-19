import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
turtle = Turtle()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move, 'a')
turtle.hideturtle()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.may_add_car()
    car_manager.move_cars()
    for car in car_manager.cars:
      if player.distance(car) < 20:
        game_is_on = False
        turtle.write("GAME OVER", align="center", font=("Courier", 24,"bold"))
        turtle.color("black")
        print("Game over")

    if player.ycor()>280:
        player.reset_position()
        scoreboard.increase_level()
        car_manager.speed_up()


screen.exitonclick()
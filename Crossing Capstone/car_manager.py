COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
#POSITIONS =[(280,0),(280,50),(280,100),(280,150),(280,200),(280,250),(280,-50),(280,-100),(280,-150),(280,-200),]
from turtle import Turtle
import random

class CarManager:
    def __init__(self):
        self.cars = []
        self.add_car()
        self.move_distance = STARTING_MOVE_DISTANCE


    def add_car(self):
        position = (300,random.randrange(-250,250))
        self.car_shape(position)

    def car_shape(self,position):
        car = Turtle(shape="square")
        car.color(random.choice(COLORS))
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.setheading(180)
        car.goto(position)
        self.cars.append(car)


    def move_cars(self):
        for car in self.cars:
           car.forward(self.move_distance)

    def may_add_car(self):
        if random.randint(0,6) == 1:
            self.add_car()

    def speed_up(self):
        self.move_distance += MOVE_INCREMENT


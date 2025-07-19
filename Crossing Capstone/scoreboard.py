FONT = ("Courier", 20, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.goto(-280,260)
        self.levels = 1
        self.level()

    def level(self):
        self.clear()
        self.write(f'Level {self.levels}', align="left", font=FONT)

    def increase_level(self):
        self.levels += 1
        self.level()



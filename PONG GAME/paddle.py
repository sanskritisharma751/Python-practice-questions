from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(x,y)
        self.y=20
        self.speed("fastest")

    def move_up(self):
      new_y = self.ycor() + 20
      self.goto(self.xcor(),new_y)


    def move_down(self):
      new_y = self.ycor() - 20
      self.goto(self.xcor(),new_y)


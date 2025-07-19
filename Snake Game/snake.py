from turtle import Turtle
MOVES =[(0,0),(-20,0),(-40,0)]
MOVE_FORWARD=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segments = []
        self.snake_shape()
        self.head = self.segments[0]

    def snake_shape(self):
        for position in MOVES:
            self.add_segment(position)

    def add_segment(self,position):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.segments.append(snake)

    def extend_segment(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
       for steps in range(len(self.segments) - 1, 0, -1):
         new_x = self.segments[steps - 1].xcor()
         new_y = self.segments[steps - 1].ycor()
         self.segments[steps].goto(new_x, new_y)
       self.head.forward(MOVE_FORWARD)

    def reset_segments(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.snake_shape()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading()!=DOWN:
           self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
           self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
           self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
           self.head.setheading(RIGHT)






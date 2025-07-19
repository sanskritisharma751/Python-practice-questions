import random
import turtle as t
import colorgram
from turtle import Screen

t.colormode(255)
def random_colors():
  colors = colorgram.extract('hirst.jpg', 20)
  color_obj = random.choice(colors)
  rgb = color_obj.rgb
  color = (rgb.r, rgb.g, rgb.b)
  print(color)
  return color
t.speed("fastest")
t.penup()
def hirst():
  count = 9
  while count>0:
   for j in range(1):
     for i in range(10):
        t.dot(10, random_colors())
        t.forward(20)
     t.left(90)
     t.forward(20)
     t.left(90)
     t.forward(200)
     t.right(180)
     count-=1



hirst()
screen = Screen()
screen.exitonclick()
import turtle as t
import random
from turtle import Turtle, Screen

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g , b)
    return random_color

direction = [0, 90, 180, 270]

t.shape("turtle")
t.pensize(10)
t.speed(10)

for x in range(100):
    t.color(random_color())
    t.forward(50)
    t.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()

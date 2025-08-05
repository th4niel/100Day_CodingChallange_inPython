from turtle import Turtle, Screen
import random

colour = ["forest green", "cornflower blue", "magenta", "dark orchid", "medium turquoise", "pale green", "dodger blue" ]

t = Turtle()
t.shape("turtle")

def draw_shape(shape_angle):
    angle = 360 / shape_angle
    for i in range (shape_angle):
        t.forward(100)
        t.right(angle)

for shape_side_n in range (3, 11):
    t.color(random.choice(colour))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()
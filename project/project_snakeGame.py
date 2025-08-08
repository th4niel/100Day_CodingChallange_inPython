import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.title("King Python Carnival")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
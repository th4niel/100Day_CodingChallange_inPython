from turtle import Turtle, Screen
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.title("King Python Carnival")
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]
segment = []

for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segment.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    for seg_num in range (len(segment)-1, 0, -1):
        new_x = segment[seg_num-1].xcor()
        new_y = segment[seg_num-1].ycor()
        segment[seg_num].goto(new_x, new_y)
    segment[0].forward(20)
    segment[0].left(90)

screen.exitonclick()
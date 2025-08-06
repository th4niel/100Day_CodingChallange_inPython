import turtle as t
import random
# import colorgram

# rgb_color = []

# colors = colorgram.extract('hirst.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)

# print(rgb_color)
t.colormode(255)
bob = t.Turtle()
bob.speed("fastest")
bob.penup()
bob.hideturtle()
color_list = [(246, 243, 239), (246, 242, 244), (202, 164, 109), (240, 245, 242), (148, 75, 50), (235, 238, 243), (53, 93, 123), (222, 201, 138), (167, 151, 45), (134, 32, 22), (133, 162, 183), (197, 92, 73), (49, 120, 88), (68, 46, 40), (17, 97, 72), (146, 178, 148), (232, 176, 167), (161, 143, 157), (107, 74, 77), (41, 61, 72), (184, 205, 171), (20, 84, 89), (52, 46, 48), (148, 16, 19), (87, 145, 128), (47, 66, 82), (178, 84, 86), (180, 192, 206), (221, 173, 175), (12, 70, 61)]
bob.setheading(225)
bob.forward(300)
bob.setheading(0)
number_of_dots = 100

for dot_count in range (1, number_of_dots +1):
    bob.dot(20, random.choice(color_list))
    bob.forward(50)

    if dot_count % 10 == 0:
        bob.setheading(90)
        bob.forward(50)
        bob.setheading(180)
        bob.forward(500)
        bob.setheading(0)

screen = t.Screen()
screen.exitonclick()
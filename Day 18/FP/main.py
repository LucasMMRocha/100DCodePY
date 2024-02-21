# import colorgram
#
# list_of_colors = []
#
# colors = colorgram.extract('img.jpg', 25)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     list_of_colors.append(new_color)
#
# print(list_of_colors)
import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()
turtle.colormode(255)
tim.speed("fastest")

tim.penup()
tim.right(120)
tim.forward(300)
tim.left(120)

list_of_colors = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]

for _ in range(10):
    for _ in range(10):
        color = list_of_colors[random.randrange(0, len(list_of_colors))]
        tim.dot(20, color)
        tim.forward(50)
    tim.left(180)
    tim.forward(500)
    tim.right(90)
    tim.forward(50)
    tim.right(90)

screen = Screen()
screen.exitonclick()

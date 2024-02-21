from turtle import Turtle, Screen
import random

tim = Turtle()
tim.color("blue")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.pencolor(r/255, g/255, b/255)


# Square
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# Line Gaps
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Nice Figure
# angle_numb = 3
#
# for numb in range(1, 9):
#     angle = (360 / angle_numb)
#     random_color()
#     for _ in range(angle_numb):
#         tim.forward(100)
#         tim.right(angle)
#
#     angle_numb += 1
#     print(angle)
#     print(angle_numb)

# Random Walk
# num = [0, 90, 180, 270]
# tim.width(5)
# tim.speed(10)
#
# for _ in range(50):
#     random_color()
#     angle = random.choice(num)
#     tim.forward(20)
#     tim.setheading(angle)

# Spirograph
# tim.speed("fastest")

# def draw_spirograph(times):
#     for _ in range(times):
#         angle = 360 / times
#         tim.circle(100)
#         tim.left(angle)
#         random_color()


# draw_spirograph(30)

screen = Screen()
screen.exitonclick()

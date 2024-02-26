from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def foward():
    tim.forward(10)


def back():
    tim.back(10)


def left():
    tim.left(10)


def right():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=foward)
screen.onkey(key="a", fun=left)
screen.onkey(key="s", fun=back)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
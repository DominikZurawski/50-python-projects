from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")
# turtle.color("blue")
screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def square(step):
    for _ in range(4):
        turtle.forward(step)
        turtle.right(90)


def break_line(distance, divide):
    step = distance / divide
    for x in range(divide):
        turtle.forward(step)
        turtle.penup()
        turtle.forward(step)
        turtle.pendown()


def figures(step, kind):
    for _ in range(kind):
        turtle.forward(step)
        turtle.right(360 / kind)


# for x in range(3, 20):
#     figures(80, x)
#     turtle.color(random_color())
#
# break_line(100, 10)
#
directions = [0, 90, 180, 270]


def random_walk(step):
    turtle.speed(0)
    turtle.pensize(3)
    for _ in range(step):
        turtle.forward(20)
        turtle.setheading(random.choice(directions))

        turtle.color(random_color())


#random_walk(100)

def Spirograph(step):
    turtle.speed(0)
    for x in range(step):
        turtle.circle(100)
        turtle.setheading(turtle.heading() + 360/step)
        turtle.color(random_color())

Spirograph(100)


screen.exitonclick()


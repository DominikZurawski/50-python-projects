from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "blue", "green", "yellow", "purple"]
is_race_on = True

user_bet = screen.textinput("Make your bet", prompt="Which turtle will win the race? Enter a color: ")

turtles = []
for x in range(0, 6):
    turtles.append(Turtle(shape="turtle"))
    turtles[x].color(colors[x])
    turtles[x].penup()
    turtles[x].goto(x=-230, y=-150 + 60 * x)

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

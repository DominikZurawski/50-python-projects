from turtle import Screen
import time

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    # Detect ball collision with top and bottom wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.detect_wall()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 55 and ball.xcor() > 325 or ball.distance(l_paddle) < 55 and ball.xcor() < -325:
        ball.detect_paddle()

    # Detect when ball left a board
    if ball.xcor() > 420:
        ball.ball_left_board()
        scoreboard.l_point()

    if ball.xcor() < -420:
        ball.ball_left_board()
        scoreboard.r_point()



screen.exitonclick()

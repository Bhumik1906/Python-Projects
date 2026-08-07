from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("gray2")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

rPaddle = Paddle((350, 0))
lPaddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(rPaddle.go_up, "Up")
screen.onkey(rPaddle.go_down, "Down")
screen.onkey(lPaddle.go_up, "w")
screen.onkey(lPaddle.go_down, "s")

gameOn = True
while gameOn:
    time.sleep(ball.moveSpeed)
    screen.update()
    ball.move()

    # DETECT COLLISION WITH WALL
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # DETECT COLLISION WITH PADDLES
    if (ball.distance(rPaddle.paddle) < 50 and ball.xcor() > 320) or (
        ball.distance(lPaddle.paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # RIGHT PLAYER MISSES
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    # LEFT PLAYER MISSES
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()
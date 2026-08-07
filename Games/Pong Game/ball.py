from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

        self.xMove = 10
        self.yMove = 10
        self.moveSpeed = 0.1

    def move(self):
        x = self.xcor() + self.xMove
        y = self.ycor() + self.yMove
        self.goto(x, y)

    def bounce_x(self):
        self.xMove *= -1
        self.moveSpeed *= 0.9

    def bounce_y(self):
        self.yMove *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.moveSpeed = 0.1

        self.xMove = random.choice([-10, 10])
        self.yMove = random.choice([-10, 10])
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

        self.lScore = 0
        self.rScore = 0

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()

        self.goto(-100, 200)
        self.write(self.lScore, align=ALIGNMENT, font=FONT)

        self.goto(100, 200)
        self.write(self.rScore, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.lScore += 1
        self.update_scoreboard()

    def r_point(self):
        self.rScore += 1
        self.update_scoreboard()
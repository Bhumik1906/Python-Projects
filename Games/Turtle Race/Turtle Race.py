from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height = 400, width = 500)

raceOn = False
userBet = screen.textinput(title = "Make Your Bet -->", prompt =  "Which Turtle Will Win The Race? Enter A Color: ").lower()

colors = ["Red", "Orange", "Pink", "Green", "Blue", "Purple"]
yPositions = [-70, -40, -10, 20, 50, 80]
allTurtles = []

for turtle_index in range(0, 6):
    newTurtle = Turtle(shape = "turtle")
    newTurtle.color(colors[turtle_index])
    newTurtle.penup()
    newTurtle.goto(x=-230, y=yPositions[turtle_index])
    allTurtles.append(newTurtle)

if userBet:
    raceOn = True

while raceOn:

    for turtle in allTurtles: 
        if turtle.xcor() > 230:
            raceOn = False
            winner = turtle.pencolor()

            if winner == userBet:
                print(f"You Won! The Winner Is {winner} Turtle.")

            else:
                print(f"You Lost! The Winner Is {winner} Turtle.")

        randomDist = random.randint(0, 10)
        turtle.forward(randomDist)



screen.exitonclick()
print(userBet)

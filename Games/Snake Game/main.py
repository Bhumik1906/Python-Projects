from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# ---------------------------- SCREEN SETUP ------------------------------- #
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gray2")
screen.title("Snake Game")
screen.tracer(0)

# ---------------------------- OBJECTS ------------------------------------ #
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# ---------------------------- KEYBOARD CONTROLS -------------------------- #
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# ---------------------------- GAME LOOP ---------------------------------- #
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # Detect collision with wall
    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        game_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()
            break

screen.exitonclick()

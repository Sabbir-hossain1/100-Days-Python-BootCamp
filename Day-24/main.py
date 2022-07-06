from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

snake = Snake()
scoreboard = Scoreboard()
food = Food()

screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    snake.move_snake()
    time.sleep(0.1)

    # Detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        scoreboard.reset()
        snake.reset()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_snake()
    # Detect tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()

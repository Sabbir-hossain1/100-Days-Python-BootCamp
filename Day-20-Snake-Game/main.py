# --------Snake without class--------------------
# from turtle import Turtle, Screen
# import time
#
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game ")
# screen.tracer(0)
#
# segments = []
# starting_position = [(0, 0), (-20, 0), (-40, 0)]
#
# for position in starting_position:
#     snake_segment = Turtle(shape="square")
#     snake_segment.penup()
#     snake_segment.color("white")
#     snake_segment.goto(position)
#     segments.append(snake_segment)
#
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     for segment_num in range(len(segments)-1, 0, -1):
#         new_x = segments[segment_num-1].xcor()
#         new_y = segments[segment_num - 1].ycor()
#         segments[segment_num].goto(new_x, new_y)
#     segments[0].forward(20)
#
# screen.exitonclick()

# ------------- Snake with class--------------
import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake")
screen.tracer(0)

snake_obj = Snake()
screen.listen()
screen.onkey(snake_obj.up, "Up")
screen.onkey(snake_obj.down, "Down")
screen.onkey(snake_obj.left, "Left")
screen.onkey(snake_obj.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake_obj.move()

screen.exitonclick()

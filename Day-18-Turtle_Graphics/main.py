# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import turtle
from turtle import Turtle,Screen

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    timmy_the_turtle = Turtle()
    screen = Screen()
    turtle.shape("turtle")
    turtle.color("red", "Green")
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)
    screen.exitonclick()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

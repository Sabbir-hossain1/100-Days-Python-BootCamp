from turtle import Turtle, Screen
import turtle as t
import random

turtle_object = Turtle()
t.colormode(255)
screen = Screen()

colors_list = ["DarkMagenta", "cyan", "LightSeaGreen", "firebrick", "DarkGreen", "crimson", "orange", "green",
               "SaddleBrown", "BlueViolet"]


def random_colors():
    """Return a random color in rgb formate"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


# def draw_shapes(number_of_sides):
#     angles = 360 / number_of_sides
#     for _ in range(number_of_sides):
#         turtle_object.forward(100)
#         turtle_object.right(angles)
#
#
# for sides_n in range(3, 11):
#     turtle_object.color(random.choice(colors_list))
#     draw_shapes(sides_n)

# turtle_object.color(colors_list[9])
# turtle_object.forward(100)
# screen.exitonclick()

turtle_object.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        current_position = turtle_object.heading()
        turtle_object.setheading(current_position + size_of_gap)
        turtle_object.color(random_colors())
        turtle_object.circle(100)


draw_spirograph(5)
screen.exitonclick()

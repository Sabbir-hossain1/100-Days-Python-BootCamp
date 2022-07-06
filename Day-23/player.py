from turtle import Turtle
STARING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.go_staring_position()

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_staring_position(self):
        self.goto(STARING_POSITION)

    def is_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False




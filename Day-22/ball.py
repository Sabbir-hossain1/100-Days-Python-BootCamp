from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_mov = 10
        self.y_mov = 10
        self.move_speed = 0.1

    def move_ball(self):
        new_xcor = self.xcor()+self.x_mov
        new_ycor = self.ycor()+self.y_mov
        self.goto(new_xcor, new_ycor)

    def bounce_y(self):
        self.y_mov *= -1

    def bounce_x(self):
        self.x_mov *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

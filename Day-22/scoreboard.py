from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0

    def update_score(self):
        self.clear()
        self.goto(x=-100, y=250)
        self.write(self.left_score, align="center", font=("Courier", 24, "normal"))
        self.goto(x=100, y=250)
        self.write(self.right_score, align="center", font=("Courier", 24, "normal"))

    def l_points(self):
        self.left_score += 1
        self.update_score()

    def r_points(self):
        self.right_score += 1
        self.update_score()

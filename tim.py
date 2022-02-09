from turtle import Turtle
from scoreboard import Scoreboard

scoreboard = Scoreboard()


class Tim(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset_tim()

    def move_forward(self):
        if self.ycor() < 280:
            self.forward(10)

    def reset_tim(self):
        self.goto(0, -280)

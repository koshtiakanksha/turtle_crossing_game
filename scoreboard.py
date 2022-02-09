from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super(). __init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(0, 250)

    def score(self):
        self.write(f"Level={self.level}", align="center", font=FONT)

    def update_level(self):
        self.level += 1
        self.clear()
        self.score()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
